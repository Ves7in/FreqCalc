#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Test platforms:
#  + macOS
#    - release: macOS 10.15.5 (Catalina)
#    - python:  Python 3.10.1
#    - require: (None)
#  + Windows
#    - release: Windows 7 Ultimate (SP1)
#    - python:  Python 2.7.18
#    - require: (None)
#  + Linux
#    - release: RHEL Server 6.10 (Santiago)
#    - python:  Python 2.6.6
#    - require: tkinter

import os, sys
from os import path

if sys.version_info[0] == 2:  # Python 2.x
	from Tkinter import *
	import Tkinter as tk
	from tkFont import Font
else:                         # Python 3.x
	from tkinter import *
	import tkinter as tk
	from tkinter.font import Font

from platform import system
_platform = system()
if _platform == 'Darwin':
	import subprocess
elif _platform == 'Windows':
	import win32con, win32clipboard
elif _platform == 'Linux':
	import gtk
else:
	pass

# -App details
_appTitle   = 'FreqCalc'
_appVersion = '0.1.3'
_appRights  = ['2021', 'Vestin', 'All rights reserved.']
_appIcon    = {'Darwin'  : './src/FreqCalc.icns',
               'Windows' : './src/FreqCalc.ico',
               'Linux'   : './src/FreqCalc.xbm',}

# -Path to the program
_bundleDir = sys._MEIPASS if getattr(sys, 'frozen', False) else os.path.dirname(os.path.abspath(__file__))

