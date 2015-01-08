'''
    PyDMET: a python implementation of density matrix embedding theory
    Copyright (C) 2014, 2015 Sebastian Wouters
    
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
'''

import numpy as np

def PullSkew2by2(HubbardU):

    umatrices = []

    umat_14 = np.array([[  6.99984384e+00 , -4.61919762e+00 , -2.67357343e-04 , 1.34211945e+00],[ -4.61919762e+00 ,  6.99984384e+00 , -6.45005348e-01 ,  1.14279907e-04],[ -2.67357343e-04 , -6.45005348e-01 ,  6.99984384e+00 , -4.72032569e+00], [  1.34211945e+00 ,  1.14279907e-04 , -4.72032569e+00 ,  6.99984384e+00]])
    umat_13 = np.array([[  6.49982634e+00 , -4.09157081e+00  , 4.24886075e-04 ,  1.20414851e+00], [ -4.09157081e+00 ,  6.49982634e+00 , -5.38391200e-01 ,  2.11957062e-04], [  4.24886075e-04 , -5.38391200e-01 ,  6.49982634e+00 , -4.21699346e+00], [  1.20414851e+00 ,  2.11957062e-04 , -4.21699346e+00 ,  6.49982634e+00]])
    umat_12 = np.array([[  6.00116098e+00 , -3.53872700e+00 , -1.07920334e-04 ,  1.05523762e+00],  [ -3.53872700e+00 ,  6.00116098e+00 , -4.37718152e-01 , -1.13920426e-04],  [ -1.07920334e-04 , -4.37718152e-01 ,  6.00116098e+00 , -3.69729220e+00], [  1.05523762e+00 , -1.13920426e-04 , -3.69729220e+00 ,  6.00116098e+00]])
    umat_11 = np.array([[  5.50012542e+00 , -2.95714776e+00 ,  9.92420010e-05 ,  8.98462292e-01], [ -2.95714776e+00 ,  5.50012542e+00 , -3.40534737e-01 , -5.00991768e-05], [  9.92420010e-05 , -3.40534737e-01 ,  5.50012542e+00 , -3.16494258e+00], [  8.98462292e-01 , -5.00991768e-05 , -3.16494258e+00 ,  5.50012542e+00]])
    umat_10 = np.array([[  4.99993638e+00 , -2.32459319e+00 ,  3.52535810e-05 ,  7.28640488e-01],  [ -2.32459319e+00 ,  4.99993638e+00 , -2.47549298e-01 , -4.69359572e-05],  [  3.52535810e-05 , -2.47549298e-01 ,  4.99993638e+00 , -2.61035757e+00], [  7.28640488e-01 , -4.69359572e-05 , -2.61035757e+00 ,  4.99993638e+00]])
    umat_9 = np.array([[  4.50003865e+00 , -1.54898321e+00 , -6.54274785e-06 ,  5.17674696e-01], [ -1.54898321e+00 ,  4.50003865e+00 , -1.56451599e-01, -3.08497889e-06], [ -6.54274785e-06 , -1.56451599e-01 ,  4.50003865e+00 , -1.98031801e+00], [  5.17674696e-01 , -3.08497889e-06 , -1.98031801e+00 ,  4.50003865e+00]])
    umat_8 = np.array([[  4.00000123e+00 , -2.16933306e-01 , -1.12507993e-05 ,  9.96969206e-02], [ -2.16933306e-01 ,  4.00000123e+00 , -1.37128943e-01 , -1.44486592e-05], [ -1.12507993e-05 , -1.37128943e-01 ,  4.00000123e+00 , -6.01707731e-01], [  9.96969206e-02 , -1.44486592e-05 , -6.01707731e-01 ,  4.00000123e+00]])
    umat_7 = np.array([[  3.49999741e+00 , -1.89488241e-01 , -4.39727640e-06 ,  8.48896579e-02], [ -1.89488241e-01,   3.49999741e+00,  -7.52697212e-02,  -6.92307302e-06], [ -4.39727640e-06,  -7.52697212e-02,   3.49999741e+00,  -3.86368973e-01], [  8.48896579e-02,  -6.92307302e-06,  -3.86368973e-01,   3.49999741e+00]])
    
    umatrices.append(umat_7)
    umatrices.append(umat_8)
    umatrices.append(umat_9)
    umatrices.append(umat_10)
    umatrices.append(umat_11)
    umatrices.append(umat_12)
    umatrices.append(umat_13)
    umatrices.append(umat_14)
    
    index = 0
    for count in range(1, len(umatrices)):
        if abs( HubbardU - 2*umatrices[index][0,0] ) > abs( HubbardU - 2*umatrices[count][0,0] ):
            index = count
            
    return HubbardU / ( 2*umatrices[index][0,0] ) * umatrices[index]
    
