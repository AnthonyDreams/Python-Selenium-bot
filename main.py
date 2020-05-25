import sys
import os
import threading
import time
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog

from tkinter import ttk
from ttkthemes import themed_tk as tk
import threading
from mutagen.mp3 import MP3
from pygame import mixer
import bot
from datetime import datetime, timedelta

def main():
	root = tk.ThemedTk()
	root.get_themes()                
	root.set_theme("radiance")       


	statusbar = ttk.Label(root, text="Bienvenido al bot", relief=SUNKEN, anchor=W, font='Times 10 italic')
	statusbar.pack(side=BOTTOM, fill=X)

	# Create the menubar
	menubar = Menu(root)
	root.config(menu=menubar)


	subMenu = Menu(menubar, tearoff=0)

	playlist = []
	global run
	date = None
	count = 0
	with open('count.txt', 'r') as count_:
			count = int(count_.readline());
	def Check():
		with open('today.txt', 'r+') as date_:
			fecha = date_.readline()
			if len(fecha) == 0:
				date_.write(str(datetime.now()))
			else:
				date = fecha
				short = date.split()[0].split('-')
				time =  date.split()[1].split(':')
				short = [int(a) for a in short]
				time = [int(float(c)) for c in time]
				if datetime.now() - timedelta(1) <= datetime(short[0], short[1], short[2], time[0], time[1], time[2]):
					if(count % 25 != 0):
						globals()['run'] = True
					else:
						globals()['run'] = False
				else:
					if datetime.now() - timedelta(1) >= datetime(short[0], short[1], short[2], time[0], time[1], time[2]) or count % 25 == 0:
						date_.seek(0)
						date_.write(str(datetime.now()))
						date_.truncate()
						globals()['run'] = True
					else:

						globals()['run'] = False
						print(run)



	def stopBot():
		
		bot.CloseChrome()

	def browse_file():
		bot.Chrome()
		try:
			Check()
			while globals()['run']:
				bot.main()
				Check()
				time.sleep(60)
			if globals()['run'] == False:
				bot.Finalizado()
				stopBot()

				
		except Exception as e:
			bot.exception()

	def startBot(Stop=None):
		t1 = threading.Thread(target=browse_file, args=[])
		t1.setDaemon(True)

		t1.start()





	def about_us():
		tkinter.messagebox.showinfo('Bot Buyer', 'this is a bot made using Python Tkinter and selenium by @theanthony2d')




	mixer.init()  

	root.title("Bot")
	root.iconbitmap(r'images/robot.ico')



	leftframe = Frame(root)
	leftframe.pack(side=LEFT, padx=30, pady=30)

	playlistbox = Listbox(leftframe)
	playlistbox.pack()

	addBtn = ttk.Button(leftframe, text="+ Comenzar", command=startBot)
	addBtn.pack(side=LEFT)





	delBtn = ttk.Button(leftframe, text="- Parar", command=stopBot)
	delBtn.pack(side=LEFT)

	rightframe = Frame(root)
	rightframe.pack(pady=30)

	topframe = Frame(rightframe)
	topframe.pack()







	middleframe = Frame(rightframe)
	middleframe.pack(pady=30, padx=30)


	bottomframe = Frame(rightframe)
	bottomframe.pack()

	if(len(sys.argv) == 2):
		startBot()


	def on_closing():
		root.destroy()


	root.protocol("WM_DELETE_WINDOW", on_closing)
	root.mainloop()


if __name__ == '__main__':
    main()