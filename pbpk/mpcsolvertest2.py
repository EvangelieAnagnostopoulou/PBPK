from state_space import *
#from MPC2 import *
from cvxopt import solvers, matrix
from scipy.linalg import block_diag



class MPCSolver(System):
    def __init__(self, System, N, x_hat, d_hat, x_, u_):

        self.dsystem = System.DiscreteSystem()
        self.N = N
        self.d_hat = d_hat
        self.x_hat = x_hat
        self.x_ = x_
        self.u_ = u_
        

    def Solver(self):
        max_liver = 1.4e-6
        max_kidney = 5.0e-6
        max_influx = 4.0e-8


        Bd = np.array([[1.], [0.], [0.], [0.], [1.], [0.], [3.], [2.], [0.], [1.], [0.], [0.], [0.], [1.]])
        Cd = np.array([[1.]])

        [nQ, mQ] = self.dsystem.A.shape
        [nR, mR] = self.dsystem.B.shape
    
        Q = np.eye(mQ, dtype="float") * 1./4.
        Q[0:1,0:1] = 40.0
        Q[9:10,9:10] = 1000.0
        Q = 55000.0 * Q
        R = 5.0* np.eye(mR, dtype="float")
        (K, X, E) = bb_dlqr(self.dsystem.A, self.dsystem.B, Q, R)
        Q_f = X

#        Lx = np.bmat([[(self.dsystem.A - np.eye(mQ)), self.dsystem.B],
#                      [self.dsystem.C, np.zeros( (self.dsystem.C.shape[0],
#                                                  self.dsystem.B.shape[1]) )]])
#        Rx = np.bmat([[np.dot(-Bd, self.d_hat)],
#                      [8.0e-7 - np.dot(Cd, self.d_hat)]])
#        xu = np.linalg.solve(Lx, Rx)
#        self.x_ = xu[0:self.dsystem.A.shape[0],:]
#        self.u_ = xu[self.dsystem.A.shape[0],:]

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
        for k in range(0, N-1):
            G = block_diag(G_block, G)

        ## Construct h ##
        h = np.zeros( (2*self.N*(mQ+mR), 1), dtype="float" )
        u_low = 0.0
        u_up = max_influx
        for k in range(0,self.N):
            u_low = np.zeros( (mR,1), dtype="float" )
            u_up = max_influx * np.ones( (mR, 1), dtype="float" )
            x_low = np.zeros( (mQ, 1),dtype="float" )
            x_up = 2.0e-5 * np.ones( (mQ, 1), dtype="float" )
            x_up[9:10,:] = max_liver
            x_up[13:14,:] = max_kidney
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
        
        #if sol['x'][0] <= 0:
        #    u = 0
        #else:
        #    u = sol['x'][0]

        
        #print sol['status']

        if sol['status'] == "optimal":
            return sol['x'][0]
        else:
            print "Problem Infeasible!"
            return 0
        
    

N = 3

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

solver1 = MPCSolver(mysystem, N, x_hat, d_hat, x_, u_)
print solver1.Solver()
solver3 = MPCSolver(mysystem, N, x_hat_3_5, d_hat_3_5, x_3_5, u_3_5)
print solver3.Solver()


