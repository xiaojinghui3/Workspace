import numpy
import cv2
# 载入人脸检测模型：AdaBoost算法模型
face_classifier = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')
font = cv2.FONT_HERSHEY_SIMPLEX # cv2字体

cap = cv2.VideoCapture(0)# 获取摄像头
def face_process(img):
    img = cv2.resize(img, (48, 48), interpolation=cv2.INTER_AREA)  # 转换为48*48大小
    print(img.shape)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#转换为灰度图
    # TODO:识别表情
    emotion = "None"
    return emotion
while True:
    print("GET")
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 灰度图
    # 人脸位置矩形框
    boxes = face_classifier.detectMultiScale(gray, 1.3, 5)
    #绘制矩形框
    for (x,y,w,h) in boxes:
        cv2.rectangle(img,(x,y),(x+w,y+h),(100,100,100),7)
        emotion = face_process(img[y:y+h, x:x+w, :])
        cv2.putText(img, emotion, (x, y), font, 1.2, (0, 0, 0), 2)
    cv2.imshow("imgs", img)
    ret = cv2.waitKey(100)
    if ret == 93: # ASCII=93的字符终止
        break
        cv2.destroyAllWindows()
