from state_space import *
#from MPC2 import *
from cvxopt import solvers, matrix
from scipy.linalg import block_diag
import numpy as np



class MPCSolver(System):
    def __init__(self, System, N, x_hat, d_hat, ref, max_liver, max_kidney, max_influx, min_residual, max_residual,
                 min_skin, max_skin, min_bladder, max_bladder, min_lung, max_lung, min_liver, min_kidney, min_heart,
                 max_heart, min_muscle, max_muscle, min_spleen, max_spleen, min_placental, max_placental, Qweight, Rweight):
        # self.del_list = System.ContinuousSystem()
        self.dsystem = System.DiscreteSystem()
        self.N = N
        self.d_hat = d_hat
        self.x_hat = x_hat
        self.r = ref
        self.max_kidney = max_kidney
        self.max_liver = max_liver
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
        self.qw = Qweight
        self.rw = Rweight


    def Solver(self):
        Bd = np.zeros((self.dsystem.A.shape[0], self.d_hat.shape[0]))
        # Bd = np.array([[1.], [0.], [0.], [0.], [1.], [0.], [3.], [2.], [0.], [1.], [0.], [0.], [0.], [1.]])

        #print Bd_new
        # Bd = Bd_new
        Cd = np.array([[1.]])
        print np.linalg.matrix_rank(np.bmat([[(np.eye(self.dsystem.A.shape[0]) - self.dsystem.A), -Bd],
                                            [self.dsystem.C, Cd]])) == \
            self.dsystem.A.shape[0] + self.d_hat.shape[0]
        [nQ, mQ] = self.dsystem.A.shape
        [nR, mR] = self.dsystem.B.shape

        Q = np.eye(mQ, dtype="float") * self.qw
        '''Q[0:1,0:1] = 40.0
        if Q.shape[0] >= 9:
            Q[9:10, 9:10] = 1000.0

        Q *= 55000.0'''
        R = self.rw * np.eye(mR, dtype="float")
        (K, X, E) = bb_dlqr(self.dsystem.A, self.dsystem.B, Q, R)
        Q_f = X

        Lx = np.bmat([[(self.dsystem.A - np.eye(mQ, dtype='float')), self.dsystem.B],
                      [self.dsystem.C, np.zeros( (self.dsystem.C.shape[0],
                                                  self.dsystem.B.shape[1]), dtype='float')]])

        Rx = np.bmat([[np.dot(-Bd, self.d_hat)],
                      [self.r - np.dot(Cd, self.d_hat)]])

        xu = np.linalg.solve(Lx, Rx)
        self.x_ = xu[0:self.dsystem.A.shape[0], :]
        self.u_ = xu[self.dsystem.A.shape[0]::, :]


        ## Equality Constraints ##
        Atil = np.zeros( (self.N * mQ, self.N * (mR + mQ)),dtype="float" )
        first_row_Atil = np.bmat([-self.dsystem.B, np.eye(mQ, dtype="float")],)
        second_row_Atil = np.bmat([-self.dsystem.A, -self.dsystem.B, np.eye(mQ, dtype="float")])
        Atil[0:nR, 0:(mQ + mR)] = first_row_Atil

        for k in range(1, self.N):
            Atil[k*nR:(k+1)*nR,
                 k*mR+(k-1)*mQ:(k+1)*mR+(k+1)*mQ] = second_row_Atil

        ###
        btil = np.zeros( (self.N*mQ, 1), dtype="float" )
        #btil[0:mQ] = np.dot(self.dsystem.A, self.x_hat)
        btil[0:mQ] = np.dot(Bd, self.d_hat) + np.dot(self.dsystem.A, self.x_hat)
        for k in range(1,self.N):
            btil[k*nR : (k+1)*nR] = np.dot(Bd, self.d_hat)
        ###

        ## Inequality Constraints ##
        H = np.zeros( (self.N*(mQ+mR),self.N*(mQ+mR)), dtype="float" )
        for k in range(0,self.N):
            H[(k)*mR+(k)*mQ:(k+1)*mR+(k)*mQ,
              (k)*mR+(k)*mQ:(k+1)*mR+(k)*mQ] = R
            H[(k+1)*mR+(k)*mQ:(k+1)*mR+(k+1)*mQ,
              (k+1)*mR+(k)*mQ:(k+1)*mR+(k+1)*mQ] = Q
            if k == self.N-1:
                H[(k+1)*mR+(k)*mQ:(k+1)*mR+(k+1)*mQ,
                  (k+1)*mR+(k)*mQ:(k+1)*mR+(k+1)*mQ] = Q_f

        ## Construct G ##
        first_col_G = np.bmat([[-np.eye(mR, dtype="float")], [np.eye(mR, dtype="float")]])
        second_col_G = np.bmat([[-np.eye(mQ, dtype="float")], [np.eye(mQ, dtype="float")]])
        G_block = block_diag(first_col_G, second_col_G)
        G = G_block
        for k in range(0, self.N-1):
            G = block_diag(G_block, G)


        ## Construct h ##
        h = np.zeros( (2*self.N*(mQ+mR), 1), dtype="float" )
        u_low = 0.0
        u_up = self.max_influx
        for k in range(0,self.N):
            u_low = np.zeros( (mR,1), dtype="float" )
            u_up = self.max_influx * np.ones( (mR, 1), dtype="float" )
            x_low = np.zeros( (mQ, 1),dtype="float" )
            x_low[3:4,:] = self.min_lung
            x_low[5:6,:] = self.min_skin
            x_low[7:8,:] = self.min_bladder
            x_low[9:10,:] = self.min_liver
            x_low[11:12,:] = self.min_residual
            x_low[13:14,:] = self.min_kidney
            x_low[25:26,:] = self.min_heart
            x_low[27:28,:] = self.min_muscle
            x_low[29:30,:] = self.min_spleen
            x_low[33:34,:] = self.min_placental
            x_up =  np.ones( (mQ, 1), dtype="float" )
            x_up[3:4,:] = self.max_lung
            x_up[5:6,:] = self.max_skin
            x_up[7:8,:] = self.max_bladder
            x_up[9:10,:] = self.max_liver
            x_up[11:12,:] = self.max_residual
            x_up[13:14,:] = self.max_kidney
            x_up[25:26,:] = self.max_heart
            x_up[27:28,:] = self.max_muscle
            x_up[29:30,:] = self.max_spleen
            x_up[33:34,:] = self.max_placental

            h[2*(k)*mR+2*(k)*mQ:2*(k)*mR+2*(k)*mQ+mR] = -u_low
            h[2*(k)*mR+2*(k)*mQ+mR:2*(k+1)*mR+2*(k)*mQ] = u_up
            h[2*(k+1)*mR+2*(k)*mQ:2*(k+1)*mR+2*(k)*mQ+mQ] = -x_low
            h[2*(k)*mR+2*(k)*mQ+2*mR+mQ:2*(k+1)*mR+2*(k+1)*mQ] = x_up


        p = np.zeros( (1, self.N*(mQ+mR)), dtype="float" )
        alin = np.dot(self.x_.T, Q)
        blin = np.dot(self.u_.T, R)
        lin = np.bmat([[blin, alin]])
        for i in range(0,self.N*(mQ+mR),(mQ+mR)):
            p[0,i:i+(mQ+mR)] = lin
        f = np.dot(self.x_.T, Q_f)
        flin = np.concatenate((blin, f), axis = 1)
        p[0,(self.N-1)*(mQ+mR):self.N*(mQ+mR)] = flin

        p = -1.0 * p.T

        #G = np.zeros((2*self.N*(mQ+mR),self.N*(mQ+mR)),dtype="float")
        #h = np.zeros((2*self.N*(mQ+mR),1),dtype="float")
        sol = solvers.qp(matrix(H), matrix(p), matrix(G), matrix(h),
                         matrix(Atil), matrix(btil))

        if sol['x'][0] <= 0:
            u = 0
        else:
            u = sol['x'][0]
        #print sol['x']
        print u
        return u, sol['status']


