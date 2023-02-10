from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QButtonGroup,QMessageBox
from PyQt5.QtWidgets import QCheckBox,QLabel,QRadioButton
from PyQt5.QtGui import QFont
import sys
app=QApplication(sys.argv)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test")
        self.setGeometry(100,50,700,580)
        self.start1()

    def font(self,obj,x,y):
        obj.setFont(QFont("Times",15))
        obj.move(x,y)

    def font1(self,obj,x,y):
        obj.setFont(QFont("Times",13))
        obj.move(x,y)

    def Hideing(self,obj):
        for i in obj:
            i.hide()

    def start1(self):

        # Test 1
        self.test1=QLabel("1) Hello, what ____ your name? ",self)
        self.font(self.test1,20,30)

        self.t1_a=QRadioButton("A) is",self)
        self.font1(self.t1_a,30,70)

        self.t1_b=QRadioButton("B) are",self)
        self.font1(self.t1_b,180,70)

        self.t1_c=QRadioButton("C) am",self)
        self.font1(self.t1_c,310,70)

        self.t1_d=QRadioButton("D) be",self)
        self.font1(self.t1_d,460,70)

        a1_group=QButtonGroup(self)
        a1_group.addButton(self.t1_a)
        a1_group.addButton(self.t1_b)
        a1_group.addButton(self.t1_c)
        a1_group.addButton(self.t1_d)

        # Test 2
        self.test2=QLabel("2) Where ___ you ___ ?",self)
        self.font(self.test2,20,130)

        self.t2_a=QRadioButton("A) if/from",self)
        self.font1(self.t2_a,30,170)

        self.t2_b=QRadioButton("B) are/in",self)
        self.font1(self.t2_b,180,170)

        self.t2_c=QRadioButton("C) are/is",self)
        self.font1(self.t2_c,310,170)

        self.t2_d=QRadioButton("D) are/from",self)
        self.font1(self.t2_d,460,170)

        a2_group=QButtonGroup(self)
        a2_group.addButton(self.t2_a)
        a2_group.addButton(self.t2_b)
        a2_group.addButton(self.t2_c)
        a2_group.addButton(self.t2_d)

        # Test 3
        self.test3=QLabel("3) ____ are you from ? Japan.",self)
        self.font(self.test3,20,230)

        self.t3_a=QRadioButton("A) What",self)
        self.font1(self.t3_a,30,270)

        self.t3_b=QRadioButton("B) Who",self)
        self.font1(self.t3_b,180,270)

        self.t3_c=QRadioButton("C) Where",self)
        self.font1(self.t3_c,310,270)

        self.t3_d=QRadioButton("D) When",self)
        self.font1(self.t3_d,460,270)

        a3_group=QButtonGroup(self)
        a3_group.addButton(self.t3_a)
        a3_group.addButton(self.t3_b)
        a3_group.addButton(self.t3_c)
        a3_group.addButton(self.t3_d)

        # Test 4
        self.test4=QLabel("4) We ___ students.",self)
        self.font(self.test4,20,330)

        self.t4_a=QRadioButton("A) are a",self)
        self.font1(self.t4_a,30,370)

        self.t4_b=QRadioButton("B) is",self)
        self.font1(self.t4_b,180,370)

        self.t4_c=QRadioButton("C) are",self)
        self.font1(self.t4_c,310,370)

        self.t4_d=QRadioButton("D) am",self)
        self.font1(self.t4_d,460,370)

        a4_group=QButtonGroup(self)
        a4_group.addButton(self.t4_a)
        a4_group.addButton(self.t4_b)
        a4_group.addButton(self.t4_c)
        a4_group.addButton(self.t4_d)

        # Test 5
        self.test5=QLabel("5) This ___ my friend. _____ name's Richard.",self)
        self.font(self.test5,20,430)

        self.t5_a=QRadioButton("A) are/His",self)
        self.font1(self.t5_a,30,470)

        self.t5_b=QRadioButton("B) is/My",self)
        self.font1(self.t5_b,180,470)

        self.t5_c=QRadioButton("C) is/His",self)
        self.font1(self.t5_c,310,470)

        self.t5_d=QRadioButton("D) his/His",self)
        self.font1(self.t5_d,460,470)
        
        a5_group=QButtonGroup(self)
        a5_group.addButton(self.t5_a)
        a5_group.addButton(self.t5_b)
        a5_group.addButton(self.t5_c)
        a5_group.addButton(self.t5_d)

        self.l1=[self.test1,self.test3,self.test3,self.test4,self.test5,self.t1_a,self.t1_b,self.t1_c,self.t1_d,self.t2_a,self.t2_b,self.t2_c,self.t2_d,self.t3_a,self.t3_b,self.t3_c,self.t3_d,self.t4_a,self.t4_b,self.t4_c,self.t4_d,self.t5_a,self.t5_b,self.t5_c,self.t5_d]

        self.check=QPushButton("----------- Check Your Score ----------",self)
        self.font(self.check,100,520)
        self.check.setGeometry(130,520,400,40)
        self.check.clicked.connect(self.run)
    
    def run(self):
        a=0
        if self.t1_a.isChecked():
            a+=1
        if self.t2_d.isChecked():
            a+=1
        if self.t3_c.isChecked():
            a+=1
        if self.t4_c.isChecked():
            a+=1
        if self.t5_c.isChecked():
            a+=1
        # self.Hideing(self.ls)
        self.msgBox=QMessageBox(self) 
        self.msgBox.setWindowTitle("Your Score")
        self.msgBox.setText("\n       Correct     ✅  "+str(a)+"  "+"                       \n\n"+"       Uncorrect  ❎  "+str(5-a)+"         ")
        # self.true=QLabel("✅"+str(a))
        self.msgBox.setFont(QFont("Times",15))
        self.msgBox.show()
        # self.msgBox.setGeometry(230,300,400,500)
win=Window()
win.show()
sys.exit(app.exec_())