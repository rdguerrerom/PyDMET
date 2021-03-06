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
    
    
    
