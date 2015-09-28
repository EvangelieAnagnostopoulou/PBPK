import json
from django.db import IntegrityError
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django import forms
import numpy as np
from pbpk.simulator import Simulator
from pbpk.openLoopSimulator import SimulatorOpenLoop, input_profile
from pbpk.forms import ModelForm, DrugForm

from pbpk.initWeb import PBPK_Model, Skin, Kidney, Bladder, Residual, Liver, Blood, Lung, Organ1, Organ2, Organ3, \
    Organ4, Organ5, Heart, Placental, Spleen, Muscle
from pbpk.models import Models, Drug
from pbpk.state_space import System
from pbpk.util import check_number, isnumber
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from os import path
import os.path

__author__ = 'evangelie'


def WelcomePage(request):
    return render(request, "mainPage.html")


def InitPage(request):
    if request.method == 'GET':
        submit = ""
        counter = 1
        form = ModelForm(initial={'bw': 0.03, 'h': 0.45, "method": "None",
                                  "method_params": '{"N": 5, "intervals": 4, "step": 0.0833, "end": 4, "time": [0, 1, 2, 3 ], "setpoint": [4e-07, 4e-07, 4e-07, 4e-07], "time_int_final": [1, 2, 3, 4], "Q": 0.25, "R":5}', },
                         prefix="mod")
        dform = DrugForm(prefix="dr", initial={'drug_name': ''})

        return render(request, "model_form.html", {'dform': dform, 'form': form, 'submit': submit, 'counter': counter})

    if request.method == 'POST':
        form = ModelForm(request.POST, prefix="mod")
        dform = DrugForm(request.POST, prefix="dr")
        meth = request.POST.get('mod-method')
        submit = request.POST.get('submit_id')
        counter = request.POST.get('counter_id')

        if not form.is_valid() or not dform.is_valid():
            params = {'form': form, 'dform': dform, "save": True, 'submit': submit, 'counter': counter}
            return render(request, "model_form.html", params)
        elif ((form['blood_volume_fraction'].value() == "0.0") | (form['lung_flow_factor'].value() == "0.0") | (
                    form['lung_volume_fraction'].value() == "0.0") | (form['blood_lung_fraction'].value() == "0.0") | (
                    dform['p_lung'].value() == "0.0")):
            if ((form['blood_volume_fraction'].value() == "0.0") & ((form['lung_flow_factor'].value() == "0.0") | (
                        form['lung_volume_fraction'].value() == "0.0") | (form['blood_lung_fraction'].value() == "0.0") | (
                        dform['p_lung'].value() == "0.0"))):
                error = "Cannot be created model without blood and lung."
                params = {'form': form, 'dform': dform, "save": True, 'error': error, 'submit': submit,
                          'counter': counter}
                return render(request, "model_form.html", params)
            elif (form['blood_volume_fraction'].value() == "0.0"):
                error = "Cannot be created model without blood."
                params = {'form': form, 'dform': dform, "save": True, 'error': error, 'submit': submit,
                          'counter': counter}
                return render(request, "model_form.html", params)
            elif ((form['lung_flow_factor'].value() == "0.0") | (form['lung_volume_fraction'].value() == "0.0") | (
                        form['blood_lung_fraction'].value() == "0.0") | (dform['p_lung'].value() == "0.0")):
                error = "Cannot be created model without lung."
                params = {'form': form, 'dform': dform, "save": True, 'error': error, 'submit': submit,
                          'counter': counter}
                return render(request, "model_form.html", params)
            elif (((form['skin_flow_factor'].value()) + (form['liver_flow_factor'].value()) + (
                    form['kidney_flow_factor'].value()) + (form['bladder_flow_factor'].value())) > 1):
                error = " Inavalid flow factor combination. The sum of skin, liver, kidney and bladder flow factors must be less than 1."
                params = {'form': form, 'dform': dform, "save": True, 'error': error, 'submit': submit,
                          'counter': counter}
                return render(request, "model_form.html", params)
            elif (((form['skin_volume_fraction'].value()) + (form['liver_volume_fraction'].value()) + (
                    form['kidney_volume_fraction'].value()) + (form['bladder_flow_factor'].value()) + form[
                'lung_volume_fraction'].value()) > 1):
                error = " Inavalid volume fraction combination. The sum of skin, liver, kidney, bladder and lung volume fractions must be less than 1."
                params = {'form': form, 'dform': dform, "save": True, 'error': error, 'submit': submit,
                          'counter': counter}
                return render(request, "model_form.html", params)
        else:
            k_bile5 = 0.0
            k_met5 = 0.0
            k_bile4 = 0.0
            k_met4 = 0.0
            k_bile3 = 0.0
            k_met3 = 0.0
            k_bile2 = 0.0
            k_met2 = 0.0
            k_bile1 = 0.0
            k_met1 = 0.0
            type1 = ""
            const1 = ""
            type2 = ""
            const2 = ""
            type3 = ""
            const3 = ""
            type4 = ""
            const4 = ""
            type5 = ""
            const5 = ""
            if submit == "Run":
                if meth == "CloseLoop-MPC":
                    new_drug = dform.save(commit=False)
                    new_model = form.save(commit=False)
                    new_model.username = request.user.username
                    # new_model.drugs.clear()
                    #convert method_params to json and read values
                    if new_drug.organ1_params:
                        org1_params_json = json.loads(new_drug.organ1_params)
                        if org1_params_json[0]:
                            type1 = org1_params_json[0]['type']
                            if type1 == "met":
                                const1 = org1_params_json[0]['const']
                                k_met1 = org1_params_json[0]['k_met']
                                k_bile1 = org1_params_json[0]['k_bile']
                                print (const1)
                            print(type1)
                        if org1_params_json[1]:
                            type2 = org1_params_json[1]['type']
                            if type2 == "met":
                                const2 = org1_params_json[1]['const']
                                k_met2 = org1_params_json[1]['k_met']
                                k_bile2 = org1_params_json[1]['k_bile']
                        if org1_params_json[2]:
                            type3 = org1_params_json[2]['type']
                            if type3 == "met":
                                const3 = org1_params_json[2]['const']
                                k_met3 = org1_params_json[2]['k_met']
                                k_bile3 = org1_params_json[2]['k_bile']
                        if org1_params_json[3]:
                            type4 = org1_params_json[3]['type']
                            if type4 == "met":
                                const4 = org1_params_json[3]['const']
                                k_met4 = org1_params_json[3]['k_met']
                                k_bile4 = org1_params_json[3]['k_bile']
                        if org1_params_json[4]:
                            type5 = org1_params_json[4]['type']
                            if type5 == "met":
                                const5 = org1_params_json[4]['const']
                                k_met5 = org1_params_json[4]['k_met']
                                k_bile5 = org1_params_json[4]['k_bile']
                    params_json = json.loads(new_model.method_params)
                    N = params_json['N']
                    intervals = params_json['intervals']
                    step = params_json['step']
                    end = params_json['end']
                    setpoint = params_json['setpoint']
                    time = params_json['time']
                    Q = params_json['Q']
                    R = params_json['R']

                    if not (check_number(N) and check_number(intervals) and check_number(step) and check_number(
                            end) and setpoint and time and check_number(k_bile1) and check_number(k_bile2) and check_number(
                            k_bile3) and check_number(k_bile4)
                            and check_number(k_bile5) and check_number(k_met1) and check_number(
                            k_met2) and check_number(k_met3) and check_number(k_met4) and check_number(k_met5)):
                        error = "The data you entered aren't valid. Please try again."
                        return render(request, "model_form.html",
                                      {"form": form, "N": N, "target": intervals, "error": error, "step": step, "end": end,
                                       'counter': counter})
                    elif float(step) > float(end):
                        error = "Wrong step and/or end time."
                        return render(request, "model_form.html",
                                      {"form": form, "N": N, "target": intervals, "error": error, "step": step, "end": end,
                                       'counter': counter})
                    else:
                        N = int(N)
                        intervals = int(intervals)
                        step = float(step)
                        end = float(end)
                        Q = float(Q)
                        R = float(R)
                        setpoint1 = []
                        setpoint2 = []
                        time1 = []
                        time2 = []
                        for e in setpoint:
                            e = float(e)
                            setpoint1.append(e)
                            e = int(e)
                            setpoint2.append(e)
                            #add the last element twice due to add the last couple for plotting
                        last_d = int(setpoint1[-1])
                        setpoint2.append(last_d)

                        for t in time:
                            t = float(t)
                            time1.append(t)
                            t = int(t)
                            time2.append(t)
                            #add the end time of simulation (time constists of initial times. For correct plotting it should be added one more couple)
                        time2.append(end)

                        k_met1 = float(k_met1)
                        k_bile1 = float(k_bile1)
                        k_met2 = float(k_met2)
                        k_bile2 = float(k_bile2)
                        k_met3 = float(k_met3)
                        k_bile3 = float(k_bile3)
                        k_met4 = float(k_met4)
                        k_bile4 = float(k_bile4)
                        k_met5 = float(k_met5)
                        k_bile5 = float(k_bile5)

                        model = PBPK_Model(new_model.bw, new_model.h, new_model.cardiac_output, new_drug.k_met,
                                           new_drug.k_bile, new_drug.k_kidney, new_drug.max_liver, new_drug.max_kidney,
                                           new_drug.max_influx,
                                           new_model.skin_flow_factor, new_model.skin_volume_fraction,
                                           new_model.blood_skin_fraction, new_drug.p_skin, new_drug.pi_skin,
                                           new_model.kidney_flow_factor, new_model.kidney_volume_fraction,
                                           new_model.blood_kidney_fraction, new_drug.p_kidney, new_drug.pi_kidney,
                                           new_model.bladder_flow_factor, new_model.bladder_volume_fraction,
                                           new_model.blood_bladder_fraction, new_drug.p_bladder, new_drug.pi_bladder,
                                           new_model.blood_rest_fraction, new_drug.p_rest, new_drug.pi_rest,
                                           new_model.liver_flow_factor, new_model.liver_volume_fraction,
                                           new_model.blood_liver_fraction, new_drug.p_liver, new_drug.pi_liver,
                                           new_model.blood_volume_fraction, new_drug.pi_rbc, new_drug.pi_plasma,
                                           new_model.lung_flow_factor, new_model.lung_volume_fraction,
                                           new_model.blood_lung_fraction, new_drug.p_lung, new_drug.pi_lung,
                                           new_drug.min_residual, new_drug.max_residual, new_drug.min_skin,
                                           new_drug.max_skin, new_drug.min_bladder, new_drug.max_bladder,
                                           new_drug.min_lung, new_drug.max_lung, new_drug.min_liver,
                                           new_drug.min_kidney,
                                           new_model.organ1_flow_factor, new_model.organ1_volume_fraction,
                                           new_model.blood_organ1_fraction, new_drug.p_organ1, new_drug.pi_organ1,
                                           type1, const1, k_met1, k_bile1,
                                           new_model.organ2_flow_factor, new_model.organ2_volume_fraction,
                                           new_model.blood_organ2_fraction, new_drug.p_organ2, new_drug.pi_organ2,
                                           type2, const2, k_met2, k_bile2,
                                           new_model.organ3_flow_factor, new_model.organ3_volume_fraction,
                                           new_model.blood_organ3_fraction, new_drug.p_organ3, new_drug.pi_organ3,
                                           type3, const3, k_met3, k_bile3,
                                           new_model.organ4_flow_factor, new_model.organ4_volume_fraction,
                                           new_model.blood_organ4_fraction, new_drug.p_organ4, new_drug.pi_organ4,
                                           type4, const4, k_met4, k_bile4,
                                           new_model.organ5_flow_factor, new_model.organ5_volume_fraction,
                                           new_model.blood_organ5_fraction, new_drug.p_organ5, new_drug.pi_organ5,
                                           type5, const5, k_met5, k_bile5,
                                           new_model.heart_flow_factor, new_model.heart_volume_fraction,
                                           new_model.blood_heart_fraction, new_drug.p_heart, new_drug.pi_heart,
                                           new_model.muscle_flow_factor, new_model.muscle_volume_fraction,
                                           new_model.blood_muscle_fraction, new_drug.p_muscle, new_drug.pi_muscle,
                                           new_model.spleen_flow_factor, new_model.spleen_volume_fraction,
                                           new_model.blood_spleen_fraction, new_drug.p_spleen, new_drug.pi_spleen,
                                           new_model.placental_flow_factor, new_model.placental_volume_fraction,
                                           new_model.blood_placental_fraction, new_drug.p_placental,
                                           new_drug.pi_placental)
                        skin = Skin(model)
                        kidney = Kidney(model)
                        bladder = Bladder(model)
                        residual = Residual(model)
                        liver = Liver(model)
                        blood = Blood(model)
                        lung = Lung(model)
                        organ1 = Organ1(model)
                        organ2 = Organ2(model)
                        organ3 = Organ3(model)
                        organ4 = Organ4(model)
                        organ5 = Organ5(model)
                        heart = Heart(model)
                        muscle = Muscle(model)
                        spleen = Spleen(model)
                        placental = Placental(model)
                        try:
                            mysystem = System(model, skin, kidney, bladder, residual, liver, blood, lung, organ1,
                                              organ2, organ3, organ4, organ5, heart, muscle, spleen, placental)
                            sys = mysystem.DiscreteSystem()
                            d_hat = 1.7408e-14 * np.ones((1, 1))
                            x_hat = np.zeros((sys.A.shape[0], 1))
                            tlist= [0.0, 4.0, 8.0]
                            ulist1 = [2.0, 2.0, 2.0]
                            sim = Simulator(mysystem, N, x_hat, d_hat, new_drug.max_liver, new_drug.max_kidney,
                                            new_drug.max_influx, new_drug.min_residual, new_drug.max_residual,
                                            new_drug.min_skin,
                                            new_drug.max_skin, new_drug.min_bladder, new_drug.max_bladder,
                                            new_drug.min_lung, new_drug.max_lung, new_drug.min_liver,
                                            new_drug.min_kidney, new_drug.min_heart, new_drug.max_heart,
                                            new_drug.min_muscle, new_drug.max_muscle, new_drug.min_spleen,
                                            new_drug.max_spleen, new_drug.min_placental, new_drug.max_placental, end, time1, setpoint1, step, Q, R)
                            Tsim, cont, ulist = sim.Simulate(step, end)
                            plot_j = []
                            # plot_j is of the following form
                            # [ [[0.0, y1.1], [0.01, y1.2], ...] -> organ1,  [[0.0, y2.1], [0.0, y2.2], ...] -> organ2, ... ]
                            adm = []
                            for i in range(len(ulist)):
                                adm.append([Tsim[i], ulist[i]])
                            adm_j = json.dumps(adm)
                            new_model.step_params = adm_j

                            for c in cont:
                                vals = []
                                for i in range(len(Tsim)):
                                    vals.append([Tsim[i], c[i]])

                                plot_j.append(vals)

                            json_object_plot = json.dumps(plot_j)
                            new_model.plot_params = json_object_plot

                        except RuntimeError as re:
                            print(re)
                            error = "An error occurred while creating the model."
                            params = {'form': form, 'dform': dform, "save": True, 'error': error, 'counter': counter}
                            return render(request, "model_form.html", params)
                        except Exception as e:
                            print(e)
                            error = "An error occurred while creating the model."
                            params = {'form': form, 'dform': dform, "save": True, 'error': error, 'counter': counter}
                            return render(request, "model_form.html", params)

                        params = {'form': form, 'dform': dform, 'save': True, 'image': True, 'counter': counter,
                                  'change': True, 'json': json_object_plot, 'adm': adm_j}
                        if request.is_ajax():
                            return HttpResponse(json_object_plot, 'application/json')

                        try:
                            new_drug.save()
                            new_model.save()
                        except IntegrityError:
                            error = "Modelname already exists."
                            params = {'form': form, 'dform': dform, "save": True, 'error': error, 'counter': counter}
                            return render(request, "model_form.html", params)

                        new_model.drugs.add(new_drug)
                        import pdb;pdb.set_trace()
                        return render(request, "model_form.html", params)
                elif meth == "OpenLoop":
                    new_drug = dform.save(commit=False)
                    new_model = form.save(commit=False)
                    new_model.username = request.user.username

                    # new_model.drugs.clear()
                    #new_model.save(commit=False)
                    #convert method_params to json and read values
                    if new_drug.organ1_params:
                        org1_params_json = json.loads(new_drug.organ1_params)
                        if org1_params_json[0]:
                            type1 = org1_params_json[0]['type']
                            if type1 == "met":
                                const1 = org1_params_json[0]['const']
                                print (const1)
                            print(type1)
                        if org1_params_json[1]:
                            type2 = org1_params_json[1]['type']
                            if type2 == "met":
                                const2 = org1_params_json[1]['const']
                        if org1_params_json[2]:
                            type3 = org1_params_json[2]['type']
                            if type3 == "met":
                                const3 = org1_params_json[2]['const']
                        if org1_params_json[3]:
                            type4 = org1_params_json[3]['type']
                            if type4 == "met":
                                const4 = org1_params_json[3]['const']
                        if org1_params_json[4]:
                            type5 = org1_params_json[4]['type']
                            if type5 == "met":
                                const5 = org1_params_json[4]['const']
                    params_json = json.loads(new_model.method_params)
                    total_time = params_json['total_time']
                    total_N = params_json['total_N']
                    dose = params_json['dose']
                    time = params_json['time']
                    dose1 = []
                    dose2 = []
                    time1 = []
                    time2 = []
                    if not (check_number(total_time) and check_number(total_N) and dose and time and check_number(
                            k_bile1) and check_number(k_bile2) and check_number(k_bile3) and check_number(k_bile4)
                            and check_number(k_bile5) and check_number(k_met1) and check_number(
                            k_met2) and check_number(k_met3) and check_number(k_met4) and check_number(k_met5) ):
                        error = "The data you entered aren't valid. Please try again."
                        params = {'form': form, 'dform': dform, 'save': True, "total_time": total_time,
                                  "total_N": total_N, "error": error, 'counter': counter}
                        return render(request, "model_form.html", params)
                    elif time > total_time:
                        error = "Wrong parameters for total time and initial time"
                        params = {'form': form, 'dform': dform, 'save': True, "total_time": total_time,
                                  "total_N": total_N, "error": error, 'counter': counter}
                        return render(request, "model_form.html", params)
                    else:
                        total_time = int(float(total_time))
                        total_N = int(total_N)
                        k_met1 = float(k_met1)
                        k_bile1 = float(k_bile1)
                        k_met2 = float(k_met2)
                        k_bile2 = float(k_bile2)
                        k_met3 = float(k_met3)
                        k_bile3 = float(k_bile3)
                        k_met4 = float(k_met4)
                        k_bile4 = float(k_bile4)
                        k_met5 = float(k_met5)
                        k_bile5 = float(k_bile5)
                        #convert list to list of floats and to list of ints
                        for e in dose:
                            e = float(e)
                            dose1.append(e)
                            e = int(e)
                            dose2.append(e)
                            #add the last element twice due to add the last couple for plotting
                        last_d = int(dose1[-1])
                        dose2.append(last_d)

                        for t in time:
                            t = float(t)
                            time1.append(t)
                            t = int(t)
                            time2.append(t)
                            #add the end time of simulation (time constists of initial times. For correct plotting it should be added one more couple)
                    time2.append(total_time)

                    model = PBPK_Model(new_model.bw, new_model.h, new_model.cardiac_output, new_drug.k_met,
                                       new_drug.k_bile, new_drug.k_kidney, new_drug.max_liver, new_drug.max_kidney,
                                       new_drug.max_influx,
                                       new_model.skin_flow_factor, new_model.skin_volume_fraction,
                                       new_model.blood_skin_fraction, new_drug.p_skin, new_drug.pi_skin,
                                       new_model.kidney_flow_factor, new_model.kidney_volume_fraction,
                                       new_model.blood_kidney_fraction, new_drug.p_kidney, new_drug.pi_kidney,
                                       new_model.bladder_flow_factor, new_model.bladder_volume_fraction,
                                       new_model.blood_bladder_fraction, new_drug.p_bladder, new_drug.pi_bladder,
                                       new_model.blood_rest_fraction, new_drug.p_rest, new_drug.pi_rest,
                                       new_model.liver_flow_factor, new_model.liver_volume_fraction,
                                       new_model.blood_liver_fraction, new_drug.p_liver, new_drug.pi_liver,
                                       new_model.blood_volume_fraction, new_drug.pi_rbc, new_drug.pi_plasma,
                                       new_model.lung_flow_factor, new_model.lung_volume_fraction,
                                       new_model.blood_lung_fraction, new_drug.p_lung, new_drug.pi_lung,
                                       new_drug.min_residual, new_drug.max_residual, new_drug.min_skin,
                                       new_drug.max_skin, new_drug.min_bladder, new_drug.max_bladder, new_drug.min_lung,
                                       new_drug.max_lung, new_drug.min_liver, new_drug.min_kidney,
                                       new_model.organ1_flow_factor, new_model.organ1_volume_fraction,
                                       new_model.blood_organ1_fraction, new_drug.p_organ1, new_drug.pi_organ1, type1,
                                       const1, k_met1, k_bile1,
                                       new_model.organ2_flow_factor, new_model.organ2_volume_fraction,
                                       new_model.blood_organ2_fraction, new_drug.p_organ2, new_drug.pi_organ2, type2,
                                       const2, k_met2, k_bile2,
                                       new_model.organ3_flow_factor, new_model.organ3_volume_fraction,
                                       new_model.blood_organ3_fraction, new_drug.p_organ3, new_drug.pi_organ3, type3,
                                       const3, k_met3, k_bile3,
                                       new_model.organ4_flow_factor, new_model.organ4_volume_fraction,
                                       new_model.blood_organ4_fraction, new_drug.p_organ4, new_drug.pi_organ4, type4,
                                       const4, k_met4, k_bile4,
                                       new_model.organ5_flow_factor, new_model.organ5_volume_fraction,
                                       new_model.blood_organ5_fraction, new_drug.p_organ5, new_drug.pi_organ5, type5,
                                       const5, k_met5, k_bile5,
                                       new_model.heart_flow_factor, new_model.heart_volume_fraction,
                                       new_model.blood_heart_fraction, new_drug.p_heart, new_drug.pi_heart,
                                       new_model.muscle_flow_factor, new_model.muscle_volume_fraction,
                                       new_model.blood_muscle_fraction, new_drug.p_muscle, new_drug.pi_muscle,
                                       new_model.spleen_flow_factor, new_model.spleen_volume_fraction,
                                       new_model.blood_spleen_fraction, new_drug.p_spleen, new_drug.pi_spleen,
                                       new_model.placental_flow_factor, new_model.placental_volume_fraction,
                                       new_model.blood_placental_fraction, new_drug.p_placental, new_drug.pi_placental)
                    skin = Skin(model)
                    kidney = Kidney(model)
                    bladder = Bladder(model)
                    residual = Residual(model)
                    liver = Liver(model)
                    blood = Blood(model)
                    lung = Lung(model)
                    organ1 = Organ1(model)
                    organ2 = Organ2(model)
                    organ3 = Organ3(model)
                    organ4 = Organ4(model)
                    organ5 = Organ5(model)
                    heart = Heart(model)
                    muscle = Muscle(model)
                    spleen = Spleen(model)
                    placental = Placental(model)

                    try:
                        mysystem = System(model, skin, kidney, bladder, residual, liver, blood, lung, organ1, organ2,
                                          organ3, organ4, organ5, heart, muscle, spleen, placental)
                        sim = SimulatorOpenLoop(mysystem, total_time, time1, dose1)
                        t, u = input_profile(total_time, time1, dose1)
                        cont, Tsim = sim.Simulate()
                        plot_j = []
                        # plot_j is of the following form
                        # [ [[0.0, y1.1], [0.01, y1.2], ...] -> organ1,  [[0.0, y2.1], [0.0, y2.2], ...] -> organ2, ... ] contains state variables of all organs
                        # adm_j contains administration rate
                        adm = []
                        for i in range(len(time2)):
                            adm.append([time2[i], dose2[i]])
                        print new_model.step_params
                        adm_j = json.dumps(adm)
                        new_model.step_params = adm_j
                        print new_model.step_params
                        print adm_j
                        for c in cont:
                            vals = []
                            for i in range(len(Tsim)):
                                vals.append([Tsim[i], c[i]])
                            plot_j.append(vals)

                        json_object_plot = json.dumps(plot_j)
                        new_model.plot_params = json_object_plot

                    except RuntimeError as re:
                        print(re)
                        error = "An error occurred while creating the model."
                        params = {'form': form, 'dform': dform, "save": True, 'error': error, 'counter': counter}
                        return render(request, "model_form.html", params)
                    except Exception as e:
                        print(e)
                        error = "An error occurred while creating the model."
                        params = {'form': form, 'dform': dform, "save": True, 'error': error, 'counter': counter}
                        return render(request, "model_form.html", params)

                    params = {'form': form, 'dform': dform, 'save': True, 'image': True, 'counter': counter,
                              'change': True, 'json': json_object_plot, 'adm': adm_j}
                    if request.is_ajax():
                        return HttpResponse(json_object_plot, 'application/json')

                    try:
                        new_drug.save()
                        new_model.save()
                    except IntegrityError:
                        error = "Modelname already exists."
                        params = {'form': form, 'dform': dform, "save": True, 'error': error, 'counter': counter}
                        return render(request, "model_form.html", params)

                    new_model.drugs.add(new_drug)
                    return render(request, "model_form.html", params)
                else:
                    error = "Your should define simulation parameters first."
                    params = {'form': form, 'dform': dform, "save": True, 'error': error, 'counter': counter}
                    return render(request, "model_form.html", params)
            else:

                try:
                    new_drug = dform.save()
                    new_model = form.save()
                except IntegrityError:
                    error = "Modelname already exists."
                    params = {'form': form, 'dform': dform, "save": True, 'error': error, 'counter': counter}
                    return render(request, "model_form.html", params)

                new_model.username = request.user.username

                new_model.drugs.clear()
                new_model.save()
                new_model.drugs.add(new_drug)

                modelid = new_model.id
                drugid = new_drug.id

                error = "Your model have been saved. If you want to run it, define simulation parameters."
                # params = {'form': form, 'dform': dform, "save": True,'edit':True, 'error': error, 'modelid':modelid, 'drugid':drugid}
                #return render(request, "model_form.html", params)
                return redirect(
                    '/edit_model?username=' + request.user.username + '&modelname=' + new_model.modelname + '&modelid=' + str(
                        modelid) + '&drugname=' + new_drug.drug_name + '&drugid=' + str(drugid) + '&error=' + error,
                    {'error': error})


