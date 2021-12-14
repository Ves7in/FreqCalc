VERSION 5.00
Object = "{831FDD16-0C5C-11D2-A9FC-0000F8754DA1}#2.0#0"; "MSCOMCTL.OCX"
Begin VB.Form FormMain 
   BorderStyle     =   1  'Fixed Single
   Caption         =   "FreqCalc - v0.1.1"
   ClientHeight    =   5625
   ClientLeft      =   45
   ClientTop       =   375
   ClientWidth     =   3480
   Icon            =   "FreqCalc.frx":0000
   LinkTopic       =   "Form1"
   MaxButton       =   0   'False
   ScaleHeight     =   375
   ScaleMode       =   3  'Pixel
   ScaleWidth      =   232
   StartUpPosition =   3  '窗口缺省
   Begin MSComctlLib.StatusBar StatusBar 
      Align           =   2  'Align Bottom
      Height          =   255
      Left            =   0
      TabIndex        =   35
      Top             =   5370
      Width           =   3480
      _ExtentX        =   6138
      _ExtentY        =   450
      Style           =   1
      SimpleText      =   "  2021 Vestin | All rigths reserved."
      _Version        =   393216
      BeginProperty Panels {8E3867A5-8586-11D1-B16A-00C0F0283628} 
         NumPanels       =   2
         BeginProperty Panel1 {8E3867AB-8586-11D1-B16A-00C0F0283628} 
            Object.Width           =   794
            MinWidth        =   794
            Text            =   "Err"
            TextSave        =   "Err"
         EndProperty
         BeginProperty Panel2 {8E3867AB-8586-11D1-B16A-00C0F0283628} 
            AutoSize        =   1
            Object.Width           =   5265
         EndProperty
      EndProperty
   End
   Begin VB.TextBox txtRsltkHz 
      Alignment       =   1  'Right Justify
      Height          =   270
      Left            =   240
      Locked          =   -1  'True
      TabIndex        =   5
      Text            =   "0"
      Top             =   1680
      Width           =   2175
   End
   Begin VB.Frame FraRsltPed 
      Caption         =   "周期转换结果"
      Height          =   2055
      Left            =   120
      TabIndex        =   24
      Top             =   3240
      Width           =   3255
      Begin VB.CommandButton btnCpyps 
         Height          =   255
         Left            =   2880
         Picture         =   "FreqCalc.frx":427A
         Style           =   1  'Graphical
         TabIndex        =   22
         Top             =   1680
         Width           =   255
      End
      Begin VB.CommandButton btnCpyns 
         Height          =   255
         Left            =   2880
         Picture         =   "FreqCalc.frx":47AC
         Style           =   1  'Graphical
         TabIndex        =   20
         Top             =   1320
         Width           =   255
      End
      Begin VB.CommandButton btnCpyus 
         Height          =   255
         Left            =   2880
         Picture         =   "FreqCalc.frx":4CDE
         Style           =   1  'Graphical
         TabIndex        =   18
         Top             =   960
         Width           =   255
      End
      Begin VB.CommandButton btnCpyms 
         Height          =   255
         Left            =   2880
         Picture         =   "FreqCalc.frx":5210
         Style           =   1  'Graphical
         TabIndex        =   16
         Top             =   600
         Width           =   255
      End
      Begin VB.CommandButton btnCpys 
         Height          =   255
         Left            =   2880
         Picture         =   "FreqCalc.frx":5742
         Style           =   1  'Graphical
         TabIndex        =   14
         Top             =   240
         Width           =   255
      End
      Begin VB.TextBox txtRsltps 
         Alignment       =   1  'Right Justify
         Height          =   270
         Left            =   120
         Locked          =   -1  'True
         TabIndex        =   21
         Text            =   "0"
         Top             =   1680
         Width           =   2175
      End
      Begin VB.TextBox txtRsltns 
         Alignment       =   1  'Right Justify
         Height          =   270
         Left            =   120
         Locked          =   -1  'True
         TabIndex        =   19
         Text            =   "0"
         Top             =   1320
         Width           =   2175
      End
      Begin VB.TextBox txtRsltus 
         Alignment       =   1  'Right Justify
         Height          =   270
         Left            =   120
         Locked          =   -1  'True
         TabIndex        =   17
         Text            =   "0"
         Top             =   960
         Width           =   2175
      End
      Begin VB.TextBox txtRsltms 
         Alignment       =   1  'Right Justify
         Height          =   270
         Left            =   120
         Locked          =   -1  'True
         TabIndex        =   15
         Text            =   "0"
         Top             =   600
         Width           =   2175
      End
      Begin VB.TextBox txtRslts 
         Alignment       =   1  'Right Justify
         Height          =   270
         Left            =   120
         Locked          =   -1  'True
         TabIndex        =   13
         Text            =   "0"
         Top             =   240
         Width           =   2175
      End
      Begin VB.Label lblUnitps 
         Caption         =   "ps"
         Height          =   255
         Left            =   2400
         TabIndex        =   34
         Top             =   1680
         Width           =   375
      End
      Begin VB.Label lblUnitns 
         Caption         =   "ns"
         Height          =   255
         Left            =   2400
         TabIndex        =   33
         Top             =   1320
         Width           =   375
      End
      Begin VB.Label lblUnitus 
         Caption         =   "us"
         Height          =   255
         Left            =   2400
         TabIndex        =   32
         Top             =   960
         Width           =   375
      End
      Begin VB.Label lblUnitms 
         Caption         =   "ms"
         Height          =   255
         Left            =   2400
         TabIndex        =   31
         Top             =   600
         Width           =   375
      End
      Begin VB.Label lblUnits 
         Caption         =   "s"
         Height          =   255
         Left            =   2400
         TabIndex        =   30
         Top             =   240
         Width           =   375
      End
   End
   Begin VB.Frame FraRsltFrq 
      Caption         =   "频率转换结果"
      Height          =   2055
      Left            =   120
      TabIndex        =   23
      Top             =   1080
      Width           =   3255
      Begin VB.CommandButton btnCpyTHz 
         Height          =   255
         Left            =   2880
         Picture         =   "FreqCalc.frx":5C74
         Style           =   1  'Graphical
         TabIndex        =   12
         Top             =   1680
         Width           =   255
      End
      Begin VB.TextBox txtRsltTHz 
         Alignment       =   1  'Right Justify
         Height          =   270
         Left            =   120
         Locked          =   -1  'True
         TabIndex        =   11
         Text            =   "0"
         Top             =   1680
         Width           =   2175
      End
      Begin VB.CommandButton btnCpyGHz 
         Height          =   255
         Left            =   2880
         Picture         =   "FreqCalc.frx":61A6
         Style           =   1  'Graphical
         TabIndex        =   10
         Top             =   1320
         Width           =   255
      End
      Begin VB.TextBox txtRsltGHz 
         Alignment       =   1  'Right Justify
         Height          =   270
         Left            =   120
         Locked          =   -1  'True
         TabIndex        =   9
         Text            =   "0"
         Top             =   1320
         Width           =   2175
      End
      Begin VB.CommandButton btnCpyMhz 
         Height          =   255
         Left            =   2880
         Picture         =   "FreqCalc.frx":66D8
         Style           =   1  'Graphical
         TabIndex        =   8
         Top             =   960
         Width           =   255
      End
      Begin VB.CommandButton btnCpykHz 
         Height          =   255
         Left            =   2880
         Picture         =   "FreqCalc.frx":6C0A
         Style           =   1  'Graphical
         TabIndex        =   6
         Top             =   600
         Width           =   255
      End
      Begin VB.TextBox txtRsltMHz 
         Alignment       =   1  'Right Justify
         Height          =   270
         Left            =   120
         Locked          =   -1  'True
         TabIndex        =   7
         Text            =   "0"
         Top             =   960
         Width           =   2175
      End
      Begin VB.CommandButton btnCpyHz 
         Height          =   255
         Left            =   2880
         Picture         =   "FreqCalc.frx":713C
         Style           =   1  'Graphical
         TabIndex        =   4
         Top             =   240
         Width           =   255
      End
      Begin VB.TextBox txtRsltHz 
         Alignment       =   1  'Right Justify
         Height          =   270
         Left            =   120
         Locked          =   -1  'True
         TabIndex        =   3
         Text            =   "0"
         Top             =   240
         Width           =   2175
      End
      Begin VB.Label lblUnitTHz 
         Caption         =   "THz"
         Height          =   255
         Left            =   2400
         TabIndex        =   29
         Top             =   1680
         Width           =   375
      End
      Begin VB.Label lblUnitGHz 
         Caption         =   "GHz"
         Height          =   255
         Left            =   2400
         TabIndex        =   28
         Top             =   1320
         Width           =   375
      End
      Begin VB.Label lblUnitMHz 
         Caption         =   "Mhz"
         Height          =   255
         Left            =   2400
         TabIndex        =   27
         Top             =   960
         Width           =   375
      End
      Begin VB.Label lblUnitkHz 
         Caption         =   "kHz"
         Height          =   255
         Left            =   2400
         TabIndex        =   26
         Top             =   600
         Width           =   375
      End
      Begin VB.Label lblUnitHz 
         Caption         =   "Hz"
         Height          =   255
         Left            =   2400
         TabIndex        =   25
         Top             =   240
         Width           =   375
      End
   End
   Begin VB.Frame FrmInput 
      Caption         =   "频率/周期输入"
      Height          =   735
      Left            =   120
      TabIndex        =   0
      Top             =   120
      Width           =   3255
      Begin VB.ComboBox cboUnit 
         Height          =   300
         ItemData        =   "FreqCalc.frx":766E
         Left            =   2400
         List            =   "FreqCalc.frx":7670
         TabIndex        =   2
         Text            =   "cboUnit"
         Top             =   240
         Width           =   735
      End
      Begin VB.TextBox txtIn 
         Alignment       =   1  'Right Justify
         Height          =   375
         Left            =   120
         TabIndex        =   1
         Top             =   240
         Width           =   2175
      End
   End
   Begin VB.Line Line1 
      BorderColor     =   &H8000000A&
      X1              =   8
      X2              =   224
      Y1              =   64
      Y2              =   64
   End