class AppUI(Frame):
	# The class will create all widgets for UI.
	def __init__(self, master=None):
		Frame.__init__(self, master)

		# -Application window initialize
		self.master.title(_appTitle+' - v'+_appVersion)  # Set title
		self.master.geometry('232x376')                  # Set window size
		self.master.resizable(0,0)                       # Set window unresizable
		self.master.iconbitmap(self.appIcon)             # Set icon

		# -Load resources
		self.imgBtnCpy = PhotoImage(file=Utils.src('./src/COPY.gif'))

		# -Get everything ready
		self.createWidgets()                             # Create widgets

	def createWidgets(self):
		self.root = self.winfo_toplevel()
		if _platform == 'Darwin':  # For better look on macOS
			fraFont = Font(font=('苹方',12))
			txtFont = Font(font=('苹方',10))
			lblFont = Font(font=('苹方',10))
			cboFont = Font(font=('苹方',10))
		else:
			fraFont = Font(font=('宋体',9))
			txtFont = Font(font=('宋体',9))
			lblFont = Font(font=('宋体',9))
			cboFont = Font(font=('宋体',9))

		# =============================================
		# [                Frame Input                ]
		# =============================================
		fraInput = LabelFrame(self.root, text='频率/周期输入', font=fraFont)
		fraInput.place(x=8, y=8, width=217, height=49)

		self.txtInVar = StringVar(value='')
		self.txtIn = Entry(fraInput, textvariable=self.txtInVar, font=txtFont, bd=2, justify=tk.RIGHT)
		self.txtIn.setText = lambda x: self.txtInVar.set(x)
		self.txtIn.text = lambda : self.txtInVar.get()
		self.txtIn.place(x=8, y=2, width=145, height=25)
		self.txtInVar.trace(tk.W, self.Input_Change)

		self.cboUnitList = ('Hz','kHz','MHz','GHz','THz','s','ms','us','ns','ps',)
		self.cboUnitVar = StringVar(value=self.cboUnitList[0])
		self.cboUnit = OptionMenu(fraInput, self.cboUnitVar, *self.cboUnitList)
		self.cboUnit.configure(takefocus=1, font=cboFont)
		self.cboUnit.option = lambda : self.cboUnitVar.get()
		self.cboUnit.place(x=152, y=2, width=59, height=25)
		self.cboUnitVar.trace(tk.W, self.Input_Change)

		# -(Break)
		sep = Label(self.root, text='', bd=1, relief=tk.GROOVE)
		sep.place(x=8, y=64, width=216, height=2)

		# =============================================
		# [               Frame frq out               ]
		# =============================================
		fraRsltFrq = LabelFrame(self.root, text='频率转换结果', font=fraFont)
		fraRsltFrq.place(x=8, y=72, width=217, height=137)

		# -Hz
		self.txtRsltHzVar = StringVar(value='')
		self.txtRsltHz = Entry(fraRsltFrq, readonlybackground='#E0E0E0', state='readonly', textvariable=self.txtRsltHzVar, font=txtFont, bd=2, justify=tk.RIGHT)
		self.txtRsltHz.setText = lambda x: self.txtRsltHzVar.set(x)
		self.txtRsltHz.text = lambda : self.txtRsltHzVar.get()
		self.txtRsltHz.place(x=8, y=2, width=145, height=18)

		lblUnitHz = Label(fraRsltFrq, text='Hz', anchor=tk.W, font=lblFont)
		lblUnitHz.place(x=157, y=4, width=25, height=13)

		btnCpyHz = Button(fraRsltFrq, image=self.imgBtnCpy, command=self.btnCpyHz_Cmd)
		btnCpyHz.place(x=192, y=2, width=17, height=17)

		# -kHz
		self.txtRsltkHzVar = StringVar(value='')
		self.txtRsltkHz = Entry(fraRsltFrq, readonlybackground='#E0E0E0', state='readonly', textvariable=self.txtRsltkHzVar, font=txtFont, bd=2, justify=tk.RIGHT)
		self.txtRsltkHz.setText = lambda x: self.txtRsltkHzVar.set(x)
		self.txtRsltkHz.text = lambda : self.txtRsltkHzVar.get()
		self.txtRsltkHz.place(x=8, y=26, width=145, height=18)

		lblUnitkHz = Label(fraRsltFrq, text='kHz', anchor=tk.W, font=lblFont)
		lblUnitkHz.place(x=157, y=28, width=25, height=13)

		btnCpykHz = Button(fraRsltFrq, image=self.imgBtnCpy, command=self.btnCpykHz_Cmd)
		btnCpykHz.place(x=192, y=26, width=17, height=17)

		# -Mhz
		self.txtRsltMHzVar = StringVar(value='')
		self.txtRsltMHz = Entry(fraRsltFrq, readonlybackground='#E0E0E0', state='readonly', textvariable=self.txtRsltMHzVar, font=txtFont, bd=2, justify=tk.RIGHT)
		self.txtRsltMHz.setText = lambda x: self.txtRsltMHzVar.set(x)
		self.txtRsltMHz.text = lambda : self.txtRsltMHzVar.get()
		self.txtRsltMHz.place(x=8, y=50, width=145, height=18)

		lblUnitMHz = Label(fraRsltFrq, text='Mhz', anchor=tk.W, font=lblFont)
		lblUnitMHz.place(x=157, y=52, width=25, height=13)

		btnCpyMhz = Button(fraRsltFrq, image=self.imgBtnCpy, command=self.btnCpyMhz_Cmd)
		btnCpyMhz.place(x=192, y=50, width=17, height=17)

		# -GHz
		self.txtRsltGHzVar = StringVar(value='')
		self.txtRsltGHz = Entry(fraRsltFrq, readonlybackground='#E0E0E0', state='readonly', textvariable=self.txtRsltGHzVar, font=txtFont, bd=2, justify=tk.RIGHT)
		self.txtRsltGHz.setText = lambda x: self.txtRsltGHzVar.set(x)
		self.txtRsltGHz.text = lambda : self.txtRsltGHzVar.get()
		self.txtRsltGHz.place(x=8, y=74, width=145, height=18)

		lblUnitGHz = Label(fraRsltFrq, text='GHz', anchor=tk.W, font=lblFont)
		lblUnitGHz.place(x=157, y=76, width=25, height=13)

		btnCpyGHz = Button(fraRsltFrq, image=self.imgBtnCpy, command=self.btnCpyGHz_Cmd)
		btnCpyGHz.place(x=192, y=74, width=17, height=17)

		# -THz
		self.txtRsltTHzVar = StringVar(value='')
		self.txtRsltTHz = Entry(fraRsltFrq, readonlybackground='#E0E0E0', state='readonly', textvariable=self.txtRsltTHzVar, font=txtFont, bd=2, justify=tk.RIGHT)
		self.txtRsltTHz.setText = lambda x: self.txtRsltTHzVar.set(x)
		self.txtRsltTHz.text = lambda : self.txtRsltTHzVar.get()
		self.txtRsltTHz.place(x=8, y=98, width=145, height=18)

		lblUnitTHz = Label(fraRsltFrq, text='THz', anchor=tk.W, font=lblFont)
		lblUnitTHz.place(x=157, y=100, width=25, height=13)

		btnCpyTHz = Button(fraRsltFrq, image=self.imgBtnCpy, command=self.btnCpyTHz_Cmd)
		btnCpyTHz.place(x=192, y=98, width=17, height=17)

		# =============================================
		# [               Frame ped out               ]
		# =============================================
		fraRsltPed = LabelFrame(self.root, text='周期转换结果', font=fraFont)
		fraRsltPed.place(x=8, y=216, width=217, height=137)

		# -s
		self.txtRsltsVar = StringVar(value='')
		self.txtRslts = Entry(fraRsltPed, readonlybackground='#E0E0E0', state='readonly', textvariable=self.txtRsltsVar, font=txtFont, bd=2, justify=tk.RIGHT)
		self.txtRslts.setText = lambda x: self.txtRsltsVar.set(x)
		self.txtRslts.text = lambda : self.txtRsltsVar.get()
		self.txtRslts.place(x=8, y=2, width=145, height=18)

		lblUnits = Label(fraRsltPed, text='s', anchor=tk.W, font=lblFont)
		lblUnits.place(x=157, y=4, width=25, height=13)

		btnCpys = Button(fraRsltPed, image=self.imgBtnCpy, command=self.btnCpys_Cmd)
		btnCpys.place(x=192, y=2, width=17, height=17)

		# -ms
		self.txtRsltmsVar = StringVar(value='')
		self.txtRsltms = Entry(fraRsltPed, readonlybackground='#E0E0E0', state='readonly', textvariable=self.txtRsltmsVar, font=txtFont, bd=2, justify=tk.RIGHT)
		self.txtRsltms.setText = lambda x: self.txtRsltmsVar.set(x)
		self.txtRsltms.text = lambda : self.txtRsltmsVar.get()
		self.txtRsltms.place(x=8, y=26, width=145, height=18)

		lblUnitms = Label(fraRsltPed, text='ms', anchor=tk.W, font=lblFont)
		lblUnitms.place(x=157, y=28, width=25, height=13)

		btnCpyms = Button(fraRsltPed, image=self.imgBtnCpy, command=self.btnCpyms_Cmd)
		btnCpyms.place(x=192, y=26, width=17, height=17)

		# -us
		self.txtRsltusVar = StringVar(value='')
		self.txtRsltus = Entry(fraRsltPed, readonlybackground='#E0E0E0', state='readonly', textvariable=self.txtRsltusVar, font=txtFont, bd=2, justify=tk.RIGHT)
		self.txtRsltus.setText = lambda x: self.txtRsltusVar.set(x)
		self.txtRsltus.text = lambda : self.txtRsltusVar.get()
		self.txtRsltus.place(x=8, y=50, width=145, height=18)

		lblUnitus = Label(fraRsltPed, text='us', anchor=tk.W, font=lblFont)
		lblUnitus.place(x=157, y=52, width=25, height=13)

		btnCpyus = Button(fraRsltPed, image=self.imgBtnCpy, command=self.btnCpyus_Cmd)
		btnCpyus.place(x=192, y=50, width=17, height=17)

		# -ns
		self.txtRsltnsVar = StringVar(value='')
		self.txtRsltns = Entry(fraRsltPed, readonlybackground='#E0E0E0', state='readonly', textvariable=self.txtRsltnsVar, font=txtFont, bd=2, justify=tk.RIGHT)
		self.txtRsltns.setText = lambda x: self.txtRsltnsVar.set(x)
		self.txtRsltns.text = lambda : self.txtRsltnsVar.get()
		self.txtRsltns.place(x=8, y=74, width=145, height=18)

		lblUnitns = Label(fraRsltPed, text='ns', anchor=tk.W, font=lblFont)
		lblUnitns.place(x=157, y=76, width=25, height=13)

		btnCpyns = Button(fraRsltPed, image=self.imgBtnCpy, command=self.btnCpyns_Cmd)
		btnCpyns.place(x=192, y=74, width=17, height=17)

		# -ps
		self.txtRsltpsVar = StringVar(value='')
		self.txtRsltps = Entry(fraRsltPed, readonlybackground='#E0E0E0', state='readonly', textvariable=self.txtRsltpsVar, font=txtFont, bd=2, justify=tk.RIGHT)
		self.txtRsltps.setText = lambda x: self.txtRsltpsVar.set(x)
		self.txtRsltps.text = lambda : self.txtRsltpsVar.get()
		self.txtRsltps.place(x=8, y=98, width=145, height=18)

		lblUnitps = Label(fraRsltPed, text='ps', anchor=tk.W, font=lblFont)
		lblUnitps.place(x=157, y=100, width=25, height=13)

		btnCpyps = Button(fraRsltPed, image=self.imgBtnCpy, command=self.btnCpyps_Cmd)
		btnCpyps.place(x=192, y=98, width=17, height=17)

		# =============================================
		# |               Copyright bar               |
		# =============================================
		lblBar = Label(self.root, text=' '+_appRights[0]+' '+_appRights[1]+' | '+_appRights[2], font=lblFont, bd=1, relief=tk.SUNKEN, justify=tk.CENTER)
		lblBar.pack(side=tk.BOTTOM, fill=tk.X)
		lblBar.bind('<Button-1>', self.lblBar_Click)

