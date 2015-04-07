import numpy as np
from control.matlab import *

class PBPK_Model():
    def __init__(self, bw, h, cardiac_output, k_met, k_bile, k_kidney, max_liver, max_kidney, max_influx,
                 skin_f_f, skin_v_f, skin_b_f, p_skin, pi_skin, kidney_f_f, kidney_v_f, kidney_b_f, p_kidney, pi_kidney,
                 bladder_f_f, bladder_v_f, bladder_b_f, p_bladder, pi_bladder, blood_r_f, p_rest, pi_rest,
                 liver_f_f, liver_v_f, liver_b_f, p_liver, pi_liver, blood_v_f, pi_rbc, pi_plasma,
                 lung_f_f, lung_v_f, lung_b_f, p_lung, pi_lung, min_residual, max_residual,
                 min_skin, max_skin, min_bladder, max_bladder, min_lung, max_lung, min_liver, min_kidney,
                 organ1_f_f, organ1_v_f, organ1_b_f, p_organ1, pi_organ1, type1, const1, k_met1, k_bile1,
                 organ2_f_f, organ2_v_f, organ2_b_f, p_organ2, pi_organ2, type2, const2, k_met2, k_bile2,
                 organ3_f_f, organ3_v_f, organ3_b_f, p_organ3, pi_organ3, type3, const3, k_met3, k_bile3,
                 organ4_f_f, organ4_v_f, organ4_b_f, p_organ4, pi_organ4, type4, const4, k_met4, k_bile4,
                 organ5_f_f, organ5_v_f, organ5_b_f, p_organ5, pi_organ5, type5, const5, k_met5, k_bile5,
                 heart_f_f, heart_v_f, heart_b_f, p_heart, pi_heart,
                 muscle_f_f, muscle_v_f, muscle_b_f, p_muscle, pi_muscle,
                 spleen_f_f, spleen_v_f, spleen_b_f, p_spleen, pi_spleen,
                 placental_f_f, placental_v_f, placental_b_f, p_placental, pi_placental):


        self.bw = bw
        self.hematocrit= h
        self.cardiac_output = cardiac_output
        self.k_met = k_met
        self.k_bile = k_bile
        self.k_kidney = k_kidney
        self.max_liver = max_liver
        self.max_kidney = max_kidney
        self.max_influx = max_influx
        self.skin_f_f = skin_f_f
        self.skin_v_f = skin_v_f
        self.skin_b_f = skin_b_f
        self.p_skin = p_skin
        self.pi_skin = pi_skin
        self.kidney_f_f = kidney_f_f
        self.kidney_v_f = kidney_v_f
        self.kidney_b_f = kidney_b_f
        self.p_kidney = p_kidney
        self.pi_kidney = pi_kidney
        self.bladder_f_f = bladder_f_f
        self.bladder_v_f = bladder_v_f
        self.bladder_b_f = bladder_b_f
        self.p_bladder = p_bladder
        self.pi_bladder = pi_bladder
        self.rest_b_f = blood_r_f
        self.p_rest = p_rest
        self.pi_rest = pi_rest
        self.liver_f_f = liver_f_f
        self.liver_v_f = liver_v_f
        self.liver_b_f = liver_b_f
        self.p_liver = p_liver
        self.pi_liver = pi_liver
        self.blood_v_f = blood_v_f
        self.pi_rbc = pi_rbc
        self.pi_plasma = pi_plasma
        self.lung_f_f = lung_f_f
        self.lung_v_f = lung_v_f
        self.lung_b_f = lung_b_f
        self.p_lung = p_lung
        self.pi_lung = pi_lung
        self.min_residual = min_residual
        self.max_residual = max_residual
        self.min_skin = min_skin
        self.max_skin = max_skin
        self.min_bladder = min_bladder
        self.max_bladder = max_bladder
        self.min_lung = min_lung
        self.max_lung = max_lung
        self.min_liver = min_liver
        self.min_kidney = min_kidney
        self.organ1_f_f = organ1_f_f
        self.organ1_v_f = organ1_v_f
        self.organ1_b_f = organ1_b_f
        self.p_organ1 = p_organ1
        self.pi_organ1 = pi_organ1
        self.organ2_f_f = organ2_f_f
        self.organ2_v_f = organ2_v_f
        self.organ2_b_f = organ2_b_f
        self.p_organ2 = p_organ2
        self.pi_organ2 = pi_organ2
        self.organ3_f_f = organ3_f_f
        self.organ3_v_f = organ3_v_f
        self.organ3_b_f = organ3_b_f
        self.p_organ3 = p_organ3
        self.pi_organ3 = pi_organ3
        self.organ4_f_f = organ4_f_f
        self.organ4_v_f = organ4_v_f
        self.organ4_b_f = organ4_b_f
        self.p_organ4 = p_organ4
        self.pi_organ4 = pi_organ4
        self.organ5_f_f = organ5_f_f
        self.organ5_v_f = organ5_v_f
        self.organ5_b_f = organ5_b_f
        self.p_organ5 = p_organ5
        self.pi_organ5 = pi_organ5
        self.type1 = type1
        self.const1 = const1
        self.k_bile1 = k_bile1
        self.k_met1 = k_met1
        self.type2 = type2
        self.const2 = const2
        self.k_bile2 = k_bile2
        self.k_met2 = k_met2
        self.type3 = type3
        self.const3 = const3
        self.k_bile3 = k_bile3
        self.k_met3 = k_met3
        self.type4 = type4
        self.const4 = const4
        self.k_bile4 = k_bile4
        self.k_met4 = k_met4
        self.type5 = type5
        self.const5 = const5
        self.k_bile5 = k_bile5
        self.k_met5 = k_met5
        self.heart_f_f = heart_f_f
        self.heart_b_f = heart_b_f
        self.heart_v_f = heart_v_f
        self.p_heart = p_heart
        self.pi_heart = pi_heart
        self.muscle_f_f = muscle_f_f
        self.muscle_b_f = muscle_b_f
        self.muscle_v_f = muscle_v_f
        self.p_muscle = p_muscle
        self.pi_muscle = pi_muscle
        self.placental_f_f = placental_f_f
        self.placental_b_f = placental_b_f
        self.placental_v_f = placental_v_f
        self.p_placental = p_placental
        self.pi_placental = pi_placental
        self.spleen_f_f = spleen_f_f
        self.spleen_b_f = spleen_b_f
        self.spleen_v_f = spleen_v_f
        self.p_spleen = p_spleen
        self.pi_spleen = pi_spleen

        self.rest_f_f = 1.0 - liver_f_f - kidney_f_f - skin_f_f - bladder_f_f - organ1_f_f - organ2_f_f - organ3_f_f - organ4_f_f - organ5_f_f - heart_f_f - placental_f_f - spleen_f_f - muscle_f_f

        # Flows in absolute numbers #
        self.liver_flow = self.liver_f_f * self.cardiac_output
        self.kidney_flow = self.kidney_f_f * self.cardiac_output
        self.skin_flow = self.skin_f_f * self.cardiac_output
        self.bladder_flow = self.bladder_f_f * self.cardiac_output
        self.lung_flow = self.lung_f_f * self.cardiac_output
        self.rest_flow = self.rest_f_f * self.cardiac_output
        self.organ1_flow = self.organ1_f_f * self.cardiac_output
        self.organ2_flow = self.organ2_f_f * self.cardiac_output
        self.organ3_flow = self.organ3_f_f * self.cardiac_output
        self.organ4_flow = self.organ4_f_f * self.cardiac_output
        self.organ5_flow = self.organ5_f_f * self.cardiac_output
        self.heart_flow = self.heart_f_f * self.cardiac_output
        self.muscle_flow = self.muscle_f_f * self.cardiac_output
        self.placental_flow = self.placental_f_f * self.cardiac_output
        self.spleen_flow = self.spleen_f_f * self.cardiac_output

        # Volumes - Coefficients #

        self.rest_v_f = 1.0 - self.liver_v_f - self.kidney_v_f - self.skin_v_f - self.organ1_v_f - self.organ2_v_f - self.organ3_v_f - self.organ4_v_f- self.organ5_v_f - self.bladder_v_f - self.lung_v_f

        #
        # Absolute Values #
        self.liver_volume = self.liver_v_f * self.bw * (1.0 - self.liver_b_f)
        self.lung_volume = self.lung_v_f * self.bw * (1.0 - self.lung_b_f)
        self.kidney_volume = self.kidney_v_f * self.bw * (1.0 - self.kidney_b_f)
        self.bladder_volume = self.bladder_v_f * self.bw * (1.0 - self.bladder_b_f)
        self.skin_volume = self.skin_v_f * self.bw * (1.0 - self.skin_b_f)
        self.rest_volume = self.rest_v_f * self.bw * (1.0 - self.rest_b_f)
        self.blood_volume = self.blood_v_f * self.bw
        self.organ1_volume = self.organ1_v_f * self.bw * (1.0 - self.organ1_b_f)
        self.organ2_volume = self.organ2_v_f * self.bw * (1.0 - self.organ2_b_f)
        self.organ3_volume = self.organ3_v_f * self.bw * (1.0 - self.organ3_b_f)
        self.organ4_volume = self.organ4_v_f * self.bw * (1.0 - self.organ4_b_f)
        self.organ5_volume = self.organ5_v_f * self.bw * (1.0 - self.organ5_b_f)
        self.heart_volume = self.heart_v_f * self.bw * (1.0 - self.heart_b_f)
        self.muscle_volume = self.muscle_v_f * self.bw * (1.0 - self.muscle_b_f)
        self.placental_volume = self.placental_v_f * self.bw * (1.0 - self.placental_b_f)
        self.spleen_volume = self.spleen_v_f * self.bw * (1.0 - self.spleen_b_f)

        # Absolute values of volumes of blood in various compartments (in L) #
        self.blood_lung = self.lung_b_f * self.lung_v_f * self.bw
        self.blood_skin = self.skin_b_f * self.skin_v_f * self.bw
        self.blood_liver = self.liver_b_f * self.liver_v_f * self.bw
        self.blood_kidney = self.kidney_b_f * self.kidney_v_f * self.bw
        self.blood_bladder = self.bladder_b_f * self.bladder_v_f * self.bw
        self.blood_rest = self.rest_b_f * self.rest_v_f * self.bw
        self.blood_organ1 = self.organ1_b_f * self.organ1_v_f * self.bw
        self.blood_organ2 = self.organ2_b_f * self.organ2_v_f * self.bw
        self.blood_organ3 = self.organ3_b_f * self.organ3_v_f * self.bw
        self.blood_organ4 = self.organ4_b_f * self.organ4_v_f * self.bw
        self.blood_organ5 = self.organ5_b_f * self.organ5_v_f * self.bw
        self.blood_heart = self.heart_b_f * self.heart_v_f * self.bw
        self.blood_muscle = self.muscle_b_f * self.muscle_v_f * self.bw
        self.blood_placental = self.placental_b_f * self.placental_v_f * self.bw
        self.blood_spleen = self.spleen_b_f * self.spleen_v_f * self.bw

        self.plasma_volume = (1 - self.hematocrit) * self.blood_volume
        self.rbc_volume = self.hematocrit * self.blood_volume


