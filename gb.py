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
import PIL
from PIL import Image,ImageTk
import pytesseract
import tkinter as tk
from tkinter import ttk
import time

def pstart():
	
	my_progress.start(10)
		#my_progress['value'] +=20
	new.update_idletasks()
		#time.sleep(1)


def imgsort():
	global x
	s=x.get()
	name=s
	root = Tk()
	root.withdraw()
	folder_selected = filedialog.askdirectory()
	
	new.destroy()
		
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

		

def add_face():
	global render2,add_btnn,myimgg
	new= Toplevel()
	new.title("Add Face")
	new.geometry('450x450')
	new.resizable(width=False,height=False)
	new.iconbitmap('./export/icn.ico')
	load2 = Image.open('./export/bg2.png')
	render2 = ImageTk.PhotoImage(load2)
	img = Label(new,image = render2)
	img.place(x = 0,y = 0)
	
	loadd=Image.open("./export/r_new.png")
	myimgg = ImageTk.PhotoImage(loadd)
	myLabell = Label(new,image = myimgg,bd=0)
	myLabell.grid(row = 0, column = 0)
	
	myimg2 = ImageTk.PhotoImage(Image.open("./export/r2_new.png"))
	myLabel2 = Label(new,image = myimg2,bd=0)
	myLabel2.grid(row = 0, column = 1)
	
	
	entry = Entry(new,width=20,font=("Arial",15), bd=0)
	entry.grid(row = 1, column = 2)
	
	
	
	add_btnn = PhotoImage(file = './export/Badd.png')
	img_label= Label(image = add_btnn)
	
	myimg3 = ImageTk.PhotoImage(Image.open("./export/l_new.png"))
	myLabel3 = Label(new,image = myimg3,bd=0)
	myLabel3.grid(row = 2, column = 2)
	
	my_btnn = Button(new, image = add_btnn, border = 0)
	my_btnn.grid(row = 3, column = 2)
	

########################################################################################		
		
def sort():

	global render2,add_btnn,myimgg,x,my_progress,new
	new= Toplevel()
	new.title("Add Face")
	new.geometry('450x450')
	new.resizable(width=False,height=False)
	new.iconbitmap('./export/icn.ico')
	load2 = Image.open('./export/bg3.png')
	render2 = ImageTk.PhotoImage(load2)
	img = Label(new,image = render2)
	img.place(x = 0,y = 0)
	
	loadd=Image.open("./export/r_new.png")
	myimgg = ImageTk.PhotoImage(loadd)
	myLabell = Label(new,image = myimgg,bd=0)
	myLabell.grid(row = 0, column = 0)
	
	myimg2 = ImageTk.PhotoImage(Image.open("./export/r2_new.png"))
	myLabel2 = Label(new,image = myimg2,bd=0)
	myLabel2.grid(row = 0, column = 1)
	
	x=StringVar()
	entry = Entry(new,width=20,font=("Arial",15), bd=0, textvariable=x)
	entry.grid(row = 1, column = 2)
	
	
	
	add_btnn = PhotoImage(file = './export/Bsort.png')
	img_label= Label(image = add_btnn)
	
	myimg3 = ImageTk.PhotoImage(Image.open("./export/l_new.png"))
	myLabel3 = Label(new,image = myimg3,bd=0)
	myLabel3.grid(row = 2, column = 2)
	
	my_btnn = Button(new, image = add_btnn, border = 0, command=imgsort)
	my_btnn.grid(row = 3, column = 2)
	
	my_progress = ttk.Progressbar(new, orient=HORIZONTAL, length= 300,mode='indeterminate')
	my_progress.grid(row = 4, column = 2)

########################################################################################		
	
	
root = Tk()
root.title('Face Match')
root.geometry('450x450')
root.resizable(width=False,height=False)
root.iconbitmap('./export/icn.ico')
load = Image.open('./export/bg1.png')
render = ImageTk.PhotoImage(load)
img = Label(root,image = render)
img.place(x = 0,y = 0)

myimg = ImageTk.PhotoImage(Image.open("./export/r.png"))
myLabel = Label(image = myimg,bd=0)
myLabel.grid(row = 0, column = 0)

myimg2 = ImageTk.PhotoImage(Image.open("./export/r2.png"))
myLabel2 = Label(image = myimg2,bd=0)
myLabel2.grid(row = 1, column = 1)



add_btn = PhotoImage(file = './export/Badd.png')
img_label = Label(image = add_btn)

add_btn2 = PhotoImage(file = './export/Bsort.png')
img_label = Label(image = add_btn2)

my_btn = Button(root, image = add_btn, border = 0, command = add_face)
my_btn.grid(row = 1, column = 3)

myLabel2 = Label(image = myimg2,bd=0)
myLabel2.grid(row = 1, column = 4)

my_btn2 = Button(root, image = add_btn2, border = 0,command = sort)
my_btn2.grid(row = 1, column = 5)

root.mainloop()

########################################################################################