def DefaultModel(request):
    default_form = ModelForm(prefix='mod',
                             initial={'modelname': 'default', 'bw': 0.03, 'h': 0.45, 'cardiac_output': 16.5,
                                      'skin_flow_factor': 0.058, 'skin_volume_fraction': 0.165,
                                      'blood_skin_fraction': 0.03,
                                      'kidney_flow_factor': 0.091, 'kidney_volume_fraction': 0.017,
                                      'blood_kidney_fraction': 0.24,
                                      'bladder_flow_factor': 0.0033, 'bladder_volume_fraction': 0.0009,
                                      'blood_bladder_fraction': 0.03,
                                      'blood_rest_fraction': 0.04, 'liver_flow_factor': 0.162,
                                      'liver_volume_fraction': 0.055, 'blood_liver_fraction': 0.31,
                                      'blood_volume_fraction': 0.5, 'lung_flow_factor': 1.0,
                                      'lung_volume_fraction': 0.007,
                                      'blood_lung_fraction': 0.5, 'method': 'none',
                                      'method_params': '{"N": 5, "intervals": 4, "step": 0.0833, "end": 4, "time": [0, 1, 2, 3 ], "setpoint": [4e-07, 4e-07, 4e-07, 4e-07], "time_int_final": [1, 2, 3, 4], "Q": 0.25, "R":5}'})
    default_drug_form = DrugForm(prefix='dr',
                                 initial={'drug_name': 'default drug', 'max_liver': 1.4e-6, 'max_kidney': 5.0e-6,
                                          'max_influx': 0.04e-6,
                                          'k_met': 0.06, 'k_bile': 0.0, 'k_kidney': 0.0164,
                                          'p_skin': 1.6, 'pi_skin': 0.0095,
                                          'p_kidney': 0.14, 'pi_kidney': 0.12,
                                          'p_bladder': 1.6, 'pi_bladder': 0.0095,
                                          'p_liver': 1.6, 'pi_liver': 0.0095,
                                          'p_rest': 1.6, 'pi_rest': 0.0095, 'pi_rbc': 1.3, 'pi_plasma': 0.81,
                                          'p_lung': 0.44, 'pi_lung': 0.94
                                 })
    if request.method == 'GET':
        params = {'form': default_form, 'dform': default_drug_form, 'default': True}
        return render(request, 'model_form.html', params)

    if request.method == 'POST':

        method = request.POST.get('mod-method')
        meth_par = request.POST.get('mod-method_params')

        params = {'form': default_form, 'dform': default_drug_form, 'default': True}

        if method == "CloseLoop-MPC":

            params_json = json.loads(meth_par)
            N = params_json['N']
            intervals = params_json['intervals']
            step = params_json['step']
            end = params_json['end']
            setpoint = params_json['setpoint']
            time = params_json['time']
            Q = params_json['Q']
            R = params_json['R']

            # change1=default_form.has_changed()
            if not (check_number(N) and check_number(intervals) and check_number(step) and check_number(end) and setpoint and time):
                error = "The data you entered aren't valid. Please try again."
                params = {'form': default_form, 'dform': default_drug_form, 'default': True, "N": N, "intervals": intervals,
                          "step": step, "end": end, "error": error}
                return render(request, "model_form.html", params)
            elif float(step) > float(end):
                error = "Wrong step and/or end time."
                params = {'form': default_form, 'dform': default_drug_form, 'default': True, "N": N, "intervals": intervals,
                          "step": step, "end": end, "error": error}
                return render(request, "model_form.html", params)
            else:
                N = int(N)
                intervals = int(intervals)
                step = float(step)
                end = float(end)
                Q = float(Q)
                R = float(R)
                setpoint1 = []
                setpoint2 = []
                time1 = []
                time2 = []
                for e in setpoint:
                    e = float(e)
                    setpoint1.append(e)
                    e = int(e)
                    setpoint2.append(e)
                    #add the last element twice due to add the last couple for plotting
                last_d = int(setpoint1[-1])
                setpoint2.append(last_d)

                for t in time:
                    t = float(t)
                    time1.append(t)
                    t = int(t)
                    time2.append(t)
                    #add the end time of simulation (time constists of initial times. For correct plotting it should be added one more couple)
                time2.append(end)
                '''filepath = path.abspath(path.join(path.dirname(path.dirname(__file__)), 'pbpk/static/results/default.png'))
                    if(os.path.exists(filepath) & change1 == False):

                        with open (filepath, "rb") as f:
                            data = f.read()
                            UU = data.encode("base64")
                            imgStr = "data: test/png;base64," + UU
                            params = {'form': default_form, 'dform': default_drug_form,'default': True, "img": UU ,'image': True}
                            return render(request, "model_form.html", params )
                    else:'''

            model = PBPK_Model(0.03, 0.45, 16.5, 0.07, 0.0, 0.0164, 1.4e-6, 5.0e-6, 0.04e-6,
                               0.058, 0.165, 0.03, 1.6, 0.0095, 0.091, 0.017, 0.24, 0.14, 0.12,
                               0.0033, 0.0009, 0.03, 1.6, 0.0095, 0.04, 1.6, 0.0095, 0.162, 0.055, 0.31, 1.6, 0.0095,
                               0.5, 1.3, 0.81, 1.0, 0.007, 0.5, 0.44, 0.94, 0.0, 1, 0.0, 1, 0.0, 1, 0.0, 1, 0.0, 0.0,
                               0.0, 0.0, 0.0, 0.0, 0.0, "", "", 0.0, 0.0,
                               0.0, 0.0, 0.0, 0.0, 0.0, "", "", 0.0, 0.0,
                               0.0, 0.0, 0.0, 0.0, 0.0, "", "", 0.0, 0.0,
                               0.0, 0.0, 0.0, 0.0, 0.0, "", "", 0.0, 0.0,
                               0.0, 0.0, 0.0, 0.0, 0.0, "", "", 0.0, 0.0,
                               0.0, 0.0, 0.0, 0.0, 0.0,
                               0.0, 0.0, 0.0, 0.0, 0.0,
                               0.0, 0.0, 0.0, 0.0, 0.0,
                               0.0, 0.0, 0.0, 0.0, 0.0)
            skin = Skin(model)
            kidney = Kidney(model)
            bladder = Bladder(model)
            residual = Residual(model)
            liver = Liver(model)
            blood = Blood(model)
            lung = Lung(model)
            organ1 = Organ1(model)
            organ2 = Organ2(model)
            organ3 = Organ3(model)
            organ4 = Organ4(model)
            organ5 = Organ5(model)
            heart = Heart(model)
            muscle = Muscle(model)
            spleen = Spleen(model)
            placental = Placental(model)

            mysystem = System(model, skin, kidney, bladder, residual, liver, blood, lung, organ1, organ2, organ3,
                              organ4, organ5, heart, muscle, spleen, placental)
            sys = mysystem.DiscreteSystem()
            d_hat = 1.74e-14 * np.ones((1, 1))
            x_hat = np.zeros((14, 1))
            sim = Simulator(mysystem, N, x_hat, d_hat, 1.4e-6, 5.0e-6, 0.04e-6, 0.0, 1, 0.0, 1, 0.0, 1, 0.0, 1, 0.0,
                            0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, end, time1, setpoint1, step, Q, R)
            Tsim, cont, ulist = sim.Simulate(step, end)
            plot_j = []
            # plot_j is of the following form
            # [ [[0.0, y1.1], [0.01, y1.2], ...] -> organ1,  [[0.0, y2.1], [0.0, y2.2], ...] -> organ2, ... ]
            adm = []
            for i in range(len(ulist)):
                adm.append([Tsim[i], ulist[i]])
            adm_j = json.dumps(adm)
            for c in cont:
                vals = []
                for i in range(len(Tsim)):
                    vals.append([Tsim[i], c[i]])

                plot_j.append(vals)

            json_object_plot = json.dumps(plot_j)

            params = {'form': default_form, 'dform': default_drug_form, 'default': True, 'image': True, 'change': True,
                      'json': json_object_plot, 'adm': adm_j}
            if request.is_ajax():
                return HttpResponse(json_object_plot, 'application/json')

            return render(request, "model_form.html", params)
        elif method == "CloseLoop-PID":
            return Http404  # todo implement CloseLoop-PID defaults
        elif method == "OpenLoop":  # OpenLoop

            # total_time = 5
            #total_N = 1
            #dose = 4.e-7
            #time = 0
            params_json = json.loads(meth_par)
            total_time = params_json['total_time']
            total_N = params_json['total_N']
            dose = params_json['dose']
            time = params_json['time']

            if not (check_number(total_time) and check_number(total_N) and dose and time):
                error = "The data you entered aren't valid. Please try again."
                params = {'form': default_form, 'dform': default_drug_form, 'default': True, "total_time": total_time,
                          "total_N": total_N, "error": error}
                return render(request, "model_form.html", params)
            elif time > total_time:
                error = "Wrong parameters for total time and initial time"
                params = {'form': default_form, 'dform': default_drug_form, 'default': True, "total_time": total_time,
                          "total_N": total_N, "error": error}
                return render(request, "model_form.html", params)
            else:
                total_time = int(float(total_time))
                total_N = int(total_N)
                dose1 = []
                dose2 = []
                time1 = []
                time2 = []
                for e in dose:
                    e = float(e)
                    dose1.append(e)
                    e = int(e)
                    dose2.append(e)
                    #add the last element twice due to add the last couple for plotting
                last_d = int(dose1[-1])
                dose2.append(last_d)

                for t in time:
                    t = float(t)
                    time1.append(t)
                    t = int(t)
                    time2.append(t)
                    #add the end time of simulation (time constists of initial times. For correct plotting it should be added one more couple)
                time2.append(total_time)

                model = PBPK_Model(0.03, 0.45, 16.5, 0.07, 0.0, 0.0164, 1.4e-6, 5.0e-6, 0.04e-6,
                                   0.058, 0.165, 0.03, 1.6, 0.0095, 0.091, 0.017, 0.24, 0.14, 0.12,
                                   0.0033, 0.0009, 0.03, 1.6, 0.0095, 0.04, 1.6, 0.0095, 0.162, 0.055, 0.31, 1.6,
                                   0.0095,
                                   0.5, 1.3, 0.81, 1.0, 0.007, 0.5, 0.44, 0.94, 0.0, 1, 0.0, 1, 0.0, 1, 0.0, 1, 0.0,
                                   0.0, 0.0, 0.0, 0.0, 0.0, 0.0, "", "", 0.0, 0.0,
                                   0.0, 0.0, 0.0, 0.0, 0.0, "", "", 0.0, 0.0,
                                   0.0, 0.0, 0.0, 0.0, 0.0, "", "", 0.0, 0.0,
                                   0.0, 0.0, 0.0, 0.0, 0.0, "", "", 0.0, 0.0,
                                   0.0, 0.0, 0.0, 0.0, 0.0, "", "", 0.0, 0.0,
                                   0.0, 0.0, 0.0, 0.0, 0.0,
                                   0.0, 0.0, 0.0, 0.0, 0.0,
                                   0.0, 0.0, 0.0, 0.0, 0.0,
                                   0.0, 0.0, 0.0, 0.0, 0.0)
                skin = Skin(model)
                kidney = Kidney(model)
                bladder = Bladder(model)
                residual = Residual(model)
                liver = Liver(model)
                blood = Blood(model)
                lung = Lung(model)
                organ1 = Organ1(model)
                organ2 = Organ2(model)
                organ3 = Organ3(model)
                organ4 = Organ4(model)
                organ5 = Organ5(model)
                heart = Heart(model)
                muscle = Muscle(model)
                spleen = Spleen(model)

                placental = Placental(model)

                mysystem = System(model, skin, kidney, bladder, residual, liver, blood, lung, organ1, organ2, organ3,
                                  organ4, organ5, heart, muscle, spleen, placental)
                sys = mysystem.ContinuousSystem()
                sim = SimulatorOpenLoop(mysystem, total_time, time1, dose1)
                t, u = input_profile(total_time, time1, dose1)
                cont, Tsim = sim.Simulate()
                plot_j = []
                # plot_j is of the following form
                # [ [[0.0, y1.1], [0.01, y1.2], ...] -> organ1,  [[0.0, y2.1], [0.0, y2.2], ...] -> organ2, ... ]

                adm = []
                for i in range(len(time2)):
                    adm.append([time2[i], dose2[i]])
                adm_j = adm
                print adm_j
                for c in cont:
                    vals = []
                    for i in range(len(Tsim)):
                        vals.append([Tsim[i], c[i]])
                    plot_j.append(vals)

                json_object_plot = plot_j

                params = {'form': default_form, 'dform': default_drug_form, 'default': True, 'image': True,
                          'change': True, 'json': json_object_plot, 'adm': adm_j}
                if request.is_ajax():
                    return HttpResponse(json_object_plot, 'application/json')
                return render(request, "model_form.html", params)
        else:
            error = "Please define the simulation parameters "
            params = {'form': default_form, 'dform': default_drug_form, 'default': True, 'error': error}
            return render(request, "model_form.html", params)