class Skin(PBPK_Model):
    def __init__(self, PBPK_Model):
        # Skin: 1Input, 2States, 2Outputs
        # x1: C_v_skin
        # x2: C_skin
        # u : C_art
        self.model = PBPK_Model

    def SkinA(self):
        if self.model.blood_skin != 0:
            self.A = np.array([[0, 0, self.model.skin_flow / self.model.blood_skin, 0, (-self.model.pi_skin - self.model.skin_flow)/self.model.blood_skin,
                                (self.model.pi_skin / self.model.p_skin)/self.model.blood_skin, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, self.model.pi_skin/self.model.skin_volume,
                                (-self.model.pi_skin / self.model.p_skin)/self.model.skin_volume, 0, 0, 0, 0, 0, 0, 0, 0]])
        else:
            self.A = np.zeros((2, 14))
        return self.A

    def SkinB(self):
        if self.model.blood_skin != 0:
            self.B = np.array([[self.model.skin_flow/self.model.blood_skin], [0]])
        else:
            self.B = np.zeros((2, 1))
        return self.B
    def SkinC(self):
        if self.model.blood_skin != 0:
            self.C = np.array([1, 0])
        else:
            self.C = np.array([0, 0])
        return self.C
    def SkinD(self):
        self.D = np.array([0])
        return self.D

