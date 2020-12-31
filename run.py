import tkinter as tk
from tkinter import ttk
import detect
import tkinter.filedialog as filedialog


LARGEFONT =("Verdana", 26)

class tkinterApp(tk.Tk):

	def __init__(self, *args, **kwargs):

		# __init__ function for class Tk
		tk.Tk.__init__(self, *args, **kwargs)

		# creating a container
		container = tk.Frame(self)
		# container.geometry("960x540+0+0")
		container.pack(fill=None, expand=False)

		container.grid_rowconfigure(0, minsize=540, weight=1)
		container.grid_columnconfigure(0, minsize=960, weight=1)
		btn = tk.Button(self, text="Exit", bg="red", fg="white",command = self.destroy)
		btn.place(relx=1.0, rely=1.0, anchor=tk.SE)
		label = tk.Label(self, text ="Face Mask Detector", font = ("Helvetica 26 bold italic"), fg = "dark green")
		label.pack(side = tk.LEFT)

		# initializing frames to an empty array
		self.frames = {}

		# iterating through a tuple consisting
		# of the different page layouts
		for F in (StartPage, Camera, Link, Videos):

			frame = F(container, self)
			# initializing frame of that object from
			# startpage, Camera, Link respectively with
			# for loop
			self.frames[F] = frame

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(StartPage)

	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

# startpage

class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		# label of frame Layout 2
		label = ttk.Label(self, text ="Main Menu", font = LARGEFONT)

		# putting the grid in its place by using
		# grid
		label.grid(row = 0, column = 0, padx = 10, pady = 10,sticky = tk.W)

		button1 = ttk.Button(self, text ="Camera ID",
		command = lambda : controller.show_frame(Camera))
		button1.grid(row = 1, column = 0, padx = 10, pady = 10,sticky = tk.W)

		button2 = ttk.Button(self, text ="Links: http/rtsp/rtmp",
		command = lambda : controller.show_frame(Link))
		button2.grid(row = 2, column = 0, padx = 10, pady = 10,sticky = tk.W)

		button3 = ttk.Button(self, text ="Videos/Images/Folders",
		command = lambda : controller.show_frame(Videos))
		button3.grid(row = 3, column = 0, padx = 10, pady = 10,sticky = tk.W)




# second window frame Camera
class Camera(tk.Frame):

	def __init__(self, parent, controller):
		def submit():
		    name=name_entry.get()
		    if(name):
		    	detect.run_function(['--source', name])
		    	name_var.set("")

		name_var=tk.StringVar()
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Camera", font = LARGEFONT)
		label.grid(row = 0, column = 0, padx = 10, pady = 10,sticky = tk.W)
		name_label = tk.Label(self, text = '  Camera ID :', font=('calibre',15, 'bold'))
		name_entry = tk.Entry(self,textvariable = name_var,font=('calibre',15,'normal'))
		name_label.grid(row=2,column=0,sticky = tk.W)
		name_entry.grid(row=2,column=1,sticky = tk.W)
		button0 = tk.Button(self, text = 'Submit',command = submit, activebackground='green', activeforeground= 'white')
		button0.grid(row = 2, column = 2, padx = 10, pady = 10,sticky = tk.W)

		# button to show frame 2 with text
		# layout2
		button1 = tk.Button(self, text ="Back to Main Menu",bg="blue", fg="white",
							command = lambda : controller.show_frame(StartPage))
		button1.grid(row = 1, column = 0, padx = 10, pady = 10,sticky = tk.W)


