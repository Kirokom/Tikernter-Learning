#  add tkinter all method module or class 
from tkinter import *  

# instalization tk all class 
window = Tk()

# widter and attruibutes 

# ----------for window tittle chnage 
window.title("Cicle Auto Mation")

# for window icon change 
window.iconbitmap(r'C:\Users\EMONALi\Desktop\Web site making\Tkinter/facebook_icon_161067.ico') 

# ----------for Transparent the window -->
window.attributes("-alpha" , 1)
# -alpha means transparent and transParent parcent goes to 0 to 1  

#----------------- Background Color change 
# window.config(bg="orange")

window['bg']="green"

window.mainloop() #  to run the desktop gui it loop contuies to  run the applicationn 




