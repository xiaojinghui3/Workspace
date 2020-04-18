# 数据源
(地址)[https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data]
# 数据说明
- 数据中为48x48像素人脸灰度图。数据中人脸在居中位置，并且面积大致相等。需要做的就是将人脸表情进行分类包含七个类：(0=Angry, 1=Disgust, 2=Fear, 3=Happy, 4=Sad, 5=Surprise, 6=Neutral).
- train.csv 包含两列，第一列是表情，第二列是像素。表情列中使用数字0-6标注不同类。像素列中包含了每个图形的像素的字符串，存储方式为列优先存储。
# 需要做什么
- 构建用于人脸表情识别的模型
- 训练数据：前2000个样本，测试数据2000以后的样本。
- 修改获取摄像头的代码，使得其可以用于输出实时表情数据。
# 参考代码
- 图像情绪识别参考.py

