# -*- coding: utf-8 -*-
 
import sys
import os
import string
import time
import chardet
import codecs
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import QObject, pyqtSignal
from Ui_file_convertor_ui import UiDialog
import xlrd;

 
class FileContrast(QtWidgets.QDialog, UiDialog):
  
    def __init__(self, parent = None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)
        
        self.exclude_list = []
        
        # Thread
        self.bee = Worker(self.process_excel_file, ())
#         self.bee.terminated.connect(self.restoreUi)

        # Console handler
        self.btn_src_choose.clicked.connect(self.choose_src)
        self.btn_execute.clicked.connect(self.process_execute)
        self.dummyEmitter = DummyEmitter();
        self.dummyEmitter.connect(self.update_progress);

    def update_progress(self,msg):
        print msg
        self.txt_output.append(msg)

    def choose_src(self):
        path, _filter = QtWidgets.QFileDialog.getOpenFileName(self,  u"选择源文件")
        if path:
            self.src_path.setText(path)
    
    def process_execute(self):
        self.txt_output.clear()
        self.bee.start()

    def process_file(self):
        src = self.raw_string(self.src_path.text())
        if not src:
            return
        suffix = src.rsplit(".",1)[1];
        if  suffix == "txt":
            self.process_txt_file()
        elif suffix == "xlsx" or suffix == "xls":
            self.process_excel_file()

    def process_txt_file(self):
        src = self.raw_string(self.src_path.text())
        if not src:
            return

        splits = src.rsplit(os.sep,1)
        des = self.raw_string(splits[0]+os.sep + "converted_"+splits[1])
        timestamp =str(long(time.time()))
        sf = open(src)
        preRead = sf.readline()
        encodeInfo = chardet.detect(preRead)
        ENCODING = encodeInfo['encoding']
        sf.close()
        sf = codecs.open(src,'r',encoding = ENCODING)
#         print "encoding = "+ENCODING
        out = codecs.open(des,'wb','UTF-8')
        for line in sf: 
            word = string.split(line, '$$')
            i=0
            for str1 in word:
                if i==0:
                    out.write('+' +str1.strip()+'\n')
                elif i==1:
                    out.write('#' +str1.strip()+'\n')
                elif i==2:
                    out.write('&' +str1.strip()+'\n')
                i = i+1
#                 print str1
            self.dummyEmitter.signal_msg(line)
            if i ==2 :
                out.write('&'+'\n')
            out.write('@' +timestamp+'\n')
            out.write('$1' +'\n')
        out.close()    
        sf.close()
        self.dummyEmitter.signal_msg('\n\n------------completed!-------------\n\n')
        self.dummyEmitter.signal_msg('输出：'+des)

    def process_excel_file(self):
        src = self.raw_string(self.src_path.text())
        if not src:
            return

        splits = src.rsplit(os.sep, 1)
        name = splits[1].split(".")[0];
        des = self.raw_string(splits[0] + os.sep + "converted_" + name+".txt")
        out = codecs.open(des, 'wb', 'UTF-8')

        timestamp = str(long(time.time()))
        data = xlrd.open_workbook(src)
        table = data.sheets()[0]
        nrows = table.nrows

        for i in range(nrows):
            row = table.row_values(i)
            if row:
                if row[0]:
                    out.write('+' + row[0] + '\n')
                if row[1]:
                    out.write('#' + row[1] + '\n')
                if row[2]:
                    out.write('&' + row[2] + '\n')
                self.dummyEmitter.signal_msg('  '.join(row))
                out.write('@' + timestamp + '\n')
                out.write('$1' + '\n')
        out.close()
        self.dummyEmitter.signal_msg('\n\n------------completed!-------------\n\n')
        self.dummyEmitter.signal_msg('输出：' + des)

    def raw_string(self,s):
        if isinstance(s, str):
            s = s.encode('string-escape')
        elif isinstance(s, unicode):
            s = s.encode('unicode-escape')
        return s


class XmlProcessor():
    def __init__(self):
        print ""

    def process_xml(self):
        print ""


class Worker(QtCore.QThread):
    def __init__(self, func, args):
        super(Worker, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)


class DummyEmitter(QObject):
    trigger = pyqtSignal(str);

    def connect(self,handle_trigger):
        self.trigger.connect(handle_trigger)

    def signal_msg(self,msg):
        self.trigger.emit(msg)


if __name__ == "__main__":
    
    # 解决编码为ascii的问题
    reload(sys)
    sys.setdefaultencoding('utf-8')
    
    app = QtWidgets.QApplication(sys.argv)
    dlg = FileContrast()
    dlg.show()
    sys.exit(app.exec_())