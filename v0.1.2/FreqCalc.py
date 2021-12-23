#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
from os import path

if sys.version_info[0] == 2:
	from Tkinter import *
	import Tkinter as tk
	from tkFont import Font
	from ttk import Separator
else:  #Python 3.x
	from tkinter import *
	import tkinter as tk
	from tkinter.font import Font
	from tkinter.ttk import Separator

from platform import system
platformD = system()
if platformD == 'Darwin':
	import subprocess
elif platformD == 'Windows':
	import win32con, win32clipboard
else:
	pass

# Path to the program
bundleDir = sys._MEIPASS if getattr(sys, 'frozen', False) else os.path.dirname(os.path.abspath(__file__))

class AppUI(Frame):
	# The class will create all widgets for UI.
	def __init__(self, master=None):
		Frame.__init__(self, master)

		# -Application window initialize
		self.master.title('FreqCalc - v0.1.2')	# Set title
		self.master.geometry('232x376')			# Set window size
		self.master.resizable(0,0)				# Set window unresizable
		self.master.iconbitmap(self.appIcon)	# Set icon

		# -Load resources
		self.imgBtnCpy = PhotoImage(file=Utils.src('./src/COPY.gif'))

		# -Get everything ready
		self.createWidgets()					# Create widgets

	def createWidgets(self):
		self.root = self.winfo_toplevel()
		self.fraFont = Font(font=('宋体',9))
		self.txtFont = Font(font=('宋体',9))
		self.lblFont = Font(font=('宋体',9))
		self.cboFont = Font(font=('宋体',9))
		self.btnFont = Font(font=('宋体',9))

		# =============================================
		# [                Frame Input                ]
		# =============================================
		self.fraInput = LabelFrame(self.root, text='频率/周期输入', font=self.fraFont)
		self.fraInput.place(x=8, y=8, width=217, height=49)

		self.txtInVar = StringVar(value='')
		self.txtIn = Entry(self.fraInput, textvariable=self.txtInVar, font=self.txtFont, bd=2, justify=tk.RIGHT)
		self.txtIn.setText = lambda x: self.txtInVar.set(x)
		self.txtIn.text = lambda : self.txtInVar.get()
		self.txtIn.place(x=8, y=2, width=145, height=25)
		self.txtInVar.trace(tk.W, self.Input_Change)

		self.cboUnitList = ('Hz','kHz','MHz','GHz','THz','s','ms','us','ns','ps',)
		self.cboUnitVar = StringVar(value=self.cboUnitList[0])
		self.cboUnit = OptionMenu(self.fraInput, self.cboUnitVar, *self.cboUnitList)
		self.cboUnit.configure(takefocus=1, font=self.cboFont)
		self.cboUnit.option = lambda : self.cboUnitVar.get()
		self.cboUnit.place(x=152, y=2, width=59, height=25)
		self.cboUnitVar.trace(tk.W, self.Input_Change)

		# -(Break)
		self.sep = Separator(self.root, orient='horizontal')
		self.sep.place(x=8, y=64, width=216, height=1)

		# =============================================
		# [               Frame frq out               ]
		# =============================================
		self.fraRsltFrq = LabelFrame(self.root, text='频率转换结果', font=self.fraFont)
		self.fraRsltFrq.place(x=8, y=72, width=217, height=137)

		# -Hz
		self.txtRsltHzVar = StringVar(value='')
		self.txtRsltHz = Entry(self.fraRsltFrq, readonlybackground='#E0E0E0', state='readonly', textvariable=self.txtRsltHzVar, font=self.txtFont, bd=2, justify=tk.RIGHT)
		self.txtRsltHz.setText = lambda x: self.txtRsltHzVar.set(x)
		self.txtRsltHz.text = lambda : self.txtRsltHzVar.get()
		self.txtRsltHz.place(x=8, y=2, width=145, height=18)

		self.lblUnitHzVar = StringVar(value='Hz')
		self.lblUnitHz = Label(self.fraRsltFrq, text='Hz', anchor=tk.W, textvariable=self.lblUnitHzVar, font=self.lblFont)
		self.lblUnitHz.setText = lambda x: self.lblUnitHzVar.set(x)
		self.lblUnitHz.text = lambda : self.lblUnitHzVar.get()
		self.lblUnitHz.place(x=157, y=4, width=25, height=13)

		self.btnCpyHzVar = StringVar(value='')
		self.btnCpyHz = Button(self.fraRsltFrq, image=self.imgBtnCpy, textvariable=self.btnCpyHzVar, command=self.btnCpyHz_Cmd, font=self.btnFont)
		self.btnCpyHz.setText = lambda x: self.btnCpyHzVar.set(x)
		self.btnCpyHz.text = lambda : self.btnCpyHzVar.get()
		self.btnCpyHz.place(x=192, y=2, width=17, height=17)

		# -kHz
		self.txtRsltkHzVar = StringVar(value='')
		self.txtRsltkHz = Entry(self.fraRsltFrq, readonlybackground='#E0E0E0', state='readonly', textvariable=self.txtRsltkHzVar, font=self.txtFont, bd=2, justify=tk.RIGHT)
		self.txtRsltkHz.setText = lambda x: self.txtRsltkHzVar.set(x)
		self.txtRsltkHz.text = lambda : self.txtRsltkHzVar.get()
		self.txtRsltkHz.place(x=8, y=26, width=145, height=18)

		self.lblUnitkHzVar = StringVar(value='kHz')
		self.lblUnitkHz = Label(self.fraRsltFrq, text='kHz', anchor=tk.W, textvariable=self.lblUnitkHzVar, font=self.lblFont)
		self.lblUnitkHz.setText = lambda x: self.lblUnitkHzVar.set(x)
		self.lblUnitkHz.text = lambda : self.lblUnitkHzVar.get()
		self.lblUnitkHz.place(x=157, y=28, width=25, height=13)

		self.btnCpykHzVar = StringVar(value='')
		self.btnCpykHz = Button(self.fraRsltFrq, image=self.imgBtnCpy, textvariable=self.btnCpykHzVar, command=self.btnCpykHz_Cmd, font=self.btnFont)
		self.btnCpykHz.setText = lambda x: self.btnCpykHzVar.set(x)
		self.btnCpykHz.text = lambda : self.btnCpykHzVar.get()
		self.btnCpykHz.place(x=192, y=26, width=17, height=17)

		# -Mhz
		self.txtRsltMHzVar = StringVar(value='')
		self.txtRsltMHz = Entry(self.fraRsltFrq, readonlybackground='#E0E0E0', state='readonly', textvariable=self.txtRsltMHzVar, font=self.txtFont, bd=2, justify=tk.RIGHT)
		self.txtRsltMHz.setText = lambda x: self.txtRsltMHzVar.set(x)
		self.txtRsltMHz.text = lambda : self.txtRsltMHzVar.get()
		self.txtRsltMHz.place(x=8, y=50, width=145, height=18)

		self.lblUnitMHzVar = StringVar(value='Mhz')
		self.lblUnitMHz = Label(self.fraRsltFrq, text='Mhz', anchor=tk.W, textvariable=self.lblUnitMHzVar, font=self.lblFont)
		self.lblUnitMHz.setText = lambda x: self.lblUnitMHzVar.set(x)
		self.lblUnitMHz.text = lambda : self.lblUnitMHzVar.get()
		self.lblUnitMHz.place(x=157, y=52, width=25, height=13)

		self.btnCpyMhzVar = StringVar(value='')
		self.btnCpyMhz = Button(self.fraRsltFrq, image=self.imgBtnCpy, textvariable=self.btnCpyMhzVar, command=self.btnCpyMhz_Cmd, font=self.btnFont)
		self.btnCpyMhz.setText = lambda x: self.btnCpyMhzVar.set(x)
		self.btnCpyMhz.text = lambda : self.btnCpyMhzVar.get()
		self.btnCpyMhz.place(x=192, y=50, width=17, height=17)

		# -GHz
		self.txtRsltGHzVar = StringVar(value='')
		self.txtRsltGHz = Entry(self.fraRsltFrq, readonlybackground='#E0E0E0', state='readonly', textvariable=self.txtRsltGHzVar, font=self.txtFont, bd=2, justify=tk.RIGHT)
		self.txtRsltGHz.setText = lambda x: self.txtRsltGHzVar.set(x)
		self.txtRsltGHz.text = lambda : self.txtRsltGHzVar.get()
		self.txtRsltGHz.place(x=8, y=74, width=145, height=18)

		self.lblUnitGHzVar = StringVar(value='GHz')
		self.lblUnitGHz = Label(self.fraRsltFrq, text='GHz', anchor=tk.W, textvariable=self.lblUnitGHzVar, font=self.lblFont)
		self.lblUnitGHz.setText = lambda x: self.lblUnitGHzVar.set(x)
		self.lblUnitGHz.text = lambda : self.lblUnitGHzVar.get()
		self.lblUnitGHz.place(x=157, y=76, width=25, height=13)

		self.btnCpyGHzVar = StringVar(value='')
		self.btnCpyGHz = Button(self.fraRsltFrq, image=self.imgBtnCpy, textvariable=self.btnCpyGHzVar, command=self.btnCpyGHz_Cmd, font=self.btnFont)
		self.btnCpyGHz.setText = lambda x: self.btnCpyGHzVar.set(x)
		self.btnCpyGHz.text = lambda : self.btnCpyGHzVar.get()
		self.btnCpyGHz.place(x=192, y=74, width=17, height=17)

		# -THz
		self.txtRsltTHzVar = StringVar(value='')
		self.txtRsltTHz = Entry(self.fraRsltFrq, readonlybackground='#E0E0E0', state='readonly', textvariable=self.txtRsltTHzVar, font=self.txtFont, bd=2, justify=tk.RIGHT)
		self.txtRsltTHz.setText = lambda x: self.txtRsltTHzVar.set(x)
		self.txtRsltTHz.text = lambda : self.txtRsltTHzVar.get()
		self.txtRsltTHz.place(x=8, y=98, width=145, height=18)

		self.lblUnitTHzVar = StringVar(value='THz')
		self.lblUnitTHz = Label(self.fraRsltFrq, text='THz', anchor=tk.W, textvariable=self.lblUnitTHzVar, font=self.lblFont)
		self.lblUnitTHz.setText = lambda x: self.lblUnitTHzVar.set(x)
		self.lblUnitTHz.text = lambda : self.lblUnitTHzVar.get()
		self.lblUnitTHz.place(x=157, y=100, width=25, height=13)

		self.btnCpyTHzVar = StringVar(value='')
		self.btnCpyTHz = Button(self.fraRsltFrq, image=self.imgBtnCpy, textvariable=self.btnCpyTHzVar, command=self.btnCpyTHz_Cmd, font=self.btnFont)
		self.btnCpyTHz.setText = lambda x: self.btnCpyTHzVar.set(x)
		self.btnCpyTHz.text = lambda : self.btnCpyTHzVar.get()
		self.btnCpyTHz.place(x=192, y=98, width=17, height=17)

		# =============================================
		# [               Frame ped out               ]
		# =============================================
		self.fraRsltPed = LabelFrame(self.root, text='周期转换结果', font=self.fraFont)
		self.fraRsltPed.place(x=8, y=216, width=217, height=137)

		# -s
		self.txtRsltsVar = StringVar(value='')
		self.txtRslts = Entry(self.fraRsltPed, readonlybackground='#E0E0E0', state='readonly', textvariable=self.txtRsltsVar, font=self.txtFont, bd=2, justify=tk.RIGHT)
		self.txtRslts.setText = lambda x: self.txtRsltsVar.set(x)
		self.txtRslts.text = lambda : self.txtRsltsVar.get()
		self.txtRslts.place(x=8, y=2, width=145, height=18)

		self.lblUnitsVar = StringVar(value='s')
		self.lblUnits = Label(self.fraRsltPed, text='s', anchor=tk.W, textvariable=self.lblUnitsVar, font=self.lblFont)
		self.lblUnits.setText = lambda x: self.lblUnitsVar.set(x)
		self.lblUnits.text = lambda : self.lblUnitsVar.get()
		self.lblUnits.place(x=157, y=4, width=25, height=13)

		self.btnCpysVar = StringVar(value='')
		self.btnCpys = Button(self.fraRsltPed, image=self.imgBtnCpy, textvariable=self.btnCpysVar, command=self.btnCpys_Cmd, font=self.btnFont)
		self.btnCpys.setText = lambda x: self.btnCpysVar.set(x)
		self.btnCpys.text = lambda : self.btnCpysVar.get()
		self.btnCpys.place(x=192, y=2, width=17, height=17)

		# -ms
		self.txtRsltmsVar = StringVar(value='')
		self.txtRsltms = Entry(self.fraRsltPed, readonlybackground='#E0E0E0', state='readonly', textvariable=self.txtRsltmsVar, font=self.txtFont, bd=2, justify=tk.RIGHT)
		self.txtRsltms.setText = lambda x: self.txtRsltmsVar.set(x)
		self.txtRsltms.text = lambda : self.txtRsltmsVar.get()
		self.txtRsltms.place(x=8, y=26, width=145, height=18)

		self.lblUnitmsVar = StringVar(value='ms')
		self.lblUnitms = Label(self.fraRsltPed, text='ms', anchor=tk.W, textvariable=self.lblUnitmsVar, font=self.lblFont)
		self.lblUnitms.setText = lambda x: self.lblUnitmsVar.set(x)
		self.lblUnitms.text = lambda : self.lblUnitmsVar.get()
		self.lblUnitms.place(x=157, y=28, width=25, height=13)

		self.btnCpymsVar = StringVar(value='')
		self.btnCpyms = Button(self.fraRsltPed, image=self.imgBtnCpy, textvariable=self.btnCpymsVar, command=self.btnCpyms_Cmd, font=self.btnFont)
		self.btnCpyms.setText = lambda x: self.btnCpymsVar.set(x)
		self.btnCpyms.text = lambda : self.btnCpymsVar.get()
		self.btnCpyms.place(x=192, y=26, width=17, height=17)

		# -us
		self.txtRsltusVar = StringVar(value='')
		self.txtRsltus = Entry(self.fraRsltPed, readonlybackground='#E0E0E0', state='readonly', textvariable=self.txtRsltusVar, font=self.txtFont, bd=2, justify=tk.RIGHT)
		self.txtRsltus.setText = lambda x: self.txtRsltusVar.set(x)
		self.txtRsltus.text = lambda : self.txtRsltusVar.get()
		self.txtRsltus.place(x=8, y=50, width=145, height=18)

		self.lblUnitusVar = StringVar(value='us')
		self.lblUnitus = Label(self.fraRsltPed, text='us', anchor=tk.W, textvariable=self.lblUnitusVar, font=self.lblFont)
		self.lblUnitus.setText = lambda x: self.lblUnitusVar.set(x)
		self.lblUnitus.text = lambda : self.lblUnitusVar.get()
		self.lblUnitus.place(x=157, y=52, width=25, height=13)

		self.btnCpyusVar = StringVar(value='')
		self.btnCpyus = Button(self.fraRsltPed, image=self.imgBtnCpy, textvariable=self.btnCpyusVar, command=self.btnCpyus_Cmd, font=self.btnFont)
		self.btnCpyus.setText = lambda x: self.btnCpyusVar.set(x)
		self.btnCpyus.text = lambda : self.btnCpyusVar.get()
		self.btnCpyus.place(x=192, y=50, width=17, height=17)

		# -ns
		self.txtRsltnsVar = StringVar(value='')
		self.txtRsltns = Entry(self.fraRsltPed, readonlybackground='#E0E0E0', state='readonly', textvariable=self.txtRsltnsVar, font=self.txtFont, bd=2, justify=tk.RIGHT)
		self.txtRsltns.setText = lambda x: self.txtRsltnsVar.set(x)
		self.txtRsltns.text = lambda : self.txtRsltnsVar.get()
		self.txtRsltns.place(x=8, y=74, width=145, height=18)

		self.lblUnitnsVar = StringVar(value='ns')
		self.lblUnitns = Label(self.fraRsltPed, text='ns', anchor=tk.W, textvariable=self.lblUnitnsVar, font=self.lblFont)
		self.lblUnitns.setText = lambda x: self.lblUnitnsVar.set(x)
		self.lblUnitns.text = lambda : self.lblUnitnsVar.get()
		self.lblUnitns.place(x=157, y=76, width=25, height=13)

		self.btnCpynsVar = StringVar(value='')
		self.btnCpyns = Button(self.fraRsltPed, image=self.imgBtnCpy, textvariable=self.btnCpynsVar, command=self.btnCpyns_Cmd, font=self.btnFont)
		self.btnCpyns.setText = lambda x: self.btnCpynsVar.set(x)
		self.btnCpyns.text = lambda : self.btnCpynsVar.get()
		self.btnCpyns.place(x=192, y=74, width=17, height=17)

		# -ps
		self.txtRsltpsVar = StringVar(value='')
		self.txtRsltps = Entry(self.fraRsltPed, readonlybackground='#E0E0E0', state='readonly', textvariable=self.txtRsltpsVar, font=self.txtFont, bd=2, justify=tk.RIGHT)
		self.txtRsltps.setText = lambda x: self.txtRsltpsVar.set(x)
		self.txtRsltps.text = lambda : self.txtRsltpsVar.get()
		self.txtRsltps.place(x=8, y=98, width=145, height=18)

		self.lblUnitpsVar = StringVar(value='ps')
		self.lblUnitps = Label(self.fraRsltPed, text='ps', anchor=tk.W, textvariable=self.lblUnitpsVar, font=self.lblFont)
		self.lblUnitps.setText = lambda x: self.lblUnitpsVar.set(x)
		self.lblUnitps.text = lambda : self.lblUnitpsVar.get()
		self.lblUnitps.place(x=157, y=100, width=25, height=13)

		self.btnCpypsVar = StringVar(value='')
		self.btnCpyps = Button(self.fraRsltPed, image=self.imgBtnCpy, textvariable=self.btnCpypsVar, command=self.btnCpyps_Cmd, font=self.btnFont)
		self.btnCpyps.setText = lambda x: self.btnCpypsVar.set(x)
		self.btnCpyps.text = lambda : self.btnCpypsVar.get()
		self.btnCpyps.place(x=192, y=98, width=17, height=17)

		# =============================================
		# |               Copyright bar               |
		# =============================================
		self.lblBar = Label(self.root, text=' 2021 Vestin | All rights reserved.', font=self.lblFont, bd=1, relief=tk.SUNKEN, justify=tk.CENTER)
		self.lblBar.pack(side=tk.BOTTOM, fill=tk.X)
		self.lblBar.bind('<Button-1>', self.lblBar_Click)