def EditIntermediate(request):
    # create list with all user's model names
    model_names = []
    models = Models.objects.filter(username=request.user.username)
    for model in models:
        model_names.append((model.modelname, model.modelname), )
    model_names.insert(0, ('', '-- choose a model --'))
    drug_choices = []
    drug_choices.insert(0, ('', '-- choose a model first --'))

    params = {}
    params = {
        "select_model": forms.Select(choices=model_names, attrs={'id': 'id_modelname', 'onchange': 'get_drug();'}).render(
            'modelname', 'modelname'),
        "select_drug": forms.Select(choices=drug_choices, attrs={'id': 'id_drugname'}).render('drug_name', 'drug_name')}

    if request.method == 'GET':
        return render(request, "edit_intermediate.html", params)

    if request.method == 'POST':
        if request.is_ajax():
            model_object = Models.objects.filter(modelname=request.POST.get('modelname'), username=request.user.username)[0]

            drug_options = []
            drug_options.insert(0, ('New', 'New Drug'))
            drugs = model_object.drugs.all()
            for drug in drugs:
                drug_options.append((drug.drug_name, drug.drug_name), )

            json_object = json.dumps(drug_options)
            return HttpResponse(json_object, 'application/json')

        else:
            modelname = request.POST.get("modelname")
            drugname = request.POST.get("drug_name")
            if not modelname or not drugname:
                params["error"] = "Please give a valid model name"
                return render(request, "edit_intermediate.html", params)
            if drugname == 'New':
                model_item = Models.objects.filter(username=request.user.username, modelname=modelname)[0]
                if not model_item:
                    params["error"] = "Please give a valid model name"
                    return render(request, "edit_intermediate.html", params)
                else:
                    drugid = '0'
                    modelid = model_item.id
                    return redirect(
                        '/edit_model?username=' + request.user.username + '&modelname=' + modelname + '&modelid=' + str(
                            modelid) + '&drugname=' + drugname + '&drugid=' + str(drugid))
            else:
                model_item = Models.objects.filter(username=request.user.username, modelname=modelname)[0]
                drug_item = Drug.objects.filter(drug_name=drugname)[0]
                drugid = drug_item.id
                modelid = model_item.id
                if not model_item:
                    params["error"] = "Please give a valid model name"
                    return render(request, "edit_intermediate.html", params)
                elif not drug_item:
                    params["error"] = "Please give a valid model name"
                    return render(request, "edit_intermediate.html", params)
                else:
                    return redirect(
                        '/edit_model?username=' + request.user.username + '&modelname=' + modelname + '&modelid=' + str(
                            modelid) + '&drugname=' + drugname + '&drugid=' + str(drugid))


