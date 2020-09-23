from tkinter import *

class Frames:

	def makeFrame(self):
		root = Tk(className="X Name")
		root.title("X title")
		root.geometry("900x900")
		root.resizable(0,0)


		def raise_frame(frame):
			frame.tkraise()

		frame1 = Frame(root, width=600)
		frame2 = Frame(root)

		for frame in (frame1,frame2):
			frame.grid(row=0, column=0, padx=50, pady=200, sticky='news')


		Label(frame1, text='Welcome to tkinter Frames',font=("Courier",40)).pack()
		Button(frame1, text="Frame 2", width=10,height=2, font=("Courier", 30), command=lambda:raise_frame(frame2)).pack(pady=10)

		Label(frame2, text='Frame 2', font=("Courier",40)).pack()
		Button(frame2, text="Frame 1",width=10,height=2, font=("Courier", 30), command=lambda:raise_frame(frame1)).pack(pady=10)

		raise_frame(frame1)
		root.mainloop()

frame = Frames().makeFrame()