def PullSquare2by2(HubbardU):

    umatrices = []

    umat_20 = np.array([[  9.99676791e+00, 1.04658416e+00, -8.38117625e+00, -4.70770865e-03],[  1.04658416e+00, 9.99676791e+00, -4.10382768e-03, -8.38744786e+00], [ -8.38117625e+00, -4.10382768e-03, 9.99676791e+00, 1.04559680e+00], [ -4.70770865e-03, -8.38744786e+00, 1.04559680e+00, 9.99676791e+00]])
    umat_19 = np.array([[ 9.44456988 , 1.07326461 ,-7.99747044 ,-0.01146101], [ 1.07326461 , 9.44456988, -0.01187153, -7.99923051], [-7.99747044, -0.01187153 , 9.44456988 , 1.07247402], [-0.01146101, -7.99923051 , 1.07247402 , 9.44456988]])
    umat_18 = np.array([[ 9.00286479,  1.04725947, -7.41642855,  0.00981632], [ 1.04725947,  9.00286479,  0.01114942, -7.41879459], [-7.41642855,  0.01114942,  9.00286479,  1.04667929], [ 0.00981632, -7.41879459,  1.04667929 , 9.00286479]])
    umat_17 = np.array([[ 8.51041956,  1.01910503, -6.940265 ,   0.01271311], [ 1.01910503 , 8.51041956 , 0.0123651 , -6.9398909 ], [-6.940265  ,  0.0123651  , 8.51041956 , 1.01822845], [ 0.01271311, -6.9398909  , 1.01822845 , 8.51041956]])
    umat_16 = np.array([[ 8.00162747,  0.99359641, -6.44053782,  0.01301817], [ 0.99359641,  8.00162747,  0.01380081, -6.4423107 ], [-6.44053782,  0.01380081,  8.00162747,  0.99300814], [ 0.01301817, -6.4423107,   0.99300814,  8.00162747]])
    umat_15 = np.array([[ 7.50383507,  0.96210568, -5.93055889,  0.0164453 ], [ 0.96210568,  7.50383507,  0.01642355, -5.9300481 ], [-5.93055889,  0.01642355,  7.50383507,  0.96192001], [ 0.0164453,  -5.9300481,   0.96192001 , 7.50383507]])
    umat_14 = np.array([[ 7.00132348,  0.93037608, -5.43633969,  0.01920754], [ 0.93037608,  7.00132348,  0.01937436, -5.43575162], [-5.43633969,  0.01937436,  7.00132348,  0.93033949], [ 0.01920754, -5.43575162,  0.93033949,  7.00132348]])
    umat_13 = np.array([[  6.48996841e+00 ,  8.67597121e-01 , -4.92209455e+00  , 2.01305717e-03], [  8.67597121e-01 ,  6.48996841e+00 ,  1.95986197e-03 , -4.92201779e+00], [ -4.92209455e+00 ,  1.95986197e-03 ,  6.48996841e+00 ,  8.67605134e-01], [  2.01305717e-03 , -4.92201779e+00 ,  8.67605134e-01 ,  6.48996841e+00]])
    umat_12 = np.array([[  5.99536407e+00,   8.24325486e-01,  -4.41852467e+00,  -3.71569967e-04], [  8.24325486e-01 ,  5.99536407e+00 , -4.99723331e-04 , -4.41839703e+00], [ -4.41852467e+00 , -4.99723331e-04 ,  5.99536407e+00 ,  8.24271665e-01], [ -3.71569967e-04 , -4.41839703e+00 ,  8.24271665e-01 ,  5.99536407e+00]])
    umat_11 = np.array([[  5.50121633e+00  , 7.74709224e-01 , -3.91991277e+00 ,  4.99958177e-04], [  7.74709224e-01 ,  5.50121633e+00  , 2.80209496e-04 , -3.92011677e+00], [ -3.91991277e+00  , 2.80209496e-04 ,  5.50121633e+00  , 7.74701056e-01], [  4.99958177e-04 , -3.92011677e+00 ,  7.74701056e-01  , 5.50121633e+00]])
    umat_10 = np.array([[  5.00005834e+00 ,  7.21238526e-01 , -3.42295923e+00 ,  3.62632463e-04], [  7.21238526e-01 ,  5.00005834e+00  , 1.53508288e-04 , -3.42301661e+00], [ -3.42295923e+00 ,  1.53508288e-04  , 5.00005834e+00  , 7.21252697e-01], [  3.62632463e-04,  -3.42301661e+00 ,  7.21252697e-01 ,  5.00005834e+00]])
    umat_9 = np.array([[  4.50033357e+00 ,  6.61060789e-01 , -2.92996448e+00 ,  2.44417578e-04], [  6.61060789e-01 ,  4.50033357e+00 ,  7.94289098e-05 , -2.93000895e+00], [ -2.92996448e+00  , 7.94289098e-05 ,  4.50033357e+00  , 6.61098054e-01], [  2.44417578e-04 , -2.93000895e+00 ,  6.61098054e-01  , 4.50033357e+00]])
    umat_8 = np.array([[  3.99950489e+00 ,  5.93406389e-01 , -2.44232564e+00 , -6.95311909e-05], [  5.93406389e-01  , 3.99950489e+00 , -8.67419589e-05 , -2.44236762e+00], [ -2.44232564e+00 , -8.67419589e-05 ,  3.99950489e+00  , 5.93438737e-01], [ -6.95311909e-05  ,-2.44236762e+00  , 5.93438737e-01  , 3.99950489e+00]])
    umat_7 = np.array([[  3.49983677e+00 ,  5.19772666e-01 , -1.96333383e+00 , -4.62350495e-05], [  5.19772666e-01 ,  3.49983677e+00 , -2.24664076e-05 , -1.96332188e+00], [ -1.96333383e+00 , -2.24664076e-05 ,  3.49983677e+00  , 5.19725454e-01], [ -4.62350495e-05 , -1.96332188e+00 ,  5.19725454e-01  , 3.49983677e+00]])
    
    umatrices.append(umat_6)
    umatrices.append(umat_7)
    umatrices.append(umat_8)
    umatrices.append(umat_9)
    umatrices.append(umat_10)
    umatrices.append(umat_11)
    umatrices.append(umat_12)
    umatrices.append(umat_13)
    umatrices.append(umat_14)
    umatrices.append(umat_15)
    umatrices.append(umat_16)
    umatrices.append(umat_17)
    umatrices.append(umat_18)
    umatrices.append(umat_19)
    umatrices.append(umat_20)
    
    index = 0
    for count in range(1, len(umatrices)):
        if abs( HubbardU - 2*umatrices[index][0,0] ) > abs( HubbardU - 2*umatrices[count][0,0] ):
            index = count
            
    return HubbardU / ( 2*umatrices[index][0,0] ) * umatrices[index]
    
    
    
