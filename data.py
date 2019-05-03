# imports
import numpy as np
import nibabel as nib
import os
import gzip
import h5py

# DATA: 145*880*880*12+35*880*880*15 = 2265*880*880*1 ->  4530*400*400*1

x_dir = 'data/train/image'
y_dir = 'data/train/groundtruth'
train_x_dirs = np.sort(os.listdir(x_dir))
train_y_dirs = np.sort(os.listdir(y_dir))

if os.path.exists('data_400.hdf5') == 0:
    if  os.path.exists('data.hdf5') == 0:
        f = h5py.File("data.hdf5", "w")
        dset_train_x = f.create_dataset("train_x", (2265,880,880,1))
        dset_train_y = f.create_dataset("train_y", (2265,880,880,1))

        #load_train_X
        i = 0
        k = 0
        for gzs in train_x_dirs:
            os.system('clear')
            print('load_train_x........' + str(k + 1) + ' / ' + '180')
            tempdir = x_dir + '/' + gzs[0:len(gzs)-3]
            f_gzip = gzip.GzipFile(x_dir + '/' + gzs,'rb')
            f_in = open(tempdir,"wb")
            f_in.write(f_gzip.read())
            f_in.close()

            a = np.array(nib.load(tempdir).get_data())
            for j in np.arange(a.shape[2]):
                dset_train_x[i + j] = a[:,:,j].reshape(880,880,1)
        
            os.remove(tempdir)
            i = i + a.shape[2]
            k = k + 1
        
        #loda_train_y   
        i = 0
        k = 0
        for gzs in train_y_dirs:
            os.system('clear')
            print('load_train_y........' + str(k + 1) + ' / ' + '180')
            tempdir = y_dir + '/' + gzs[0:len(gzs)-3]
            f_gzip = gzip.GzipFile(y_dir + '/' + gzs,'rb')
            f_in = open(tempdir,"wb")
            f_in.write(f_gzip.read())
            f_in.close()
        
            a = np.array(nib.load(tempdir).get_data())
            for j in np.arange(a.shape[2]):
                dset_train_y[i + j] = a[:,:,j].reshape(880,880,1)
        
            os.remove(tempdir)
            i = i + a.shape[2]
            k = k + 1

f = h5py.File('data.hdf5', 'r')
train_x = f['train_x']
train_y = f['train_y']

    #400*400
if os.path.exists('data_400.hdf5') == 0:
    if  os.path.exists('data.hdf5'):
        f = h5py.File("data_400.hdf5", "w")
        dset_train_x_400 = f.create_dataset("train_x_400", (4530,400,400,1))
        dset_train_y_400 = f.create_dataset("train_y_400", (4530,400,400,1))
    
        for i in range(2265):
            for j in range(2):
                dset_train_x_400[i*2+j] = train_x[i][200:600,20+400*j:420+400*j,:]
                dset_train_y_400[i*2+j] = train_y[i][200:600,20+400*j:420+400*j,:]
            os.system('clear')
            print('segmentating......' + str(i+1) + ' / ' + '2265')
    else: print('Error without data\n')

f1 = h5py.File('data_400.hdf5', 'r')
train_x_400 = f1['train_x_400']
train_y_400 = f1['train_y_400']