End
Attribute VB_Name = "FormMain"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit

Private Sub Form_Load()
    ' ++++ 控件初始化 ++++
    ' ----  频率选项  ----
    cboUnit.AddItem "Hz"
    cboUnit.AddItem "kHz"
    cboUnit.AddItem "MHz"
    cboUnit.AddItem "GHz"
    cboUnit.AddItem "THz"
    ' ----  周期选项  ----
    cboUnit.AddItem "s"
    cboUnit.AddItem "ms"
    cboUnit.AddItem "us"
    cboUnit.AddItem "ns"
    cboUnit.AddItem "ps"
    ' ++++ 启动预处理 ++++
    cboUnit.ListIndex = 0
End Sub
Private Sub StatusBar_Click()
    frmAbout.Show vbModal
End Sub
Private Sub txtIn_Change()
    RefreshRslt
End Sub
Private Sub cboUnit_Click()
    RefreshRslt
End Sub
' ------------------------------------ btn Copy Hz
Private Sub btnCpyHz_Click()
    Clipboard.Clear
    Clipboard.SetText txtRsltHz.Text
End Sub
' ------------------------------------ btn Copy kHz
Private Sub btnCpykHz_Click()
    Clipboard.Clear
    Clipboard.SetText txtRsltkHz.Text
End Sub
' ------------------------------------ btn Copy MHz
Private Sub btnCpyMHz_Click()
    Clipboard.Clear
    Clipboard.SetText txtRsltMHz.Text
