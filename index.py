import datetime
import random

from PyQt5 import QtCore, QtGui, QtWidgets
import os

from PyQt5.QtCore import Qt, QDateTime, QDate
from PyQt5.QtWidgets import QWidget, QTableWidget, QHeaderView, QAbstractItemView, QTableWidgetItem, QMessageBox, QMenu


class Enter_info(QWidget):
    #判断文件是否存在


    def init_file(self):
        path = 'info.txt'
        if not os.path.exists(path):
            f=open(path,'w',encoding='utf-8')
            f.close()
        else:
            pass
    #把数据装进list
    def init_data(self):
        path = 'info.txt'
        self.info = []
        with open(path, 'r', encoding='utf-8') as file:
            txt_infos = file.readlines()
            for i in txt_infos:
                self.info.append(i.replace('\n', ''))

    # 把数据装进表格
    def get_all(self):
        self.all_len = len(self.info)
        if self.all_len==0:
            self.tableView.setRowCount(self.all_len)
            QMessageBox.information(self,"提示","没有数据",  QMessageBox.Yes | QMessageBox.No)
        else:
            self.tableView.setRowCount(self.all_len)
            for i, j in zip(self.info, range(self.all_len)):
                for k in range(11):

                    newItem = QTableWidgetItem(i.split(",")[k])
                    newItem.setTextAlignment(Qt.AlignHCenter)
                    self.tableView.setItem(j, k,newItem)

    def setupUi(self, Form):
        self.sear_key='姓名'
        self.flag=False
        self.init_file()
        self.init_data()
        Form.setObjectName("Form")
        Form.setFixedSize(1220, 771)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 30, 54, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(270, 30, 54, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(580, 30, 54, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 110, 54, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(270, 70, 54, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(590, 70, 54, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(580, 110, 81, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(40, 70, 51, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(270, 110, 51, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(40, 150, 51, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.line_id = QtWidgets.QLineEdit(Form)
        self.line_id.setGeometry(QtCore.QRect(90, 220, 141, 20))
        self.line_id.setObjectName("lineE_id")
        self.line_id.setText("333")
        self.line_id.setVisible(False)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(90, 30, 141, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QComboBox(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(340, 30, 201, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.addItems(['男','女'])
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(660, 30, 221, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 70, 141, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(340, 70, 201, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(660, 70, 221, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QDateTimeEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(670, 110, 211, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setCalendarPopup(True)
        self.lineEdit_7.setDisplayFormat("yyyy-MM-dd")
        self.lineEdit_8 = QtWidgets.QLineEdit(Form)
        self.lineEdit_8.setGeometry(QtCore.QRect(92, 110, 141, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(Form)
        self.lineEdit_9.setGeometry(QtCore.QRect(340, 110, 201, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(90, 150, 381, 71))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(580, 190, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_change = QtWidgets.QPushButton("修改信息",Form)
        self.pushButton_change.setGeometry(QtCore.QRect(700, 190, 75, 23))
        self.pushButton_change.setObjectName("pushButton_change")
        self.pushButton_change.setVisible(False)

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(74, 290, 81, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(780, 290, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(330, 295, 91, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(420, 290, 111, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit_10 = QtWidgets.QLineEdit(Form)
        self.lineEdit_10.setGeometry(QtCore.QRect(550, 290, 161, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_star_time = QtWidgets.QDateTimeEdit(Form)
        self.lineEdit_star_time.setGeometry(QtCore.QRect(550, 290, 100, 20))
        self.lineEdit_star_time.setObjectName("lineEdit_star_time")
        self.lineEdit_end_time = QtWidgets.QDateTimeEdit(Form)
        self.lineEdit_end_time.setGeometry(QtCore.QRect(655, 290, 100, 20))
        self.lineEdit_end_time.setObjectName("lineEdit_end_time")
        self.lineEdit_star_time.setCalendarPopup(True)
        self.lineEdit_star_time.setDisplayFormat("yyyy-MM-dd")
        self.lineEdit_end_time.setCalendarPopup(True)
        self.lineEdit_end_time.setDisplayFormat("yyyy-MM-dd")
        self.lineEdit_end_time.setVisible(False)
        self.lineEdit_star_time.setVisible(False)
        self.tableView = QTableWidget(Form)
        self.tableView.setGeometry(QtCore.QRect(10, 350, 1200, 411))
        self.tableView.setObjectName("tableView")
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.tableView.setColumnCount(11)
        self.tableView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableView.customContextMenuRequested.connect(self.generateMenu)
        self.tableView.horizontalHeader().setSectionResizeMode(10, QHeaderView.ResizeToContents)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.setHorizontalHeaderLabels(['编号','姓名','性别','身份证','专业','电话','部门','地址','职务','参加工作时间','备注'])
        self.get_all()
        self.retranslateUi(Form)
        self.button_con()
        QtCore.QMetaObject.connectSlotsByName(Form)

    # 右键菜单
    def generateMenu(self, pos):
        menu = QMenu()
        item1 = menu.addAction(u"修改")
        item2 = menu.addAction(u"删除")
        action = menu.exec_(self.tableView.mapToGlobal(pos))
        if action==item2:
            self.pushButton_change.setVisible(True)
            indexs = self.tableView.currentIndex().row()
            model = self.tableView.model()
            idst = model.index(indexs, 0)
            ids=model.data(idst)
            result=[]
            with open("info.txt", 'r+', encoding='utf-8') as f:
                txt_info = f.readlines()
                for txt in txt_info:
                    result.append(txt.replace('\n', ''))
                f.close()
            for re in range(len(result)):
                id = result[re].split(",")[0]
                if id == str(ids):
                    result.remove(result[re])
            with open("info.txt", 'r+', encoding='utf-8') as f1:
                f1.truncate()
                f1.close()
            with open("info.txt", 'a+', encoding='utf-8') as f2:
                for text in result:
                    f2.write(text + '\n')
                f2.close()
            self.get_all_data()
            QMessageBox.information(self, '提示', '删除成功')
        if action == item1:
            self.flag=True
            self.pushButton_change.setVisible(True)
            indexs = self.tableView.currentIndex().row()
            model = self.tableView.model()
            id = model.index(indexs, 0)
            name = model.index(indexs, 1)
            sex = model.index(indexs, 2)
            iden = model.index(indexs, 3)
            major = model.index(indexs, 4)
            tel = model.index(indexs, 5)
            apart = model.index(indexs, 6)
            address = model.index(indexs, 7)
            positon = model.index(indexs, 8)
            brithday = model.index(indexs, 9)
            info = model.index(indexs, 10)
            self.lineEdit.setText(model.data(name))
            if model.data(sex)=='男':
                self.lineEdit_2.setItemText(0,model.data(sex))
                self.lineEdit_2.setItemText(1, '女')
            else:
                self.lineEdit_2.setItemText(0, model.data(sex))
                self.lineEdit_2.setItemText(1, '男')
            self.line_id.setText(model.data(id))
            self.lineEdit_3.setText(model.data(iden))
            self.lineEdit_4.setText(model.data(major))
            self.lineEdit_5.setText(model.data(tel))
            self.lineEdit_6.setText(model.data(apart))
            self.lineEdit_8.setText(model.data(address))
            self.lineEdit_9.setText(model.data(positon))
            self.lineEdit_7.setDate(QDate.currentDate())
            a = QDate.fromString(model.data(brithday), "yyyy-MM-dd")
            self.lineEdit_7.setDate(a)
            self.textEdit.setPlainText(model.data(info))
    #按钮链接
    def button_con(self):
        self.pushButton.clicked.connect(self.get_enter)
        self.pushButton_2.clicked.connect(self.get_all_data)
        self.pushButton_change.clicked.connect(self.get_change)
        self.comboBox.currentIndexChanged.connect(self.get_search_key)
        self.pushButton_3.clicked.connect(self.get_search_result)

    # 按钮搜索
    def get_search_result(self):
        key_word=self.lineEdit_10.text()
        if self.sear_key=='出生日期范围':
            star_time=self.lineEdit_star_time.text()
            end_time=self.lineEdit_end_time.text()
            d1 = datetime.date(int(star_time.split('-')[0]), int(star_time.split('-')[1]), int(star_time.split('-')[2]))
            d2 = datetime.date(int(end_time.split('-')[0]), int(end_time.split('-')[1]), int(end_time.split('-')[2]))
            if (d2 - d1).days<0:
                QMessageBox.information(self,'提示','开始日期不能小于结束日期')
            else:
                result = self.set_key_get_data(self.sear_key, '',star_time,end_time)
                self.info = result
                self.get_all()
        else:
            result=self.set_key_get_data(self.sear_key,key_word,'','')
            self.info=result
            self.get_all()

    # 搜索获取数据
    def set_key_get_data(self,key,word,star,end):
        result=[]
        return_result=[]
        with open("info.txt", 'r+', encoding='utf-8') as f:
            txt_info = f.readlines()
            for txt in txt_info:
                result.append(txt.replace('\n', ''))
            f.close()
        for i in result:
            if key == '姓名':
                if word == i.split(",")[1]:
                    return_result.append(i)
            if key == '性别':
                if word == i.split(",")[2]:
                    return_result.append(i)
            if key == '编号':
                if word == i.split(",")[0]:
                    return_result.append(i)
            if key == '身份证':
                if word == i.split(",")[3]:
                    return_result.append(i)
            if key == '专业':
                if word == i.split(",")[4]:
                    return_result.append(i)
            if key == '部门':
                if word == i.split(",")[5]:
                    return_result.append(i)
            if key=='出生日期范围':
                d_time1 = datetime.datetime.strptime(str(star), '%Y-%m-%d')
                d_time2 = datetime.datetime.strptime(str(end), '%Y-%m-%d')
                n_time = datetime.datetime.strptime(str(i.split(",")[9]), '%Y-%m-%d')
                if n_time >= d_time1 and n_time <= d_time2:
                    return_result.append(i)

        return return_result
    # 得到搜索的关键词
    def get_search_key(self):
        self.sear_key=self.comboBox.currentText()
        if self.sear_key=='出生日期范围':
            self.lineEdit_star_time.setVisible(True)
            self.lineEdit_end_time.setVisible(True)
            self.lineEdit_10.setVisible(False)
        else:
            self.lineEdit_star_time.setVisible(False)
            self.lineEdit_end_time.setVisible(False)
            self.lineEdit_10.setVisible(True)
    #查看全部
    def get_all_data(self):
        self.init_data()
        self.get_all()

    # 修改数据
    def get_change(self):
        ids=self.line_id.text()
        name = self.lineEdit.text()
        sex = self.lineEdit_2.currentText()
        iden = self.lineEdit_3.text()
        major = self.lineEdit_4.text()
        tel = self.lineEdit_5.text()
        apart = self.lineEdit_6.text()
        address = self.lineEdit_8.text()
        positon = self.lineEdit_9.text()
        brithday = self.lineEdit_7.text()
        info = self.textEdit.toPlainText()
        if name == '' or iden == '' or major == '' or tel == '' or apart == '' or address == '' or positon == '' or info == '':
            QMessageBox.information(self, '提示', '修改的信息不能为空')
        result = []
        with open("info.txt", 'r+', encoding='utf-8') as f:
            txt_info = f.readlines()
            for txt in txt_info:
                result.append(txt.replace('\n', ''))
            f.close()
        for re in range(len(result)):
            id = result[re].split(",")[0]
            if id == str(ids):
                result[re] = id+','+name+','+sex+','+iden+','+major+','+tel+','+apart+','+address+','+positon+','+brithday+','+info
        with open("info.txt", 'r+', encoding='utf-8') as f1:
            f1.truncate()
            f1.close()
        with open("info.txt", 'a+', encoding='utf-8') as f2:
            for text in result:
                f2.write(text+'\n')
            f2.close()
        self.init_data()
        self.get_all()
        self.flag=False
        self.line_id.setText('')
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')
        self.lineEdit_5.setText('')
        self.lineEdit_6.setText('')
        self.lineEdit_8.setText('')
        self.lineEdit_9.setText('')
        self.textEdit.setPlainText('')
        QMessageBox.information(self, '提示', '修改成功')

    # 判断用户是否存在
    def testing_id(self,id):
        flag = False
        with open('info.txt', 'r', encoding='utf-8') as f:
            for i in f.readlines():
                if str(id) == i.replace('\n', '').split(',')[0]:
                    flag = True
                    break
        f.close()
        return flag
    #数据数据
    def get_enter(self):
        if self.flag==True:
            QMessageBox.information(self, '提示', '请点击修改信息')
        else:
            name=self.lineEdit.text()
            sex = self.lineEdit_2.currentText()
            iden = self.lineEdit_3.text()
            major = self.lineEdit_4.text()
            tel = self.lineEdit_5.text()
            apart = self.lineEdit_6.text()
            address = self.lineEdit_8.text()
            positon= self.lineEdit_9.text()
            brithday = self.lineEdit_7.text()
            info = self.textEdit.toPlainText()
            while True:
                id = random.randint(10000, 99999)
                had_id = self.testing_id(id)
                if had_id==False:
                    break
            if name==''or iden=='' or major=='' or tel=='' or apart=='' or address=='' or positon=='' or info=='':
                QMessageBox.information(self,'提示','输入的信息不能为空')
            else:
                txt=str(id)+','+name+','+sex+','+iden+','+major+','+tel+','+apart+','+address+','+positon+','+brithday+','+info
                with open('info.txt','a+',encoding='utf-8') as f:
                    f.write(txt+'\n')
                    f.close()
                QMessageBox.information(self, '提示', '提交成功')
                self.init_data()
                self.get_all()
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "信息管理"))
        self.label.setText(_translate("Form", "姓名："))
        self.label_2.setText(_translate("Form", "性别："))
        self.label_3.setText(_translate("Form", "身份证："))
        self.label_4.setText(_translate("Form", "地址："))
        self.label_5.setText(_translate("Form", "电话:"))
        self.label_6.setText(_translate("Form", "部门:"))
        self.label_7.setText(_translate("Form", "出生日期："))
        self.label_8.setText(_translate("Form", "专业："))
        self.label_9.setText(_translate("Form", "职务："))
        self.label_10.setText(_translate("Form", "备注："))
        self.pushButton.setText(_translate("Form", "录入信息"))
        self.pushButton_2.setText(_translate("Form", "查看全部"))
        self.pushButton_3.setText(_translate("Form", "查找"))
        self.label_11.setText(_translate("Form", "按类型查找"))
        self.comboBox.setItemText(0, _translate("Form", "姓名"))
        self.comboBox.setItemText(1, _translate("Form", "性别"))
        self.comboBox.setItemText(2, _translate("Form", "身份证"))
        self.comboBox.setItemText(3, _translate("Form", "专业"))
        self.comboBox.setItemText(4, _translate("Form", "部门"))
        self.comboBox.setItemText(5, _translate("Form", "出生日期范围"))
        self.comboBox.setItemText(6, _translate("Form", "编号"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Enter_info()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())