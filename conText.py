from tkinter import *
from tkinter.filedialog import askopenfilename
import re
import re
import webbrowser
import xml_parser as xp
import detect
import builtins
import ActivityIndicator as ai
import threading

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500

root = Tk()
root.wm_title("conText by EXZACKLY and ZENO")
root.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)

def print(*args, **kwargs):
	outputTextarea.configure(state="normal")
	outputTextarea.insert(INSERT, *args)
	outputTextarea.insert(INSERT, "\n")
	outputTextarea.configure(state="disabled")
	return builtins.print(*args, **kwargs)
	
def getFile():
	#show activity indicator
	root.a = ai.Activity(root, 500, bg = "gray", height=2, width=5)
	root.a.pack()
	root.a.place(bordermode=OUTSIDE, x = 220, y = 200)
	root.a.start()
	
	filename = askopenfilename()
	name = re.search("/.*/(.*?)\.htm", filename).group(1)
	print("Training neural network...")
	threading.Thread(target=detect.train, args=(name,)).start()
	print("Training completed.")
	
	#stop activity indicator
	root.after(5000, root.a.stop)

def exitProgram():
	root.destroy()

def displayHelp():
	webbrowser.open("https://github.com/exzackly/conText", new=2)

def displayResults(percent):
	toplevel = Toplevel()
	print("Computing cross entropy.")	
	cross_entropy = detect.test(inputTextarea.get("1.0",END))
	label = Label(toplevel, text="cross entropy {0}".format(cross_entropy), height=0, width=50)
	label.pack()
	toplevel.focus()
	
#create menu
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open...", command=getFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exitProgram)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Documentation...", command=displayHelp)

#create header label
headerLabel = Label(root, text="Enter Text To Compare:", font=("Helvetica", 21))
headerLabel.pack()
headerLabel.place(bordermode=OUTSIDE, x = 30, y = 15)

#create textarea
inputTextarea = Text(root, height = 10, width = 54)
inputTextarea.pack()
inputTextarea.place(bordermode=OUTSIDE, x = 30, y = 50)

#create output textarea
outputTextarea = Text(root, state=DISABLED, height = 10, width = 54, bg="lightGray")
outputTextarea.pack()
outputTextarea.place(bordermode=OUTSIDE, x = 30, y = 230)

#create compare button
compareButton = Button(root, text="Compare Text", command=lambda: displayResults(21))
compareButton.pack()
compareButton.place(bordermode=OUTSIDE, x = 200, y = 410)

#create result label
resultLabel = Label(root, text="", font=("Helvetica", 21))
resultLabel.pack()
resultLabel.place(bordermode=OUTSIDE, x = 30, y = 450)

root.mainloop()
