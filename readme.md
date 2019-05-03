**文件说明**:
        
    data/train 数据集,其中10%为验证集  
    data/rest 测试集,其中predict,predict1,predict11为运行三次的结果  
    data/test 课程设计要求预测文件

**运行方式:**

    进入unet文件夹:cd /path/to/unet 
    安装依赖:pip(3) install -r environment.txt
    运行程序:python3 name.py    
        
        name.py:
        1.data.py 进行用于训练的数据的准备
        2.unet_model.py 建立的unet模型
        3.train.py 训练模型
        4.predict.py predict_rest.py 对data/teat/image,data/rest/image的图片分割,保存到data/test/predict,data/rest/predict中
        5.see.py 输入文件路径,看.nii文件

**参考**:https://github.com/zhixuhao/unet