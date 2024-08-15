# Importing Necessary Libraries
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image,ImageTk
import numpy
import numpy as np

from tensorflow.keras.models import load_model

# loading the model 
# model = load_model("gender_detector_custom.keras.keras")
model = load_model("gender_detector_vgg16.keras")

# Initializing the GUI
top=tk.Tk()
top.geometry('800x600')
top.title('Male or Female')
top.configure(background='#101820')


label1=Label(top,background="#FEE715",font=('arial',15,"bold"))
sign_image=Label(top)


def Detect(file_path):
    global label_packed
    
    image=Image.open(file_path)

    image=image.resize((224,224))
    image=np.expand_dims(image,axis=0)
    
    print(image.shape, len(image))
    image=np.array(image, dtype=np.float32)/255.0
    print(image.shape, len(image))
    gender_dict = {0: 'man', 1: 'woman'}
    prediction=model.predict(image)
    
    pred=int(np.round(prediction[0][0]))
    print(prediction, pred)
    output_text = "He is a male" if(pred == 0) else "She is a female"
    label1.configure(foreground="#011638",text=output_text)

# Defining Show_detect button function
def show_Detect_button(file_path):
    Detect_b=Button(top,text="Detect Image",command=lambda: Detect(file_path),padx=10,pady=5)
    Detect_b.configure(background="#FEE715",foreground='#101820',font=('arial',10,'bold'))
    Detect_b.place(relx=0.79,rely=0.46) 

# Definig Upload Image Function
def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image=im
        label1.configure(text='')
        show_Detect_button(file_path)
    except:
        
        pass

upload=Button(top,text="Upload an Image",command=upload_image,padx=10,pady=5)
upload.configure(background="#FEE715",foreground='#101820',font=('arial',10,'bold'))
upload.pack(side='bottom',pady=50)
sign_image.pack(side='bottom',expand=True)
label1.pack(side="bottom",expand=True)
heading=Label(top,text="Gender Detector",pady=20,font=('arial',20,"bold"))
heading.configure(background="#101820",foreground="#FEE715")
heading.pack()
top.mainloop()