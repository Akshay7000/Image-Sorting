import cv2
import os

name = input("Enter your Name: ")

try:
	os.mkdir("./faces/"+ name +"/")
	cam = cv2.VideoCapture(0)

	while True:
		ret,frame = cam.read()
		if not ret:
			print("Frame not readed")
			
		cv2.imshow("test",frame)
		
		key = cv2.waitKey(1)
		if key%256 == 27:
			cv2.imwrite("./faces/"+ name +"/" + name +".jpg",frame)
			break
			
	cam.release()
	print("Image Saved to the "+ name +" 	folder")
			
except OSError as e:
    print(" Cannot create the folder, already exists")
	#cam.release()
    
cv2.destroyAllWindows()