def Edit(request):
    username = request.user.username
    if 'error' in request.GET:
        error = request.GET.get('error')
    else:
        error = ""

    if request.method == 'GET':
        modelname = request.GET.get('modelname')
        drugname = request.GET.get('drugname')
        drugid = request.GET.get('drugid')
        modelid = request.GET.get('modelid')

        counter = 1
    else:
        modelname = request.POST.get('mod-modelname')
        drugname = request.POST.get('dr-drug_name')
        drugid = request.POST.get('dr-drug_id')
        modelid = request.POST.get('model_id')
        meth = request.POST.get('mod-method')
    counter = 1
    read_models = Models.objects.filter(pk=modelid)
    if read_models:
        model_item = read_models[0]


        if (model_item.organ5_flow_factor) or (model_item.organ5_volume_fraction) or (model_item.blood_organ5_fraction) or (model_item.organ5_name):
            counter = counter + 5
        elif (model_item.organ4_flow_factor) or (model_item.organ4_volume_fraction) or (model_item.blood_organ4_fraction) or (model_item.organ4_name):
            counter = counter + 4
        elif (model_item.organ3_flow_factor) or (model_item.organ3_volume_fraction) or (model_item.blood_organ3_fraction) or (model_item.organ3_name):
            counter = counter + 3
        elif (model_item.organ2_flow_factor) or (model_item.organ2_volume_fraction) or (model_item.blood_organ2_fraction) or (model_item.organ2_name):
            counter = counter + 2
        elif (model_item.organ1_flow_factor) or (model_item.organ1_volume_fraction) or (model_item.blood_organ1_fraction) or (model_item.organ1_name):
            counter = counter + 1

    else:
        model_item = None

    read_drug = Drug.objects.filter(pk=drugid)
    if read_drug:
        drug = Drug.objects.get(pk=drugid)
        if not model_item or not drug:
            return Http404

        params = {'form': ModelForm(instance=model_item, prefix='mod'), 'dform': DrugForm(instance=drug, prefix='dr'),
                  "drugid": drugid, "modelid": modelid, 'edit': True, 'send': True, 'counter': counter}
    else:
        if not model_item:
            return Http404
        params = {'form': ModelForm(instance=model_item, prefix='mod'),
                  'dform': DrugForm(initial={'drug_name': ' '}, prefix='dr'), 'edit': True, 'counter': counter}

    if request.method == 'GET':
        if read_drug:
            drug = Drug.objects.get(pk=drugid)
            if not model_item or not drug:
                return Http404

            params = {'form': ModelForm(instance=model_item, prefix='mod'),
                      'dform': DrugForm(instance=drug, prefix='dr'), 'edit': True, "drugid": drugid, "modelid": modelid,
                      'send': True, 'counter': counter, 'error': error}
        else:
            if not model_item:
                return Http404

            params = {'form': ModelForm(instance=model_item, prefix='mod'),
                      'dform': DrugForm(initial={'drug_name': ' '}, prefix='dr'), 'edit': True, "drugid": drugid,
                      "modelid": modelid, 'send': True, 'counter': counter, 'error': error}
        return render(request, 'model_form.html', params)

    if request.method == 'POST':
        meth = model_item.method  # if user run the model without define openloop or closeloop, the method will be load from the database
        meth = request.POST.get('mod-method')  # if user choose the method.
        counter = request.POST.get('counter_id')
        read_drug = Drug.objects.filter(pk=drugid)
        if read_drug:
            drug = Drug.objects.get(pk=drugid)
            form = ModelForm(request.POST, instance=model_item, prefix='mod')
            dform = DrugForm(request.POST, instance=drug, prefix='dr')

        else:
            if not model_item:
                return Http404
            form = ModelForm(request.POST, instance=model_item, prefix='mod')
            dform = DrugForm(request.POST, prefix='dr')

        if not form.is_valid() or not dform.is_valid():
            params = {'form': form, 'dform': dform, 'edit': True, "drugid": drugid, "modelid": modelid, 'send': True,
                      'counter': counter}
            return render(request, "model_form.html", params)
        elif ( ( ( (form['lung_flow_factor'].value() != "0.0") | (form['lung_volume_fraction'].value() != "0.0") | (form['blood_lung_fraction'].value() != "0.0") )& ( (dform['pi_lung'].value() == "0.0") | (dform['p_lung'].value() == "0.0") ) )| (
            ( (form['skin_flow_factor'].value() != "0.0") | (form['skin_volume_fraction'].value() != "0.0") | (form['blood_skin_fraction'].value() != "0.0") )& ( (dform['pi_skin'].value() == "0.0") | (dform['p_skin'].value() == "0.0") ) )| (
            ( (form['kidney_flow_factor'].value() != "0.0") | (form['kidney_volume_fraction'].value() != "0.0") | (form['blood_kidney_fraction'].value() != "0.0") )& ( (dform['pi_kidney'].value() == "0.0") | (dform['p_kidney'].value() == "0.0") ) )| (
            ( (form['bladder_flow_factor'].value() != "0.0") | (form['bladder_volume_fraction'].value() != "0.0") | (form['blood_bladder_fraction'].value() != "0.0") )& ( (dform['pi_bladder'].value() == "0.0") | (dform['p_bladder'].value() == "0.0") ) )| (
            ( (form['blood_rest_fraction'].value() != "0.0") )& ( (dform['pi_rest'].value() == "0.0") | (dform['p_rest'].value() == "0.0") ) )| (
            ( (form['liver_flow_factor'].value() != "0.0") | (form['liver_volume_fraction'].value() != "0.0") | (form['blood_liver_fraction'].value() != "0.0") )& ( (dform['pi_liver'].value() == "0.0") | (dform['p_liver'].value() == "0.0") ) )| (
            ( (form['blood_volume_fraction'].value() != "0.0") )& ( (dform['pi_rbc'].value() == "0.0") | (dform['pi_plasma'].value() == "0.0") ) )| (
            ( (form['organ1_flow_factor'].value() != "0.0") | (form['organ1_volume_fraction'].value() != "0.0") | (form['blood_organ1_fraction'].value() != "0.0") )& ( (dform['pi_organ1'].value() == "0.0") | (dform['p_organ1'].value() == "0.0") ) )| (
            ( (form['organ2_flow_factor'].value() != "0.0") | (form['organ2_volume_fraction'].value() != "0.0") | (form['blood_organ2_fraction'].value() != "0.0") )& ( (dform['pi_organ2'].value() == "0.0") | (dform['p_organ2'].value() == "0.0") ) )| (
            ( (form['organ3_flow_factor'].value() != "0.0") | (form['organ3_volume_fraction'].value() != "0.0") | (form['blood_organ3_fraction'].value() != "0.0") )& ( (dform['pi_organ3'].value() == "0.0") | (dform['p_organ3'].value() == "0.0") ) )| (
            ( (form['organ4_flow_factor'].value() != "0.0") | (form['organ4_volume_fraction'].value() != "0.0") | (form['blood_organ4_fraction'].value() != "0.0") )& ( (dform['pi_organ4'].value() == "0.0") | (dform['p_organ4'].value() == "0.0") ) )| (
            ( (form['organ5_flow_factor'].value() != "0.0") | (form['organ5_volume_fraction'].value() != "0.0") | (form['blood_organ5_fraction'].value() != "0.0") )& ( (dform['pi_organ5'].value() == "0.0") | (dform['p_organ5'].value() == "0.0") ) )
        ):
                error = "Model has some errors. Please check drug properties"
                params = {'form': form, 'dform': dform, "edit": True, 'error': error, 'drugid': drugid, 'modelid': modelid, 'send': True,
                          'counter': counter}

                return render(request, "model_form.html", params)

        else:
            k_bile5 = 0.0
            k_met5 = 0.0
            k_bile4 = 0.0
            k_met4 = 0.0
            k_bile3 = 0.0
            k_met3 = 0.0
            k_bile2 = 0.0
            k_met2 = 0.0
            k_bile1 = 0.0
            k_met1 = 0.0
            type1 = ""
            const1 = ""
            type2 = ""
            const2 = ""
            type3 = ""
            const3 = ""
            type4 = ""
            const4 = ""
            type5 = ""
            const5 = ""
            if meth == "CloseLoop-MPC":
                # if user create new drug, create and save it
                if not read_drug:
                    drug = dform.save(commit=False)
                    new_model = form.save(commit=False)
                else:
                    drug = Drug.objects.get(pk=drugid)
                    drug = dform.save(commit=False)
                    model_item = form.save(commit=False)

                model_id = model_item.id
                #model_name = model_item.modelname
                #convert method_params to json and read values
                if drug.organ1_params:
                    org1_params_json = json.loads(drug.organ1_params)
                    if org1_params_json[0]:
                        type1 = org1_params_json[0]['type']
                        if type1 == "met":
                            const1 = org1_params_json[0]['const']
                            k_met1 = org1_params_json[0]['k_met']
                            k_bile1 = org1_params_json[0]['k_bile']
                    if org1_params_json[1]:
                        type2 = org1_params_json[1]['type']
                        if type2 == "met":
                            const2 = org1_params_json[1]['const']
                            k_met2 = org1_params_json[1]['k_met']
                            k_bile2 = org1_params_json[1]['k_bile']

                    if org1_params_json[2]:
                        type3 = org1_params_json[2]['type']
                        if type3 == "met":
                            const3 = org1_params_json[2]['const']
                            k_met3 = org1_params_json[2]['k_met']
                            k_bile3 = org1_params_json[2]['k_bile']
                    if org1_params_json[3]:
                        type4 = org1_params_json[3]['type']
                        if type4 == "met":
                            const4 = org1_params_json[3]['const']
                            k_met4 = org1_params_json[3]['k_met']
                            k_bile4 = org1_params_json[3]['k_bile']
                    if org1_params_json[4]:
                        type5 = org1_params_json[4]['type']
                        if type5 == "met":
                            const5 = org1_params_json[4]['const']
                            k_met5 = org1_params_json[4]['k_met']
                            k_bile5 = org1_params_json[4]['k_bile']
                params_json = json.loads(model_item.method_params)
                N = params_json['N']
                intervals = params_json ['intervals']
                step = params_json['step']
                end = params_json['end']
                setpoint = params_json['setpoint']
                time = params_json['time']
                Q = params_json['Q']
                R = params_json['R']
                if not (check_number(N) and check_number(intervals) and check_number(step) and check_number(
                        end) and setpoint and time and check_number(k_bile1) and check_number(k_bile2) and check_number(
                        k_bile3) and check_number(k_bile4)
                        and check_number(k_bile5) and check_number(k_met1) and check_number(k_met2) and check_number(
                        k_met3) and check_number(k_met4) and check_number(k_met5)):
                    error = "The data you entered aren't valid. Please try again."
                    return render(request, "model_form.html", {'form': ModelForm(instance=model_item, prefix='mod'),
                                                               'dform': DrugForm(instance=drug, prefix='dr'),
                                                               'edit': True, "N": N, "target": intervals, "error": error,
                                                               "step": step, "end": end, "drugid": drugid,
                                                               "modelid": modelid, 'send': True, 'counter': counter})
                elif float(step) > float(end):
                    error = "Wrong step and/or end time."
                    return render(request, "model_form.html", {'form': ModelForm(instance=model_item, prefix='mod'),
                                                               'dform': DrugForm(instance=drug, prefix='dr'),
                                                               'edit': True, "N": N, "target": intervals, "error": error,
                                                               "step": step, "end": end, "drugid": drugid,
                                                               "modelid": modelid, 'send': True, 'counter': counter})
                else:

                    N = int(N)
                    intervals = int(intervals)
                    step = float(step)
                    end = float(end)
                    Q = float(Q)
                    R = float(R)
                    setpoint1 = []
                    setpoint2 = []
                    time1 = []
                    time2 = []
                    for e in setpoint:
                        e = float(e)
                        setpoint1.append(e)
                        e = int(e)
                        setpoint2.append(e)
                         #add the last element twice due to add the last couple for plotting
                    last_d = int(setpoint1[-1])
                    setpoint2.append(last_d)

                    for t in time:
                        t = float(t)
                        time1.append(t)
                        t = int(t)
                        time2.append(t)
                        #add the end time of simulation (time constists of initial times. For correct plotting it should be added one more couple)
                    time2.append(end)

                    k_met1 = float(k_met1)
                    k_bile1 = float(k_bile1)
                    k_met2 = float(k_met2)
                    k_bile2 = float(k_bile2)
                    k_met3 = float(k_met3)
                    k_bile3 = float(k_bile3)
                    k_met4 = float(k_met4)
                    k_bile4 = float(k_bile4)
                    k_met5 = float(k_met5)
                    k_bile5 = float(k_bile5)
                '''model = Models.objects.get(pk=model_item.id)
                print model
                if model_item.step_params == "":
                    form.fields['step_params'].initial =model.step_params
                if model_item.plot_params == "":
                    form.fields['plot_params'].initial =model.plot_params
                print form
                print form.has_changed()'''

                if (not form.has_changed()) and (not dform.has_changed()) and model_item.plot_params:
                    # if model & drug haven't changed, load from database
                    json_object_plot = json.loads(model_item.plot_params)
                    adm_j = json.loads(model_item.step_params)
                    params = {'form': form, 'dform': dform, 'edit': True, 'image': True, "drugid": drugid,
                              "modelid": modelid, 'send': True, 'counter': counter, 'adm': adm_j,
                              'json': json_object_plot}
                    if request.is_ajax():
                        return HttpResponse(json_object_plot, 'application/json')
                    return render(request, "model_form.html", params)
                else:
                    # changes detected, create the graph again

                    ### Check PBPK Class
                    model = PBPK_Model(model_item.bw, model_item.h, model_item.cardiac_output, drug.k_met, drug.k_bile,
                                       drug.k_kidney, drug.max_liver, drug.max_kidney, drug.max_influx,
                                       model_item.skin_flow_factor, model_item.skin_volume_fraction,
                                       model_item.blood_skin_fraction, drug.p_skin, drug.pi_skin,
                                       model_item.kidney_flow_factor, model_item.kidney_volume_fraction,
                                       model_item.blood_kidney_fraction, drug.p_kidney, drug.pi_kidney,
                                       model_item.bladder_flow_factor, model_item.bladder_volume_fraction,
                                       model_item.blood_bladder_fraction, drug.p_bladder, drug.pi_bladder,
                                       model_item.blood_rest_fraction, drug.p_rest, drug.pi_rest,
                                       model_item.liver_flow_factor, model_item.liver_volume_fraction,
                                       model_item.blood_liver_fraction, drug.p_liver, drug.pi_liver,
                                       model_item.blood_volume_fraction, drug.pi_rbc, drug.pi_plasma,
                                       model_item.lung_flow_factor, model_item.lung_volume_fraction,
                                       model_item.blood_lung_fraction, drug.p_lung, drug.pi_lung,
                                       drug.min_residual, drug.max_residual, drug.min_skin, drug.max_skin,
                                       drug.min_bladder, drug.max_bladder, drug.min_lung, drug.max_lung, drug.min_liver,
                                       drug.min_kidney,
                                       model_item.organ1_flow_factor, model_item.organ1_volume_fraction,
                                       model_item.blood_organ1_fraction, drug.p_organ1, drug.pi_organ1, type1, const1,
                                       k_met1, k_bile1,
                                       model_item.organ2_flow_factor, model_item.organ2_volume_fraction,
                                       model_item.blood_organ2_fraction, drug.p_organ2, drug.pi_organ2, type2, const2,
                                       k_met2, k_bile2,
                                       model_item.organ3_flow_factor, model_item.organ3_volume_fraction,
                                       model_item.blood_organ3_fraction, drug.p_organ3, drug.pi_organ3, type3, const3,
                                       k_met3, k_bile3,
                                       model_item.organ4_flow_factor, model_item.organ4_volume_fraction,
                                       model_item.blood_organ4_fraction, drug.p_organ4, drug.pi_organ4, type4, const4,
                                       k_met4, k_bile4,
                                       model_item.organ5_flow_factor, model_item.organ5_volume_fraction,
                                       model_item.blood_organ5_fraction, drug.p_organ5, drug.pi_organ5, type5, const5,
                                       k_met5, k_bile5,
                                       model_item.heart_flow_factor, model_item.heart_volume_fraction,
                                       model_item.blood_heart_fraction, drug.p_heart, drug.pi_heart,
                                       model_item.muscle_flow_factor, model_item.muscle_volume_fraction,
                                       model_item.blood_muscle_fraction, drug.p_muscle, drug.pi_muscle,
                                       model_item.spleen_flow_factor, model_item.spleen_volume_fraction,
                                       model_item.blood_spleen_fraction, drug.p_spleen, drug.pi_spleen,
                                       model_item.placental_flow_factor, model_item.placental_volume_fraction,
                                       model_item.blood_placental_fraction, drug.p_placental, drug.pi_placental)

                    skin = Skin(model)
                    kidney = Kidney(model)
                    bladder = Bladder(model)
                    residual = Residual(model)
                    liver = Liver(model)
                    blood = Blood(model)
                    lung = Lung(model)
                    organ1 = Organ1(model)
                    organ2 = Organ2(model)
                    organ3 = Organ3(model)
                    organ4 = Organ4(model)
                    organ5 = Organ5(model)
                    heart = Heart(model)
                    muscle = Muscle(model)
                    spleen = Spleen(model)
                    placental = Placental(model)
                    try:
                        mysystem = System(model, skin, kidney, bladder, residual, liver, blood, lung, organ1, organ2,
                                              organ3, organ4, organ5, heart, muscle, spleen, placental)
                        sys = mysystem.DiscreteSystem()
                        d_hat = 1.7408e-14 * np.ones((1, 1))
                        x_hat = np.zeros((sys.A.shape[0], 1))
                        sim = Simulator(mysystem, N, x_hat, d_hat, drug.max_liver, drug.max_kidney, drug.max_influx,
                                            drug.min_residual, drug.max_residual, drug.min_skin, drug.max_skin,
                                            drug.min_bladder, drug.max_bladder, drug.min_lung, drug.max_lung,
                                            drug.min_liver, drug.min_kidney,
                                            drug.min_heart, drug.max_heart, drug.min_muscle, drug.max_muscle,
                                            drug.min_spleen, drug.max_spleen, drug.min_placental, drug.max_placental, end, time1, setpoint1, step, Q, R)
                        Tsim, cont, ulist = sim.Simulate(step, end)
                        plot_j = []

                        # plot_j is of the following form
                        # [ [[0.0, y1.1], [0.01, y1.2], ...] -> organ1,  [[0.0, y2.1], [0.0, y2.2], ...] -> organ2, ... ]
                        adm = []
                        for i in range(len(ulist)):
                            adm.append([Tsim[i], ulist[i]])
                        adm_j = json.dumps(adm)
                        model_item.step_params = adm_j

                        for c in cont:
                            vals = []
                            for i in range(len(Tsim)):
                                vals.append([Tsim[i], c[i]])

                            plot_j.append(vals)

                        json_object_plot = json.dumps(plot_j)
                        model_item.plot_params = json_object_plot

                    except RuntimeError as re:
                        error = "An error occurred while creating the model: ", re
                        params = {'form': form, 'dform': dform, "save": True, "edit": True, 'error': error,
                                  "drugid": drugid, "modelid": modelid, 'send': True, 'counter': counter}
                        return render(request, "model_form.html", params)

                    except Exception as e:
                        error = "An error occurred while creating the model: ", e
                        params = {'form': form, 'dform': dform, "save": True, "edit": True, 'error': error,
                                  "drugid": drugid, "modelid": modelid, 'send': True, 'counter': counter}
                        return render(request, "model_form.html", params)
                    #if user does not change modelname save user changes to the existing model.
                    if 'modelname' not in form.changed_data:

                        if not read_drug:
                            drug = dform.save()
                            new_model = form.save()
                            new_model.drugs.add(drug)
                        else:
                            drug = Drug.objects.get(pk=drugid)
                            dform.save()
                            form.save()
                    #if user change modelname create new model and save it.
                    else:
                        form = ModelForm(request.POST, prefix="mod")
                        dform = DrugForm(request.POST, prefix="dr")
                        new_drug = dform.save(commit=False)
                        new_model = form.save(commit=False)
                        new_model.username = request.user.username
                        new_drug.save()
                        new_model.save()
                        new_model.drugs.add(new_drug)

                    params = {'form': form, 'dform': dform, 'edit': True, 'image': True, "drugid": drugid,
                              "modelid": modelid, 'send': True, 'change': True, 'counter': counter, 'adm': adm_j,
                              'json': json_object_plot}
                    if request.is_ajax():
                        return HttpResponse(json_object_plot, 'application/json')
                    return render(request, "model_form.html", params)

            elif meth == "OpenLoop":
                # if user create new drug, create and save it
                if not read_drug:
                    drug = dform.save(commit=False)
                    new_model = form.save(commit=False)
                else:
                    drug = Drug.objects.get(pk=drugid)
                    drug = dform.save(commit=False)
                    model_item = form.save(commit=False)
                model_id = model_item.id
                #model_name = model_item.modelname
                #code for openloop
                print drug.organ1_params
                print model_item.organ1_flow_factor
                print model_item.organ1_volume_fraction
                print model_item.organ2_flow_factor
                print model_item.organ2_volume_fraction
                #convert method_params to json and read values
                if drug.organ1_params:
                    org1_params_json = json.loads(drug.organ1_params)
                    if org1_params_json[0]:
                        type1 = org1_params_json[0]['type']
                        if type1 == "met":
                            const1 = org1_params_json[0]['const']
                            k_met1 = org1_params_json[0]['k_met']
                            k_bile1 = org1_params_json[0]['k_bile']
                            print (const1)
                            #print(type1)
                    if org1_params_json[1]:
                        if org1_params_json[1]['type']:
                            type2 = org1_params_json[1]['type']
                            if type2 == "met":
                                const2 = org1_params_json[1]['const']
                                k_met2 = org1_params_json[1]['k_met']
                                k_bile2 = org1_params_json[1]['k_bile']
                    if org1_params_json[2]:
                        if org1_params_json[2]['type']:
                            type3 = org1_params_json[2]['type']
                            if type3 == "met":
                                const3 = org1_params_json[2]['const']
                                k_met3 = org1_params_json[2]['k_met']
                                k_bile3 = org1_params_json[2]['k_bile']
                    if org1_params_json[3]:
                        type4 = org1_params_json[3]['type']
                        if org1_params_json[3]['type']:
                            if type4 == "met":
                                const4 = org1_params_json[3]['const']
                                k_met4 = org1_params_json[3]['k_met']
                                k_bile4 = org1_params_json[3]['k_bile']
                    if org1_params_json[4]:
                        type5 = org1_params_json[4]['type']
                        if org1_params_json[4]['type']:
                            if type5 == "met":
                                const5 = org1_params_json[4]['const']
                                k_met5 = org1_params_json[4]['k_met']
                                k_bile5 = org1_params_json[4]['k_bile']

                params_json = json.loads(model_item.method_params)
                total_time = params_json['total_time']
                total_N = params_json['total_N']
                dose = params_json['dose']
                time = params_json['time']
                if not (check_number(total_time) and check_number(total_N) and dose and time and check_number(
                        k_bile1) and check_number(k_bile2) and check_number(k_bile3) and check_number(k_bile4)
                        and check_number(k_bile5) and check_number(k_met1) and check_number(k_met2) and check_number(
                        k_met3) and check_number(k_met4) and check_number(k_met5)):
                    error = "The data you entered aren't valid. Please try again."
                    params = {'form': form, 'dform': dform, 'edit': True, "total_time": total_time, "total_N": total_N,
                              "error": error, "drugid": drugid, "modelid": modelid, 'send': True, 'counter': counter}
                    return render(request, "model_form.html", params)
                elif time > total_time:
                    error = "Wrong parameters for total time and initial time"
                    params = {'form': form, 'dform': dform, 'edit': True, "total_time": total_time, "total_N": total_N,
                              "error": error, "drugid": drugid, "modelid": modelid, 'send': True, 'counter': counter}
                    return render(request, "model_form.html", params)
                else:
                    total_time = int(float(total_time))
                    total_N = int(total_N)
                    k_met1 = float(k_met1)
                    k_bile1 = float(k_bile1)
                    k_met2 = float(k_met2)
                    k_bile2 = float(k_bile2)
                    k_met3 = float(k_met3)
                    k_bile3 = float(k_bile3)
                    k_met4 = float(k_met4)
                    k_bile4 = float(k_bile4)
                    k_met5 = float(k_met5)
                    k_bile5 = float(k_bile5)

                    dose1 = []
                    dose2 = []
                    time1 = []
                    time2 = []

                    for e in dose:
                        e = float(e)
                        dose1.append(e)
                        e = int(e)
                        dose2.append(e)
                    #add the last element twice due to add the last couple for plotting
                    last_d = int(dose1[-1])
                    dose2.append(last_d)

                    for t in time:
                        t = float(t)
                        time1.append(t)
                        t = int(t)
                        time2.append(t)
                    #add the end time of simulation (time consists of initial times. For correct plotting it should be added one more couple)
                    time2.append(total_time)

                if (not form.has_changed()) and (not dform.has_changed()) and model_item.plot_params:
                    # if model & drug haven't changed, load from database
                    json_object_plot = json.loads(model_item.plot_params)
                    adm_j = json.loads(model_item.step_params)
                    params = {'form': form, 'dform': dform, 'edit': True, 'image': True, "drugid": drugid,
                              "modelid": modelid, 'send': True, 'counter': counter, 'json': json_object_plot,
                              'adm': adm_j}
                    if request.is_ajax():
                        return HttpResponse(json_object_plot, 'application/json')
                    return render(request, "model_form.html", params)

                else:
                    # changes detected, create the graph again

                    ### Check PBPK Class
                    model = PBPK_Model(model_item.bw, model_item.h, model_item.cardiac_output, drug.k_met, drug.k_bile,
                                       drug.k_kidney, drug.max_liver, drug.max_kidney, drug.max_influx,
                                       model_item.skin_flow_factor, model_item.skin_volume_fraction,
                                       model_item.blood_skin_fraction, drug.p_skin, drug.pi_skin,
                                       model_item.kidney_flow_factor, model_item.kidney_volume_fraction,
                                       model_item.blood_kidney_fraction, drug.p_kidney, drug.pi_kidney,
                                       model_item.bladder_flow_factor, model_item.bladder_volume_fraction,
                                       model_item.blood_bladder_fraction, drug.p_bladder, drug.pi_bladder,
                                       model_item.blood_rest_fraction, drug.p_rest, drug.pi_rest,
                                       model_item.liver_flow_factor, model_item.liver_volume_fraction,
                                       model_item.blood_liver_fraction, drug.p_liver, drug.pi_liver,
                                       model_item.blood_volume_fraction, drug.pi_rbc, drug.pi_plasma,
                                       model_item.lung_flow_factor, model_item.lung_volume_fraction,
                                       model_item.blood_lung_fraction, drug.p_lung, drug.pi_lung,
                                       drug.min_residual, drug.max_residual, drug.min_skin, drug.max_skin,
                                       drug.min_bladder, drug.max_bladder, drug.min_lung, drug.max_lung, drug.min_liver,
                                       drug.min_kidney,
                                       model_item.organ1_flow_factor, model_item.organ1_volume_fraction,
                                       model_item.blood_organ1_fraction, drug.p_organ1, drug.pi_organ1, type1, const1,
                                       k_met1, k_bile1,
                                       model_item.organ2_flow_factor, model_item.organ2_volume_fraction,
                                       model_item.blood_organ2_fraction, drug.p_organ2, drug.pi_organ2, type2, const2,
                                       k_met2, k_bile2,
                                       model_item.organ3_flow_factor, model_item.organ3_volume_fraction,
                                       model_item.blood_organ3_fraction, drug.p_organ3, drug.pi_organ3, type3, const3,
                                       k_met3, k_bile3,
                                       model_item.organ4_flow_factor, model_item.organ4_volume_fraction,
                                       model_item.blood_organ4_fraction, drug.p_organ4, drug.pi_organ4, type4, const4,
                                       k_met4, k_bile4,
                                       model_item.organ5_flow_factor, model_item.organ5_volume_fraction,
                                       model_item.blood_organ5_fraction, drug.p_organ5, drug.pi_organ5, type5, const5,
                                       k_met5, k_bile5,
                                       model_item.heart_flow_factor, model_item.heart_volume_fraction,
                                       model_item.blood_heart_fraction, drug.p_heart, drug.pi_heart,
                                       model_item.muscle_flow_factor, model_item.muscle_volume_fraction,
                                       model_item.blood_muscle_fraction, drug.p_muscle, drug.pi_muscle,
                                       model_item.spleen_flow_factor, model_item.spleen_volume_fraction,
                                       model_item.blood_spleen_fraction, drug.p_spleen, drug.pi_spleen,
                                       model_item.placental_flow_factor, model_item.placental_volume_fraction,
                                       model_item.blood_placental_fraction, drug.p_placental, drug.pi_placental)

                    skin = Skin(model)
                    kidney = Kidney(model)
                    bladder = Bladder(model)
                    residual = Residual(model)
                    liver = Liver(model)
                    blood = Blood(model)
                    lung = Lung(model)
                    organ1 = Organ1(model)
                    organ2 = Organ2(model)
                    organ3 = Organ3(model)
                    organ4 = Organ4(model)
                    organ5 = Organ5(model)
                    heart = Heart(model)
                    muscle = Muscle(model)
                    spleen = Spleen(model)
                    placental = Placental(model)

                    try:
                        mysystem = System(model, skin, kidney, bladder, residual, liver, blood, lung, organ1, organ2,
                                          organ3, organ4, organ5, heart, muscle, spleen, placental)
                        sys = mysystem.ContinuousSystem()
                        sim = SimulatorOpenLoop(mysystem, total_time, time1, dose1)
                        t, u = input_profile(total_time, time1, dose1)
                        cont, Tsim = sim.Simulate()
                        plot_j = []
                        # plot_j is of the following form
                        # [ [[0.0, y1.1], [0.01, y1.2], ...] -> organ1,  [[0.0, y2.1], [0.0, y2.2], ...] -> organ2, ... ]

                        adm = []
                        for i in range(len(time2)):
                            adm.append([time2[i], dose2[i]])
                        adm_j = json.dumps(adm)
                        model_item.step_params = adm_j
                        for c in cont:
                            vals = []
                            for i in range(len(Tsim)):
                                vals.append([Tsim[i], c[i]])
                            plot_j.append(vals)

                        json_object_plot = json.dumps(plot_j)
                        model_item.plot_params = json_object_plot

                    except RuntimeError as re:
                        error = "An error occurred while creating the model: ", re
                        params = {'form': form, 'dform': dform, "save": True, "edit": True, 'error': error,
                                  "drugid": drugid, "modelid": modelid, 'send': True, 'counter': counter}
                        return render(request, "model_form.html", params)

                    except Exception as e:
                        error = "An error occurred while creating the model: ", e
                        params = {'form': form, 'dform': dform, "save": True, "edit": True, 'error': error,
                                  "drugid": drugid, "modelid": modelid, 'send': True, 'counter': counter}
                        return render(request, "model_form.html", params)

                    #if user does not change modelname save user changes to the existing model.
                    if 'modelname' not in form.changed_data:

                        if not read_drug:
                            drug = dform.save()
                            new_model = form.save()
                            new_model.drugs.add(drug)
                        else:
                            drug = Drug.objects.get(pk=drugid)
                            dform.save()
                            form.save()
                    #if user change modelname create new model and save it.
                    else:
                        form = ModelForm(request.POST, prefix="mod")
                        dform = DrugForm(request.POST, prefix="dr")
                        new_drug = dform.save(commit=False)
                        new_model = form.save(commit=False)
                        new_model.username = request.user.username
                        new_drug.save()
                        new_model.save()
                        new_model.drugs.add(new_drug)
                    params = {'form': form, 'dform': dform, 'edit': True, 'image': True, "drugid": drugid,
                              "modelid": modelid, 'send': True, 'counter': counter, 'change': True, 'adm': adm_j,
                              'json': json_object_plot}
                    if request.is_ajax():
                        return HttpResponse(json_object_plot, 'application/json')
                    return render(request, "model_form.html", params)
            else:
                # if user create new drug and save it
                if not read_drug:
                    drug = dform.save(commit=False)
                    new_model = form.save(commit=False)
                    #new_model.drugs.add(drug)
                else:
                    drug = Drug.objects.get(pk=drugid)
                    dform.save(commit=False)
                    form.save(commit=False)

                error = "You should define simulation parameters first! "
                return render(request, "model_form.html",
                              {'form': ModelForm(request.POST, instance=model_item, prefix='mod'),
                               'dform': DrugForm(request.POST, instance=drug, prefix='dr'), 'edit': True,
                               "error": error, "drugid": drugid, "modelid": modelid, 'send': True, 'counter': counter})