class AboutDialog(Toplevel):
	# The class will create all widgets for about form UI.
	def __init__(self, master=None):
		self.master = master
		self.takefocus = True

		self.dlgIcon    = None				# String, path of icns/ico/xbm
		self.appIcon    = None				# PhotoImage, size 32x32
		self.appTitle   = 'App Title'		# String
		self.appVersion = 'App Version'		# String
		self.appRights  = 'Copyrights...'	# String

	def createWidgets(self):
		# -App icon
		appIcon = Label(self, anchor='center', image=self.appIcon, relief=SUNKEN, bd='2')
		appIcon.place(x=72, y=16, width=36, height=36)

		# -App title
		appTitleFont = Font(font=('宋体',10,'bold'))
		appTitle = Label(self, text=self.appTitle, anchor='center', font=appTitleFont)
		appTitle.place(x=8, y=63, width=161, height=16)

		# -App version
		appVersionFont = Font(font=('宋体',9))
		appVersion = Label(self, text=self.appVersion, anchor='center', font=appVersionFont)
		appVersion.place(x=8, y=86, width=161, height=15)

		# -(Break)
		sep = Separator(self, orient='horizontal')
		sep.place(x=8, y=112, width=161, height=1)

		# -Copyrights...
		appRightsFont = Font(font=('宋体',9))
		appRights = Label(self, text=self.appRights, anchor='center', font=appRightsFont)
		appRights.place(x=8, y=117, width=162, height=31)

	# To pop up dialog after setting up 
	def popUp(self):
		Toplevel.__init__(self, self.master)
		self.transient(self.master)

		# -Dialog window initialize
		self.title('About '+self.appTitle)	# Set title
		self.geometry('177x156+153+104')	# Set window size
		self.resizable(0,0)					# Set window unresizable
		self.iconbitmap(self.dlgIcon)		# Set icon

		# -Get everything ready
		self.createWidgets()
		self.grab_set()
		self.focus_set()