# third window frame Link
class Link(tk.Frame):
	def __init__(self, parent, controller):
		def submit():
		    v1 = v.get()
		    ip1 = ip_var.get()
		    user1 = user_var.get()
		    pass1 = pass_var.get()
		    if v1 and ip1:
		    	if(user1):
		    		detect.run_function(['--source', v1+"://"+user1+":"+pass1+"@"+ip1])
		    	else:
		    		detect.run_function(['--source', v1+"://"+ip1])

		v = tk.StringVar()
		user_var=tk.StringVar()
		pass_var=tk.StringVar()
		ip_var=tk.StringVar()
		values = {"Http" : "http",
		          "Rtsp" : "rtsp",
				  "Rtmp" : "rtmp"}
		tk.Frame.__init__(self, parent)
		# button to show frame 3 with text
		# layout3
		button1 = tk.Button(self, text ="Back to Main Menu",bg="blue", fg="white",
							command = lambda : controller.show_frame(StartPage))
		button1.grid(row = 1, column = 0, padx = 10, pady = 10,sticky = tk.W)
		label = ttk.Label(self, text ="Links", font = LARGEFONT)
		label.grid(row = 0, column = 0, padx = 10, pady = 10,sticky = tk.W)

		for (text, value) in values.items():
		    tk.Radiobutton(self, text = text, variable = v,indicatoron = 0,width = 20,
		                value = value,font=('calibre',15,'normal'),
		                background = "light blue",padx =20).grid(sticky = tk.W)
		ip_label = tk.Label(self, text = 'IP address :', font=('calibre',15, 'bold'))
		ip_entry = tk.Entry(self,textvariable = ip_var,font=('calibre',15,'normal'))
		ip_label.grid(row=2,column=2,sticky = tk.W, padx = 10)
		ip_entry.grid(row=2,column=3,sticky = tk.W)
		user_label = tk.Label(self, text = 'Username :', font=('calibre',15, 'bold'))
		user_entry = tk.Entry(self,textvariable = user_var,font=('calibre',15,'normal'))
		user_label.grid(row=3,column=2,sticky = tk.W, padx = 10)
		user_entry.grid(row=3,column=3,sticky = tk.W)
		pass_label = tk.Label(self, text = 'Password :', font=('calibre',15, 'bold'))
		pass_entry = tk.Entry(self,textvariable = pass_var,font=('calibre',15,'normal'))
		pass_label.grid(row=4,column=2,sticky = tk.W, padx = 10)
		pass_entry.grid(row=4,column=3,sticky = tk.W)
		button0 = tk.Button(self, text = 'Submit',command = submit,bg='green',fg='white',font=('Gothic', '13'), activebackground='#ADD8E6')
		button0.grid(row = 5, column = 2, padx = 10, pady = 10,sticky = tk.W)


# third window frame video
class Videos(tk.Frame):
	def __init__(self, parent, controller):
		def browse_button():
		    filename = tk.filedialog.askopenfilename(title = "Select a Video/Image")
		    self.folder_path.set(filename)
		    if (filename):
			    label_done = tk.Label(self,text = "Processed!!!",
		                            width = 20, height = 5,fg = "green",font=('calibre',15, 'bold'))
			    label_done.grid(row = 40, column = 1,sticky = tk.W)
			    detect.run_function(['--source', filename])

		self.folder_path = tk.StringVar()
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Videos / Images / Folders", font = LARGEFONT)
		label.grid(row = 0, column = 0, padx = 10, pady = 10,sticky = tk.W)
		label_file_explorer = tk.Label(self,text = "Choose Video/Image",
                            width = 30, height = 5,fg = "blue",font=("Helvetica", "16"))
		label_file_explorer.grid(row = 20, column = 0,sticky = tk.W)
		label_warning = tk.Label(self,text = "Please Wait after choosing the file",
                            width = 30, height = 5,fg = "Red")
		label_warning.grid(row = 30, column = 0,sticky = tk.W)

		button3 = tk.Button(self, text ="browse",
							command = browse_button,bg='green',fg='white',font=('Gothic', '13'), activebackground='#ADD8E6',relief=tk.RAISED,cursor="plus")
		button3.grid(row = 20, column = 1,sticky = tk.W)

		# button to show frame 3 with text
		# layout3
		button1 = tk.Button(self, text ="Back to Main Menu",bg="blue", fg="white",
							command = lambda : controller.show_frame(StartPage))
		button1.grid(row = 10, column = 0, padx = 10, pady = 10,sticky = tk.W)



# Driver Code
app = tkinterApp()
app.mainloop()