def delete(request):
    # create list with all user's model names
    model_names = []
    models = Models.objects.filter(username=request.user.username)
    for model in models:
        model_names.append((model.modelname, model.modelname), )
    model_names.insert(0, ('', '-- choose a model --'))
    drug_choices = []
    drug_choices.insert(0, ('', '-- choose a model first --'))

    params = {}
    params = {
        "select_model": forms.Select(choices=model_names, attrs={'id': 'id_modelname', 'onchange': 'get_drug();'}).render(
            'modelname', 'modelname'),
        "select_drug": forms.Select(choices=drug_choices, attrs={'id': 'id_drugname'}).render('drug_name', 'drug_name')}

    if request.method == 'GET':
        return render(request, "delete_model.html", params)

    if request.method == 'POST':
        if request.is_ajax():
            model_object = Models.objects.filter(modelname=request.POST.get('modelname'))[0]

            drug_options = []
            drug_options.insert(0, ('model', 'All drugs and model'))
            drugs = model_object.drugs.all()
            for drug in drugs:
                drug_options.append((drug.drug_name, drug.drug_name), )

            json_object = json.dumps(drug_options)
            return HttpResponse(json_object, 'application/json')

        else:
            modelname = request.POST.get("modelname")
            drugname = request.POST.get("drug_name")
            if not modelname or not drugname:
                params["error"] = "Please give a valid model name"
                return render(request, "delete_model.html", params)
            if drugname == 'model':
                model_item = Models.objects.filter(username=request.user.username, modelname=modelname)[0]
                if not model_item:
                    params["error"] = "Please give a valid model name"
                    return render(request, "delete_model.html", params)
                else:
                    drugs = model_item.drugs.all()
                    for drug in drugs:
                        drug.delete()
                    model_item.delete()
                    return render(request, "delete.html")
            else:
                model_item = Models.objects.filter(username=request.user.username, modelname=modelname)[0]
                drug_item = Drug.objects.filter(drug_name=drugname)[0]
                if not model_item:
                    params["error"] = "Please give a valid model name"
                    return render(request, "delete_model.html", params)
                elif not drug_item:
                    params["error"] = "Please give a valid model name"
                    return render(request, "delete_model.html", params)
                else:
                    drug_item.delete()
                    return render(request, "delete_drug.html")


