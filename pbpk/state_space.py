from initWeb import *
from control.matlab import *
from scipy.signal import cont2discrete
import numpy as np

from yottalab import bb_dlqr, bb_dare
from util import *


class System(PBPK_Model, Skin, Kidney, Bladder, Residual,
                 Liver, Blood, Lung, Organ1, Organ2, Organ3, Organ4, Organ5):
    def __init__(self, PBPK_Model, Skin, Kidney, Bladder, Residual,
                 Liver, Blood, Lung, Organ1, Organ2, Organ3, Organ4, Organ5, Heart, Muscle, Spleen, Placental):
        self.model = PBPK_Model
        self.skin = Skin
        self.kidney = Kidney
        self.bladder = Bladder
        self.residual = Residual
        self.liver = Liver
        self.blood = Blood
        self.lung = Lung
        self.organ1 = Organ1
        self.organ2 = Organ2
        self.organ3 = Organ3
        self.organ4 = Organ4
        self.organ5 = Organ5
        self.heart = Heart
        self.muscle = Muscle
        self.spleen = Spleen
        self.placental = Placental


    def ContinuousSystem(self):
        self.A = np.array([self.BloodA()[0], self.BloodA()[1],
                           self.LungA()[0], self.LungA()[1]])
        if self.model.blood_skin != 0:
            mid_matrix = np.zeros((2, self.A.shape[0]))
            mid_matrix[0:1, 2:3] = self.model.skin_flow / self.model.blood_skin
            self.A = np.append(self.A, mid_matrix, axis=0)
            mid_matrix = np.zeros((self.A.shape[0], 2))
            mid_matrix[0:1, :] = np.array([[self.model.skin_flow / self.model.plasma_volume, 0]])
            mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_skin - self.model.skin_flow)
                                                                           / self.model.blood_skin,
                                                                           (self.model.pi_skin / self.model.p_skin) /
                                                                           self.model.blood_skin],
                                                                          [self.model.pi_skin/self.model.skin_volume,
                                                                           (-self.model.pi_skin / self.model.p_skin) /
                                                                           self.model.skin_volume]])

            self.A = np.append(self.A, mid_matrix, axis=1)
        if self.model.blood_bladder != 0:
            mid_matrix = np.zeros((2, self.A.shape[0]))
            mid_matrix[0:1, 2:3] = self.model.bladder_flow / self.model.blood_bladder
            self.A = np.append(self.A, mid_matrix, axis=0)
            mid_matrix = np.zeros((self.A.shape[0], 2))
            mid_matrix[0:1, :] = np.array([[self.model.bladder_flow / self.model.plasma_volume, 0]])
            mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_bladder -
                                                                             self.model.bladder_flow)
                                                                          / self.model.blood_bladder,
                                                                          (self.model.pi_bladder / self.model.p_bladder)
                                                                          / self.model.blood_bladder],
                                                                           [self.model.pi_bladder /
                                                                            self.model.bladder_volume,
                                                                            (-self.model.pi_bladder /
                                                                             self.model.p_bladder) /
                                                                            self.model.bladder_volume]])
            self.A = np.append(self.A, mid_matrix, axis=1)
        if self.model.blood_liver != 0:
            mid_matrix = np.zeros((2, self.A.shape[0]))
            mid_matrix[0:1, 2:3] = self.model.liver_flow / self.model.blood_liver
            self.A = np.append(self.A, mid_matrix, axis=0)
            mid_matrix = np.zeros((self.A.shape[0], 2))
            mid_matrix[0:1, :] = np.array([[self.model.liver_flow / self.model.plasma_volume, 0]])
            mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_liver -
                                                                             self.model.liver_flow)
                                                                          / self.model.blood_liver,
                                                                          (self.model.pi_liver / self.model.p_liver)
                                                                          / self.model.blood_liver],
                                                                           [self.model.pi_liver /
                                                                            self.model.liver_volume,
                                                                            (-self.model.pi_liver /
                                                                             self.model.p_liver -
                                                                             (self.model.k_met+self.model.k_bile) * self.model.liver_volume) /
                                                                            self.model.liver_volume]])
            self.A = np.append(self.A, mid_matrix, axis=1)
        if self.model.blood_rest != 0:
            mid_matrix = np.zeros((2, self.A.shape[0]))
            mid_matrix[0:1, 2:3] = self.model.rest_flow / self.model.blood_rest
            self.A = np.append(self.A, mid_matrix, axis=0)
            mid_matrix = np.zeros((self.A.shape[0], 2))
            mid_matrix[0:1, :] = np.array([[self.model.rest_flow / self.model.plasma_volume, 0]])
            mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_rest -
                                                                             self.model.rest_flow)
                                                                          / self.model.blood_rest,
                                                                          (self.model.pi_rest / self.model.p_rest)
                                                                          / self.model.blood_rest],
                                                                           [self.model.pi_rest /
                                                                            self.model.rest_volume,
                                                                            (-self.model.pi_rest /
                                                                             self.model.p_rest) /
                                                                            self.model.rest_volume]])
            self.A = np.append(self.A, mid_matrix, axis=1)
        if self.model.blood_kidney != 0:
            mid_matrix = np.zeros((2, self.A.shape[0]))
            mid_matrix[0:1, 2:3] = self.model.kidney_flow / self.model.blood_kidney
            self.A = np.append(self.A, mid_matrix, axis=0)
            mid_matrix = np.zeros((self.A.shape[0], 2))
            mid_matrix[0:1, :] = np.array([[self.model.kidney_flow / self.model.plasma_volume, 0]])
            mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_kidney -
                                                                             self.model.kidney_flow)
                                                                          / self.model.blood_kidney,
                                                                          (self.model.pi_kidney / self.model.p_kidney)
                                                                          / self.model.blood_kidney],
                                                                           [self.model.pi_kidney /
                                                                            self.model.kidney_volume,
                                                                            (-self.model.pi_kidney /
                                                                             self.model.p_kidney) /
                                                                            self.model.kidney_volume]])
            self.A = np.append(self.A, mid_matrix, axis=1)
        if self.model.blood_organ1 != 0:
            mid_matrix = np.zeros((2, self.A.shape[0]))
            mid_matrix[0:1, 2:3] = self.model.organ1_flow / self.model.blood_organ1
            self.A = np.append(self.A, mid_matrix, axis=0)
            mid_matrix = np.zeros((self.A.shape[0], 2))
            mid_matrix[0:1, :] = np.array([[self.model.organ1_flow / self.model.plasma_volume, 0]])
            if self.model.type1 == 'met':
                mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_organ1 -
                                                                                 self.model.organ1_flow)
                                                                              / self.model.blood_organ1,
                                                                              (self.model.pi_organ1 / self.model.p_organ1)
                                                                              / self.model.blood_organ1],
                                                                               [self.model.pi_organ1 /
                                                                                self.model.organ1_volume,
                                                                                (-self.model.pi_organ1 /
                                                                                 self.model.p_organ1 -
                                                                             (self.model.k_met1+self.model.k_bile1) * self.model.organ1_volume) /
                                                                                self.model.organ1_volume]])
            if self.model.type1 == 'non-met':
                mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_organ1 -
                                                                                 self.model.organ1_flow)
                                                                              / self.model.blood_organ1,
                                                                              (self.model.pi_organ1 / self.model.p_organ1)
                                                                              / self.model.blood_organ1],
                                                                               [self.model.pi_organ1 /
                                                                                self.model.organ1_volume,
                                                                                (-self.model.pi_organ1 /
                                                                                 self.model.p_organ1) /
                                                                                self.model.organ1_volume]])
            self.A = np.append(self.A, mid_matrix, axis=1)

        if self.model.blood_organ2 != 0:
            mid_matrix = np.zeros((2, self.A.shape[0]))
            mid_matrix[0:1, 2:3] = self.model.organ2_flow / self.model.blood_organ2
            self.A = np.append(self.A, mid_matrix, axis=0)
            mid_matrix = np.zeros((self.A.shape[0], 2))
            mid_matrix[0:1, :] = np.array([[self.model.organ2_flow / self.model.plasma_volume, 0]])
            if self.model.type2 == 'non-met':
                mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_organ2 -
                                                                                 self.model.organ2_flow)
                                                                              / self.model.blood_organ2,
                                                                              (self.model.pi_organ2 / self.model.p_organ2)
                                                                              / self.model.blood_organ2],
                                                                               [self.model.pi_organ2 /
                                                                                self.model.organ2_volume,
                                                                                (-self.model.pi_organ2 /
                                                                                 self.model.p_organ2) /
                                                                                self.model.organ2_volume]])
            if self.model.type2 == 'met':
                mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_organ2 -
                                                                                 self.model.organ2_flow)
                                                                              / self.model.blood_organ2,
                                                                              (self.model.pi_organ2 / self.model.p_organ2)
                                                                              / self.model.blood_organ2],
                                                                               [self.model.pi_organ2 /
                                                                                self.model.organ2_volume,
                                                                                (-self.model.pi_organ2 /
                                                                                 self.model.p_organ2 -
                                                                             (self.model.k_met2+self.model.k_bile2) * self.model.organ2_volume) /
                                                                                self.model.organ2_volume]])
            self.A = np.append(self.A, mid_matrix, axis=1)

        if self.model.blood_organ3 != 0:
            mid_matrix = np.zeros((2, self.A.shape[0]))
            mid_matrix[0:1, 2:3] = self.model.organ3_flow / self.model.blood_organ3
            self.A = np.append(self.A, mid_matrix, axis=0)
            mid_matrix = np.zeros((self.A.shape[0], 2))
            mid_matrix[0:1, :] = np.array([[self.model.organ3_flow / self.model.plasma_volume, 0]])
            if self.model.type3 == 'non-met':
                mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_organ3 -
                                                                                 self.model.organ3_flow)
                                                                              / self.model.blood_organ3,
                                                                              (self.model.pi_organ3 / self.model.p_organ3)
                                                                              / self.model.blood_organ3],
                                                                               [self.model.pi_organ3 /
                                                                                self.model.organ3_volume,
                                                                                (-self.model.pi_organ3 /
                                                                                 self.model.p_organ3) /
                                                                                self.model.organ3_volume]])
            if self.model.type3 == 'met':
                 mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_organ3 -
                                                                                 self.model.organ3_flow)
                                                                              / self.model.blood_organ3,
                                                                              (self.model.pi_organ3 / self.model.p_organ3)
                                                                              / self.model.blood_organ3],
                                                                               [self.model.pi_organ3 /
                                                                                self.model.organ3_volume,
                                                                                (-self.model.pi_organ3 /
                                                                                 self.model.p_organ3 -
                                                                                 (self.model.k_met3+self.model.k_bile3) * self.model.organ3_volume) /
                                                                                self.model.organ3_volume]])

            self.A = np.append(self.A, mid_matrix, axis=1)

        if self.model.blood_organ4 != 0:
            mid_matrix = np.zeros((2, self.A.shape[0]))
            mid_matrix[0:1, 2:3] = self.model.organ4_flow / self.model.blood_organ4
            self.A = np.append(self.A, mid_matrix, axis=0)
            mid_matrix = np.zeros((self.A.shape[0], 2))
            mid_matrix[0:1, :] = np.array([[self.model.organ4_flow / self.model.plasma_volume, 0]])
            if self.model.type4 == 'non-met':
                mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_organ4 -
                                                                             self.model.organ4_flow)
                                                                          / self.model.blood_organ4,
                                                                          (self.model.pi_organ4 / self.model.p_organ4)
                                                                          / self.model.blood_organ4],
                                                                           [self.model.pi_organ4 /
                                                                            self.model.organ4_volume,
                                                                            (-self.model.pi_organ4 /
                                                                             self.model.p_organ4) /
                                                                            self.model.organ4_volume]])
            if self.model.type4 == "met":
                 mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_organ4 -
                                                                             self.model.organ4_flow)
                                                                          / self.model.blood_organ4,
                                                                          (self.model.pi_organ4 / self.model.p_organ4)
                                                                          / self.model.blood_organ4],
                                                                           [self.model.pi_organ4 /
                                                                            self.model.organ4_volume,
                                                                            (-self.model.pi_organ4 /
                                                                              self.model.p_organ4 -
                                                                                 (self.model.k_met4+self.model.k_bile4) * self.model.organ4_volume) /
                                                                            self.model.organ4_volume]])

            self.A = np.append(self.A, mid_matrix, axis=1)

        if self.model.blood_organ5 != 0:
            mid_matrix = np.zeros((2, self.A.shape[0]))
            mid_matrix[0:1, 2:3] = self.model.organ5_flow / self.model.blood_organ5
            self.A = np.append(self.A, mid_matrix, axis=0)
            mid_matrix = np.zeros((self.A.shape[0], 2))
            mid_matrix[0:1, :] = np.array([[self.model.organ5_flow / self.model.plasma_volume, 0]])
            if self.model.type5 == "non-met":
                mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_organ5 -
                                                                                 self.model.organ5_flow)
                                                                              / self.model.blood_organ5,
                                                                              (self.model.pi_organ5 / self.model.p_organ5)
                                                                              / self.model.blood_organ5],
                                                                               [self.model.pi_organ5 /
                                                                                self.model.organ5_volume,
                                                                                (-self.model.pi_organ5 /
                                                                                 self.model.p_organ5) /
                                                                                self.model.organ5_volume]])
            if self.model.type5 == "met":
                mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_organ5 -
                                                                                 self.model.organ5_flow)
                                                                              / self.model.blood_organ5,
                                                                              (self.model.pi_organ5 / self.model.p_organ5)
                                                                              / self.model.blood_organ5],
                                                                               [self.model.pi_organ5 /
                                                                                self.model.organ5_volume,
                                                                                (-self.model.pi_organ5 /
                                                                                  self.model.p_organ5 -
                                                                                 (self.model.k_met5+self.model.k_bile5) * self.model.organ5_volume) /
                                                                                self.model.organ5_volume]])
            self.A = np.append(self.A, mid_matrix, axis=1)

        if self.model.blood_heart != 0:
            mid_matrix = np.zeros((2, self.A.shape[0]))
            mid_matrix[0:1, 2:3] = self.model.heart_flow / self.model.blood_heart
            self.A = np.append(self.A, mid_matrix, axis=0)
            mid_matrix = np.zeros((self.A.shape[0], 2))
            mid_matrix[0:1, :] = np.array([[self.model.heart_flow / self.model.plasma_volume, 0]])
            mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_heart -
                                                                             self.model.heart_flow)
                                                                          / self.model.blood_heart,
                                                                          (self.model.pi_heart / self.model.p_heart)
                                                                          / self.model.blood_heart],
                                                                           [self.model.pi_heart /
                                                                            self.model.heart_volume,
                                                                            (-self.model.pi_heart /
                                                                             self.model.p_heart) /
                                                                            self.model.heart_volume]])
            self.A = np.append(self.A, mid_matrix, axis=1)

        if self.model.blood_muscle != 0:
            mid_matrix = np.zeros((2, self.A.shape[0]))
            mid_matrix[0:1, 2:3] = self.model.muscle_flow / self.model.blood_muscle
            self.A = np.append(self.A, mid_matrix, axis=0)
            mid_matrix = np.zeros((self.A.shape[0], 2))
            mid_matrix[0:1, :] = np.array([[self.model.muscle_flow / self.model.plasma_volume, 0]])
            mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_muscle -
                                                                             self.model.muscle_flow)
                                                                          / self.model.blood_muscle,
                                                                          (self.model.pi_muscle / self.model.p_muscle)
                                                                          / self.model.blood_muscle],
                                                                           [self.model.pi_muscle /
                                                                            self.model.muscle_volume,
                                                                            (-self.model.pi_muscle /
                                                                             self.model.p_muscle) /
                                                                            self.model.muscle_volume]])
            self.A = np.append(self.A, mid_matrix, axis=1)

        if self.model.blood_spleen != 0:
            mid_matrix = np.zeros((2, self.A.shape[0]))
            mid_matrix[0:1, 2:3] = self.model.spleen_flow / self.model.blood_spleen
            self.A = np.append(self.A, mid_matrix, axis=0)
            mid_matrix = np.zeros((self.A.shape[0], 2))
            mid_matrix[0:1, :] = np.array([[self.model.spleen_flow / self.model.plasma_volume, 0]])
            mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_spleen -
                                                                             self.model.spleen_flow)
                                                                          / self.model.blood_spleen,
                                                                          (self.model.pi_spleen / self.model.p_spleen)
                                                                          / self.model.blood_spleen],
                                                                           [self.model.pi_spleen /
                                                                            self.model.spleen_volume,
                                                                            (-self.model.pi_spleen /
                                                                             self.model.p_spleen) /
                                                                            self.model.spleen_volume]])
            self.A = np.append(self.A, mid_matrix, axis=1)


        if self.model.blood_placental != 0:
            mid_matrix = np.zeros((2, self.A.shape[0]))
            mid_matrix[0:1, 2:3] = self.model.placental_flow / self.model.blood_placental
            self.A = np.append(self.A, mid_matrix, axis=0)
            mid_matrix = np.zeros((self.A.shape[0], 2))
            mid_matrix[0:1, :] = np.array([[self.model.placental_flow / self.model.plasma_volume, 0]])
            mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_placental -
                                                                             self.model.placental_flow)
                                                                          / self.model.blood_placental,
                                                                          (self.model.pi_placental / self.model.p_placental)
                                                                          / self.model.blood_placental],
                                                                           [self.model.pi_placental /
                                                                            self.model.placental_volume,
                                                                            (-self.model.pi_placental /
                                                                             self.model.p_placental) /
                                                                            self.model.placental_volume]])
            self.A = np.append(self.A, mid_matrix, axis=1)

        self.B = np.zeros((self.A.shape[0], 1))
        self.B[0:1, 0:1] = 1./self.model.plasma_volume
        self.C = np.zeros((1, self.A.shape[0]))
        self.C[0:1, 0:1] = 1
        self.D = np.zeros((1, 1))
        csys = ss(self.A, self.B, self.C, self.D)
        return csys

    def DiscreteSystem(self):
        self.A = np.array([self.BloodA()[0], self.BloodA()[1],
                           self.LungA()[0], self.LungA()[1]])
        if self.model.blood_skin != 0:
            mid_matrix = np.zeros((2, self.A.shape[0]))
            mid_matrix[0:1, 2:3] = self.model.skin_flow / self.model.blood_skin
            self.A = np.append(self.A, mid_matrix, axis=0)
            mid_matrix = np.zeros((self.A.shape[0], 2))
            mid_matrix[0:1, :] = np.array([[self.model.skin_flow / self.model.plasma_volume, 0]])
            mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_skin - self.model.skin_flow)
                                                                           / self.model.blood_skin,
                                                                           (self.model.pi_skin / self.model.p_skin) /
                                                                           self.model.blood_skin],
                                                                          [self.model.pi_skin/self.model.skin_volume,
                                                                           (-self.model.pi_skin / self.model.p_skin) /
                                                                           self.model.skin_volume]])
            self.A = np.append(self.A, mid_matrix, axis=1)
        if self.model.blood_bladder != 0:
            mid_matrix = np.zeros((2, self.A.shape[0]))
            mid_matrix[0:1, 2:3] = self.model.bladder_flow / self.model.blood_bladder
            self.A = np.append(self.A, mid_matrix, axis=0)
            mid_matrix = np.zeros((self.A.shape[0], 2))
            mid_matrix[0:1, :] = np.array([[self.model.bladder_flow / self.model.plasma_volume, 0]])
            mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_bladder -
                                                                             self.model.bladder_flow)
                                                                          / self.model.blood_bladder,
                                                                          (self.model.pi_bladder / self.model.p_bladder)
                                                                          / self.model.blood_bladder],
                                                                           [self.model.pi_bladder /
                                                                            self.model.bladder_volume,
                                                                            (-self.model.pi_bladder /
                                                                             self.model.p_bladder) /
                                                                            self.model.bladder_volume]])
            self.A = np.append(self.A, mid_matrix, axis=1)
        if self.model.blood_liver != 0:
            mid_matrix = np.zeros((2, self.A.shape[0]))
            mid_matrix[0:1, 2:3] = self.model.liver_flow / self.model.blood_liver
            self.A = np.append(self.A, mid_matrix, axis=0)
            mid_matrix = np.zeros((self.A.shape[0], 2))
            mid_matrix[0:1, :] = np.array([[self.model.liver_flow / self.model.plasma_volume, 0]])
            mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_liver -
                                                                             self.model.liver_flow)
                                                                          / self.model.blood_liver,
                                                                          (self.model.pi_liver / self.model.p_liver)
                                                                          / self.model.blood_liver],
                                                                           [self.model.pi_liver /
                                                                            self.model.liver_volume,
                                                                            (-self.model.pi_liver /
                                                                             self.model.p_liver -
                                                                             (self.model.k_met+self.model.k_bile) * self.model.liver_volume) /
                                                                            self.model.liver_volume]])
            self.A = np.append(self.A, mid_matrix, axis=1)
        if self.model.blood_rest != 0:
            mid_matrix = np.zeros((2, self.A.shape[0]))
            mid_matrix[0:1, 2:3] = self.model.rest_flow / self.model.blood_rest
            self.A = np.append(self.A, mid_matrix, axis=0)
            mid_matrix = np.zeros((self.A.shape[0], 2))
            mid_matrix[0:1, :] = np.array([[self.model.rest_flow / self.model.plasma_volume, 0]])
            mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_rest -
                                                                             self.model.rest_flow)
                                                                          / self.model.blood_rest,
                                                                          (self.model.pi_rest / self.model.p_rest)
                                                                          / self.model.blood_rest],
                                                                           [self.model.pi_rest /
                                                                            self.model.rest_volume,
                                                                            (-self.model.pi_rest /
                                                                             self.model.p_rest) /
                                                                            self.model.rest_volume]])
            self.A = np.append(self.A, mid_matrix, axis=1)
        if self.model.blood_kidney != 0:
            mid_matrix = np.zeros((2, self.A.shape[0]))
            mid_matrix[0:1, 2:3] = self.model.kidney_flow / self.model.blood_kidney
            self.A = np.append(self.A, mid_matrix, axis=0)
            mid_matrix = np.zeros((self.A.shape[0], 2))
            mid_matrix[0:1, :] = np.array([[self.model.kidney_flow / self.model.plasma_volume, 0]])
            mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_kidney -
                                                                             self.model.kidney_flow)
                                                                          / self.model.blood_kidney,
                                                                          (self.model.pi_kidney / self.model.p_kidney)
                                                                          / self.model.blood_kidney],
                                                                           [self.model.pi_kidney /
                                                                            self.model.kidney_volume,
                                                                            (-self.model.pi_kidney /
                                                                             self.model.p_kidney) /
                                                                            self.model.kidney_volume]])
            self.A = np.append(self.A, mid_matrix, axis=1)
        if self.model.blood_organ1 != 0:
            mid_matrix = np.zeros((2, self.A.shape[0]))
            mid_matrix[0:1, 2:3] = self.model.organ1_flow / self.model.blood_organ1
            self.A = np.append(self.A, mid_matrix, axis=0)
            mid_matrix = np.zeros((self.A.shape[0], 2))
            mid_matrix[0:1, :] = np.array([[self.model.organ1_flow / self.model.plasma_volume, 0]])
            if self.model.type1 == 'met':
                mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_organ1 -
                                                                                 self.model.organ1_flow)
                                                                              / self.model.blood_organ1,
                                                                              (self.model.pi_organ1 / self.model.p_organ1)
                                                                              / self.model.blood_organ1],
                                                                               [self.model.pi_organ1 /
                                                                                self.model.organ1_volume,
                                                                                (-self.model.pi_organ1 /
                                                                                 self.model.p_organ1 -
                                                                             (self.model.k_met1+self.model.k_bile1) * self.model.organ1_volume) /
                                                                                self.model.organ1_volume]])
            if self.model.type1 == 'non-met':
                mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_organ1 -
                                                                                 self.model.organ1_flow)
                                                                              / self.model.blood_organ1,
                                                                              (self.model.pi_organ1 / self.model.p_organ1)
                                                                              / self.model.blood_organ1],
                                                                               [self.model.pi_organ1 /
                                                                                self.model.organ1_volume,
                                                                                (-self.model.pi_organ1 /
                                                                                 self.model.p_organ1) /
                                                                                self.model.organ1_volume]])
            self.A = np.append(self.A, mid_matrix, axis=1)

        if self.model.blood_organ2 != 0:
            mid_matrix = np.zeros((2, self.A.shape[0]))
            mid_matrix[0:1, 2:3] = self.model.organ2_flow / self.model.blood_organ2
            self.A = np.append(self.A, mid_matrix, axis=0)
            mid_matrix = np.zeros((self.A.shape[0], 2))
            mid_matrix[0:1, :] = np.array([[self.model.organ1_flow / self.model.plasma_volume, 0]])
            if self.model.type2 == 'non-met':
                mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_organ2 -
                                                                                 self.model.organ2_flow)
                                                                              / self.model.blood_organ2,
                                                                              (self.model.pi_organ2 / self.model.p_organ2)
                                                                              / self.model.blood_organ2],
                                                                               [self.model.pi_organ2 /
                                                                                self.model.organ2_volume,
                                                                                (-self.model.pi_organ2 /
                                                                                 self.model.p_organ2) /
                                                                                self.model.organ2_volume]])
            if self.model.type2 == 'met':
                mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_organ2 -
                                                                                 self.model.organ2_flow)
                                                                              / self.model.blood_organ2,
                                                                              (self.model.pi_organ2 / self.model.p_organ2)
                                                                              / self.model.blood_organ2],
                                                                               [self.model.pi_organ2 /
                                                                                self.model.organ2_volume,
                                                                                (-self.model.pi_organ2 /
                                                                                 self.model.p_organ2 -
                                                                             (self.model.k_met2+self.model.k_bile2) * self.model.organ2_volume) /
                                                                                self.model.organ2_volume]])
            self.A = np.append(self.A, mid_matrix, axis=1)

        if self.model.blood_organ3 != 0:
            mid_matrix = np.zeros((2, self.A.shape[0]))
            mid_matrix[0:1, 2:3] = self.model.organ3_flow / self.model.blood_organ3
            self.A = np.append(self.A, mid_matrix, axis=0)
            mid_matrix = np.zeros((self.A.shape[0], 2))
            mid_matrix[0:1, :] = np.array([[self.model.organ3_flow / self.model.plasma_volume, 0]])
            if self.model.type3 == 'non-met':
                mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_organ3 -
                                                                                 self.model.organ3_flow)
                                                                              / self.model.blood_organ3,
                                                                              (self.model.pi_organ3 / self.model.p_organ3)
                                                                              / self.model.blood_organ3],
                                                                               [self.model.pi_organ3 /
                                                                                self.model.organ3_volume,
                                                                                (-self.model.pi_organ3 /
                                                                                 self.model.p_organ3) /
                                                                                self.model.organ3_volume]])
            if self.model.type3 == 'met':
                 mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_organ3 -
                                                                                 self.model.organ3_flow)
                                                                              / self.model.blood_organ3,
                                                                              (self.model.pi_organ3 / self.model.p_organ3)
                                                                              / self.model.blood_organ3],
                                                                               [self.model.pi_organ3 /
                                                                                self.model.organ3_volume,
                                                                                (-self.model.pi_organ3 /
                                                                                 self.model.p_organ3 -
                                                                                 (self.model.k_met3+self.model.k_bile3) * self.model.organ3_volume) /
                                                                                self.model.organ3_volume]])

            self.A = np.append(self.A, mid_matrix, axis=1)

        if self.model.blood_organ4 != 0:
            mid_matrix = np.zeros((2, self.A.shape[0]))
            mid_matrix[0:1, 2:3] = self.model.organ4_flow / self.model.blood_organ4
            self.A = np.append(self.A, mid_matrix, axis=0)
            mid_matrix = np.zeros((self.A.shape[0], 2))
            mid_matrix[0:1, :] = np.array([[self.model.organ4_flow / self.model.plasma_volume, 0]])
            if self.model.type4 == 'non-met':
                mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_organ4 -
                                                                             self.model.organ4_flow)
                                                                          / self.model.blood_organ4,
                                                                          (self.model.pi_organ4 / self.model.p_organ4)
                                                                          / self.model.blood_organ4],
                                                                           [self.model.pi_organ4 /
                                                                            self.model.organ4_volume,
                                                                            (-self.model.pi_organ4 /
                                                                             self.model.p_organ4) /
                                                                            self.model.organ4_volume]])
            if self.model.type4 == "met":
                 mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_organ4 -
                                                                             self.model.organ4_flow)
                                                                          / self.model.blood_organ4,
                                                                          (self.model.pi_organ4 / self.model.p_organ4)
                                                                          / self.model.blood_organ4],
                                                                           [self.model.pi_organ4 /
                                                                            self.model.organ4_volume,
                                                                            (-self.model.pi_organ4 /
                                                                              self.model.p_organ4 -
                                                                                 (self.model.k_met4+self.model.k_bile4) * self.model.organ4_volume) /
                                                                            self.model.organ4_volume]])
            self.A = np.append(self.A, mid_matrix, axis=1)


        if self.model.blood_organ5 != 0:
            mid_matrix = np.zeros((2, self.A.shape[0]))
            mid_matrix[0:1, 2:3] = self.model.organ5_flow / self.model.blood_organ5
            self.A = np.append(self.A, mid_matrix, axis=0)
            mid_matrix = np.zeros((self.A.shape[0], 2))
            mid_matrix[0:1, :] = np.array([[self.model.organ5_flow / self.model.plasma_volume, 0]])
            if self.model.type5 == "non-met":
                mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_organ5 -
                                                                                 self.model.organ5_flow)
                                                                              / self.model.blood_organ5,
                                                                              (self.model.pi_organ5 / self.model.p_organ5)
                                                                              / self.model.blood_organ5],
                                                                               [self.model.pi_organ5 /
                                                                                self.model.organ5_volume,
                                                                                (-self.model.pi_organ5 /
                                                                                 self.model.p_organ5) /
                                                                                self.model.organ5_volume]])
            if self.model.type5 == "met":
                mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_organ5 -
                                                                                 self.model.organ5_flow)
                                                                              / self.model.blood_organ5,
                                                                              (self.model.pi_organ5 / self.model.p_organ5)
                                                                              / self.model.blood_organ5],
                                                                               [self.model.pi_organ5 /
                                                                                self.model.organ5_volume,
                                                                                (-self.model.pi_organ5 /
                                                                                  self.model.p_organ5 -
                                                                                 (self.model.k_met5+self.model.k_bile5) * self.model.organ5_volume) /
                                                                                self.model.organ5_volume]])
            self.A = np.append(self.A, mid_matrix, axis=1)

        if self.model.blood_heart != 0:
            mid_matrix = np.zeros((2, self.A.shape[0]))
            mid_matrix[0:1, 2:3] = self.model.heart_flow / self.model.blood_heart
            self.A = np.append(self.A, mid_matrix, axis=0)
            mid_matrix = np.zeros((self.A.shape[0], 2))
            mid_matrix[0:1, :] = np.array([[self.model.heart_flow / self.model.plasma_volume, 0]])
            mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_heart -
                                                                             self.model.heart_flow)
                                                                          / self.model.blood_heart,
                                                                          (self.model.pi_heart / self.model.p_heart)
                                                                          / self.model.blood_heart],
                                                                           [self.model.pi_heart /
                                                                            self.model.heart_volume,
                                                                            (-self.model.pi_heart /
                                                                             self.model.p_heart) /
                                                                            self.model.heart_volume]])
            self.A = np.append(self.A, mid_matrix, axis=1)

        if self.model.blood_muscle != 0:
            mid_matrix = np.zeros((2, self.A.shape[0]))
            mid_matrix[0:1, 2:3] = self.model.muscle_flow / self.model.blood_muscle
            self.A = np.append(self.A, mid_matrix, axis=0)
            mid_matrix = np.zeros((self.A.shape[0], 2))
            mid_matrix[0:1, :] = np.array([[self.model.muscle_flow / self.model.plasma_volume, 0]])
            mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_muscle -
                                                                             self.model.muscle_flow)
                                                                          / self.model.blood_muscle,
                                                                          (self.model.pi_muscle / self.model.p_muscle)
                                                                          / self.model.blood_muscle],
                                                                           [self.model.pi_muscle /
                                                                            self.model.muscle_volume,
                                                                            (-self.model.pi_muscle /
                                                                             self.model.p_muscle) /
                                                                            self.model.muscle_volume]])
            self.A = np.append(self.A, mid_matrix, axis=1)

        if self.model.blood_spleen != 0:
            mid_matrix = np.zeros((2, self.A.shape[0]))
            mid_matrix[0:1, 2:3] = self.model.spleen_flow / self.model.blood_spleen
            self.A = np.append(self.A, mid_matrix, axis=0)
            mid_matrix = np.zeros((self.A.shape[0], 2))
            mid_matrix[0:1, :] = np.array([[self.model.spleen_flow / self.model.plasma_volume, 0]])
            mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_spleen -
                                                                             self.model.spleen_flow)
                                                                          / self.model.blood_spleen,
                                                                          (self.model.pi_spleen / self.model.p_spleen)
                                                                          / self.model.blood_spleen],
                                                                           [self.model.pi_spleen /
                                                                            self.model.spleen_volume,
                                                                            (-self.model.pi_spleen /
                                                                             self.model.p_spleen) /
                                                                            self.model.spleen_volume]])
            self.A = np.append(self.A, mid_matrix, axis=1)

        if self.model.blood_placental != 0:
            mid_matrix = np.zeros((2, self.A.shape[0]))
            mid_matrix[0:1, 2:3] = self.model.placental_flow / self.model.blood_placental
            self.A = np.append(self.A, mid_matrix, axis=0)
            mid_matrix = np.zeros((self.A.shape[0], 2))
            mid_matrix[0:1, :] = np.array([[self.model.placental_flow / self.model.plasma_volume, 0]])
            mid_matrix[self.A.shape[0] - 2:self.A.shape[0], :] = np.array([[(-self.model.pi_placental -
                                                                             self.model.placental_flow)
                                                                          / self.model.blood_placental,
                                                                          (self.model.pi_placental / self.model.p_placental)
                                                                          / self.model.blood_placental],
                                                                           [self.model.pi_placental /
                                                                            self.model.placental_volume,
                                                                            (-self.model.pi_placental /
                                                                             self.model.p_placental) /
                                                                            self.model.placental_volume]])
            self.A = np.append(self.A, mid_matrix, axis=1)



        self.B = np.zeros((self.A.shape[0], 1))
        self.B[0:1, 0:1] = 1./self.model.plasma_volume
        self.C = np.zeros((1, self.A.shape[0]))
        self.C[0:1, 0:1] = 1
        self.D = np.zeros((1, 1))
        self.sys_cont = ss(self.A, self.B, self.C, self.D)
        sys_d = cont2discrete((self.A, self.B, self.C, self.D), 5./60, 'zoh')
        # sys_d = tf2ss(sys_d)
        a = sys_d[0]
        b = sys_d[1]
        c = sys_d[2]
        d = sys_d[3]
        sys_d = ss(a, b, c, d)

        return sys_d