# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui,QtWidgets
# from PyQt5.QtWidgets import QApplication,QDialog,
# from PyQt5.QtWidgets import QDialog

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
 
try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)


class UiDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 400)
        Dialog.setMinimumSize(QtCore.QSize(400, 400))
        Dialog.setMaximumSize(QtCore.QSize(400, 400))
        self.btn_execute = QtWidgets.QPushButton(Dialog)
        self.btn_execute.setGeometry(QtCore.QRect(10, 340, 381, 51))
        self.btn_execute.setObjectName(_fromUtf8("btnContrast"))
        self.group_box_choose = QtWidgets.QGroupBox(Dialog)
        self.group_box_choose.setGeometry(QtCore.QRect(10, 20, 381, 62))
        self.group_box_choose.setObjectName(_fromUtf8("groupBox"))
        self.src_path = QtWidgets.QLineEdit(self.group_box_choose)
        self.src_path.setGeometry(QtCore.QRect(95, 30, 216, 20))
        self.src_path.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.src_path.setReadOnly(True)
        self.src_path.setObjectName(_fromUtf8("txtPath1"))
        self.btn_src_choose = QtWidgets.QPushButton(self.group_box_choose)
        self.btn_src_choose.setGeometry(QtCore.QRect(320, 28, 40, 25))
        self.btn_src_choose.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_src_choose.setObjectName(_fromUtf8("btnPathChoose1"))
        self.btn_src_choose.setToolTip('支持txt和xlsx格式文本')
        self.label_src = QtWidgets.QLabel(self.group_box_choose)
        self.label_src.setGeometry(QtCore.QRect(20, 32, 64, 12))
        self.label_src.setObjectName(_fromUtf8("label"))
        self.group_box_output = QtWidgets.QGroupBox(Dialog)
        self.group_box_output.setGeometry(QtCore.QRect(10, 90, 381, 231))
        self.group_box_output.setObjectName(_fromUtf8("groupBox_2"))
        self.txt_output = QtWidgets.QTextBrowser(self.group_box_output)
        self.txt_output.setGeometry(QtCore.QRect(20, 27, 341, 185))
        self.txt_output.setObjectName(_fromUtf8("txtPathExclude"))

        self.set_text(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
 
    def set_text(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "生词本背单词—生词本制作工具v1.1", None))
        self.btn_execute.setText(_translate("Dialog", "开始转换", None))
        self.group_box_choose.setTitle(_translate("Dialog", "选择需要转换的文件", None))
        self.btn_src_choose.setText(_translate("Dialog", "...", None))
        self.label_src.setText(_translate("Dialog", "生词源文件：：", None))
        self.group_box_output.setTitle(_translate("Dialog", "正在转换", None))

 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = UiDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())