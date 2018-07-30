import numpy as np
from scipy import io
import os
import h5py
os.chdir(r'Data/mat/')
for i in range(1,5):
    data = []
    mat = h5py.File('Part_%d.mat'%(i), 'r')
    matdata = [mat[cell[0]][:] for cell in mat['Part_%d'%(i)]]
    for j in range(len(matdata)):
        data.append(matdata[j])
    np.save(r'../npy/data%d.npy'%(i),data)