class Kidney(PBPK_Model):
    def __init__(self, PBPK_Model):
        # Kidney : 1 Input, 2 States, 2 Outputs
        # x1 : C_v_kid
        # x2 : C_kid
        # u : C_art
        self.model = PBPK_Model
    def KidneyA(self):
        if self.model.kidney_flow != 0:
            self.A = np.array([[0, 0, (self.model.kidney_flow / self.model.blood_kidney), 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                (-self.model.kidney_flow- self.model.pi_kidney - self.model.k_kidney * self.model.blood_kidney) / self.model.blood_kidney,
                                (self.model.pi_kidney / self.model.p_kidney) / self.model.blood_kidney],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                self.model.pi_kidney/self.model.kidney_volume, -(self.model.pi_kidney / self.model.p_kidney)/self.model.kidney_volume]])
        else:
            self.A = np.zeros((2,14))
        return self.A
    def KidneyB(self):
        if self.model.kidney_flow != 0:
            self.B = np.array([[self.model.kidney_flow / self.model.blood_kidney], [0]])
        else:
            self.B = np.zeros((2,1))
        return self.B
    def KidneyC(self):
        if self.model.kidney_flow != 0:
            self.C = np.array([1, 0])
        else:
            self.C = np.array([0, 0])
        return self.C
    def KidneyD(self):
        self.D = np.array([0])
        return self.D