'''
N = 35

u_ = 1.0226e-10 * np.ones((1,1))
d_hat = 1.7408e-14 * np.ones((1,1))
x_hat = 1.0e-5 * np.array([[0.0791], [0.0486], [0.0791], [0.0348], [0.0787], [0.0699], [0.0789], [0.1248], [0.0790],
                         [0.0847], [0.0790], [0.0449], [0.0791], [0.0111]])
x_ = 1.0e-05 * np.array([[0.0800], [0.0498], [0.0800], [0.0352], [0.0800], [0.1280], [0.0800], [0.1280], [0.0800],
                         [0.1263], [0.0800], [0.1280], [0.0800], [0.0112]])

x_hat_3_5 = 1.0e-06 * np.array([[0.4000], [0.2493], [0.4000], [0.1760], [0.4000], [0.6314], [0.4000],
                                [0.6401], [0.4000], [0.6315], [0.3999], [0.3933], [0.4000], [0.0560]])
x_3_5 = 1.0e-06 * np.array([[0.4000], [0.2492], [0.4000], [0.1760], [0.4000], [0.6400], [0.4000],
                            [0.6400], [0.4000], [0.6315], [0.4000], [0.6400], [0.4000], [0.0560]])
d_hat_3_5 = -6.9043e-16 * np.ones((1,1))
u_3_5 = 5.1130e-11 * np.ones((1,1))

x_hat_4_3 = 1.0e-05 * np.array([[0.0952], [0.0587], [0.0952], [0.0419], [0.0947], [0.0767], [0.0950],
                             [0.1507], [0.0950], [0.1039], [0.0951], [0.0470], [0.0952], [0.0133]])
x_4_3 = 1.0e-5 * np.array([[0.0800], [0.0498], [0.0800], [0.0352], [0.0800], [0.1280], [0.0800],
                         [0.1280], [0.0800], [0.1263], [0.0800], [0.1280], [0.0800], [0.0112]])
d_hat_4_3 = 2.2965e-14 * np.ones((1,1))
u_4_3 = 1.0226e-10 * np.ones((1,1))

#solver1 = MPCSolver(mysystem, N, x_hat, d_hat, 4.0e-7)
#print solver1.Solver()
#solver3 = MPCSolver(mysystem, N, x_hat_3_5, d_hat_3_5, 8.0e-7)
#print solver3.Solver()

'''