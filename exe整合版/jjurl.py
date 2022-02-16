# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jjurl.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(610, 773)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/dell/Downloads/jjlogo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 591, 741))
        self.tabWidget.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"font: 9pt \"Microsoft YaHei UI\",\"思源黑体 CN\",\"黑体\",\"Arial\",sans-serif;")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 72, 21))
        self.label_3.setObjectName("label_3")
        self.jjurl = QtWidgets.QLineEdit(self.tab)
        self.jjurl.setGeometry(QtCore.QRect(80, 10, 381, 31))
        self.jjurl.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.jjurl.setObjectName("jjurl")
        self.start = QtWidgets.QPushButton(self.tab)
        self.start.setGeometry(QtCore.QRect(480, 10, 93, 31))
        self.start.setObjectName("start")
        self.configsave = QtWidgets.QPushButton(self.tab)
        self.configsave.setGeometry(QtCore.QRect(480, 50, 93, 31))
        self.configsave.setObjectName("configsave")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 72, 21))
        self.label_4.setObjectName("label_4")
        self.jjcookie = QtWidgets.QLineEdit(self.tab)
        self.jjcookie.setGeometry(QtCore.QRect(80, 50, 381, 31))
        self.jjcookie.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.jjcookie.setObjectName("jjcookie")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 90, 171, 51))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.fileend = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.fileend.setContentsMargins(0, 0, 0, 0)
        self.fileend.setObjectName("fileend")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.fileend.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.format = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.format.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.format.setObjectName("format")
        self.format.addItem("")
        self.format.addItem("")
        self.format.addItem("")
        self.fileend.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.format)
        self.formLayoutWidget = QtWidgets.QWidget(self.tab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(230, 90, 171, 53))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.tstran = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.tstran.setContentsMargins(0, 0, 0, 0)
        self.tstran.setObjectName("tstran")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.tstran.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.stch = QtWidgets.QComboBox(self.formLayoutWidget)
        self.stch.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stch.setObjectName("stch")
        self.stch.addItem("")
        self.stch.addItem("")
        self.stch.addItem("")
        self.tstran.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.stch)
        self.hvol = QtWidgets.QCheckBox(self.tab)
        self.hvol.setGeometry(QtCore.QRect(10, 190, 171, 19))
        self.hvol.setObjectName("hvol")
        self.special = QtWidgets.QCheckBox(self.tab)
        self.special.setGeometry(QtCore.QRect(10, 130, 164, 19))
        self.special.setObjectName("special")
        self.chInfo = QtWidgets.QCheckBox(self.tab)
        self.chInfo.setGeometry(QtCore.QRect(230, 120, 281, 31))
        self.chInfo.setObjectName("chInfo")
        self.cover = QtWidgets.QCheckBox(self.tab)
        self.cover.setGeometry(QtCore.QRect(10, 150, 181, 41))
        self.cover.setChecked(True)
        self.cover.setObjectName("cover")
        self.formLayoutWidget_4 = QtWidgets.QWidget(self.tab)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(236, 150, 301, 31))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 220, 191, 98))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.titlestyle = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.titlestyle.setContentsMargins(0, 0, 0, 0)
        self.titlestyle.setObjectName("titlestyle")
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.titlestyle.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.number = QtWidgets.QCheckBox(self.formLayoutWidget_3)
        self.number.setChecked(True)
        self.number.setObjectName("number")
        self.titlestyle.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.number)
        self.title = QtWidgets.QCheckBox(self.formLayoutWidget_3)
        self.title.setChecked(True)
        self.title.setObjectName("title")
        self.titlestyle.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.title)
        self.summary = QtWidgets.QCheckBox(self.formLayoutWidget_3)
        self.summary.setChecked(True)
        self.summary.setObjectName("summary")
        self.titlestyle.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.summary)
        self.line_3 = QtWidgets.QFrame(self.formLayoutWidget_3)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.titlestyle.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.line_3)
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(230, 190, 341, 115))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)
        self.cssedit = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.cssedit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.cssedit.setPlainText("")
        self.cssedit.setObjectName("cssedit")
        self.gridLayout.addWidget(self.cssedit, 1, 1, 3, 1)
        self.cssbutton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cssbutton.setObjectName("cssbutton")
        self.gridLayout.addWidget(self.cssbutton, 2, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 0, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(30, 450, 81, 21))
        self.label_8.setObjectName("label_8")
        self.pct = QtWidgets.QLabel(self.tab)
        self.pct.setGeometry(QtCore.QRect(440, 450, 131, 31))
        self.pct.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pct.setObjectName("pct")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(30, 410, 81, 31))
        self.label_9.setObjectName("label_9")
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(120, 420, 451, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.textEdit = QtWidgets.QTextBrowser(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(20, 480, 551, 221))
        self.textEdit.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.textEdit.setStyleSheet("background-color: transparent;\n"
"font: 9pt \"Microsoft YaHei UI\",\"思源黑体 CN\",\"黑体\",\"Arial\",sans-serif;")
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(230, 150, 328, 39))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.threadnum = QtWidgets.QLineEdit(self.layoutWidget)
        self.threadnum.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.threadnum.setInputMask("")
        self.threadnum.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.threadnum.setObjectName("threadnum")
        self.horizontalLayout.addWidget(self.threadnum)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.formLayoutWidget_5 = QtWidgets.QWidget(self.tab)
        self.formLayoutWidget_5.setGeometry(QtCore.QRect(20, 320, 318, 92))
        self.formLayoutWidget_5.setObjectName("formLayoutWidget_5")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_5)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.tfedit = QtWidgets.QLineEdit(self.formLayoutWidget_5)
        self.tfedit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tfedit.setObjectName("tfedit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.tfedit)
        self.selftitle = QtWidgets.QCheckBox(self.formLayoutWidget_5)
        self.selftitle.setObjectName("selftitle")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.selftitle)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.formLayoutWidget_6 = QtWidgets.QWidget(self.tab)
        self.formLayoutWidget_6.setGeometry(QtCore.QRect(340, 320, 225, 92))
        self.formLayoutWidget_6.setObjectName("formLayoutWidget_6")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_6)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.selfvol = QtWidgets.QCheckBox(self.formLayoutWidget_6)
        self.selfvol.setObjectName("selfvol")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.selfvol)
        self.voledit = QtWidgets.QLineEdit(self.formLayoutWidget_6)
        self.voledit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.voledit.setObjectName("voledit")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.voledit)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.label_12.setObjectName("label_12")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.line_2 = QtWidgets.QFrame(self.tab)
        self.line_2.setGeometry(QtCore.QRect(200, 90, 20, 221))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_4 = QtWidgets.QFrame(self.tab)
        self.line_4.setGeometry(QtCore.QRect(10, 210, 191, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 10, 531, 691))
        self.textBrowser_2.setStyleSheet("“background:transparent;border-width:0;border-style:outset”")
        self.textBrowser_2.setReadOnly(True)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "晋江小说下载"))
        self.label_3.setText(_translate("MainWindow", "小说网址："))
        self.jjurl.setText(_translate("MainWindow", "http://www.jjwxc.net/onebook.php?novelid=1"))
        self.start.setText(_translate("MainWindow", "开始下载"))
        self.configsave.setText(_translate("MainWindow", "保存配置"))
        self.label_4.setText(_translate("MainWindow", "cookie："))
        self.jjcookie.setText(_translate("MainWindow", "请输入cookie"))
        self.label_2.setText(_translate("MainWindow", "下载格式："))
        self.format.setItemText(0, _translate("MainWindow", "txt"))
        self.format.setItemText(1, _translate("MainWindow", "epub2"))
        self.format.setItemText(2, _translate("MainWindow", "epub3"))
        self.label.setText(_translate("MainWindow", "繁简转换："))
        self.stch.setItemText(0, _translate("MainWindow", "不变"))
        self.stch.setItemText(1, _translate("MainWindow", "繁转简"))
        self.stch.setItemText(2, _translate("MainWindow", "简转繁"))
        self.hvol.setText(_translate("MainWindow", "epub2添加网页目录"))
        self.special.setText(_translate("MainWindow", "epub文案加特效"))
        self.chInfo.setText(_translate("MainWindow", "是否添加章节信息（字数、更新时间）"))
        self.cover.setText(_translate("MainWindow", "epub格式文件添加封面"))
        self.label_5.setText(_translate("MainWindow", "标题格式："))
        self.number.setText(_translate("MainWindow", "序号"))
        self.title.setText(_translate("MainWindow", "章节名称"))
        self.summary.setText(_translate("MainWindow", "内容提要"))
        self.label_10.setText(_translate("MainWindow", "自定义css："))
        self.cssbutton.setText(_translate("MainWindow", "恢复默认"))
        self.label_8.setText(_translate("MainWindow", "下载信息："))
        self.pct.setText(_translate("MainWindow", "0/0"))
        self.label_9.setText(_translate("MainWindow", "下载进度："))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft YaHei UI\',\'思源黑体 CN\',\'黑体\',\'Arial\',\'sans-serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">（当前无输出信息）</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "最大线程数："))
        self.threadnum.setText(_translate("MainWindow", "100"))
        self.label_7.setText(_translate("MainWindow", "（建议范围：1-999）"))
        self.tfedit.setText(_translate("MainWindow", "$1 $2 $3"))
        self.selftitle.setText(_translate("MainWindow", "是否自定义标题格式"))
        self.label_11.setText(_translate("MainWindow", "（$1为序号，$2为章节名称，$3为内容提要）"))
        self.selfvol.setText(_translate("MainWindow", "是否自定义卷标格式"))
        self.label_12.setText(_translate("MainWindow", "（$1为卷标号，$2为卷标内容）"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "下载页面"))
        self.textBrowser_2.setMarkdown(_translate("MainWindow", "本软件由7325156制作，若运行软件时有问题，请 [联系作者](https://github.com/7325156/jjwxcNovelCrawler)\n"
"\n"
"版本：2.4.3\n"
"\n"
"最新版本下载： [github](https://github.com/7325156/jjwxcNovelCrawler/releases/latest/)\n"
"| [蓝奏云](https://wwr.lanzoui.com/b02oduqmd#a5jo)\n"
"\n"
"此项目仅供学习交流使用，严禁用于商业用途，请在24小时之内删除。\n"
"\n"
"**更新记录**：\n"
"\n"
"2022-01-01\n"
"\n"
"- 修改网址不能匹配https的bug。\n"
"\n"
"2021-11-09 \n"
"\n"
"- 添加自定义标题、卷标格式功能。\n"
"\n"
"2021-10-26 \n"
"\n"
"- 为epub2添加网页目录 获取未购买、被锁章节信息\n"
"\n"
"2021-10-22 \n"
"\n"
"- 使用app接口下载，无需反爬虫。感谢 **酷安 @关耳010225 @乃星 @viviyaaa** 的方案。 \n"
"- 添加编辑css功能。\n"
"\n"
"2021-9-30\n"
"\n"
"- 新增窗口模式，可自由选择反爬虫模式（侵删）、文件下载格式以及其他必备配置。\n"
""))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft YaHei UI\',\'思源黑体 CN\',\'黑体\',\'Arial\',\'sans-serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\',\'sans-serif\'; font-size:10pt;\">本软件由7325156制作，若运行软件时有问题，请 </span><a href=\"https://github.com/7325156/jjwxcNovelCrawler\"><span style=\" font-family:\'SimSun\'; font-size:10pt; text-decoration: underline; color:#0000ff;\">联系作者</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\',\'sans-serif\'; font-size:10pt;\">版本：2.4.3</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\',\'sans-serif\'; font-size:10pt;\">最新版本下载： </span><a href=\"https://github.com/7325156/jjwxcNovelCrawler/releases/latest/\"><span style=\" font-family:\'SimSun\'; font-size:10pt; text-decoration: underline; color:#0000ff;\">github</span></a><span style=\" font-family:\'微软雅黑\',\'sans-serif\'; font-size:10pt;\"> | </span><a href=\"https://wwr.lanzoui.com/b02oduqmd#a5jo\"><span style=\" font-family:\'SimSun\'; font-size:10pt; text-decoration: underline; color:#0000ff;\">蓝奏云</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:10pt;\">此项目仅供学习交流使用，严禁用于商业用途，请在24小时之内删除。</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\',\'sans-serif\'; font-size:10pt; font-weight:600;\">更新记录</span><span style=\" font-family:\'微软雅黑\',\'sans-serif\'; font-size:10pt;\">：</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\',\'sans-serif\'; font-size:10pt;\">2022-01-01</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'微软雅黑\',\'sans-serif\'; font-size:10pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">修改网址不能匹配https的bug。</li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\',\'sans-serif\'; font-size:10pt;\">2021-11-09 </span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'微软雅黑\',\'sans-serif\'; font-size:10pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">添加自定义标题、卷标格式功能。</li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\',\'sans-serif\'; font-size:10pt;\">2021-10-26 </span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'微软雅黑\',\'sans-serif\'; font-size:10pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">为epub2添加网页目录 获取未购买、被锁章节信息</li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\',\'sans-serif\'; font-size:10pt;\">2021-10-22 </span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'微软雅黑\',\'sans-serif\'; font-size:10pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">使用app接口下载，无需反爬虫。感谢 <span style=\" font-weight:600;\">酷安 @关耳010225 @乃星 @viviyaaa</span> 的方案。 </li>\n"
"<li style=\" font-family:\'微软雅黑\',\'sans-serif\'; font-size:10pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">添加编辑css功能。</li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\',\'sans-serif\'; font-size:10pt;\">2021-9-30</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'微软雅黑\',\'sans-serif\'; font-size:10pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">新增窗口模式，可自由选择反爬虫模式（侵删）、文件下载格式以及其他必备配置。</li></ul></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "帮助"))