class Bladder(PBPK_Model):
    def __init__(self, PBPK_Model):
        # Bladder : 1Input, 2States, 2Outputs
        # x1 : C_v_bladder
        # x2 : C_bladder
        # u : C_art
        self.model = PBPK_Model
    def BladderA(self):
        if self.model.blood_bladder != 0:
            self.A = np.array([[0, 0, self.model.bladder_flow / self.model.blood_bladder, 0,
                                0, 0, (-self.model.pi_bladder - self.model.bladder_flow) / self.model.blood_bladder,
                                (self.model.pi_bladder / self.model.p_bladder)/self.model.blood_bladder, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, (self.model.pi_bladder / self.model.bladder_volume),
                                (-self.model.pi_bladder / self.model.p_bladder) / self.model.bladder_volume, 0, 0, 0, 0, 0, 0]])
        else:
            self.A = np.zeros((2,14))
        return self.A
    def BladderB(self):
        if self.model.blood_bladder != 0:
            self.B = np.array([[self.model.bladder_flow / self.model.blood_bladder], [0]])
        else:
            self.B = np.zeros((2,1))
        return self.B
    def BladderC(self):
        if self.model.blood_bladder != 0:
            self.C = np.array([1, 0])
        else:
            self.C = np.array([0, 0])
        return self.C
    def BladderD(self):
        self.D = np.array([0])
        return self.D

class Residual(PBPK_Model):
    def __init__(self, PBPK_Model):
        # Residual: 1Input, 2States, 2Outputs
        # x1 : C_v_r
        # x2 : C_r
        # u : C_art
        self.model = PBPK_Model
    def ResidualA(self):
        if self.model.blood_rest != 0:
            self.A = np.array([[0, 0, self.model.rest_flow / self.model.blood_rest, 0, 0, 0, 0, 0, 0, 0,
                                (-self.model.pi_rest - self.model.rest_flow) / self.model.blood_rest,
                                (self.model.pi_rest / self.model.p_rest) / self.model.blood_rest, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, self.model.pi_rest / self.model.rest_volume,
                                (-self.model.pi_rest / self.model.p_rest) / self.model.rest_volume, 0, 0]])
        else:
            self.A = np.zeros((2, 14))
        return self.A
    def ResidualB(self):
        if self.model.blood_rest != 0:
            self.B = np.array([ [self.model.rest_flow / self.model.blood_rest], [0]])
        else:
            self.B = np.zeros((2, 1))
        return self.B
    def ResidualC(self):
        if self.model.blood_rest != 0:
            self.C = np.array([1, 0])
        else:
            self.C = np.array([0, 0])
        return self.C
    def ResidualD(self):
        self.D = np.array([0])
        return self.D

class Liver(PBPK_Model):
    def __init__(self, PBPK_Model):
        # Liver : 1 Input, 2 States, 2 Outputs
        # x1 : C_v_liv
        # x2 : C_liv
        # u : C_art
        self.model = PBPK_Model
    def LiverA(self):
        if self.model.blood_liver != 0:
            self.A = np.array([[0, 0, self.model.liver_flow / self.model.blood_liver, 0, 0, 0, 0, 0,
                                (-self.model.pi_liver - self.model.liver_flow)/self.model.blood_liver,
                                (self.model.pi_liver / self.model.p_liver) / self.model.blood_liver, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, (self.model.pi_liver / self.model.liver_volume),
                                ((-self.model.pi_liver / self.model.p_liver) - (self.model.k_met + self.model.k_bile)*self.model.liver_volume) / self.model.liver_volume,
                                0, 0, 0, 0]])
        else:
            self.A = np.zeros((2, 14))
        return self.A
    def LiverB(self):
        if self.model.blood_liver != 0:
            self.B = np.array([[self.model.liver_flow / self.model.blood_liver], [0]])
        else:
            self.B = np.zeros((2, 1))
        return self.B
    def LiverC(self):
        if self.model.blood_liver != 0:
            self.C = np.array([1, 0])
        else:
            self.C = np.array([0, 0])
        return self.C
    def LiverD(self):
        self.D = np.array([0])
        return self.D



