# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals
from django.db.models.signals import post_save, m2m_changed
from django.db import models
from django.contrib.auth.models import User

def on_user_create(sender, instance, created, **kwargs):
    if created:
        d1 = Drug.objects.create(drug_name="default_drug", max_liver="1.4e-6", max_kidney="5.0e-6", max_influx= "0.04e-6", k_met="0.06", k_bile="0.0", k_kidney="0.0164",
                                                  p_skin="1.6", pi_skin="0.0095", p_kidney="0.14", pi_kidney="0.12", p_bladder="1.6", pi_bladder="0.0095",
                                                  p_liver="1.6", pi_liver="0.0095", p_rest="1.6", pi_rest="0.0095", pi_rbc="1.3", pi_plasma= "0.81",
                                                  p_lung="0.44", pi_lung="0.94")
        m1 = Models.objects.create(modelname="default", username=instance.username, bw="0.03", h="0.45", cardiac_output="16.5", skin_flow_factor = "0.058",skin_volume_fraction= "0.165", blood_skin_fraction="0.03",
                                          kidney_flow_factor="0.091", kidney_volume_fraction="0.017",blood_kidney_fraction="0.24",bladder_flow_factor="0.0033", bladder_volume_fraction= "0.0009",
                                          blood_bladder_fraction="0.03", blood_rest_fraction ="0.04", liver_flow_factor="0.162", liver_volume_fraction="0.055", blood_liver_fraction="0.31",
                                          blood_volume_fraction="0.5", lung_flow_factor="1.0", lung_volume_fraction="0.007", blood_lung_fraction="0.5", method="CloseLoop-MPC",
                                          method_params='{"N": 35, "target": 4.0e-7, "step": 0.0833, "end": 4}')
        m1.drugs.add(d1)