class AboutDialog(Toplevel):
	# The class will create all widgets for about form UI.
	def __init__(self, master=None):
		self.master = master
		self.takefocus = True

		self.dlgIcon    = None              # String, path of icns/ico/xbm
		self.appIcon    = None              # PhotoImage, size 32x32
		self.appTitle   = 'App Title'       # String
		self.appVersion = 'App Version'     # String
		self.appRights  = 'Copyrights...'   # String

	def createWidgets(self):
		# -App icon
		appIcon = Label(self, anchor=tk.CENTER, image=self.appIcon, relief=SUNKEN, bd='2')
		appIcon.place(x=72, y=16, width=36, height=36)

		# -App title
		appTitleFont = Font(font=('宋体',10,'bold'))
		appTitle = Label(self, text=self.appTitle, anchor=tk.CENTER, font=appTitleFont)
		appTitle.place(x=8, y=63, width=161, height=16)

		# -App version
		appVersionFont = Font(font=('宋体',9))
		appVersion = Label(self, text=self.appVersion, anchor=tk.CENTER, font=appVersionFont)
		appVersion.place(x=8, y=86, width=161, height=15)

		# -(Break)
		sep = Label(self, text='', bd=1, relief=tk.GROOVE)
		sep.place(x=8, y=112, width=161, height=2)

		# -Copyrights...
		appRightsFont = Font(font=('宋体',9))
		appRights = Label(self, text=self.appRights, anchor=tk.CENTER, font=appRightsFont)
		appRights.place(x=8, y=117, width=162, height=31)

	# To pop up dialog after setting up 
	def popUp(self):
		Toplevel.__init__(self, self.master)
		self.transient(self.master)

		# -Dialog window initialize
		self.title('About '+self.appTitle)  # Set title
		self.geometry('177x156+153+104')    # Set window size
		self.resizable(0,0)                 # Set window unresizable
		self.iconbitmap(self.dlgIcon)       # Set icon

		# -Get everything ready
		self.createWidgets()
		self.wait_visibility()
		if sys.version_info[0] == 2:  # Python 2.x
			self.grab_set()
		else:                         # Python 3.x
			self.grab_set_global()
		self.focus_set()