class Blood(PBPK_Model):
    def __init__(self, PBPK_Model):
        # Blood : 6 Inputs, 2 States, 2 Outputs
        # u1 : C_v_s
        # u2 : C_v_k
        # u3 : C_v_b (bladder)
        # u4 : C_v_r
        # u5 : C_v_liv
        # u6 : u (ivrate)
        # x1 : C_plasma
        # x2 : C_rbc
        self.model = PBPK_Model

    def BloodA(self):
        self.A = np.array([[(-self.model.pi_plasma - self.model.cardiac_output) / self.model.plasma_volume,
                            self.model.pi_rbc / self.model.plasma_volume, 0., 0.],
                           [self.model.pi_plasma / self.model.rbc_volume,
                            -self.model.pi_rbc / self.model.rbc_volume, 0., 0.]])
        return self.A

    def BloodB(self):
        # self.B = np.array([ [model.skin_flow / model.plasma_volume, model.kidney_flow / model.plasma_volume,
        #            model.bladder_flow/model.plasma_volume, model.rest_flow / model.plasma_volume,
        #            model.liver_flow / model.plasma_volume, 1 / model.plasma_volume], np.zeros( (1,6) )])
        self.B = np.array([[self.model.kidney_flow / self.model.plasma_volume,
                            self.model.skin_flow / self.model.plasme_volume,
                            self.model.rest_flow / self.model.plasme_volume,
                            self.model.bladder_flow / self.model.plasma_volume,
                            self.model.liver_flow / self.model.plasma_volume,
                            1 / self.model.plasma_volume,
                            self.model.organ1_flow / self.model.plasma_volume,
                            self.model.organ2_flow / self.model.plasma_volume,
                            self.model.organ3_flow / self.model.plasma_volume,
                            self.model.organ4_flow / self.model.plasma_volume,
                            self.model.organ5_flow / self.model.plasma_volume,]
                           [np.zeros((1, 11))]])
        return self.B

    def BloodC(self):
        self.C = np.array([1, 0])
        return self.C

    def BloodD(self):
        self.D = np.zeros((1, 11))
        return self.D


class Lung(PBPK_Model):
    def __init__(self, PBPK_Model):
        # Lung : 1 Input, 2 States, 2 Outputs
        # u : C_pl
        # x1 : C_art
        # x2 : C_lu
        self.model = PBPK_Model

    def LungA(self):
        self.A = np.array([[self.model.cardiac_output/self.model.blood_lung, 0,
                            (-self.model.pi_lung - self.model.cardiac_output) / self.model.blood_lung,
                            (self.model.pi_lung / self.model.p_lung) / self.model.blood_lung],
                           [0, 0, self.model.pi_lung / self.model.lung_volume,
                            (-self.model.pi_lung / self.model.p_lung) / self.model.lung_volume]])
        return self.A

    def LungB(self):
        self.B = np.array([[self.model.cardiac_output / self.model.blood_lung], [0]])
        return self.B

    def LungC(self):
        self.C = np.array([1, 0])
        return self.C

    def LungD(self):
        self.D = np.array([0])
        return self.D


class Organ1(PBPK_Model):
    def __init__(self, PBPK_Model):
        # Skin: 1Input, 2States, 2Outputs
        # x1: C_v_skin
        # x2: C_skin
        # u : C_art
        self.model = PBPK_Model

    def Organ1A(self):

        if self.model.blood_organ1 != 0:
            if self.type1 == 'met':
                self.A = np.array([[0, 0, self.model.organ1_flow / self.model.blood_organ1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                (-self.model.pi_organ1 - self.model.organ1_flow) / self.model.blood_organ1,
                                (self.model.pi_organ1 / self.model.p_organ1) / self.model.blood_organ1],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                self.model.pi_organ1 / self.model.organ1_volume,
                                (-self.model.pi_organ1 / self.model.p_organ1) / self.model.organ1_volume]])

            if self.type1 == 'non-met':
                self.A = np.array([[0, 0, self.model.organ1_flow / self.model.blood_organ1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                    (-self.model.pi_organ1 - self.model.organ1_flow)/self.model.blood_organ1,
                                    (self.model.pi_organ1 / self.model.p_organ1) / self.model.blood_organ1],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                    (self.model.pi_organ1 / self.model.organ1_volume),
                                    ((-self.model.pi_organ1 / self.model.p_organ1) - (self.model.k_met1 + self.model.k_bile1)
                                     * self.model.organ1_volume) / self.model.organ1_volume]])

        else:
            self.A = np.zeros((2, 16))
        return self.A

    def Organ1B(self):
        if self.model.blood_organ1 != 0:
            self.B = np.array([[self.model.organ1_flow/self.model.blood_organ1], [0]])
        else:
            self.B = np.zeros((2, 1))
        return self.B

    def Organ1C(self):
        if self.model.blood_organ1 != 0:
            self.C = np.array([1, 0])
        else:
            self.C = np.array([0, 0])
        return self.C

    def Organ1D(self):
        self.D = np.array([0])
        return self.D

