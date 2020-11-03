import pickle
import tkinter
from tkinter import *
from child_window import ChildWindow
from PIL import Image as PilImage
from PIL import ImageTk

class Window:
	def __init__(self, width, height, title='AKYPOK', resizable=(False, False), icon=r'resources/AKYPOK.ico'):
		self.root = Tk()
		self.root.title(title)
		self.root.resizable(resizable[0], resizable[1])
		self.root.geometry(f"{width}x{height}+200+200")
		if icon:
			self.root.iconbitmap(icon)


		#img = PilImage.open(r'resources/AKYPOK.png')
		#img = img.resize((20, 20), PilImage.ANTIALIAS)
		#self.photo_image = ImageTk.PhotoImage(img)
		
		img1 = PilImage.open(r'resources/leave.png')
		img1 = img1.resize((25, 25), PilImage.ANTIALIAS)
		self.photo_image1 = ImageTk.PhotoImage(img1)

		# text='Твой текст' ; bg='цвет фона' ; relief=Вид текста ; wraplength=ширина строки ; font='Название шрифта  Размер'
		#self.label = Label(self.root, text="Some", bg='#a4a', relief=FLAT, wraplength=0, font='Consolas 15')
		
		# Форматы изображения - .pgm, .ppm, .gif, .png
		#self.face_image = PhotoImage(file=r'resources/AKYPOK.png')
		#self.label = Label(self.root, image=self.face_image)
		#self.label.image = self.face_image

	def AddNumber(self):
		Window.create_child(self, 400, 200)

	def run(self):
		self.draw_widgets()
		self.root.mainloop()

	def draw_widgets(self):
		#Button(self.root, width=30, height=5, text='Жмяк!', relief=GROOVE, bd=8).pack()
		#Button(self.root, width=30, text='Жмык', font=('Consolas', 10, 'bold'), wraplength=15, justify=LEFT, underline=0).pack()
		
		Button(self.root, image=self.photo_image1, command=self.root.destroy).pack(anchor=E)
		#Button(self.root, image=self.photo_image, command=self.Show_number).pack()

		# text='Текст' ; bg=Фон ; fg=Цвет текста ; activebackground='Фон при нажатии'
		Button(self.root, text="Добавить", bg='black', fg='white', activebackground="cyan", activeforeground='black', command=self.AddNumber).pack()

		# Frame()
		#top_frame = Frame(self.root)
		#bottom_frame = Frame(self.root)
		#top_frame.pack()
		#bottom_frame.pack()

		# LabelFrame()
		#top_frame = LabelFrame(self.root, text='First')
		#bottom_frame = LabelFrame(self.root, text='Second')
		#top_frame.pack()
		#bottom_frame.pack()


		#self.label.pack(anchor=NW, padx=20, pady=100)
		# метод pack()
		#Label(top_frame, width=30, height=2, bg='red', text='First').pack(side=LEFT)
		#Label(top_frame, width=30, height=2, bg='yellow', text='Second').pack(side=LEFT)
		#Label(bottom_frame, width=30, height=2, bg='cyan', text='Third').pack(side=LEFT)
		#Label(bottom_frame, width=30, height=2, bg='green', text='Fourth').pack(side=LEFT)

		# Frame()
		#f = Frame(self.root)
		#f.pack()

	def Show_number(self):
		print('Вася Пупкин : 89898989')

	def create_child(self, width, height, title='AKYPOK/cld', resizable=(False, False), icon=None):
		ChildWindow(self.root, width, height, title, resizable, icon)

if __name__ == '__main__':
	
	window = Window(500, 500, 'AKYPOK')
	#window.create_child(200, 100)
	window.run()
