import nibabel as nib
import numpy as np
import gzip
import os

def access(dir_y,dir_y1):
    f_gzip = gzip.GzipFile(dir_y,'rb')
    f_in = open('temp.nii',"wb")
    f_in.write(f_gzip.read())
    f_in.close()
    f1_gzip = gzip.GzipFile(dir_y1,'rb')
    f1_in = open('temp1.nii',"wb")
    f1_in.write(f1_gzip.read())
    f1_in.close()
    y = np.array(nib.load('temp.nii').get_data())
    y1 = np.array(nib.load('temp1.nii').get_data())
    
    TP = 0
    FN = 0
    FP = 0
    for i in range(y.shape[2]):
        TP = TP + sum(sum(y[:,:,i]*y1[:,:,i]))
        FP = FP + sum(sum(y[:,:,i]))-sum(sum(y[:,:,i]*y1[:,:,i]))
        FN = FN + sum(sum(y1[:,:,i]))-sum(sum(y[:,:,i]*y1[:,:,i]))

    print('DSC = '+str(2*TP/(FP+2*TP+FN)))
    print('PPV = '+str(TP/(TP+FP)))
    print('SEN = '+str(TP/(TP+FN))+'\n')

    os.remove('temp.nii')
    os.remove('temp1.nii')

#print('input the pic u want to compare(with no \'')
#print('y:')
#dir_y = input()
#print('y1:')
#dir_y1 = input()
pathtruth = '/home/yex/unet/data/rest/truth/'
pathpredict = '/home/yex/unet/data/rest/predict.bak/'
a = np.sort(os.listdir(pathtruth))
b = np.sort(os.listdir(pathpredict))

for i in range(len(a)):
	print("for " + a[i])
	dir_y = pathtruth + '/' + a[i]
	dir_y1 = pathpredict + '/' + b[i]
	access(dir_y,dir_y1)