class Organ2(PBPK_Model):
    def __init__(self, PBPK_Model):
        # Skin: 1Input, 2States, 2Outputs
        # x1: C_v_skin
        # x2: C_skin
        # u : C_art
        self.model = PBPK_Model

    def Organ2A(self):
        if self.model.blood_organ2 != 0:
            if self.type1 == 'non-met':
                self.A = np.array([[0, 0, self.model.organ2_flow / self.model.blood_organ2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                (-self.model.pi_organ2 - self.model.organ2_flow) / self.model.blood_organ2,
                                (self.model.pi_organ2 / self.model.p_organ2) / self.model.blood_organ2],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                self.model.pi_organ2 / self.model.organ2_volume,
                                (-self.model.pi_organ2 / self.model.p_organ2) / self.model.organ2_volume]])

            if self.type1 == 'met':
                self.A = np.array([[0, 0, self.model.organ2_flow / self.model.blood_organ2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                    (-self.model.pi_organ2 - self.model.organ2_flow)/self.model.blood_organ2,
                                    (self.model.pi_organ2 / self.model.p_organ2) / self.model.blood_organ2],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                    (self.model.pi_organ2 / self.model.organ2_volume),
                                    ((-self.model.pi_organ2 / self.model.p_organ2) - (self.model.k_met2 + self.model.k_bile2)
                                     * self.model.organ2_volume) / self.model.organ2_volume]])
        else:
            self.A = np.zeros((2, 18))
        return self.A

    def Organ2B(self):
        if self.model.blood_organ2 != 0:
            self.B = np.array([[self.model.organ2_flow/self.model.blood_organ2], [0]])
        else:
            self.B = np.zeros((2, 1))
        return self.B

    def Organ2C(self):
        if self.model.blood_organ2 != 0:
            self.C = np.array([1, 0])
        else:
            self.C = np.array([0, 0])
        return self.C

    def Organ2D(self):
        self.D = np.array([0])
        return self.D

class Organ3(PBPK_Model):
        def __init__(self, PBPK_Model):
            # Skin: 1Input, 2States, 2Outputs
            # x1: C_v_skin
            # x2: C_skin
            # u : C_art
            self.model = PBPK_Model

        def Organ3A(self):
            if self.model.blood_organ3 != 0:
                if self.type1 == 'non-met':
                    self.A = np.array([[0, 0, self.model.organ3_flow / self.model.blood_organ3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                    (-self.model.pi_organ3 - self.model.organ3_flow) / self.model.blood_organ3,
                                    (self.model.pi_organ3 / self.model.p_organ3) / self.model.blood_organ3],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                    self.model.pi_organ3 / self.model.organ3_volume,
                                    (-self.model.pi_organ3 / self.model.p_organ3) / self.model.organ3_volume]])

                if self.type1 == 'met':

                    self.A = np.array([[0, 0, self.model.organ3_flow / self.model.blood_organ3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                        (-self.model.pi_organ3 - self.model.organ3_flow)/self.model.blood_organ3,
                                        (self.model.pi_organ3 / self.model.p_organ3) / self.model.blood_organ3],
                                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                        (self.model.pi_organ3 / self.model.organ3_volume),
                                        ((-self.model.pi_organ3 / self.model.p_organ3) - (self.model.k_met + self.model.k_bile)
                                         * self.model.organ3_volume) / self.model.organ3_volume]])
            else:
                self.A = np.zeros((2, 20))
            return self.A

        def Organ3B(self):
            if self.model.blood_organ3 != 0:
                self.B = np.array([[self.model.organ3_flow/self.model.blood_organ3], [0]])
            else:
                self.B = np.zeros((2, 1))
            return self.B

        def Organ3C(self):
            if self.model.blood_organ3 != 0:
                self.C = np.array([1, 0])
            else:
                self.C = np.array([0, 0])
            return self.C

        def Organ3D(self):
            self.D = np.array([0])
            return self.D

