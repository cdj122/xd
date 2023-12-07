import cv2
from face import *


'''
功能：识别image身份
输入：
	1)image：被测图片
	2）libpath：人脸库地址
	3）save_dir：图片保存地址
	4)Threshold：人脸相似度阈值，Threshold越高识别越精准，但是检出率越低
'''
def pic(image,libpath,save_dir,Threshold=0.65):
	known_face_encodings, known_face_names = registeredIdentity(libpath)
	retname, retscore,face_locations = identityRecognition(image[:, :, ::-1], known_face_encodings, known_face_names,Threshold=Threshold)

	image = age_show(image, face_locations, retname)
	print('识别为：%s\n相似度：%2f' % (str(retname), retscore))
	cv2.imwrite(save_dir, image)
	cv2.imshow('img', image)
	cv2.waitKey(0)

if __name__ == '__main__':
	image = cv2.imread('Test/pic_in/test1.png')
	pic(image=image,libpath='./facelib/',save_dir='./Test/pic_out/test1.png')

