import pickle
import tkinter
from tkinter import *
from PIL import Image as PilImage
from PIL import ImageTk

class ChildWindow:
	def __init__(self, parent, width, height, title='AKYPOK', resizable=(False, False), icon=None):
		self.root = Toplevel(parent)
		self.root.title(title)
		self.root.resizable(resizable[0], resizable[1])
		self.root.geometry(f"{width}x{height}+200+200")
		if icon is not None:
			self.root.iconbitmap(icon)

		self.grab_focus()

	def grab_focus(self):
		self.root.grab_set()
		self.root.focus_set()
		self.root.wait_window()