class Organ4(PBPK_Model):
        def __init__(self, PBPK_Model):
            # Skin: 1Input, 2States, 2Outputs
            # x1: C_v_skin
            # x2: C_skin
            # u : C_art
            self.model = PBPK_Model

        def Organ4A(self):
            if self.model.blood_organ4 != 0:
                if self.type1 == 'non-met':
                    self.A = np.array([[0, 0, self.model.organ4_flow / self.model.blood_organ4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                    (-self.model.pi_organ4 - self.model.organ4_flow) / self.model.blood_organ4,
                                    (self.model.pi_organ4 / self.model.p_organ4) / self.model.blood_organ4],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                    self.model.pi_organ4 / self.model.organ4_volume,
                                    (-self.model.pi_organ4 / self.model.p_organ4) / self.model.organ4_volume]])

                if self.type1 == 'met':
                    self.A = np.array([[0, 0, self.model.organ4_flow / self.model.blood_organ4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                        (-self.model.pi_organ4 - self.model.organ4_flow)/self.model.blood_organ4,
                                        (self.model.pi_organ4 / self.model.p_organ4) / self.model.blood_organ4],
                                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                        (self.model.pi_organ4 / self.model.organ4_volume),
                                        ((-self.model.pi_organ4 / self.model.p_organ4) - (self.model.k_met + self.model.k_bile)
                                         * self.model.organ4_volume) / self.model.organ4_volume]])
            else:
                self.A = np.zeros((2, 22))
            return self.A

        def Organ4B(self):
            if self.model.blood_organ4 != 0:
                self.B = np.array([[self.model.organ4_flow/self.model.blood_organ4], [0]])
            else:
                self.B = np.zeros((2, 1))
            return self.B

        def Organ4C(self):
            if self.model.blood_organ4 != 0:
                self.C = np.array([1, 0])
            else:
                self.C = np.array([0, 0])
            return self.C

        def Organ4D(self):
            self.D = np.array([0])
            return self.D

class Organ5(PBPK_Model):
        def __init__(self, PBPK_Model):
            # Skin: 1Input, 2States, 2Outputs
            # x1: C_v_skin
            # x2: C_skin
            # u : C_art
            self.model = PBPK_Model

        def Organ5A(self):
            if self.model.blood_organ5 != 0:
                if self.type1 == 'non-met':
                    self.A = np.array([[0, 0, self.model.organ5_flow / self.model.blood_organ5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                    (-self.model.pi_organ5 - self.model.organ5_flow) / self.model.blood_organ5,
                                    (self.model.pi_organ5 / self.model.p_organ5) / self.model.blood_organ5],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                    self.model.pi_organ5 / self.model.organ5_volume,
                                    (-self.model.pi_organ5 / self.model.p_organ5) / self.model.organ5_volume]])

                if self.type1 == 'met':
                    self.A = np.array([[0, 0, self.model.organ5_flow / self.model.blood_organ5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                        (-self.model.pi_organ5 - self.model.organ5_flow)/self.model.blood_organ5,
                                        (self.model.pi_organ5 / self.model.p_organ5) / self.model.blood_organ5],
                                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                        (self.model.pi_organ5 / self.model.organ5_volume),
                                        ((-self.model.pi_organ5 / self.model.p_organ5) - (self.model.k_met + self.model.k_bile)
                                         * self.model.organ5_volume) / self.model.organ5_volume]])
            else:
                self.A = np.zeros((2, 24))
            return self.A

        def Organ5B(self):
            if self.model.blood_organ5 != 0:
                self.B = np.array([[self.model.organ5_flow/self.model.blood_organ5], [0]])
            else:
                self.B = np.zeros((2, 1))
            return self.B

        def Organ5C(self):
            if self.model.blood_organ5 != 0:
                self.C = np.array([1, 0])
            else:
                self.C = np.array([0, 0])
            return self.C

        def Organ5D(self):
            self.D = np.array([0])
            return self.D

class Heart(PBPK_Model):
    def __init__(self, PBPK_Model):
        # Heart: 1Input, 2States, 2Outputs
        # x1: C_v_skin
        # x2: C_skin
        # u : C_art
        self.model = PBPK_Model

    def HeartA(self):
        if self.model.blood_heart != 0:
            self.A = np.array([[0, 0, self.model.heart_flow / self.model.blood_heart, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                        (-self.model.pi_heart - self.model.heart_flow)/self.model.blood_heart,
                                        (self.model.pi_heart / self.model.p_heart) / self.model.blood_heart],
                                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                        self.model.pi_heart / self.model.heart_volume,
                                    (-self.model.pi_heart / self.model.p_heart) / self.model.heart_volume]])
        else:
            self.A = np.zeros((2, 26))
        return self.A

    def HeartB(self):
        if self.model.blood_heart != 0:
            self.B = np.array([[self.model.heart_flow/self.model.blood_heart], [0]])
        else:
            self.B = np.zeros((2, 1))
        return self.B
    def HeartC(self):
        if self.model.blood_heart != 0:
            self.C = np.array([1, 0])
        else:
            self.C = np.array([0, 0])
        return self.C
    def HeartD(self):
        self.D = np.array([0])
        return self.D