def user_profile(request):
    #get all user's models
    models = Models.objects.filter(username=request.user.username)
     #get all drugs !!this should changed user should see his drugs not all.!!
    list_of_drugs = []
    for model in models:
        drugs = model.drugs.all()
        for drug in drugs:
            list_of_drugs.append(drug)

    return render(request, "user_profile.html", {'models': models, 'drugs': list_of_drugs})

def tutorial(request):
    default_form = ModelForm(prefix='mod',
                             initial={'modelname': 'default', 'bw': 0.03, 'h': 0.45, 'cardiac_output': 16.5,
                                      'skin_flow_factor': 0.058, 'skin_volume_fraction': 0.165,
                                      'blood_skin_fraction': 0.03,
                                      'kidney_flow_factor': 0.091, 'kidney_volume_fraction': 0.017,
                                      'blood_kidney_fraction': 0.24,
                                      'bladder_flow_factor': 0.0033, 'bladder_volume_fraction': 0.0009,
                                      'blood_bladder_fraction': 0.03,
                                      'blood_rest_fraction': 0.04, 'liver_flow_factor': 0.162,
                                      'liver_volume_fraction': 0.055, 'blood_liver_fraction': 0.31,
                                      'blood_volume_fraction': 0.5, 'lung_flow_factor': 1.0,
                                      'lung_volume_fraction': 0.007,
                                      'blood_lung_fraction': 0.5, 'method': 'none',
                                      'method_params': '{"N": 5, "intervals": 4, "step": 0.0833, "end": 4, "time": [0, 1, 2, 3 ], "setpoint": [4e-07, 4e-07, 4e-07, 4e-07], "time_int_final": [1, 2, 3, 4], "Q": 0.25, "R":5}'})
    default_drug_form = DrugForm(prefix='dr',
                                 initial={'drug_name': 'default drug', 'max_liver': 1.4e-6, 'max_kidney': 5.0e-6,
                                          'max_influx': 0.04e-6,
                                          'k_met': 0.06, 'k_bile': 0.0, 'k_kidney': 0.0164,
                                          'p_skin': 1.6, 'pi_skin': 0.0095,
                                          'p_kidney': 0.14, 'pi_kidney': 0.12,
                                          'p_bladder': 1.6, 'pi_bladder': 0.0095,
                                          'p_liver': 1.6, 'pi_liver': 0.0095,
                                          'p_rest': 1.6, 'pi_rest': 0.0095, 'pi_rbc': 1.3, 'pi_plasma': 0.81,
                                          'p_lung': 0.44, 'pi_lung': 0.94
                                 })
    if request.method == 'GET':
        params = {'form': default_form, 'dform': default_drug_form, 'default': True, 'tutorial': True}
        return render(request, 'model_form.html', params)

    if request.method == 'POST':

        method = request.POST.get('mod-method')
        meth_par = request.POST.get('mod-method_params')

        params = {'form': default_form, 'dform': default_drug_form, 'default': True, 'tutorial': True}

        if method == "CloseLoop-MPC":

            params_json = json.loads(meth_par)
            N = params_json['N']
            intervals = params_json['intervals']
            step = params_json['step']
            end = params_json['end']
            setpoint = params_json['setpoint']
            time = params_json['time']
            Q = params_json['Q']
            R = params_json['R']

            # change1=default_form.has_changed()
            if not (check_number(N) and check_number(intervals) and check_number(step) and check_number(end)):
                error = "The data you entered aren't valid. Please try again."
                params = {'form': default_form, 'dform': default_drug_form, 'default': True, "N": N, "intervals": intervals,
                          "step": step, "end": end, "error": error}
                return render(request, "model_form.html", params)
            elif float(step) > float(end):
                error = "Wrong step and/or end time."
                params = {'form': default_form, 'dform': default_drug_form, 'default': True, "N": N, "intervals": intervals,
                          "step": step, "end": end, "error": error}
                return render(request, "model_form.html", params)
            else:
                N = int(N)
                intervals = int(intervals)
                step = float(step)
                end = float(end)
                Q = float(Q)
                R = float(R)
                setpoint1 = []
                setpoint2 = []
                time1 = []
                time2 = []
                for e in setpoint:
                    e = float(e)
                    setpoint1.append(e)
                    e = int(e)
                    setpoint2.append(e)
                    #add the last element twice due to add the last couple for plotting
                last_d = int(setpoint1[-1])
                setpoint2.append(last_d)

                for t in time:
                    t = float(t)
                    time1.append(t)
                    t = int(t)
                    time2.append(t)
                    #add the end time of simulation (time constists of initial times. For correct plotting it should be added one more couple)
                time2.append(end)

            read_models = Models.objects.filter(modelname='default', pk=128)
            if read_models and read_models[0].plot_params and N == int(5) and intervals == int(4) and step == float(0.0833) and end == float(4):
                model_item = read_models[0]
                json_object_plot = json.loads(model_item.plot_params)
                adm_j = json.loads(model_item.step_params)
                params = {'form': default_form, 'dform': default_drug_form, 'default': True, 'image': True, 'change': True,
                          'json': json_object_plot, 'adm': adm_j, 'tutorial': True, 'tutorial_result': True}
                if request.is_ajax():
                    return HttpResponse(json_object_plot, 'application/json')
                return render(request, "model_form.html", params)
            else:

                model = PBPK_Model(0.03, 0.45, 16.5, 0.07, 0.0, 0.0164, 1.4e-6, 5.0e-6, 0.04e-6,
                                   0.058, 0.165, 0.03, 1.6, 0.0095, 0.091, 0.017, 0.24, 0.14, 0.12,
                                   0.0033, 0.0009, 0.03, 1.6, 0.0095, 0.04, 1.6, 0.0095, 0.162, 0.055, 0.31, 1.6, 0.0095,
                                   0.5, 1.3, 0.81, 1.0, 0.007, 0.5, 0.44, 0.94, 0.0, 1, 0.0, 1, 0.0, 1, 0.0, 1, 0.0, 0.0,
                                   0.0, 0.0, 0.0, 0.0, 0.0, "", "", 0.0, 0.0,
                                   0.0, 0.0, 0.0, 0.0, 0.0, "", "", 0.0, 0.0,
                                   0.0, 0.0, 0.0, 0.0, 0.0, "", "", 0.0, 0.0,
                                   0.0, 0.0, 0.0, 0.0, 0.0, "", "", 0.0, 0.0,
                                   0.0, 0.0, 0.0, 0.0, 0.0, "", "", 0.0, 0.0,
                                   0.0, 0.0, 0.0, 0.0, 0.0,
                                   0.0, 0.0, 0.0, 0.0, 0.0,
                                   0.0, 0.0, 0.0, 0.0, 0.0,
                                   0.0, 0.0, 0.0, 0.0, 0.0)
                skin = Skin(model)
                kidney = Kidney(model)
                bladder = Bladder(model)
                residual = Residual(model)
                liver = Liver(model)
                blood = Blood(model)
                lung = Lung(model)
                organ1 = Organ1(model)
                organ2 = Organ2(model)
                organ3 = Organ3(model)
                organ4 = Organ4(model)
                organ5 = Organ5(model)
                heart = Heart(model)
                muscle = Muscle(model)
                spleen = Spleen(model)
                placental = Placental(model)

                mysystem = System(model, skin, kidney, bladder, residual, liver, blood, lung, organ1, organ2, organ3,
                                  organ4, organ5, heart, muscle, spleen, placental)
                sys = mysystem.DiscreteSystem()
                d_hat = 1.74e-14 * np.ones((1, 1))
                x_hat = np.zeros((14, 1))
                sim = Simulator(mysystem, N, x_hat, d_hat, 1.4e-6, 5.0e-6, 0.04e-6, 0.0, 1, 0.0, 1, 0.0, 1, 0.0, 1, 0.0,
                                0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, end, time1, setpoint1, step, Q, R)
                Tsim, cont, ulist = sim.Simulate(step, end)
                plot_j = []
                # plot_j is of the following form
                # [ [[0.0, y1.1], [0.01, y1.2], ...] -> organ1,  [[0.0, y2.1], [0.0, y2.2], ...] -> organ2, ... ]
                adm = []
                for i in range(len(ulist)):
                    adm.append([Tsim[i], ulist[i]])
                adm_j = json.dumps(adm)

                for c in cont:
                    vals = []
                    for i in range(len(Tsim)):
                        vals.append([Tsim[i], c[i]])

                    plot_j.append(vals)

                json_object_plot = json.dumps(plot_j)

                params = {'form': default_form, 'dform': default_drug_form, 'default': True, 'image': True, 'change': True,
                          'json': json_object_plot, 'adm': adm_j, 'tutorial': True, 'tutorial_result': True}
                if request.is_ajax():
                    return HttpResponse(json_object_plot, 'application/json')

                return render(request, "model_form.html", params)
        elif method == "CloseLoop-PID":
            return Http404  # todo implement CloseLoop-PID defaults
        elif method == "OpenLoop":  # OpenLoop
            params_json = json.loads(meth_par)
            total_time = params_json['total_time']
            total_N = params_json['total_N']
            dose = params_json['dose']
            time = params_json['time']

            if not (check_number(total_time) and check_number(total_N) and dose and time):
                error = "The data you entered aren't valid. Please try again."
                params = {'form': default_form, 'dform': default_drug_form, 'default': True, "total_time": total_time,
                          "total_N": total_N, "error": error}
                return render(request, "model_form.html", params)
            elif time > total_time:
                error = "Wrong parameters for total time and initial time"
                params = {'form': default_form, 'dform': default_drug_form, 'default': True, "total_time": total_time,
                          "total_N": total_N, "error": error}
                return render(request, "model_form.html", params)
            else:
                total_time = int(total_time)
                total_N = int(total_N)
                dose1 = []
                dose2 = []
                time1 = []
                time2 = []
                for e in dose:
                    e = float(e)
                    dose1.append(e)
                    e = int(e)
                    dose2.append(e)
                    #add the last element twice due to add the last couple for plotting
                last_d = int(dose1[-1])
                dose2.append(last_d)

                for t in time:
                    t = float(t)
                    time1.append(t)
                    t = int(t)
                    time2.append(t)
                    #add the end time of simulation (time constists of initial times. For correct plotting it should be added one more couple)
                time2.append(total_time)

                model = PBPK_Model(0.03, 0.45, 16.5, 0.07, 0.0, 0.0164, 1.4e-6, 5.0e-6, 0.04e-6,
                                   0.058, 0.165, 0.03, 1.6, 0.0095, 0.091, 0.017, 0.24, 0.14, 0.12,
                                   0.0033, 0.0009, 0.03, 1.6, 0.0095, 0.04, 1.6, 0.0095, 0.162, 0.055, 0.31, 1.6,
                                   0.0095,
                                   0.5, 1.3, 0.81, 1.0, 0.007, 0.5, 0.44, 0.94, 0.0, 1, 0.0, 1, 0.0, 1, 0.0, 1, 0.0,
                                   0.0, 0.0, 0.0, 0.0, 0.0, 0.0, "", "", 0.0, 0.0,
                                   0.0, 0.0, 0.0, 0.0, 0.0, "", "", 0.0, 0.0,
                                   0.0, 0.0, 0.0, 0.0, 0.0, "", "", 0.0, 0.0,
                                   0.0, 0.0, 0.0, 0.0, 0.0, "", "", 0.0, 0.0,
                                   0.0, 0.0, 0.0, 0.0, 0.0, "", "", 0.0, 0.0,
                                   0.0, 0.0, 0.0, 0.0, 0.0,
                                   0.0, 0.0, 0.0, 0.0, 0.0,
                                   0.0, 0.0, 0.0, 0.0, 0.0,
                                   0.0, 0.0, 0.0, 0.0, 0.0)
                skin = Skin(model)
                kidney = Kidney(model)
                bladder = Bladder(model)
                residual = Residual(model)
                liver = Liver(model)
                blood = Blood(model)
                lung = Lung(model)
                organ1 = Organ1(model)
                organ2 = Organ2(model)
                organ3 = Organ3(model)
                organ4 = Organ4(model)
                organ5 = Organ5(model)
                heart = Heart(model)
                muscle = Muscle(model)
                spleen = Spleen(model)

                placental = Placental(model)

                mysystem = System(model, skin, kidney, bladder, residual, liver, blood, lung, organ1, organ2, organ3,
                                  organ4, organ5, heart, muscle, spleen, placental)
                sys = mysystem.ContinuousSystem()
                sim = SimulatorOpenLoop(mysystem, total_time, time1, dose1)
                t, u = input_profile(total_time, time1, dose1)
                cont, Tsim = sim.Simulate()
                plot_j = []
                # plot_j is of the following form
                # [ [[0.0, y1.1], [0.01, y1.2], ...] -> organ1,  [[0.0, y2.1], [0.0, y2.2], ...] -> organ2, ... ]

                adm = []
                for i in range(len(time2)):
                    adm.append([time2[i], dose2[i]])
                adm_j = json.dumps(adm)
                print adm_j
                for c in cont:
                    vals = []
                    for i in range(len(Tsim)):
                        vals.append([Tsim[i], c[i]])
                    plot_j.append(vals)

                json_object_plot = json.dumps(plot_j)

                params = {'form': default_form, 'dform': default_drug_form, 'default': True, 'image': True,
                          'change': True, 'json': json_object_plot, 'adm': adm_j, 'tutorial': True, 'tutorial_openloop_result': True}
                if request.is_ajax():
                    return HttpResponse(json_object_plot, 'application/json')
                return render(request, "model_form.html", params)
        else:
            error = "Please define the simulation parameters "
            params = {'form': default_form, 'dform': default_drug_form, 'default': True, 'error': error, 'tutorial': True}
            return render(request, "model_form.html", params)


