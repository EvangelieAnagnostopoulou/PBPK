import matplotlib.pyplot as plt
from mpcsolverWeb import *
from state_space import *
from kalman3 import KalmanFilter
from control import forced_response
#import plotly.plotly as py
def is_strictly_schur(x):
    return np.all(np.linalg.norm(np.linalg.eigvals(x) < 1))


def ss_opt(a, b, c, bd, cd, ref, d_hat):
    mq = a.shape[0]
    mr = b.shape[1]
    a_mpc = np.bmat([[a - np.eye(mq), b], [c, np.zeros((mr, mr))]])
    b_mpc = np.bmat([[-np.dot(bd, d_hat)], [ref - np.dot(cd, d_hat)]])
    x_mpc = np.linalg.solve(a_mpc, b_mpc)
    x_ = x_mpc[0:mq, :]
    u_ = x_mpc[mq::, :]
    return x_, u_

class Simulator:
    def __init__(self, System, N, x_hat, d_hat, max_liver, max_kidney, max_influx, min_residual, max_residual, min_skin, max_skin, min_bladder, max_bladder, min_lung, max_lung, min_liver, min_kidney,
                  min_heart, max_heart, min_muscle, max_muscle, min_spleen, max_spleen, min_placental, max_placental, time, tlist, ulist, step, Qweight, Rweight):
        self.System = System
        self.N = N
        self.x_hat = x_hat
        self.d_hat = d_hat
        self.max_liver = max_liver
        self.max_kidney = max_kidney
        self.max_influx = max_influx
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
        self.min_heart = min_heart
        self.max_heart = max_heart
        self.min_muscle = min_muscle
        self.max_muscle = max_muscle
        self.min_spleen = min_spleen
        self.max_spleen = max_spleen
        self.min_placental = min_placental
        self.max_placental = max_placental
        self.T = time
        self.tlist = tlist
        self.ulist = ulist
        self.step = step
        self.qw = Qweight
        self.rw = Rweight

    def InputCloseProfile(self, T, tlist, ulist, step):
        h = step
        t = np.arange(tlist[0], T, h)
        tlist.append(T)
        inp = np.zeros((t.shape[0]))
        n = len(tlist) - 1
        m = len(t) - 1
        inp[0:int(round(m * tlist[1]/T) )] = ulist[0]
        for i in range(1, n):  # Before: range(1, n)
            inp[int(round(m * tlist[i]/T)):int(round(m * tlist[i+1]/T) + 1)] = ulist[i]
        return t, inp

    def Simulate(self, step, end):
        exit_status = 'optimal'
        #n = self.System.DiscreteSystem().A.shape[0]
        n = self.System.ContinuousSystem().A.shape[0]
        A = self.System.DiscreteSystem().A
        B = self.System.DiscreteSystem().B
        C = self.System.DiscreteSystem().C
        #Bd = np.array([[1.], [0.], [0.], [0], [1.], [0.], [3.], [2.], [0.], [1.], [0.], [0.], [0.], [1.]])
        Bd = np.array([[1.], [0.], [0.], [0], [1.], [0.], [3.], [2.], [0.], [1.], [0.], [0.], [0.], [1.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.], [0.]])
        nx=len(A)
        Bd = Bd[:nx]
        Cd = np.array([[1.]])
        if is_strictly_schur(A):
            print "A is strictly Schur."
            # Bd = np.zeros((n, 1))
            lx = np.zeros((A.shape[0], B.shape[1]))
            ly = np.ones((C.shape[0], B.shape[1]))
            l = np.concatenate((lx, ly), axis=0)
        else:
            print "A is not strictly Schur."
        ulist = []
        tlist = []
        a_kalman = np.bmat([[A, Bd],
                            [np.zeros((B.shape[1], A.shape[1])), np.eye(B.shape[1])]])
        b_kalman = np.bmat([[B], [np.zeros((B.shape[1], B.shape[1]))]])
        c_kalman = np.bmat([[C, Cd]])
        c_pl_d_list = []
        c_pl_d_list1 = []
        g = globals()
        leng = len(self.x_hat)
        for m in range(0,leng):
            g['c_pl_c_list_{0}'.format(m)] = []
            g['c_pl_c_last_{0}'.format(m)] = []
            g['c_pl_d_list_{0}'.format(m)] = []
        i, t, u = 0, 0, 0
        count = 0
        time, setpoint = self.InputCloseProfile(self.T, self.tlist, self.ulist, self.step)

        length = int(end/step)
        x = np.zeros((A.shape[0], length))
        x[:, 0:1] = self.x_hat
        x_k = self.x_hat                    # x_k is for the observer
        ym = np.dot(C, x_k)              # Output of the real system
        u_matrix = np.zeros((length, 1))
        response = np.zeros((length, 1))
        dist = np.zeros((length, 1))

        #target = ref

        # Initial estimations for the observer
        self.d_hat = np.array([[0.]])      # So to match with Pantelis code
        d_p = self.d_hat
        u = np.array([[0.]])
        x_real_old = self.x_hat

        # Kalman Matrices
        PN = 1.e-14 * np.eye(n+1)
        QN = 1.e-5 * np.eye(n+1)
        RN = 2.e-2 * np.ones((1, 1))  # * 200

        check_matrix1 = np.bmat([[A, Bd], [np.zeros((C.shape[0], A.shape[1])), np.eye(C.shape[0])]])
        check_matrix2 = np.dot(np.bmat([[lx], [ly]]), np.bmat([[C, Cd]]))
        check_matrix = check_matrix1 - np.dot(check_matrix1, check_matrix2)
        if is_strictly_schur(check_matrix):
            print "Estimator is Stable"
        else:
            return "Unstable Estimator"

        dist[i-1: i] = d_p
        j_pred = np.concatenate((x_k, d_p), axis=0)

        # ---------------------- ************* ---------------------- #
        # Here comes the Estimator
        kalman = KalmanFilter(a_kalman, b_kalman, c_kalman, j_pred, PN, QN, RN)

        for i in range(1, length+1):
            # Tracking calculation
            x_s, u_s = ss_opt(A, B, C, Bd, Cd, setpoint[count], self.d_hat)
            print "Running " + str(i) + ", " + str(length+1 - i) + " left."
            # MPC Controller
            solver = MPCSolver(self.System, self.N, x_k, d_p, x_s, u_s, self.max_liver,
                               self.max_kidney, self.max_influx, self.min_residual, self.max_residual, self.min_skin, self.max_skin, self.min_bladder, self.max_bladder, self.min_lung, self.max_lung, self.min_liver, self.min_kidney,
                               self.min_heart, self.max_heart, self.min_muscle, self.max_muscle, self.min_spleen,self.max_spleen, self.min_placental, self.max_placental, self.qw, self.rw)
            u, status = solver.Solver()
            print "u = " + str(u)

            # Run Real Patient 's Dynamics first!
            time = linspace(t, t + step, 10)
            u_sim = np.dot(u, np.ones((1, 10)))
            time, ym, x_real_new = forced_response(self.System.ContinuousSystem(), time, u_sim, x_real_old)
            # x_real_new = np.dot(A, x_k) + np.dot(B, u) + np.dot(Bd, d_p)
            xforce= x_real_new[:,-1]
            x_real_new = x_real_new[:, -1]
            x_real_new = np.array([x_real_new])
            ym = ym[-1]

            dist[i-1: i] = d_p

            # ---------------------- ************* ---------------------- #
            # Here comes the Estimator
            measured = ym
            j_k = kalman.Step(u, measured)

            x_k = j_k[0: A.shape[0], :]
            d_p = j_k[A.shape[0]::, :]
            print "Estimated State vector(0, 0):" + str(x_k[0, 0])
            print "Estimated disturbance:" + str(d_p)
            # ---------------------- ************* ---------------------- #
            x_real_old = x_real_new.T

            # Fill the corresponding matrices
            response[i+1: i+2] = measured
            u_matrix[i: i+1] = u

            ulist.append(u)
            tlist.append(t)
            print ym
            print t
            for m in range(0, leng):
                g['c_pl_c_{0}'.format(m)] = xforce[m]
                g['c_pl_c_last_{0}'.format(m)]= g['c_pl_c_{0}'.format(m)]
                g['c_pl_c_list_{0}'.format(m)].append(g['c_pl_c_last_{0}'.format(m)])
            t += step
            count += 1



        ### ----------------------------- Results Presentation ---------------------------- ###
        plt.subplot(211)
        plt.step(np.asarray(tlist), u_matrix)
        plt.xlabel('Time(hr)')
        plt.ylabel('Administration Rate (ug/hr)')
        plt.subplot(212)
        array_plots=[]
        for m in range(0,leng):
            plt.step(np.asarray(tlist), np.asarray(g['c_pl_c_list_{0}'.format(m)]))
            array_plots.append(g['c_pl_c_list_{0}'.format(m)])


        plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
        return tlist, array_plots, ulist




