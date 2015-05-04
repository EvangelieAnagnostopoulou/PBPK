import matplotlib.pyplot as plt
from mpcsolverWeb import *
from state_space import *
# from scipy.signal import lsim
import warnings
from control import forced_response
warnings.filterwarnings("ignore")


def input_profile(tf, tlist, ulist):
    h = (tf - tlist[0] * 1.0 / 1000.0)
    t = np.arange(tlist[0], tf, h)
    tlist.append(tf)
    inp = np.zeros((t.shape[0]))
    n = len(tlist) - 1
    m = len(t) -1
    inp[0:round(m * tlist[1]/tf)] = ulist[0]
    for i in range(1, n-1): ### Edw htan range(1, n)
        inp[round(m * tlist[i]/tf) : round(m * tlist[i+1]/tf) + 1] = ulist[i]
    return t, inp

class SimulatorOpenLoop:
    def __init__(self, System, T, t_init, ulist):
        self.System = System
        self.T = T
        self.t_init = t_init
        self.ulist = ulist
        print t_init
        print ulist

    def InputProfile(self, T, tlist, ulist):
        h = (T - tlist[0]) * 1.0 / 1000.0
        t = np.arange(tlist[0], T, h)
        tlist.append(T)
        inp = np.zeros((t.shape[0]))
        n = len(tlist) - 1
        m = len(t) - 1
        inp[0:round(m * tlist[1]/T)] = ulist[0]
        for i in range(1, n-1):  # Before: range(1, n)
            inp[round(m * tlist[i]/T): round(m * tlist[i+1]/T) + 1] = ulist[i]
        return t, inp

    def Simulate(self):
        Aol = self.System.ContinuousSystem().A
        Bol = self.System.ContinuousSystem().B
        Col = self.System.ContinuousSystem().C
        Dol = self.System.ContinuousSystem().D
        t, u = self.InputProfile(self.T, self.t_init, self.ulist)
        print t,u

        Tsim, ycont, xcont = forced_response(self.System.ContinuousSystem(), t, u)

        #plt.plot(Tsim, u, Tsim, xcont[0, :])
        '''ax = plt.subplot(111)
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
        plt.xlabel('Time(hr)')
        plt.ylabel('State Variables')
        fig1 = plt.gcf()
        fig1.savefig(self.filename, dpi=100)
        fig1.clear()'''
        return xcont, Tsim
#         while i <= end:
#             print "------------------ New round -------------------"
#             aug_state = np.append(self.x_hat, self.d_hat, axis = 0)
#             aug_input = np.append(u * np.ones((1,1)), self.d_hat, axis = 1)
#             ### -------------------------Continuous System Response ----------------------- ###
#             T = linspace(i, i + step, 100)
#             T, you, xout = lsim(self.System.ContinuousSystem()[0], u, T, self.x_hat)
#             c_pl_c = xout[:,0]
#             c_pl_c_last = c_pl_c[end]
#             if i >= step:
#                 c_pl_c_list.append(c_pl_c_last)
#
#             ### --------------------------Discrete System Response ------------------------ ###
#             Td = linspace(i, i + step, 100)
#             Td, yd, xd = lsim(self.System.DiscreteSystem(), u, Td, self.x_hat)
#             c_pl_d = xd[:,0]
#             c_pl_d_last = c_pl_d[end]
#             c_pl_d_list.append(c_pl_d_last)
#
#             ### ----------------------------Here comes the Kalman!------------------------- ###
#             u_matrix = u * np.ones((1,1))
#             A = self.System.DiscreteSystem().A
#             B = self.System.DiscreteSystem().B
#             C = self.System.DiscreteSystem().C
#
#             kalman = KalmanFilter(A, B, C, self.x_hat, P, Q, R)
#             self.x_hat, P = kalman.Step(u_matrix, c_pl_c_last)
#
#             ### ------------------------------ MPC SOLVER --------------------------------- ###
#             solver = MPCSolver(self.System, self.N, self.x_hat, self.d_hat, ref, self.max_liver,
#                                self.max_kidney, self.max_influx)
#             u, status = solver.Solver()
#             if status != 'optimal':
#                 exit_status = 'Not optimal'
#
#             ulist.append(u)
#             tlist.append(t)
#             ### ------------------- If the system was fully observable... ----------------- ###
# ##            self.x_hat = np.dot(self.System.DiscreteSystem().A, self.x_hat) +\
# ##                         np.dot(self.System.DiscreteSystem().B, u) + np.dot(Bd, self.d_hat)
#             print t
#             i += step
#             t += step
#
#         T = linspace(i, i + step, 100)
#         T, yout, xout = lsim(self.System.ContinuousSystem()[0], u, T, self.x_hat)
#         c_pl_c = xout[:,0]
#         c_pl_c_last = c_pl_c[end]
#         c_pl_c_list.append(c_pl_c_last)
#         #print np.array(tlist)
#         #print np.array(ulist)
#         ### ----------------------------- Results Presentation ---------------------------- ###
#         plt.subplot(211)
#         plt.step(np.asarray(tlist), np.asarray(ulist))
#         plt.xlabel('Time(hr)')
#         plt.ylabel('Administration Rate (ug/hr)')
#         plt.subplot(212)
#         plt.plot(np.asarray(tlist), np.asarray(c_pl_c_list))
#         plt.step(np.asarray(tlist), np.asarray(c_pl_d_list))
#         fig1 = plt.gcf()
#         fig1.savefig(self.filename, dpi=100)
#         return exit_status

