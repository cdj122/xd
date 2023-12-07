import cv2
from face import *
'''
功能：实时人脸识别，并保存视频到本地
输入：
	1)known_face_encodings:人脸库特征向量
	2)known_face_names:人脸库名字标签
	3)source:视频源，PC摄像头读取设置为0，本地视频源则设置为地址，如：'./Test/video_in/1.avi'
	4)save_dir:视频保存地址
	5)Threshold：人脸相似度阈值，Threshold越高识别越精准，但是检出率越低
备注：按q退出
'''

def video(known_face_encodings,known_face_names,source,save_dir,Threshold=0.65):
	cap = cv2.VideoCapture(source)
	size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
	        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
	video_writer = cv2.VideoWriter(save_dir,cv2.VideoWriter_fourcc('X','V','I','D'),17,size)
	ret,image = cap.read()
	while(ret):
		retname, retscore,face_locations = identityRecognition(image[:, :, ::-1], known_face_encodings, known_face_names,
		                                        Threshold=Threshold)
		image = age_show(image, face_locations, retname)
		video_writer.write(image)
		cv2.imshow('face_recognition',image)
		cv2.waitKey(5)
		ret, image = cap.read()

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

if __name__ == '__main__':
	source = 0
	libpath = './facelib/'
	save_dir = './Test/video_out/1.avi'
	known_face_encodings, known_face_names = registeredIdentity(libpath)
	video(known_face_encodings,known_face_names,source,save_dir,Threshold=0.65)