class Utils:
	# The class implements utils.

	# --------------------
	# src()
	# + Get resource path.
	# --------------------
	@staticmethod
	def src(resource):
		return path.join(bundleDir, resource)

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
		if platformD == 'Darwin':
			p=subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
			p.stdin.write(rslt.encode('utf-8'))
			p.stdin.close()
			p.communicate()
		elif platformD == 'Windows':
			win32clipboard.OpenClipboard()
			win32clipboard.EmptyClipboard()
			win32clipboard.SetClipboardData(win32con.CF_TEXT, rslt)
			win32clipboard.CloseClipboard()
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
		floatStr = "{:.15g}".format(floatNum)
		isNeg = False
		rsltStr = ''

		# If is not by scientific notation
		if not "e" in floatStr:
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
			rsltStr += ''.join(['0' for _ in range(0, abs(expNum - len(coefStr.split('.')[1])))])
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
		if platformD == 'Darwin':
			self.appIcon = Utils.src('./src/FreqCalc.icns')
		elif platformD == 'Windows':
			self.appIcon = Utils.src('./src/FreqCalc.ico')
		else:
			self.appIcon = Utils.src('./src/logo.xbm')

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
		d.appTitle = 'FreqCalc'
		d.appVersion = 'Version 0.1.2'
		d.appRights = 'Copyright(C) 2021 Vestin.\nAll rights reserved.'
		d.popUp() # Popup about dialog

if __name__ == "__main__":
	root = Tk()
	Application(root).mainloop()

