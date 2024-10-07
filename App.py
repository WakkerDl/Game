from tkinter import * 
from PIL import ImageTk, Image
import sys
import sched, time


def switch():
    root.withdraw()
    root2.deiconify()
    
def switchBack1():
    root2.withdraw()
    root.deiconify()

def exitWindow():
    sys.exit()



root = Tk()
root2 = Tk()

canvas = Canvas(root, width=500, height=500, background="white")
canvas.place(x=0, y=100)

root['bg'] = '#fafafa'
root.title('Cock')
root.wm_attributes('-alpha', 1)
root.geometry('500x750')
root.resizable(width=False, height=False)

root2.title('Penis')
root2.geometry('500x500')

imageExit = ImageTk.PhotoImage(file='Exit.png')
picture = Image.open("Wheel.png")
picture = picture.resize((500,500))
imageWheel = ImageTk.PhotoImage(picture)
canvas.create_image(1,1, anchor=NW, image=imageWheel)


throttle = Scale(root, from_=0, to=100, orient=HORIZONTAL)
throttle.pack()

btn = Button(text='List', bg='green', width=30, command=switch)
btn.pack()

btnExit = Button(root, image=imageExit, height=30, width=30, text=exit, command=exitWindow)
btnExit.place(x=0, y=0)

btnBack = Button(root2, text='Back', bg='green', width=30, command=switchBack1)
btnBack.pack()

btnSelectEngine = Button(root2, text='I4', bg='Red', width=30)
btnSelectEngine.pack()



root2.withdraw()
root.mainloop()

while True:
    throttle.get()
    picture = picture.rotate(angle=50)
    time.sleep(0.5)
