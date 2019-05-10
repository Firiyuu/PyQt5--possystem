from PyQt5 import QtWidgets,QtCore
import sys
import os

from db_connection import search_request, fetch_items, add_request, update_budget, fetch_budget, delete_request



class window(QtWidgets.QMainWindow):
    def __init__(self):
        super(window,self).__init__()
        centwid=QtWidgets.QWidget()

        self.mylineEdit = QtWidgets.QLineEdit()
        self.mylineEdit2 = QtWidgets.QLineEdit()
        self.startNew=1
        #initialise to empty string on start up
        self.mylineEdit.setText(' ')


        #barcode scans here and then a returnPressed is registered

        #connect to a function
        self.mylineEdit.returnPressed.connect(self.set_sample_name) #here is where I want to delete the previous entry without backspacing by hand
        self.mylineEdit.textChanged.connect(self.delete_previous)


        total, items = fetch_items()
        print(str(total))
        v_box = QtWidgets.QVBoxLayout()
        message = QtWidgets.QLabel(centwid)
        message.setText("Items Scanned")
        v_box.addWidget(message)

        for item in items:
            item = str(item[0]) + ' - ' + str(item[2]) +'x'
            self.b3 = QtWidgets.QPushButton(item)
            v_box.addWidget(self.b3)
            self.b3.clicked.connect(self.btn_click1)

        v_box.addStretch()
        v_box.addStretch()
        v_box.addStretch()

        curr_budget = fetch_budget()
        curr_budget = curr_budget[0]


        

        self.le = QtWidgets.QLineEdit()
        self.budget = QtWidgets.QPushButton('Enter Budget')
        self.budget_status = QtWidgets.QLabel(centwid)
        self.budget_status.setText("Budget: " + str(curr_budget))

        self.message1 = QtWidgets.QLabel(centwid)
        self.message1.setText("Scan an item: ")

        self.message2 = QtWidgets.QLabel(centwid)
        self.message2.setText("Total: " + str(total))

        self.message3 = QtWidgets.QLabel(centwid)
        self.message3.setText(" ")

        self.budget_message = QtWidgets.QLabel(centwid)

        if total > curr_budget:
            status = "You are over budget!"
        else:
            status = "Still in budget!"
        self.budget_message.setText("Budget Status: " + str(status))


        v_box1 =QtWidgets.QVBoxLayout()



       
        v_box1.addWidget(self.le)
        v_box1.addWidget(self.budget)
        v_box1.addWidget(self.budget_message)
        v_box1.addWidget(self.budget_status)

        v_box1.addStretch()
        v_box1.addWidget(self.message1)
        v_box1.addWidget(self.message2)
        v_box1.addWidget(self.mylineEdit)
        v_box1.addWidget(self.message3)    

        v_box1.addStretch()
        v_box1.addStretch()

        lay=QtWidgets.QHBoxLayout()



        
        lay.addLayout(v_box1)
        lay.addLayout(v_box)

        centwid.setLayout(lay)
        self.budget.clicked.connect(self.btn_click)
        
        self.setCentralWidget(centwid)
        self.show()

    def btn_click(self):
        sender = self.sender()
        if sender.text() == 'Enter Budget':
            print(self.le.text())
            budget = float(self.le.text())
            update_budget(budget)
            curr_budget = fetch_budget()
            curr_budget = curr_budget[0]
            self.budget_status.setText("Budget: " + str(curr_budget))
       
 

    def btn_click1(self):
        sender = self.sender()
        item = sender.text()
        item = item.split('-')[0]
        item = item.strip()
        delete_request(item)
        self.restart_program()


        #set the sample name variable
    def set_sample_name(self):
        self.sample_name = self.mylineEdit.text()
        print(self.sample_name)
        request = search_request(self.sample_name)
        if request is not False:
            item, value = search_request(self.sample_name)
            print(str(item) + '-' + str(value))
            add_request(str(item), str(value))
            self.restart_program()
            self.startNew=1
        else:
            self.message3.setText("Item does not exist")
            self.startNew=1

    def delete_previous(self,text):
        if self.startNew:
            self.mylineEdit.setText(text[-1])
            self.startNew=0

    def restart_program(self):
        """Restarts the current program.
        Note: this function does not return. Any cleanup action (like
        saving data) must be done before calling this function."""
        python = sys.executable
        os.execl(python, python, * sys.argv)



app=QtWidgets.QApplication(sys.argv)

ex=window()
ex.setWindowTitle('POS System')
ex.setGeometry(100, 100, 800, 480)
sys.exit(app.exec_())