class Drug(models.Model):
    id = models.AutoField(primary_key=True)
    drug_name = models.TextField(db_column='drugName', blank=False)  # Field name made lowercase.
    k_met = models.FloatField(blank=True, null=True, default=0.0)
    k_bile = models.FloatField(blank=True, null=True, default=0.0)
    k_kidney = models.FloatField(blank=True, null=True, default=0.0)
    max_liver = models.FloatField(blank=True, null=True, default=0.0)
    max_kidney = models.FloatField(blank=True, null=True, default=0.0)
    max_influx = models.FloatField(blank=True, null=True, default=0.0)
    p_skin = models.FloatField(db_column='P_skin', blank=True, null=True, default=0.0)  # Field name made lowercase.
    pi_skin = models.FloatField(db_column='Pi_skin', blank=True, null=True, default=0.0)  # Field name made lowercase.
    p_kidney = models.FloatField(db_column='P_kidney', blank=True, null=True, default=0.0)  # Field name made lowercase.
    pi_kidney = models.FloatField(db_column='Pi_kidney', blank=True, null=True, default=0.0)  # Field name made lowercase.
    p_bladder = models.FloatField(db_column='P_bladder', blank=True, null=True, default=0.0)  # Field name made lowercase.
    pi_bladder = models.FloatField(db_column='Pi_bladder', blank=True, null=True, default=0.0)  # Field name made lowercase.
    p_rest = models.FloatField(db_column='P_rest', blank=True, null=True, default=0.0)  # Field name made lowercase.
    pi_rest = models.FloatField(db_column='Pi_rest', blank=True, null=True, default=0.0)  # Field name made lowercase.
    p_liver = models.FloatField(db_column='P_liver', blank=True, null=True, default=0.0)  # Field name made lowercase.
    pi_liver = models.FloatField(db_column='Pi_liver', blank=True, null=True, default=0.0)  # Field name made lowercase.
    pi_rbc = models.FloatField(db_column='Pi_rbc', blank=True, null=True, default=0.0)  # Field name made lowercase.
    pi_plasma = models.FloatField(db_column='Pi_plasma', blank=True, null=True, default=0.0)  # Field name made lowercase.
    p_lung = models.FloatField(db_column='P_lung', blank=True, null=True, default=0.0)  # Field name made lowercase.
    pi_lung = models.FloatField(db_column='Pi_lung', blank=True, null=True, default=0.0)  # Field name made lowercase.
    min_liver = models.FloatField(blank=True, null=True, default=0.0)
    min_kidney = models.FloatField(blank=True, null=True, default=0.0)
    max_residual = models.FloatField(blank=True, null=True, default=1)
    min_residual = models.FloatField(blank=True, null=True, default=0.0)
    max_skin = models.FloatField(blank=True, null=True, default=1)
    min_skin = models.FloatField(blank=True, null=True, default=0.0)
    max_bladder = models.FloatField(blank=True, null=True, default=1)
    min_bladder = models.FloatField(blank=True, null=True, default=0.0)
    max_lung = models.FloatField(blank=True, null=True, default=1)
    min_lung = models.FloatField(blank=True, null=True, default=0.0)
    p_organ1 = models.FloatField(db_column='P_organ1', blank=True, null=True, default=0.0)  # Field name made lowercase.
    pi_organ1 = models.FloatField(db_column='Pi_organ1', blank=True, null=True, default=0.0)  # Field name made lowercase.
    p_organ2 = models.FloatField(db_column='P_organ2', blank=True, null=True, default=0.0)  # Field name made lowercase.
    pi_organ2 = models.FloatField(db_column='Pi_organ2', blank=True, null=True, default=0.0)  # Field name made lowercase.
    p_organ3 = models.FloatField(db_column='P_organ3', blank=True, null=True, default=0.0)  # Field name made lowercase.
    pi_organ3 = models.FloatField(db_column='Pi_organ3', blank=True, null=True, default=0.0)  # Field name made lowercase.
    p_organ4 = models.FloatField(db_column='P_organ4', blank=True, null=True, default=0.0)  # Field name made lowercase.
    pi_organ4 = models.FloatField(db_column='Pi_organ4', blank=True, null=True, default=0.0)  # Field name made lowercase.
    p_organ5 = models.FloatField(db_column='P_organ5', blank=True, null=True, default=0.0)  # Field name made lowercase.
    pi_organ5 = models.FloatField(db_column='Pi_organ5', blank=True, null=True, default=0.0)  # Field name made lowercase.
    p_heart = models.FloatField(db_column='P_heart', blank=True, null=True, default=0.0)  # Field name made lowercase.
    pi_heart = models.FloatField(db_column='Pi_heart', blank=True, null=True, default=0.0)  # Field name made lowercase.
    max_heart = models.FloatField(blank=True, null=True, default=1)
    min_heart = models.FloatField(blank=True, null=True, default=0.0)
    p_muscle = models.FloatField(db_column='P_muscle', blank=True, null=True, default=0.0)  # Field name made lowercase.
    pi_muscle = models.FloatField(db_column='Pi_muscle', blank=True, null=True, default=0.0)  # Field name made lowercase.
    max_muscle = models.FloatField(blank=True, null=True, default=1)
    min_muscle = models.FloatField(blank=True, null=True, default=0.0)
    p_spleen = models.FloatField(db_column='P_spleen', blank=True, null=True, default=0.0)  # Field name made lowercase.
    pi_spleen = models.FloatField(db_column='Pi_spleen', blank=True, null=True, default=0.0)  # Field name made lowercase.
    max_spleen = models.FloatField(blank=True, null=True, default=1)
    min_spleen = models.FloatField(blank=True, null=True, default=0.0)
    p_placental = models.FloatField(db_column='P_placental', blank=True, null=True, default=0.0)  # Field name made lowercase.
    pi_placental = models.FloatField(db_column='Pi_placental', blank=True, null=True, default=0.0)  # Field name made lowercase.
    max_placental = models.FloatField(blank=True, null=True, default=1)
    min_placental = models.FloatField(blank=True, null=True, default=0.0)

    organ1_params = models.TextField(blank=True, null=True, max_length=2048)  # json string with method parameters for additional organs

    class Meta:
        db_table = 'drugs'


