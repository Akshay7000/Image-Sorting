import face_recognition as fr
import os
import cv2
import face_recognition
import shutil
import glob
from tkinter import filedialog
from tkinter import *
import numpy as np
from time import sleep


def create():
	name = input("\n\nEnter your Name: ")

	try:
		os.mkdir("./faces/"+ name +"/")
		
		cam = cv2.VideoCapture(0)
		
		while True:
			ret,frame = cam.read()
			cv2.imshow("Press Esc to capture and exit.",frame)
			
			if not ret:
				print("Frame not readed")
				break
			
			key = cv2.waitKey(1)
			try:
				if key == 27:
					os.rmdir("./faces/"+ name )
					break
			except OSError as e:
				print("Face data created")
				break
				
			if key == ord('c'):
				cv2.imwrite("./faces/"+ name +"/" + name +".jpg",frame)
				print("Image Saved to the "+ name +" folder")
				
		
		cam.release()
		cv2.destroyAllWindows()
				
	except OSError as e:
		print(" Cannot create the folder, already exists")
 
def sort():
	name = input("\n\nEnter Your Name: ")
	# Select the image Dir
	root = Tk()
	root.withdraw()
	folder_selected = filedialog.askdirectory()


		
	def face_code():
		def get_encoded_faces():

			
			
			"""
			looks through the faces folder and encodes all
			the faces

			:return: dict of (name, image encoded)
			"""
			
			encoded = {}

			for dirpath, dnames, fnames in os.walk("./faces/" + name):
				for f in fnames:
					if f.endswith(".jpg") or f.endswith(".png"):
						face = fr.load_image_file("faces/"+ name +"/" + f)
						encoding = fr.face_encodings(face)[0]
						encoded[f.split(".")[0]] = encoding

			return encoded


		def unknown_image_encoded(img):
			"""
			encode a face given the file name
			"""
			face = fr.load_image_file("faces/"+ name +"/" + img)
			encoding = fr.face_encodings(face)[0]

			return encoding


		def classify_face(b=[]):
			
			
			for x in range(len(b)):
				img = cv2.imread(b[x], 1)

			
				faces = get_encoded_faces()
				faces_encoded = list(faces.values())
				known_face_names = list(faces.keys())
				 
				
				#img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
				#img = img[:,:,::-1]
			 
				face_locations = face_recognition.face_locations(img)
				unknown_face_encodings = face_recognition.face_encodings(img, face_locations)

				face_names = []
				for face_encoding in unknown_face_encodings:
					# See if the face is a match for the known face(s)
					matches = face_recognition.compare_faces(faces_encoded, face_encoding)
					name = "Unknown"

					# use the known face with the smallest distance to the new face
					face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
					best_match_index = np.argmin(face_distances)
					if matches[best_match_index]:
						name = known_face_names[best_match_index]
						print("match " + b[x])
						shutil.copy(b[x],"./copy/"+name+"/")
					#else:
						#print("not match " + b[x])

					face_names.append(name)

					for (top, right, bottom, left), name in zip(face_locations, face_names):
						# Draw a box around the face
						cv2.rectangle(img, (left-20, top-20), (right+20, bottom+20), (255, 0, 0), 2)

						# Draw a label with a name below the face
						cv2.rectangle(img, (left-20, bottom -15), (right+20, bottom+20), (255, 0, 0), cv2.FILLED)
						font = cv2.FONT_HERSHEY_DUPLEX
						cv2.putText(img,'Press Q to exit',(50, 50),font, 1,(0, 255, 255),2, cv2.LINE_4)
						cv2.putText(img, name, (left -20, bottom + 15), font, 1.0, (255, 255, 255), 2)


				# Display the resulting image
			while True:
				img_scale = cv2.resize(img, None, fx=0.25, fy=0.25)
				cv2.imshow('Image Sorted, Press Q to Exit', img_scale)
				if cv2.waitKey(1) & 0xFF == ord('q'):
					return face_names 


		#Reads the files with extintion .jpg in working dir
		#a = glob.glob('*.jpg')

		a = glob.glob(folder_selected + '/'+'*.jpg')
		#print(a - folder_selected)

		print(classify_face(a))

	try:
		#make folder in copy dir
		os.mkdir("./copy/"+ name +"/")
		face_code()
		
	except OSError as e:

		face_code()

	

print("\n\n1. Create Face Data \n2. Short Images \n3. EXIT\n\n")

n = int(input("Enter the no. from below:  "))

if 1 == n:
	create()

elif n == 2:
	sort()
	
else:
	print("exit")
