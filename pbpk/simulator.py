import matplotlib.pyplot as plt
from mpcsolverWeb import *
from state_space import *
from kalman3 import KalmanFilter
#import plotly.plotly as py
class Simulator:
    def __init__(self, System, N, x_hat, d_hat, max_liver, max_kidney, max_influx, min_residual, max_residual, min_skin, max_skin, min_bladder, max_bladder, min_lung, max_lung, min_liver, min_kidney,
                  min_heart, max_heart, min_muscle, max_muscle, min_spleen, max_spleen, min_placental, max_placental, time, tlist, ulist, step):
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

    def InputCloseProfile(self, T, tlist, ulist, step):
        h = step
        t = np.arange(tlist[0], T, h)
        tlist.append(T)
        inp = np.zeros((t.shape[0]))
        n = len(tlist) - 1
        m = len(t) - 1
        inp[0:round(m * tlist[1]/T)] = ulist[0]
        for i in range(1, n-1):  # Before: range(1, n)
            inp[round(m * tlist[i]/T): round(m * tlist[i+1]/T) + 1] = ulist[i]
        return t, inp

    def Simulate(self, ref, step, end):
        exit_status = 'optimal'
        #n = self.System.DiscreteSystem().A.shape[0]
        n = self.System.ContinuousSystem().A.shape[0]
        self.x_hat = np.zeros((n,1))
        P = np.eye(n)
        Q = np.eye(n)
        Q[0,0] = 10.0
        #Q[9,9] = 10.0
        #set size of R equal to end+1
        r = end + 1
        R = r * np.ones((1,1))
        if Q.shape[0] >= 9:
            Q[9:10, 9:10] = 10.0

        Bd = np.array([[1.], [0.], [0.], [0.], [1.], [0.], [3.], [2.], [0.], [1.], [0.], [0.], [0.], [1.], [0.], [0.]])

        ulist = []
        tlist = []
        c_pl_d_list = []
        c_pl_d_list1 = []
        g = globals()
        leng = len(self.x_hat)
        for m in range(0,leng):
            g['c_pl_c_list_{0}'.format(m)] = []
            g['c_pl_c_last_{0}'.format(m)] = []
            g['c_pl_d_list_{0}'.format(m)] = []
        i, t, u = 0, 0, 0

        time, targ = self.InputCloseProfile(self.T, self.tlist, self.ulist, self.step)
        print time , targ
        while i <= end:
            print "------------------ New round -------------------"
            aug_state = np.append(self.x_hat, self.d_hat, axis = 0)
            aug_input = np.append(u * np.ones((1,1)), self.d_hat, axis = 1)
            ### -------------------------Continuous System Response ----------------------- ###
            T = linspace(i, i + step, r)
            T, you, xout = lsim(self.System.ContinuousSystem(), u, T, self.x_hat)
            c_pl_c = xout[:,0]
            c_pl_c_last = c_pl_c[end]
            for m in range(0, leng):
                g['c_pl_c_{0}'.format(m)] = xout[:, m]
                g['c_pl_c_last_{0}'.format(m)]= g['c_pl_c_{0}'.format(m)][end]
                if i >= step:
                    g['c_pl_c_list_{0}'.format(m)].append(g['c_pl_c_last_{0}'.format(m)])


            ### --------------------------Discrete System Response ------------------------ ###
            Td = linspace(i, i + step, r)
            Td, yd, xd = lsim(self.System.DiscreteSystem(), u, Td, self.x_hat)
            for m in range(0, leng):
                g['c_pl_d_{0}'.format(m)] = xd[:,m]
                g['c_pl_d_last_{0}'.format(m)]= g['c_pl_d_{0}'.format(m)][end]
                g['c_pl_d_list_{0}'.format(m)].append(g['c_pl_d_last_{0}'.format(m)])


            ### ----------------------------Here comes the Kalman!------------------------- ###

            u_matrix = u * np.ones((1,1))
            A = self.System.DiscreteSystem().A
            B = self.System.DiscreteSystem().B
            C = self.System.DiscreteSystem().C

            kalman = KalmanFilter(A, B, C, self.x_hat, P, Q, R)
            self.x_hat, P = kalman.Step(u_matrix, c_pl_c_last)

            ### ------------------------------ MPC SOLVER --------------------------------- ###
            solver = MPCSolver(self.System, self.N, self.x_hat, self.d_hat, ref, self.max_liver,
                               self.max_kidney, self.max_influx, self.min_residual, self.max_residual, self.min_skin, self.max_skin, self.min_bladder, self.max_bladder, self.min_lung, self.max_lung, self.min_liver, self.min_kidney,
                               self.min_heart, self.max_heart, self.min_muscle, self.max_muscle, self.min_spleen,self.max_spleen, self.min_placental, self.max_placental)
            u, status = solver.Solver()
            if status != 'optimal':
                exit_status = 'Not optimal'

            ulist.append(u)
            tlist.append(t)
            ### ------------------- If the system was fully observable... ----------------- ###
##            self.x_hat = np.dot(self.System.DiscreteSystem().A, self.x_hat) +\
##                         np.dot(self.System.DiscreteSystem().B, u) + np.dot(Bd, self.d_hat)
            print t
            i += step
            t += step

        T = linspace(i, i + step, r)
        T, yout, xout = lsim(self.System.ContinuousSystem(), u, T, self.x_hat)
        print("------")
        print tlist
        print xout
        print("------")
        for m in range(0, leng):
                g['c_pl_c_{0}'.format(m)] = xout[:, m]
                g['c_pl_c_last_{0}'.format(m)]= g['c_pl_c_{0}'.format(m)][end]
                g['c_pl_c_list_{0}'.format(m)].append(g['c_pl_c_last_{0}'.format(m)])
        #print np.array(tlist)
        #print np.array(ulist)

        ### ----------------------------- Results Presentation ---------------------------- ###
        plt.subplot(211)
        plt.step(np.asarray(tlist), np.asarray(ulist))
        plt.xlabel('Time(hr)')
        plt.ylabel('Administration Rate (ug/hr)')
        plt.subplot(212)
        #plt.plot(np.asarray(tlist), np.asarray(c_pl_c_list[0:l]))
        array_plots=[]
        for m in range(0,leng):
            plt.plot(np.asarray(tlist), np.asarray(g['c_pl_c_list_{0}'.format(m)]))
            plt.step(np.asarray(tlist), np.asarray(g['c_pl_d_list_{0}'.format(m)]))
            array_plots.append(g['c_pl_d_list_{0}'.format(m)])
            print array_plots


        #plt.step(np.asarray(tlist), np.asarray(c_pl_d_list))


        plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
        '''fig1 = plt.gcf()
        fig1.savefig(self.filename, dpi=100)
        fig1.clear()'''
        return tlist, array_plots, ulist



