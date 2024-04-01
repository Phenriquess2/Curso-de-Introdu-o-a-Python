from tkinter import *
from tkinter import messagebox
import random
from PIL import Image, ImageTk

def no():\
    messagebox.showinfo(' ', 'TE LOVO <3')
    root.after(2000, show_image)  # Mostra a imagem após 2 segundos

def motionMouse(event):
    btnYes.place(x=random.randint(0, 500), y=random.randint(0, 500))

def show_image():
    heart_image = Image.open("C:/Users/pedro/Downloads/teresh.jpg")  # Insira o caminho para sua imagem de coração
    heart_photo = ImageTk.PhotoImage(heart_image)
    image_label = Label(root, image=heart_photo)
    image_label.image = heart_photo
    image_label.place(x=200, y=200)

root = Tk()
root.geometry('600x600')
root.title('survey')
root.resizable(width=False, height=False)
root['bg'] = 'white'

label = Label(root, text='QUER NAMORAR COMIGO?', font=('Arial 20 bold'), bg='white').pack()
btnYes = Button(root, text='NÃO', font=('Arial 20 bold'))
btnYes.place(x=170, y=100)
btnYes.bind('<Enter>', motionMouse)
btnNo = Button(root, text='SIM', font='Arial 20 bold', command=no)
btnNo.place(x=350, y=100)

root.mainloop()