class Muscle(PBPK_Model):
    def __init__(self, PBPK_Model):
        # Muscle: 1Input, 2States, 2Outputs
        # x1: C_v_skin
        # x2: C_skin
        # u : C_art
        self.model = PBPK_Model

    def MuscleA(self):
        if self.model.blood_muscle != 0:
            self.A = np.array([[0, 0, self.model.muscle_flow / self.model.blood_muscle, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                        (-self.model.pi_muscle - self.model.muscle_flow)/self.model.blood_muscle,
                                        (self.model.pi_muscle / self.model.p_muscle) / self.model.blood_muscle],
                                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                        self.model.pi_muscle / self.model.muscle_volume,
                                    (-self.model.pi_muscle / self.model.p_muscle) / self.model.muscle_volume]])
        else:
            self.A = np.zeros((2, 28))
        return self.A

    def MuscleB(self):
        if self.model.blood_muscle != 0:
            self.B = np.array([[self.model.muscle_flow/self.model.blood_muscle], [0]])
        else:
            self.B = np.zeros((2, 1))
        return self.B
    def MuscleC(self):
        if self.model.blood_muscle != 0:
            self.C = np.array([1, 0])
        else:
            self.C = np.array([0, 0])
        return self.C
    def MuscleD(self):
        self.D = np.array([0])
        return self.D

class Spleen(PBPK_Model):
    def __init__(self, PBPK_Model):
        # Spleen: 1Input, 2States, 2Outputs
        # x1: C_v_skin
        # x2: C_skin
        # u : C_art
        self.model = PBPK_Model

    def SpleenA(self):
        if self.model.blood_spleen != 0:
            self.A = np.array([[0, 0, self.model.spleen_flow / self.model.blood_spleen, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                        (-self.model.pi_spleen - self.model.spleen_flow)/self.model.blood_spleen,
                                        (self.model.pi_spleen / self.model.p_spleen) / self.model.blood_spleen],
                                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                        self.model.pi_spleen / self.model.spleen_volume,
                                    (-self.model.pi_spleen / self.model.p_spleen) / self.model.spleen_volume]])
        else:
            self.A = np.zeros((2, 30))
        return self.A

    def SpleenB(self):
        if self.model.blood_spleen != 0:
            self.B = np.array([[self.model.spleen_flow/self.model.blood_spleen], [0]])
        else:
            self.B = np.zeros((2, 1))
        return self.B
    def SpleenC(self):
        if self.model.blood_spleen != 0:
            self.C = np.array([1, 0])
        else:
            self.C = np.array([0, 0])
        return self.C
    def SpleenD(self):
        self.D = np.array([0])
        return self.D

class Placental(PBPK_Model):
    def __init__(self, PBPK_Model):
        # Placental: 1Input, 2States, 2Outputs
        # x1: C_v_skin
        # x2: C_skin
        # u : C_art
        self.model = PBPK_Model

    def PlacentalA(self):
        if self.model.blood_placental != 0:
            self.A = np.array([[0, 0, self.model.placental_flow / self.model.blood_placental, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                        (-self.model.pi_placental - self.model.placental_flow)/self.model.blood_placental,
                                        (self.model.pi_placental / self.model.p_placental) / self.model.blood_placental],
                                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                        self.model.pi_placental / self.model.placental_volume,
                                    (-self.model.pi_placental / self.model.p_placental) / self.model.placental_volume]])
        else:
            self.A = np.zeros((2, 32))
        return self.A

    def PlacentalB(self):
        if self.model.blood_placental != 0:
            self.B = np.array([[self.model.placental_flow/self.model.blood_placental], [0]])
        else:
            self.B = np.zeros((2, 1))
        return self.B
    def PlacentalC(self):
        if self.model.blood_placental != 0:
            self.C = np.array([1, 0])
        else:
            self.C = np.array([0, 0])
        return self.C
    def PlacentalD(self):
        self.D = np.array([0])
        return self.D