class Utils:
	# The class implements utils.

	# --------------------
	# src()
	# + Get resource path.
	# --------------------
	@staticmethod
	def src(resource):
		return path.join(_bundleDir, resource)

	# --------------------
	# RefreshRslt()
	# + Refresh results.
	# --------------------
	@staticmethod
	def RefreshRslt(master):
		print("RefreshRslt:", master.txtIn.text(), master.cboUnit.option()) # *debug
		Input = float(master.txtIn.text())
		InputInit = {
			'Hz'  : [lambda x: x              , lambda x: 1/x             ],
			'kHz' : [lambda x: x*1000         , lambda x: 0.001/x         ],
			'MHz' : [lambda x: x*1000000      , lambda x: 0.000001/x      ],
			'GHz' : [lambda x: x*1000000000   , lambda x: 0.000000001/x   ],
			'THz' : [lambda x: x*1000000000000, lambda x: 0.000000000001/x],

			's'   : [lambda x: 1/x            , lambda x: x               ],
			'ms'  : [lambda x: 1000/x         , lambda x: x/1000          ],
			'us'  : [lambda x: 1000000/x      , lambda x: x/1000000       ],
			'ns'  : [lambda x: 1000000000/x   , lambda x: x/1000000000    ],
			'ps'  : [lambda x: 1000000000000/x, lambda x: x/1000000000000 ],
		}

		RsltByHz  = float(InputInit[master.cboUnit.option()][0](Input))
		RsltBySec = float(InputInit[master.cboUnit.option()][1](Input))

		master.txtRsltHz.setText(Utils.getFormattedResult(RsltByHz))
		master.txtRsltkHz.setText(Utils.getFormattedResult(RsltByHz / 1000))
		master.txtRsltMHz.setText(Utils.getFormattedResult(RsltByHz / 1000000))
		master.txtRsltGHz.setText(Utils.getFormattedResult(RsltByHz / 1000000000))
		master.txtRsltTHz.setText(Utils.getFormattedResult(RsltByHz / 1000000000000))

		master.txtRslts.setText(Utils.getFormattedResult(RsltBySec))
		master.txtRsltms.setText(Utils.getFormattedResult(RsltBySec * 1000))
		master.txtRsltus.setText(Utils.getFormattedResult(RsltBySec * 1000000))
		master.txtRsltns.setText(Utils.getFormattedResult(RsltBySec * 1000000000))
		master.txtRsltps.setText(Utils.getFormattedResult(RsltBySec * 1000000000000))

	# --------------------
	# CpyRslt()
	# + Copy results.
	# --------------------
	@staticmethod
	def CpyRslt(rslt):
		print("CpyRslt:", rslt) # *debug
		if _platform == 'Darwin':
			p=subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
			p.stdin.write(rslt.encode('utf-8'))
			p.stdin.close()
			p.communicate()
		elif _platform == 'Windows':
			win32clipboard.OpenClipboard()
			win32clipboard.EmptyClipboard()
			win32clipboard.SetClipboardData(win32con.CF_TEXT, rslt)
			win32clipboard.CloseClipboard()
		elif _platform == 'Linux':
			clipboard = gtk.clipboard_get()
			clipboard.set_text(rslt)
			clipboard.store()
		else:
			pass

	# --------------------
	# RstRslt()
	# + Reset results.
	# --------------------
	@staticmethod
	def RstRslt(master):
		master.txtRsltHz.setText('0')
		master.txtRsltkHz.setText('0')
		master.txtRsltMHz.setText('0')
		master.txtRsltGHz.setText('0')
		master.txtRsltTHz.setText('0')

		master.txtRslts.setText('0')
		master.txtRsltms.setText('0')
		master.txtRsltus.setText('0')
		master.txtRsltns.setText('0')
		master.txtRsltps.setText('0')

	# --------------------
	# getFormattedResult()
	# + Return formatted
	#   float as string.
	# --------------------
	@staticmethod
	def getFormattedResult(floatNum):
		floatStr = "{0:.15g}".format(floatNum)
		isNeg = False
		rsltStr = ''

		# If is not by scientific notation
		if not 'e' in floatStr:
			return floatStr

		# If is over max length
		if len(floatStr) >= 20:
			return floatStr

		# If is negative
		if floatNum < 0:
			floatStr = floatStr[1:]
			isNeg = True 

		splitStr = floatStr.split('e')
		coefStr = str(splitStr[0])
		expNum = int(splitStr[1])

		if expNum > 0:
			rsltStr += coefStr.replace('.', '')
			rsltStr += ''.join(['0' for _ in range(0, abs(expNum - (len(coefStr.split('.')[1]) if '.' in coefStr else 0)))])
		elif expNum < 0:
			rsltStr += '0.'
			rsltStr += ''.join(['0' for _ in range(0, abs(expNum) - 1)])
			rsltStr += coefStr.replace('.', '')

		# If is over max length
		if len(rsltStr) > 20:
			return floatStr
		return rsltStr if not isNeg else '-' + rsltStr

