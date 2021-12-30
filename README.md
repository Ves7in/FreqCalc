# FreqCalc
频率和周期的转换计算小工具🛠。

A conversion and calculation tool for frequency and period🛠.

![preview_all_logo - v0 1 3](https://user-images.githubusercontent.com/31813146/147745354-7aeff124-e819-4eda-82fa-971caa3c1839.png)

## 🗝简介
数字IC的设计必定离不开时许控制，因而设计及仿真测试过程中不得不与时钟信号打交道。

这个小工具能够帮助数字工程师处理好时钟信号的频率及周期，将转换计算后的结果应用于不同的仿真环境。

## 👨🏻‍💻开发
1. 作者并非专职软件开发，后续主动更新仅取决于个人或同事的需求，欢迎向本仓库提交有价值的Issues，作者将在精力和能力范围内采纳并实现其中的开发建议；
2. 软件开发完全为个人兴趣，开发过程即是作者的学习过程，开发语言也可能随更新改变，因此本软件的代码并不保证具有参考价值；
3. 尽可能使用系统原生控件、API，如有引用三方API，将会在更新日志中注明，如有必要，将会在有引用的Release中注明license；
4. 无兴趣做花里胡哨的界面，但保证界面整洁直观、操作人性。

## 📙更新日志
#### 2021/11/25 - v0.0.1(1)
1. 发布v0.0.1(1)，由Excel实现。

#### 2021/12/13 - v0.1.1(2)
1. 更新至v0.1.1(2)，由Visual Basic实现；
2. 添加输入错误提示功能；
3. 添加计算结果一键复制按钮；
4. 添加关于界面。

#### 2021/12/23 - v0.1.2(3)
1. 更新至v0.1.2(3)，使用Python重写,同时适配了Python2及Python3；
2. Windows单文件可执行程序由[PyInstaller](https://github.com/pyinstaller/pyinstaller)生成；
3. UI部分代码由[Tkinter Designer (@cdhigh)](https://github.com/cdhigh/tkinter-designer)生成；
4. UI延用v0.1.1(2)版本设计，并做部分优化；
5. 源代码在装有Python环境的Windows 7及MacOS 10.15.5上完成测试，均正常运行；
6. MacOS上运行的界面仍存在设计缺陷，将在后续改进完善。
