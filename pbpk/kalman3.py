import numpy as np

class KalmanFilter:
    def __init__(self, A, B, C, _x, _P, Q, R):
        self.current_state_estimate = _x        # initial state estimate
        self.current_prob_estimate = _P         # initial covariance estimate
        self.A = A      # state transition matrix
        self.B = B      # Control matrix
        self.C = C      # Observation matrix
        self.Q = Q      # Estimated error in process
        self.R = R      # Estimated error in measurements
    def GetCurrentState(self):
        return self.current_state_estimate

    def Step(self, control_vector, measurement_vector):
        # --------------------------------------- Prediction Step ---------------------------------------------
        predicted_state_estimate = np.dot(self.A, self.current_state_estimate) + np.dot(self.B, control_vector)
        predicted_prob_estimate = (self.A * self.current_prob_estimate) * np.transpose(self.A) + self.Q
        # -------------------------------------- Observation Step ---------------------------------------------
        innovation = measurement_vector - self.C * predicted_state_estimate
        innovation_covariance = self.C * predicted_prob_estimate * np.transpose(self.C) + self.R
        # ----------------------------------------- Update Step -----------------------------------------------
        kalman_gain = predicted_prob_estimate * np.transpose(self.C) * np.linalg.inv(innovation_covariance)
        #print "Kalman " + str((np.dot(kalman_gain, innovation).shape))
        self.current_state_estimate = predicted_state_estimate + kalman_gain * innovation
        # we need the size of the matrix so we can make an identity matrix
        size = self.current_prob_estimate.shape[0]
        # eye(n) = nxn identity matrix
        self.current_prob_estimate = (np.eye(size) - kalman_gain * self.C) * predicted_prob_estimate
        return self.current_state_estimate, self.current_prob_estimate

