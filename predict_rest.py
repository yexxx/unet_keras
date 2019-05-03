from unet_model import unet
import gzip
import os
import numpy as np
import nibabel as nib

# load & predict
model = unet()
model.load_weights('unet_50_val')
test_folder = 'data/rest/image'
predict_folder = 'data/rest/predict'
test_dirs = os.listdir(test_folder)

k = 0
for gzs in test_dirs:
    os.system('clear')
    print('predicting........' + str(k + 1) + ' / ' + str(len(test_dirs)))
    tempdir = test_folder + '/' + gzs[0:len(gzs)-3]
    f_gzip = gzip.GzipFile(test_folder + '/' + gzs,'rb')
    f_in = open(tempdir,"wb")
    f_in.write(f_gzip.read())
    f_in.close()
    a = np.array(nib.load(tempdir).get_data())
    affine = nib.load(tempdir).affine
    a = a.reshape(a.shape[0],a.shape[1],a.shape[2],1)
    for i in range(a.shape[2]):
        a[:,:,i] = model.predict(a[:,:,i].reshape([1,a.shape[0],a.shape[1],1])).reshape([a.shape[0],a.shape[1],1])
    a = a.reshape([a.shape[0],a.shape[1],a.shape[2]])
    a[a<1] = 0
    a[a>=1] = 1
    os.remove(tempdir)
    a = nib.Nifti1Image(a,affine)
    nib.save(a,os.path.join(predict_folder,gzs))
    k = k+1
print('done')
