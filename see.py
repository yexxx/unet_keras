import os
import nibabel as nib
import gzip
import numpy as np
def see(dirc):
    f_gzip = gzip.GzipFile(dirc,'rb')
    f_in = open('temp.nii',"wb")
    f_in.write(f_gzip.read())
    f_in.close()
    a = np.array(nib.load('temp.nii').get_data())
    nib.viewers.OrthoSlicer3D(a).show()
    os.remove('temp.nii')
    return a

print('input the pic u want to seek (with no \')')
dirc = input()
see(dirc)