def get_plot_params(request, pk):
    model = Models.objects.get(pk=pk)
    return HttpResponse(model.plot_params)


def get_step_params(request, pk):
    model = Models.objects.get(pk=pk)
    return HttpResponse(model.step_params)


def tutorial_create(request):
    if request.method == 'GET':
        submit = ""
        counter = 1
        form = ModelForm(initial={'bw': 0.03, 'h': 0.45, "method": "None",
                                  "method_params": '{"N": 5, "intervals": 4, "step": 0.0833, "end": 4, "time": [0, 1, 2, 3 ], "setpoint": [4e-07, 4e-07, 4e-07, 4e-07], "time_int_final": [1, 2, 3, 4], "Q": 0.25, "R":5}', },
                         prefix="mod")
        dform = DrugForm(prefix="dr", initial={'drug_name': ''})

        return render(request, "model_form.html", {'dform': dform, 'form': form, 'submit': submit, 'counter': counter, 't_create':True})

    if request.method == 'POST':
        form = ModelForm(request.POST, prefix="mod")
        dform = DrugForm(request.POST, prefix="dr")
        meth = request.POST.get('mod-method')
        submit = request.POST.get('submit_id')
        counter = request.POST.get('counter_id')

        if not form.is_valid() or not dform.is_valid():
            params = {'form': form, 'dform': dform, "save": True, 'submit': submit, 'counter': counter}
            return render(request, "model_form.html", params)
        elif ((form['blood_volume_fraction'].value() == "0.0") | (form['lung_flow_factor'].value() == "0.0") | (
                    form['lung_volume_fraction'].value() == "0.0") | (form['blood_lung_fraction'].value() == "0.0") | (
                    dform['p_lung'].value() == "0.0")):
            if ((form['blood_volume_fraction'].value() == "0.0") & ((form['lung_flow_factor'].value() == "0.0") | (
                        form['lung_volume_fraction'].value() == "0.0") | (form['blood_lung_fraction'].value() == "0.0") | (
                        dform['p_lung'].value() == "0.0"))):
                error = "Cannot be created model without blood and lung."
                params = {'form': form, 'dform': dform, "save": True, 'error': error, 'submit': submit,
                          'counter': counter}
                return render(request, "model_form.html", params)
            elif (form['blood_volume_fraction'].value() == "0.0"):
                error = "Cannot be created model without blood."
                params = {'form': form, 'dform': dform, "save": True, 'error': error, 'submit': submit,
                          'counter': counter}
                return render(request, "model_form.html", params)
            elif ((form['lung_flow_factor'].value() == "0.0") | (form['lung_volume_fraction'].value() == "0.0") | (
                        form['blood_lung_fraction'].value() == "0.0") | (dform['p_lung'].value() == "0.0")):
                error = "Cannot be created model without lung."
                params = {'form': form, 'dform': dform, "save": True, 'error': error, 'submit': submit,
                          'counter': counter}
                return render(request, "model_form.html", params)
            elif (((form['skin_flow_factor'].value()) + (form['liver_flow_factor'].value()) + (
                    form['kidney_flow_factor'].value()) + (form['bladder_flow_factor'].value())) > 1):
                error = " Inavalid flow factor combination. The sum of skin, liver, kidney and bladder flow factors must be less than 1."
                params = {'form': form, 'dform': dform, "save": True, 'error': error, 'submit': submit,
                          'counter': counter}
                return render(request, "model_form.html", params)
            elif (((form['skin_volume_fraction'].value()) + (form['liver_volume_fraction'].value()) + (
                    form['kidney_volume_fraction'].value()) + (form['bladder_flow_factor'].value()) + form[
                'lung_volume_fraction'].value()) > 1):
                error = " Inavalid volume fraction combination. The sum of skin, liver, kidney, bladder and lung volume fractions must be less than 1."
                params = {'form': form, 'dform': dform, "save": True, 'error': error, 'submit': submit,
                          'counter': counter}
                return render(request, "model_form.html", params)
        else:
            k_bile5 = 0.0
            k_met5 = 0.0
            k_bile4 = 0.0
            k_met4 = 0.0
            k_bile3 = 0.0
            k_met3 = 0.0
            k_bile2 = 0.0
            k_met2 = 0.0
            k_bile1 = 0.0
            k_met1 = 0.0
            type1 = ""
            const1 = ""
            type2 = ""
            const2 = ""
            type3 = ""
            const3 = ""
            type4 = ""
            const4 = ""
            type5 = ""
            const5 = ""
            if submit == "Run":
                if meth == "CloseLoop-MPC":
                    new_drug = dform.save(commit=False)
                    new_model = form.save(commit=False)
                    new_model.username = request.user.username
                    # new_model.drugs.clear()
                    #convert method_params to json and read values
                    if new_drug.organ1_params:
                        org1_params_json = json.loads(new_drug.organ1_params)
                        if org1_params_json[0]:
                            type1 = org1_params_json[0]['type']
                            if type1 == "met":
                                const1 = org1_params_json[0]['const']
                                k_met1 = org1_params_json[0]['k_met']
                                k_bile1 = org1_params_json[0]['k_bile']
                                print (const1)
                            print(type1)
                        if org1_params_json[1]:
                            type2 = org1_params_json[1]['type']
                            if type2 == "met":
                                const2 = org1_params_json[1]['const']
                                k_met2 = org1_params_json[1]['k_met']
                                k_bile2 = org1_params_json[1]['k_bile']
                        if org1_params_json[2]:
                            type3 = org1_params_json[2]['type']
                            if type3 == "met":
                                const3 = org1_params_json[2]['const']
                                k_met3 = org1_params_json[2]['k_met']
                                k_bile3 = org1_params_json[2]['k_bile']
                        if org1_params_json[3]:
                            type4 = org1_params_json[3]['type']
                            if type4 == "met":
                                const4 = org1_params_json[3]['const']
                                k_met4 = org1_params_json[3]['k_met']
                                k_bile4 = org1_params_json[3]['k_bile']
                        if org1_params_json[4]:
                            type5 = org1_params_json[4]['type']
                            if type5 == "met":
                                const5 = org1_params_json[4]['const']
                                k_met5 = org1_params_json[4]['k_met']
                                k_bile5 = org1_params_json[4]['k_bile']
                    params_json = json.loads(new_model.method_params)
                    N = params_json['N']
                    intervals = params_json['intervals']
                    step = params_json['step']
                    end = params_json['end']
                    setpoint = params_json['setpoint']
                    time = params_json['time']
                    Q = params_json['Q']
                    R = params_json['R']

                    if not (check_number(N) and check_number(intervals) and check_number(step) and check_number(
                            end) and setpoint and time and check_number(k_bile1) and check_number(k_bile2) and check_number(
                            k_bile3) and check_number(k_bile4)
                            and check_number(k_bile5) and check_number(k_met1) and check_number(
                            k_met2) and check_number(k_met3) and check_number(k_met4) and check_number(k_met5)):
                        error = "The data you entered aren't valid. Please try again."
                        return render(request, "model_form.html",
                                      {"form": form, "N": N, "target": intervals, "error": error, "step": step, "end": end,
                                       'counter': counter})
                    elif float(step) > float(end):
                        error = "Wrong step and/or end time."
                        return render(request, "model_form.html",
                                      {"form": form, "N": N, "target": intervals, "error": error, "step": step, "end": end,
                                       'counter': counter})
                    else:
                        N = int(N)
                        intervals = int(intervals)
                        step = float(step)
                        end = float(end)
                        Q = float(Q)
                        R = float(R)
                        setpoint1 = []
                        setpoint2 = []
                        time1 = []
                        time2 = []
                        for e in setpoint:
                            e = float(e)
                            setpoint1.append(e)
                            e = int(e)
                            setpoint2.append(e)
                            #add the last element twice due to add the last couple for plotting
                        last_d = int(setpoint1[-1])
                        setpoint2.append(last_d)

                        for t in time:
                            t = float(t)
                            time1.append(t)
                            t = int(t)
                            time2.append(t)
                            #add the end time of simulation (time constists of initial times. For correct plotting it should be added one more couple)
                        time2.append(end)

                        k_met1 = float(k_met1)
                        k_bile1 = float(k_bile1)
                        k_met2 = float(k_met2)
                        k_bile2 = float(k_bile2)
                        k_met3 = float(k_met3)
                        k_bile3 = float(k_bile3)
                        k_met4 = float(k_met4)
                        k_bile4 = float(k_bile4)
                        k_met5 = float(k_met5)
                        k_bile5 = float(k_bile5)

                        model = PBPK_Model(new_model.bw, new_model.h, new_model.cardiac_output, new_drug.k_met,
                                           new_drug.k_bile, new_drug.k_kidney, new_drug.max_liver, new_drug.max_kidney,
                                           new_drug.max_influx,
                                           new_model.skin_flow_factor, new_model.skin_volume_fraction,
                                           new_model.blood_skin_fraction, new_drug.p_skin, new_drug.pi_skin,
                                           new_model.kidney_flow_factor, new_model.kidney_volume_fraction,
                                           new_model.blood_kidney_fraction, new_drug.p_kidney, new_drug.pi_kidney,
                                           new_model.bladder_flow_factor, new_model.bladder_volume_fraction,
                                           new_model.blood_bladder_fraction, new_drug.p_bladder, new_drug.pi_bladder,
                                           new_model.blood_rest_fraction, new_drug.p_rest, new_drug.pi_rest,
                                           new_model.liver_flow_factor, new_model.liver_volume_fraction,
                                           new_model.blood_liver_fraction, new_drug.p_liver, new_drug.pi_liver,
                                           new_model.blood_volume_fraction, new_drug.pi_rbc, new_drug.pi_plasma,
                                           new_model.lung_flow_factor, new_model.lung_volume_fraction,
                                           new_model.blood_lung_fraction, new_drug.p_lung, new_drug.pi_lung,
                                           new_drug.min_residual, new_drug.max_residual, new_drug.min_skin,
                                           new_drug.max_skin, new_drug.min_bladder, new_drug.max_bladder,
                                           new_drug.min_lung, new_drug.max_lung, new_drug.min_liver,
                                           new_drug.min_kidney,
                                           new_model.organ1_flow_factor, new_model.organ1_volume_fraction,
                                           new_model.blood_organ1_fraction, new_drug.p_organ1, new_drug.pi_organ1,
                                           type1, const1, k_met1, k_bile1,
                                           new_model.organ2_flow_factor, new_model.organ2_volume_fraction,
                                           new_model.blood_organ2_fraction, new_drug.p_organ2, new_drug.pi_organ2,
                                           type2, const2, k_met2, k_bile2,
                                           new_model.organ3_flow_factor, new_model.organ3_volume_fraction,
                                           new_model.blood_organ3_fraction, new_drug.p_organ3, new_drug.pi_organ3,
                                           type3, const3, k_met3, k_bile3,
                                           new_model.organ4_flow_factor, new_model.organ4_volume_fraction,
                                           new_model.blood_organ4_fraction, new_drug.p_organ4, new_drug.pi_organ4,
                                           type4, const4, k_met4, k_bile4,
                                           new_model.organ5_flow_factor, new_model.organ5_volume_fraction,
                                           new_model.blood_organ5_fraction, new_drug.p_organ5, new_drug.pi_organ5,
                                           type5, const5, k_met5, k_bile5,
                                           new_model.heart_flow_factor, new_model.heart_volume_fraction,
                                           new_model.blood_heart_fraction, new_drug.p_heart, new_drug.pi_heart,
                                           new_model.muscle_flow_factor, new_model.muscle_volume_fraction,
                                           new_model.blood_muscle_fraction, new_drug.p_muscle, new_drug.pi_muscle,
                                           new_model.spleen_flow_factor, new_model.spleen_volume_fraction,
                                           new_model.blood_spleen_fraction, new_drug.p_spleen, new_drug.pi_spleen,
                                           new_model.placental_flow_factor, new_model.placental_volume_fraction,
                                           new_model.blood_placental_fraction, new_drug.p_placental,
                                           new_drug.pi_placental)
                        skin = Skin(model)
                        kidney = Kidney(model)
                        bladder = Bladder(model)
                        residual = Residual(model)
                        liver = Liver(model)
                        blood = Blood(model)
                        lung = Lung(model)
                        organ1 = Organ1(model)
                        organ2 = Organ2(model)
                        organ3 = Organ3(model)
                        organ4 = Organ4(model)
                        organ5 = Organ5(model)
                        heart = Heart(model)
                        muscle = Muscle(model)
                        spleen = Spleen(model)
                        placental = Placental(model)
                        try:
                            mysystem = System(model, skin, kidney, bladder, residual, liver, blood, lung, organ1,
                                              organ2, organ3, organ4, organ5, heart, muscle, spleen, placental)
                            sys = mysystem.DiscreteSystem()
                            d_hat = 1.7408e-14 * np.ones((1, 1))
                            x_hat = np.zeros((sys.A.shape[0], 1))
                            tlist= [0.0, 4.0, 8.0]
                            ulist1 = [2.0, 2.0, 2.0]
                            sim = Simulator(mysystem, N, x_hat, d_hat, new_drug.max_liver, new_drug.max_kidney,
                                            new_drug.max_influx, new_drug.min_residual, new_drug.max_residual,
                                            new_drug.min_skin,
                                            new_drug.max_skin, new_drug.min_bladder, new_drug.max_bladder,
                                            new_drug.min_lung, new_drug.max_lung, new_drug.min_liver,
                                            new_drug.min_kidney, new_drug.min_heart, new_drug.max_heart,
                                            new_drug.min_muscle, new_drug.max_muscle, new_drug.min_spleen,
                                            new_drug.max_spleen, new_drug.min_placental, new_drug.max_placental, end, time1, setpoint1, step, Q, R)
                            Tsim, cont, ulist = sim.Simulate(step, end)
                            plot_j = []
                            # plot_j is of the following form
                            # [ [[0.0, y1.1], [0.01, y1.2], ...] -> organ1,  [[0.0, y2.1], [0.0, y2.2], ...] -> organ2, ... ]
                            adm = []
                            for i in range(len(ulist)):
                                adm.append([Tsim[i], ulist[i]])
                            adm_j = json.dumps(adm)
                            new_model.step_params = adm_j

                            for c in cont:
                                vals = []
                                for i in range(len(Tsim)):
                                    vals.append([Tsim[i], c[i]])

                                plot_j.append(vals)

                            json_object_plot = json.dumps(plot_j)
                            new_model.plot_params = json_object_plot

                        except RuntimeError as re:
                            print(re)
                            error = "An error occurred while creating the model."
                            params = {'form': form, 'dform': dform, "save": True, 'error': error, 'counter': counter}
                            return render(request, "model_form.html", params)
                        except Exception as e:
                            print(e)
                            error = "An error occurred while creating the model."
                            params = {'form': form, 'dform': dform, "save": True, 'error': error, 'counter': counter}
                            return render(request, "model_form.html", params)

                        params = {'form': form, 'dform': dform, 'save': True, 'image': True, 'counter': counter,
                                  'change': True, 'json': json_object_plot, 'adm': adm_j, 't_create_final':True}
                        if request.is_ajax():
                            return HttpResponse(json_object_plot, 'application/json')
                        new_drug.save()
                        new_model.save()
                        new_model.drugs.add(new_drug)
                        return render(request, "model_form.html", params)
                elif meth == "OpenLoop":
                    new_drug = dform.save(commit=False)
                    new_model = form.save(commit=False)
                    new_model.username = request.user.username

                    # new_model.drugs.clear()
                    #new_model.save(commit=False)
                    #convert method_params to json and read values
                    if new_drug.organ1_params:
                        org1_params_json = json.loads(new_drug.organ1_params)
                        if org1_params_json[0]:
                            type1 = org1_params_json[0]['type']
                            if type1 == "met":
                                const1 = org1_params_json[0]['const']
                                print (const1)
                            print(type1)
                        if org1_params_json[1]:
                            type2 = org1_params_json[1]['type']
                            if type2 == "met":
                                const2 = org1_params_json[1]['const']
                        if org1_params_json[2]:
                            type3 = org1_params_json[2]['type']
                            if type3 == "met":
                                const3 = org1_params_json[2]['const']
                        if org1_params_json[3]:
                            type4 = org1_params_json[3]['type']
                            if type4 == "met":
                                const4 = org1_params_json[3]['const']
                        if org1_params_json[4]:
                            type5 = org1_params_json[4]['type']
                            if type5 == "met":
                                const5 = org1_params_json[4]['const']
                    params_json = json.loads(new_model.method_params)
                    total_time = params_json['total_time']
                    total_N = params_json['total_N']
                    dose = params_json['dose']
                    time = params_json['time']
                    dose1 = []
                    dose2 = []
                    time1 = []
                    time2 = []
                    if not (check_number(total_time) and check_number(total_N) and dose and time and check_number(
                            k_bile1) and check_number(k_bile2) and check_number(k_bile3) and check_number(k_bile4)
                            and check_number(k_bile5) and check_number(k_met1) and check_number(
                            k_met2) and check_number(k_met3) and check_number(k_met4) and check_number(k_met5) ):
                        error = "The data you entered aren't valid. Please try again."
                        params = {'form': form, 'dform': dform, 'save': True, "total_time": total_time,
                                  "total_N": total_N, "error": error, 'counter': counter}
                        return render(request, "model_form.html", params)
                    elif time > total_time:
                        error = "Wrong parameters for total time and initial time"
                        params = {'form': form, 'dform': dform, 'save': True, "total_time": total_time,
                                  "total_N": total_N, "error": error, 'counter': counter}
                        return render(request, "model_form.html", params)
                    else:
                        total_time = int(float(total_time))
                        total_N = int(total_N)
                        k_met1 = float(k_met1)
                        k_bile1 = float(k_bile1)
                        k_met2 = float(k_met2)
                        k_bile2 = float(k_bile2)
                        k_met3 = float(k_met3)
                        k_bile3 = float(k_bile3)
                        k_met4 = float(k_met4)
                        k_bile4 = float(k_bile4)
                        k_met5 = float(k_met5)
                        k_bile5 = float(k_bile5)
                        #convert list to list of floats and to list of ints
                        for e in dose:
                            e = float(e)
                            dose1.append(e)
                            e = int(e)
                            dose2.append(e)
                            #add the last element twice due to add the last couple for plotting
                        last_d = int(dose1[-1])
                        dose2.append(last_d)

                        for t in time:
                            t = float(t)
                            time1.append(t)
                            t = int(t)
                            time2.append(t)
                            #add the end time of simulation (time constists of initial times. For correct plotting it should be added one more couple)
                    time2.append(total_time)

                    model = PBPK_Model(new_model.bw, new_model.h, new_model.cardiac_output, new_drug.k_met,
                                       new_drug.k_bile, new_drug.k_kidney, new_drug.max_liver, new_drug.max_kidney,
                                       new_drug.max_influx,
                                       new_model.skin_flow_factor, new_model.skin_volume_fraction,
                                       new_model.blood_skin_fraction, new_drug.p_skin, new_drug.pi_skin,
                                       new_model.kidney_flow_factor, new_model.kidney_volume_fraction,
                                       new_model.blood_kidney_fraction, new_drug.p_kidney, new_drug.pi_kidney,
                                       new_model.bladder_flow_factor, new_model.bladder_volume_fraction,
                                       new_model.blood_bladder_fraction, new_drug.p_bladder, new_drug.pi_bladder,
                                       new_model.blood_rest_fraction, new_drug.p_rest, new_drug.pi_rest,
                                       new_model.liver_flow_factor, new_model.liver_volume_fraction,
                                       new_model.blood_liver_fraction, new_drug.p_liver, new_drug.pi_liver,
                                       new_model.blood_volume_fraction, new_drug.pi_rbc, new_drug.pi_plasma,
                                       new_model.lung_flow_factor, new_model.lung_volume_fraction,
                                       new_model.blood_lung_fraction, new_drug.p_lung, new_drug.pi_lung,
                                       new_drug.min_residual, new_drug.max_residual, new_drug.min_skin,
                                       new_drug.max_skin, new_drug.min_bladder, new_drug.max_bladder, new_drug.min_lung,
                                       new_drug.max_lung, new_drug.min_liver, new_drug.min_kidney,
                                       new_model.organ1_flow_factor, new_model.organ1_volume_fraction,
                                       new_model.blood_organ1_fraction, new_drug.p_organ1, new_drug.pi_organ1, type1,
                                       const1, k_met1, k_bile1,
                                       new_model.organ2_flow_factor, new_model.organ2_volume_fraction,
                                       new_model.blood_organ2_fraction, new_drug.p_organ2, new_drug.pi_organ2, type2,
                                       const2, k_met2, k_bile2,
                                       new_model.organ3_flow_factor, new_model.organ3_volume_fraction,
                                       new_model.blood_organ3_fraction, new_drug.p_organ3, new_drug.pi_organ3, type3,
                                       const3, k_met3, k_bile3,
                                       new_model.organ4_flow_factor, new_model.organ4_volume_fraction,
                                       new_model.blood_organ4_fraction, new_drug.p_organ4, new_drug.pi_organ4, type4,
                                       const4, k_met4, k_bile4,
                                       new_model.organ5_flow_factor, new_model.organ5_volume_fraction,
                                       new_model.blood_organ5_fraction, new_drug.p_organ5, new_drug.pi_organ5, type5,
                                       const5, k_met5, k_bile5,
                                       new_model.heart_flow_factor, new_model.heart_volume_fraction,
                                       new_model.blood_heart_fraction, new_drug.p_heart, new_drug.pi_heart,
                                       new_model.muscle_flow_factor, new_model.muscle_volume_fraction,
                                       new_model.blood_muscle_fraction, new_drug.p_muscle, new_drug.pi_muscle,
                                       new_model.spleen_flow_factor, new_model.spleen_volume_fraction,
                                       new_model.blood_spleen_fraction, new_drug.p_spleen, new_drug.pi_spleen,
                                       new_model.placental_flow_factor, new_model.placental_volume_fraction,
                                       new_model.blood_placental_fraction, new_drug.p_placental, new_drug.pi_placental)
                    skin = Skin(model)
                    kidney = Kidney(model)
                    bladder = Bladder(model)
                    residual = Residual(model)
                    liver = Liver(model)
                    blood = Blood(model)
                    lung = Lung(model)
                    organ1 = Organ1(model)
                    organ2 = Organ2(model)
                    organ3 = Organ3(model)
                    organ4 = Organ4(model)
                    organ5 = Organ5(model)
                    heart = Heart(model)
                    muscle = Muscle(model)
                    spleen = Spleen(model)
                    placental = Placental(model)

                    try:
                        mysystem = System(model, skin, kidney, bladder, residual, liver, blood, lung, organ1, organ2,
                                          organ3, organ4, organ5, heart, muscle, spleen, placental)
                        sim = SimulatorOpenLoop(mysystem, total_time, time1, dose1)
                        t, u = input_profile(total_time, time1, dose1)
                        cont, Tsim = sim.Simulate()
                        plot_j = []
                        # plot_j is of the following form
                        # [ [[0.0, y1.1], [0.01, y1.2], ...] -> organ1,  [[0.0, y2.1], [0.0, y2.2], ...] -> organ2, ... ] contains state variables of all organs
                        # adm_j contains administration rate
                        adm = []
                        for i in range(len(time2)):
                            adm.append([time2[i], dose2[i]])
                        print new_model.step_params
                        adm_j = json.dumps(adm)
                        new_model.step_params = adm_j
                        print new_model.step_params
                        print adm_j
                        for c in cont:
                            vals = []
                            for i in range(len(Tsim)):
                                vals.append([Tsim[i], c[i]])
                            plot_j.append(vals)

                        json_object_plot = json.dumps(plot_j)
                        new_model.plot_params = json_object_plot

                    except RuntimeError as re:
                        print(re)
                        error = "An error occurred while creating the model."
                        params = {'form': form, 'dform': dform, "save": True, 'error': error, 'counter': counter}
                        return render(request, "model_form.html", params)
                    except Exception as e:
                        print(e)
                        error = "An error occurred while creating the model."
                        params = {'form': form, 'dform': dform, "save": True, 'error': error, 'counter': counter}
                        return render(request, "model_form.html", params)

                    params = {'form': form, 'dform': dform, 'save': True, 'image': True, 'counter': counter,
                              'change': True, 'json': json_object_plot, 'adm': adm_j, 't_create':True}
                    if request.is_ajax():
                        return HttpResponse(json_object_plot, 'application/json')
                    new_drug.save()
                    new_model.save()
                    new_model.drugs.add(new_drug)
                    return render(request, "model_form.html", params)
                else:
                    error = "Your should define simulation parameters first."
                    params = {'form': form, 'dform': dform, "save": True, 'error': error, 'counter': counter, 't_create':True}
                    return render(request, "model_form.html", params)
            else:

                new_drug = dform.save()
                new_model = form.save()
                new_model.username = request.user.username

                new_model.drugs.clear()
                new_model.save()
                new_model.drugs.add(new_drug)

                modelid = new_model.id
                drugid = new_drug.id

                error = "Your model have been saved. If you want to run it, define simulation parameters."
                # params = {'form': form, 'dform': dform, "save": True,'edit':True, 'error': error, 'modelid':modelid, 'drugid':drugid}
                #return render(request, "model_form.html", params)
                return redirect(
                    '/edit_model?username=' + request.user.username + '&modelname=' + new_model.modelname + '&modelid=' + str(
                        modelid) + '&drugname=' + new_drug.drug_name + '&drugid=' + str(drugid) + '&error=' + error,
                    {'error': error})