class Application(AppUI, AboutDialog):
	# The class implements callback function for events and logical code.
	def __init__(self, master=None):
		# -Load app icon
		self.appIcon = Utils.src(_appIcon[_platform])
		if _platform == 'Linux':
			self.appIcon = '@' + self.appIcon

		# -UI initialize
		AppUI.__init__(self, master)
		Utils.RstRslt(self)
		self.txtIn.focus_set()

	# -Input callback
	def Input_Change(self, *args):
		try:
			1/float(self.txtIn.text())
		except ValueError:
			if self.txtIn.text() == '':
				print("ValueError: Void input!") # *debug
				self.txtIn['bg'] = '#FFFFFF'
			else:
				print("ValueError: Illegal input!") # *debug
				self.txtIn['bg'] = '#FFC0C0'
			Utils.RstRslt(self)
		except ZeroDivisionError:
			print("ZeroDivisionError: Nothing to do!") # *debug
			self.txtIn['bg'] = '#FFFFFF'
			Utils.RstRslt(self)
		else:
			self.txtIn['bg'] = '#FFFFFF'
			Utils.RefreshRslt(self)

	# -Copy buttons callback
	def btnCpyTHz_Cmd(self, event=None):
		Utils.CpyRslt(self.txtRsltTHz.text())

	def btnCpyGHz_Cmd(self, event=None):
		Utils.CpyRslt(self.txtRsltGHz.text())

	def btnCpyMhz_Cmd(self, event=None):
		Utils.CpyRslt(self.txtRsltMHz.text())

	def btnCpykHz_Cmd(self, event=None):
		Utils.CpyRslt(self.txtRsltkHz.text())

	def btnCpyHz_Cmd(self, event=None):
		Utils.CpyRslt(self.txtRsltHz.text())

	def btnCpyps_Cmd(self, event=None):
		Utils.CpyRslt(self.txtRsltps.text())

	def btnCpyns_Cmd(self, event=None):
		Utils.CpyRslt(self.txtRsltns.text())

	def btnCpyus_Cmd(self, event=None):
		Utils.CpyRslt(self.txtRsltus.text())

	def btnCpyms_Cmd(self, event=None):
		Utils.CpyRslt(self.txtRsltms.text())

	def btnCpys_Cmd(self, event=None):
		Utils.CpyRslt(self.txtRslts.text())

	# -Copyright bar callback
	def lblBar_Click(self, event=None):
		icon_x32 = PhotoImage(file=Utils.src('./src/FreqCalc_x32.gif'))
		d = AboutDialog()
		d.dlgIcon = self.appIcon
		d.appIcon = icon_x32
		d.appTitle = _appTitle
		d.appVersion = 'Version ' + _appVersion
		d.appRights = 'Copyright(C) '+_appRights[0]+' '+_appRights[1]+'.\n'+_appRights[2]
		d.popUp() # Popup about dialog
		self.wait_window(d)

if __name__ == "__main__":
	root = Tk()
	Application(root).mainloop()

