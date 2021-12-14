VERSION 5.00
Begin VB.Form frmAbout 
   BorderStyle     =   3  'Fixed Dialog
   Caption         =   "About this App"
   ClientHeight    =   2340
   ClientLeft      =   2340
   ClientTop       =   1935
   ClientWidth     =   2655
   ClipControls    =   0   'False
   Icon            =   "frmAbout.frx":0000
   LinkTopic       =   "Form2"
   MaxButton       =   0   'False
   MinButton       =   0   'False
   ScaleHeight     =   1615.11
   ScaleMode       =   0  'User
   ScaleWidth      =   2493.182
   ShowInTaskbar   =   0   'False
   Begin VB.PictureBox picIcon 
      AutoSize        =   -1  'True
      ClipControls    =   0   'False
      Height          =   540
      Left            =   1080
      Picture         =   "frmAbout.frx":427A
      ScaleHeight     =   337.12
      ScaleMode       =   0  'User
      ScaleWidth      =   337.12
      TabIndex        =   0
      Top             =   240
      Width           =   540
   End
   Begin VB.Line Line1 
      BorderColor     =   &H00808080&
      BorderStyle     =   6  'Inside Solid
      Index           =   1
      X1              =   112.686
      X2              =   2366.41
      Y1              =   1159.566
      Y2              =   1159.566
   End
   Begin VB.Label lblTitle 
      Alignment       =   2  'Center
      Caption         =   "App Title"
      BeginProperty Font 
         Name            =   "ËÎÌו"
         Size            =   10.5
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H00000000&
      Height          =   240
      Left            =   120
      TabIndex        =   2
      Top             =   960
      Width           =   2415
   End
   Begin VB.Line Line1 
      BorderColor     =   &H00FFFFFF&
      BorderWidth     =   2
      Index           =   0
      X1              =   98.6
      X2              =   4056.703
      Y1              =   1697.936
      Y2              =   1905.001
   End
   Begin VB.Label lblVersion 
      Alignment       =   2  'Center
      Caption         =   "App Version"
      Height          =   225
      Left            =   120
      TabIndex        =   3
      Top             =   1320
      Width           =   2415
   End
   Begin VB.Label lblDisclaimer 
      Alignment       =   2  'Center
      Caption         =   "CopyRights ..."
      ForeColor       =   &H00000000&
      Height          =   465
      Left            =   120
      TabIndex        =   1
      Top             =   1800
      Width           =   2430
   End
End
Attribute VB_Name = "frmAbout"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit

Private Sub Form_Load()
    Me.Caption = "About " & App.Title
    lblVersion.Caption = "Version " & App.Major & "." & App.Minor & "." & App.Revision
    lblTitle.Caption = App.Title
    lblDisclaimer.Caption = App.LegalCopyright
End Sub

