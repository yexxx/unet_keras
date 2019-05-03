from data import train_x_400,train_y_400
from unet_model import unet
from keras.callbacks import TensorBoard
import os

if os.path.exists('unet_50_val') == 0:
	model = unet()
	model.fit(train_x_400,train_y_400,epochs = 50,batch_size = 2, validation_split=0.1, 		shuffle="batch", callbacks = [TensorBoard(log_dir = './tmp/log')])
	model.save_weights('unet_50_val')