class Models(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.TextField(db_column='userName', blank=False)  # Field name made lowercase.
    modelname = models.TextField(db_column='modelName', blank=False)  # Field name made lowercase.

    bw = models.FloatField(blank=True, null=True)
    h = models.FloatField(blank=True, null=True)
    cardiac_output = models.FloatField(blank=True, null=True, default=0.0)
    skin_flow_factor = models.FloatField(blank=True, null=True, default=0.0)
    skin_volume_fraction = models.FloatField(blank=True, null=True, default=0.0)
    blood_skin_fraction = models.FloatField(blank=True, null=True, default=0.0)
    kidney_flow_factor = models.FloatField(blank=True, null=True, default=0.0)
    kidney_volume_fraction = models.FloatField(blank=True, null=True, default=0.0)
    blood_kidney_fraction = models.FloatField(blank=True, null=True, default=0.0)
    bladder_flow_factor = models.FloatField(blank=True, null=True, default=0.0)
    bladder_volume_fraction = models.FloatField(blank=True, null=True, default=0.0)
    blood_bladder_fraction = models.FloatField(blank=True, null=True, default=0.0)
    blood_rest_fraction = models.FloatField(blank=True, null=True, default=0.0)
    liver_flow_factor = models.FloatField(blank=True, null=True, default=0.0)
    liver_volume_fraction = models.FloatField(blank=True, null=True, default=0.0)
    blood_liver_fraction = models.FloatField(blank=True, null=True, default=0.0)
    blood_volume_fraction = models.FloatField(blank=True, null=True, default=0.0)
    lung_flow_factor = models.FloatField(blank=True, null=True, default=0.0)
    lung_volume_fraction = models.FloatField(blank=True, null=True, default=0.0)
    blood_lung_fraction = models.FloatField(blank=True, null=True, default=0.0)
    organ1_flow_factor = models.FloatField(blank=True, null=True, default=0.0)
    organ1_volume_fraction = models.FloatField(blank=True, null=True, default=0.0)
    blood_organ1_fraction = models.FloatField(blank=True, null=True, default=0.0)
    organ2_flow_factor = models.FloatField(blank=True, null=True, default=0.0)
    organ2_volume_fraction = models.FloatField(blank=True, null=True, default=0.0)
    blood_organ2_fraction = models.FloatField(blank=True, null=True, default=0.0)
    organ3_flow_factor = models.FloatField(blank=True, null=True, default=0.0)
    organ3_volume_fraction = models.FloatField(blank=True, null=True, default=0.0)
    blood_organ3_fraction = models.FloatField(blank=True, null=True, default=0.0)
    organ4_flow_factor = models.FloatField(blank=True, null=True, default=0.0)
    organ4_volume_fraction = models.FloatField(blank=True, null=True, default=0.0)
    blood_organ4_fraction = models.FloatField(blank=True, null=True, default=0.0)
    organ5_flow_factor = models.FloatField(blank=True, null=True, default=0.0)
    organ5_volume_fraction = models.FloatField(blank=True, null=True, default=0.0)
    blood_organ5_fraction = models.FloatField(blank=True, null=True, default=0.0)
    organ1_name= models.TextField(db_column='organ1Name', blank=True,)  # Field name made lowercase
    organ2_name= models.TextField(db_column='organ2Name', blank=True,)  # Field name made lowercase
    organ3_name= models.TextField(db_column='organ3Name', blank=True,)  # Field name made lowercase
    organ4_name= models.TextField(db_column='organ4Name', blank=True,)  # Field name made lowercase
    organ5_name= models.TextField(db_column='organ5Name', blank=True,)  # Field name made lowercase
    heart_flow_factor = models.FloatField(blank=True, null=True, default=0.0)
    heart_volume_fraction = models.FloatField(blank=True, null=True, default=0.0)
    blood_heart_fraction = models.FloatField(blank=True, null=True, default=0.0)
    muscle_flow_factor = models.FloatField(blank=True, null=True, default=0.0)
    muscle_volume_fraction = models.FloatField(blank=True, null=True, default=0.0)
    blood_muscle_fraction = models.FloatField(blank=True, null=True, default=0.0)
    blood_gut_fraction = models.FloatField(blank=True, null=True, default=0.0)
    spleen_flow_factor = models.FloatField(blank=True, null=True, default=0.0)
    spleen_volume_fraction = models.FloatField(blank=True, null=True, default=0.0)
    blood_spleen_fraction = models.FloatField(blank=True, null=True, default=0.0)
    placental_flow_factor = models.FloatField(blank=True, null=True, default=0.0)
    placental_volume_fraction = models.FloatField(blank=True, null=True, default=0.0)
    blood_placental_fraction = models.FloatField(blank=True, null=True, default=0.0)

    method = models.TextField(blank=False, null=True)  # OpenLoop, CloseLoop-MPC or CloseLoop-PID
    method_params = models.TextField(blank=False, null=True)  # json string with method parameters
    plot_params = models.TextField(blank=True, null=True)  # json string with all organs plots
    step_params = models.TextField(blank=True, null=True)  # json string with data for plotting administration rate


    #N = models.IntegerField(blank=False, null=False, default=35)
    #target = models.FloatField(blank=False, null=False, default=4.0e-7)
    #step = models.FloatField(blank=False, null=False, default=0.0833)
    #end = models.FloatField(blank=False, null=False, default=4.0)
    drugs=models.ManyToManyField(Drug, blank=True)

    class Meta:
        db_table = 'models'
        unique_together = ('username', 'modelname',)

post_save.connect(on_user_create, sender=User)

