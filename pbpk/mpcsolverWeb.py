from state_space import *
#from MPC2 import *
from cvxopt import solvers, matrix
from scipy.linalg import block_diag
import numpy as np

def ss_opt(a, b, c, bd, cd, ref, d_hat):
    mq = a.shape[0]
    mr = b.shape[1]
    a_mpc = np.bmat([[a - np.eye(mq), b], [c, np.zeros((mr, mr))]])
    b_mpc = np.bmat([[-np.dot(bd, d_hat)], [ref - np.dot(cd, d_hat)]])
    x_mpc = np.linalg.solve(a_mpc, b_mpc)
    x_ = x_mpc[0:mq, :]
    u_ = x_mpc[mq::, :]
    return x_, u_

class MPCSolver(System):
    def __init__(self, System, N, x_hat, d_hat, x_, u_,  max_liver, max_kidney, max_influx, min_residual, max_residual,
                 min_skin, max_skin, min_bladder, max_bladder, min_lung, max_lung, min_liver, min_kidney, min_heart,
                 max_heart, min_muscle, max_muscle, min_spleen, max_spleen, min_placental, max_placental, Qweight, Rweight):
        # self.del_list = System.ContinuousSystem()
        self.del_list = System.ContinuousSystem()
        self.dsystem = System.DiscreteSystem()
        self.N = N
        self.d_hat = d_hat
        self.x_hat = x_hat
        self.x_ = x_
        self.u_ = u_
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

        Cd = np.array([[1.]])

        [nQ, mQ] = self.dsystem.A.shape
        [nR, mR] = self.dsystem.B.shape

        qmpc = np.eye(mQ, dtype="float") * self.qw
        #qmpc[0:1, 0:1] = 40.0
        #qmpc[9-len(self.del_list), 9-len(self.del_list)] = 1000.0
        #qmpc *= 5500.0
        rmpc = self.rw * np.eye(mR, dtype="float")  # 5.0
        (kl, ll, el) = bb_dlqr(self.dsystem.A, self.dsystem.B, qmpc, rmpc)
        q_fmpc = ll

        # Equality Constraints #
        a_til = np.zeros((self.N * mQ, self.N * (mR + mQ)), dtype="float")
        first_row = np.bmat([-self.dsystem.B, np.eye(mQ, dtype="float")])
        second_row = np.bmat([-self.dsystem.A, -self.dsystem.B, np.eye(mQ, dtype="float")])
        a_til[0:nR, 0:(mQ + mR)] = first_row

        for k in range(1, self.N):
            a_til[k*nR:(k+1)*nR, k*mR+(k-1)*mQ:(k+1)*mR+(k+1)*mQ] = second_row

        #
        b_til = np.zeros((self.N*mQ, 1), dtype="float")
        b_til[0:mQ] = np.dot(Bd, self.d_hat) + np.dot(self.dsystem.A, self.x_hat)
        for k in range(1, self.N):
            b_til[k*nR: (k+1)*nR] = np.dot(Bd, self.d_hat)
        #

        # Inequality Constraints #
        hc = np.zeros((self.N*(mQ+mR), self.N*(mQ+mR)), dtype="float")
        for k in range(0, self.N):
            hc[k*mR+k*mQ:(k+1)*mR+k*mQ, k*mR+k*mQ:(k+1)*mR+k*mQ] = rmpc
            hc[(k+1)*mR+k*mQ:(k+1)*mR+(k+1)*mQ, (k+1)*mR+k*mQ:(k+1)*mR+(k+1)*mQ] = qmpc
            if k == self.N-1:
                hc[(k+1)*mR+k*mQ:(k+1)*mR+(k+1)*mQ, (k+1)*mR+k*mQ:(k+1)*mR+(k+1)*mQ] = q_fmpc
        hc *= 2.
        # Construct G #
        first_col_g = np.bmat([[-np.eye(mR, dtype="float")], [np.eye(mR, dtype="float")]])
        second_col_g = np.bmat([[-np.eye(mQ, dtype="float")], [np.eye(mQ, dtype="float")]])
        g_block = block_diag(first_col_g, second_col_g)
        g = g_block
        for k in range(0, self.N-1):
            g = block_diag(g_block, g)

        # Construct h #
        h = np.zeros((2*self.N*(mQ+mR), 1), dtype="float")
        u_low = np.zeros((mR, 1), dtype="float")
        u_up = self.max_influx*np.ones((mR, 1), dtype="float")
        x_low = np.zeros((mQ, 1), dtype="float")

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

        for k in range(0, self.N):
            h[2*k*mR+2*k*mQ:2*k*mR+2*k*mQ+mR] = u_low
            h[2*k*mR+2*k*mQ+mR:2*(k+1)*mR+2*k*mQ] = u_up
            h[2*(k+1)*mR+2*k*mQ:2*(k+1)*mR+2*k*mQ+mQ] = x_low
            h[2*k*mR+2*k*mQ+2*mR+mQ:2*(k+1)*mR+2*(k+1)*mQ] = x_up

        plin = np.zeros((1, self.N*(mQ+mR)), dtype="float")
        a_lin = np.dot(self.x_.T, qmpc)
        b_lin = np.dot(self.u_.T, rmpc)
        lin = np.bmat([[b_lin, a_lin]])
        for i in range(0, self.N*(mQ+mR), (mQ+mR)):
            plin[0, i:i+(mQ+mR)] = lin
        f = np.dot(self.x_.T, q_fmpc)
        flin = np.concatenate((b_lin, f), axis=1)
        plin[0, (self.N-1)*(mQ+mR)::] = flin
        plin = -2. * plin.T

        solvers.options['abstol'] = 1.e-324
        sol = solvers.qp(matrix(hc), matrix(plin), matrix(g), matrix(h),
                         matrix(a_til), matrix(b_til))

        if sol['x'][0] <= 0:
            u = 0
        else:
            u = sol['x'][0]

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