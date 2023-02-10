from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QMainWindow
from PyQt5.QtWidgets import QCheckBox,QLabel
from PyQt5.QtGui import QFont
import sys
app=QApplication(sys.argv)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu")
        self.setGeometry(100,100,620,500)
        # self.win2=Window2()
        self.start1()

    def Hideing(self,obj):
        for i in obj:
            i.hide()
    def font(self,obj,x,y):
        obj.setFont(QFont("Times",18))
        obj.move(x,y)

    def font1(self,obj,x,y):
        obj.setFont(QFont("Times",15))
        obj.move(x,y)
        # obj.setFixedSize(150,50)
    def start1(self):
        self.t1=QLabel("1-TAOM",self)
        self.font(self.t1,30,10)

        self.t1_v1=QCheckBox(" Sho'rva",self)
        self.font1(self.t1_v1,35,50)

        self.t1_v2=QCheckBox(" Mastva",self)
        self.font1(self.t1_v2,35,80)

        self.t1_v3=QCheckBox(" Lag'mon",self)
        self.font1(self.t1_v3,35,110)

        self.t1_v4=QCheckBox(" Chuchvara",self)
        self.font1(self.t1_v4,35,140)

        self.n=QLabel("Narx",self)
        self.font1(self.n,200,10)

        self.t1_v1_n=QLabel("22000",self)
        self.font1(self.t1_v1_n,200,50)

        self.t1_v2_n=QLabel("17000",self)
        self.font1(self.t1_v2_n,200,80)

        self.t1_v3_n=QLabel("26000",self)
        self.font1(self.t1_v3_n,200,110)

        self.t1_v4_n=QLabel("18000",self)
        self.font1(self.t1_v4_n,200,140)
       
        self.t2=QLabel("2-TAOM",self)
        self.font(self.t2,350,10)

        self.t2_v1=QCheckBox(" Osh",self)
        self.font1(self.t2_v1,350,50)

        self.t2_v2=QCheckBox(" Bishteks",self)
        self.font1(self.t2_v2,350,80)

        self.t2_v3=QCheckBox(" Beshbarmoq",self)
        self.font1(self.t2_v3,350,110)
        self.t2_v3.adjustSize()

        self.t2_v4=QCheckBox(" Dimlama",self)
        self.font1(self.t2_v4,350,140)
        self.t2_v4.adjustSize()


        self.n1=QLabel("Narx",self)
        self.font1(self.n1,520,10)

        self.t2_v1_n=QLabel("30000",self)
        self.font1(self.t2_v1_n,520,50)

        self.t2_v2_n=QLabel("27000",self)
        self.font1(self.t2_v2_n,520,80)

        self.t2_v3_n=QLabel("45000",self)
        self.font1(self.t2_v3_n,520,110)

        self.t2_v4_n=QLabel("35000",self)
        self.font1(self.t2_v4_n,520,140)

        self.t3=QLabel("DISERT",self)
        self.font(self.t3,30,200)

        self.t3_v1=QCheckBox(" Tort",self)
        self.font1(self.t3_v1,35,240)

        self.t3_v2=QCheckBox(" Pirok",self)
        self.font1(self.t3_v2,35,270)

        self.t3_v3=QCheckBox(" Pahlava",self)
        self.font1(self.t3_v3,35,300)

        self.t3_v4=QCheckBox(" Muzqaymoq",self)
        self.font1(self.t3_v4,35,330)
        self.t3_v4.adjustSize()

        # self.t1=QLabel("Narx",self)
        # self.font1(self.t1,200,10)

        self.t3_v1_n=QLabel("12000",self)
        self.font1(self.t3_v1_n,200,240)

        self.t3_v2_n=QLabel("7000",self)
        self.font1(self.t3_v2_n,200,270)

        self.t3_v3_n=QLabel("25000",self)
        self.font1(self.t3_v3_n,200,300)

        self.t3_v4_n=QLabel("10000",self)
        self.font1(self.t3_v4_n,200,330)


        self.t4=QLabel("ICHIMLIKLAR",self)
        self.font(self.t4,350,200)
        self.t4.adjustSize()


        self.t4_v1=QCheckBox(" Choy",self)
        self.font1(self.t4_v1,350,240)

        self.t4_v2=QCheckBox(" Pepsi",self)
        self.font1(self.t4_v2,350,270)

        self.t4_v3=QCheckBox(" Fanta",self)
        self.font1(self.t4_v3,350,300)

        self.t4_v4=QCheckBox(" Moxito",self)
        self.font1(self.t4_v4,350,330)


        self.t4_v1_n=QLabel("6000",self)
        self.font1(self.t4_v1_n,520,240)

        self.t4_v2_n=QLabel("12000",self)
        self.font1(self.t4_v2_n,520,270)

        self.t4_v3_n=QLabel("11000",self)
        self.font1(self.t4_v3_n,520,300)

        self.t4_v4_n=QLabel("10000",self)
        self.font1(self.t4_v4_n,520,330)

        
        self.Sign_up=QPushButton("Check",self)
        self.Sign_up.setFont(QFont("Times",16))
        self.Sign_up.setGeometry(210,390,200,40)
        self.Sign_up.clicked.connect(self.run1)

        self.l1=[self.t2,self.t3,self.t4,self.Sign_up,self.n,self.t1_v1,self.t1_v2,self.t1_v3,self.t1_v4,self.t1_v1_n,self.t1_v2_n,self.t1_v3_n,self.t1_v4_n]
        self.l2=[self.n1,self.t2_v1,self.t2_v2,self.t2_v3,self.t2_v4,self.t2_v1_n,self.t2_v2_n,self.t2_v3_n,self.t2_v4_n]
        self.l3=[self.t3_v1,self.t3_v2,self.t3_v3,self.t3_v4,self.t3_v1_n,self.t3_v2_n,self.t3_v3_n,self.t3_v4_n]
        self.l4=[self.t4_v1,self.t4_v2,self.t4_v3,self.t4_v4,self.t4_v1_n,self.t4_v2_n,self.t4_v3_n,self.t4_v4_n]


    def run1(self):
        self.setWindowTitle("Hisob")
        self.setGeometry(270,100,300,550)

        self.t1.setText("----------Hisob----------\n\n")
        hisob=[]
        if self.t1_v1.isChecked():
            self.t1.setText(self.t1.text()+self.t1_v1.text()+"           "+self.t1_v1_n.text()+"\n")
            hisob.append(self.t1_v1_n)
        if self.t1_v2.isChecked():
            self.t1.setText(self.t1.text()+self.t1_v2.text()+"           "+self.t1_v2_n.text()+"\n")
        if self.t1_v3.isChecked():
            self.t1.setText(self.t1.text()+self.t1_v3.text()+"          "+self.t1_v3_n.text()+"\n")
        if self.t1_v4.isChecked():
            self.t1.setText(self.t1.text()+self.t1_v4.text()+"       "+self.t1_v4_n.text()+"\n")

        if self.t2_v1.isChecked():
            self.t1.setText(self.t1.text()+self.t2_v1.text()+"                "+self.t2_v1_n.text()+"\n")
        if self.t2_v2.isChecked():
            self.t1.setText(self.t1.text()+self.t2_v2.text()+"          "+self.t2_v2_n.text()+"\n")
        if self.t2_v3.isChecked():
            self.t1.setText(self.t1.text()+self.t2_v3.text()+"     "+self.t2_v3_n.text()+"\n")
        if self.t2_v4.isChecked():
            self.t1.setText(self.t1.text()+self.t2_v4.text()+"          "+self.t2_v4_n.text()+"\n")

        if self.t3_v1.isChecked():
            self.t1.setText(self.t1.text()+self.t3_v1.text()+"                "+self.t3_v1_n.text()+"\n")
        if self.t3_v2.isChecked():
            self.t1.setText(self.t1.text()+self.t3_v2.text()+"               "+self.t3_v2_n.text()+"\n")
        if self.t3_v3.isChecked():
            self.t1.setText(self.t1.text()+self.t3_v3.text()+"            "+self.t3_v3_n.text()+"\n")
        if self.t3_v4.isChecked():
            self.t1.setText(self.t1.text()+self.t3_v4.text()+"      "+self.t3_v4_n.text()+"\n")

        if self.t4_v1.isChecked():
            self.t1.setText(self.t1.text()+self.t4_v1.text()+"               "+self.t4_v1_n.text()+"\n")
        if self.t4_v2.isChecked():
            self.t1.setText(self.t1.text()+self.t4_v2.text()+"               "+self.t4_v2_n.text()+"\n")
        if self.t4_v3.isChecked():
            self.t1.setText(self.t1.text()+self.t4_v3.text()+"              "+self.t4_v3_n.text()+"\n")
        if self.t4_v4.isChecked():
            self.t1.setText(self.t1.text()+self.t4_v4.text()+"             "+self.t4_v4_n.text()+"\n")
        self.Hideing(self.l1)
        self.Hideing(self.l2)
        self.Hideing(self.l3)
        self.Hideing(self.l4)
        self.t1.adjustSize()
       
win=Window()
win.show()
sys.exit(app.exec_())