End Sub
' ------------------------------------ btn Copy GHz
Private Sub btnCpyGHz_Click()
    Clipboard.Clear
    Clipboard.SetText txtRsltGHz.Text
End Sub
' ------------------------------------ btn Copy THz
Private Sub btnCpyTHz_Click()
    Clipboard.Clear
    Clipboard.SetText txtRsltTHz.Text
End Sub
' ------------------------------------ btn Copy s
Private Sub btnCpys_Click()
    Clipboard.Clear
    Clipboard.SetText txtRslts.Text
End Sub
' ------------------------------------ btn Copy ms
Private Sub btnCpyms_Click()
    Clipboard.Clear
    Clipboard.SetText txtRsltms.Text
End Sub
' ------------------------------------ btn Copy us
Private Sub btnCpyus_Click()
    Clipboard.Clear
    Clipboard.SetText txtRsltus.Text
End Sub
' ------------------------------------ btn Copy ns
Private Sub btnCpyns_Click()
    Clipboard.Clear
    Clipboard.SetText txtRsltns.Text
End Sub
' ------------------------------------ btn Copy ps
Private Sub btnCpyps_Click()
    Clipboard.Clear
    Clipboard.SetText txtRsltps.Text
End Sub
' ======================== Functions ========================
'****************
'   RefreshRslt()
' + Refresh results.
'****************
Private Function RefreshRslt()
    txtIn.BackColor = &H80000005    ' 复位错误提醒效果
    If txtIn.Text = "" Then RstRslt: Exit Function  ' 输入框为空时清零
    On Error GoTo cerror    ' 错误跳转
    
    Dim RsltByHz As Double  ' Double精度
    Dim RsltBySec As Double ' Double精度
    
    Select Case cboUnit
        Case "Hz"
            RsltByHz = txtIn.Text
            RsltBySec = 1 / RsltByHz
        Case "kHz"
            RsltByHz = txtIn.Text * 1000
            RsltBySec = 1 / RsltByHz
        Case "MHz"
            RsltByHz = txtIn.Text * 1000000
            RsltBySec = 1 / RsltByHz
        Case "GHz"
            RsltByHz = txtIn.Text * 1000000000
            RsltBySec = 1 / RsltByHz
        Case "THz"
            RsltByHz = txtIn.Text * 1000000000000#
            RsltBySec = 1 / RsltByHz
        Case "s"
            RsltBySec = txtIn.Text
            RsltByHz = 1 / RsltBySec
        Case "ms"
            RsltBySec = txtIn.Text / 1000
            RsltByHz = 1 / RsltBySec
        Case "us"
            RsltBySec = txtIn.Text / 1000000
            RsltByHz = 1 / RsltBySec
        Case "ns"
            RsltBySec = txtIn.Text / 1000000000
            RsltByHz = 1 / RsltBySec
        Case "ps"
            RsltBySec = txtIn.Text / 1000000000000#
            RsltByHz = 1 / RsltBySec
    End Select
    ' 输出频率
    txtRsltHz.Text = RsltByHz
    txtRsltkHz.Text = RsltByHz / 1000
    txtRsltMHz.Text = RsltByHz / 1000000
    txtRsltGHz.Text = RsltByHz / 1000000000
    txtRsltTHz.Text = RsltByHz / 1000000000000#
    ' 输出周期
    txtRslts.Text = RsltBySec
    txtRsltms.Text = RsltBySec * 1000
    txtRsltus.Text = RsltBySec * 1000000
    txtRsltns.Text = RsltBySec * 1000000000
    txtRsltps.Text = RsltBySec * 1000000000000#
    ' 跳过错误执行过程，结束函数
    Exit Function
' 错误执行过程
cerror:
    txtIn.BackColor = &HC0C0FF
    RstRslt
End Function
'****************
'   RstRslt()
' + Reset results.
'****************
Private Function RstRslt()
    txtRsltHz.Text = 0
    txtRsltkHz.Text = 0
    txtRsltMHz.Text = 0
    txtRsltGHz.Text = 0
    txtRsltTHz.Text = 0
    
    txtRslts.Text = 0
    txtRsltms.Text = 0
    txtRsltus.Text = 0
    txtRsltns.Text = 0
    txtRsltps.Text = 0
End Function
