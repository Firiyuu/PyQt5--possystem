from PyQt5 import QtWidgets,QtCore
import sys
import os
import sip
from db_connection import clear_scan, search_request, fetch_items, add_request, update_budget, fetch_budget, delete_request, search_request_delete, reduce_quantity_scan, reduce_quantity_item, increase_quantity_item, search_request_delete_item



class window(QtWidgets.QMainWindow):
    def __init__(self):
        super(window,self).__init__()
        centwid=QtWidgets.QWidget()

        self.mylineEdit = QtWidgets.QLineEdit()

        f = self.mylineEdit.font()
        f.setPointSize(24) # sets the size to 27
        self.mylineEdit.setFont(f)


        self.mylineEdit2 = QtWidgets.QLineEdit()


        self.startNew=1
        #initialise to empty string on start up
        self.mylineEdit.setText(' ')
        self.toggle = False

        #barcode scans here and then a returnPressed is registered

        #connect to a function
        self.mylineEdit.returnPressed.connect(self.set_sample_name) #here is where I want to delete the previous entry without backspacing by hand
        self.mylineEdit.textChanged.connect(self.delete_previous)


        total, items = fetch_items()
        print(str(total))
        self.v_box = QtWidgets.QVBoxLayout()
        message = QtWidgets.QLabel(centwid)
        message.setText("Items Scanned")
        f = message.font()
        f.setPointSize(7) # sets the size to 27
        f.setBold(True)
        message.setFont(f)

        self.v_box.addWidget(message)



        self.v_box.addStretch()
        self.v_box.addStretch()
        self.v_box.addStretch()

        curr_budget = fetch_budget()
        curr_budget = curr_budget[0]

        self.welcome = QtWidgets.QLabel(centwid)
        self.welcome.setText("ENJOY YOUR SHOPPING!")
        f = self.welcome.font()
        f.setPointSize(24) # sets the size to 27
        f.setBold(True)
        self.welcome.setFont(f)




        self.le = QtWidgets.QLineEdit()
        g = self.le.font()
        g.setPointSize(24) # sets the size to 27
        self.le.setFont(g)

        self.budget = QtWidgets.QPushButton('Enter Budget')
        self.budget.setSizePolicy(
        QtWidgets.QSizePolicy.Preferred,
        QtWidgets.QSizePolicy.Expanding)


        self.done = QtWidgets.QPushButton('Done Shopping')
        self.done.setSizePolicy(
        QtWidgets.QSizePolicy.Preferred,
        QtWidgets.QSizePolicy.Expanding)


        self.budget_status = QtWidgets.QLabel(centwid)
        self.budget_status.setText("Budget: " + str(curr_budget))
        f = self.budget_status.font()
        f.setPointSize(10) # sets the size to 27
        f.setBold(True)
        self.budget_status.setFont(f)

        self.message1 = QtWidgets.QLabel(centwid)
        self.message1.setText("Scan an item: ")
        f = self.message1.font()
        f.setPointSize(10) # sets the size to 27
        f.setBold(True)
        self.message1.setFont(f)


        self.message2 = QtWidgets.QLabel(centwid)
        self.message2.setText("Total: " + str(total))
        f = self.message2.font()
        f.setPointSize(10) # sets the size to 27
        f.setBold(True)
        self.message2.setFont(f)

        self.message3 = QtWidgets.QLabel(centwid)
        self.message3.setText(" ")

        self.message4 = QtWidgets.QLabel(centwid)
        self.message4.setText(" ")


        self.budget_message = QtWidgets.QLabel(centwid)

        if total > (curr_budget*70)/100:
            if total > curr_budget: 
                status = "You are over budget!"
                QtWidgets.QMessageBox.about(self, "Warning!!", "You are over budget!")
            else:
                status = "You are close to over budgeting!"
                QtWidgets.QMessageBox.about(self, "Caution!!", "You are close to over budgeting!")

        else:
            status = "Still in budget!"
        self.budget_message.setText("Budget Status: " + str(status))
        f = self.budget_message.font()
        f.setPointSize(10) # sets the size to 27
        f.setBold(True)
        self.budget_message.setFont(f)

        self.v_box1 =QtWidgets.QVBoxLayout()



        self.v_box1.addWidget(self.welcome)
        self.v_box1.addWidget(self.le)
        self.v_box1.addWidget(self.budget)
        self.v_box1.addWidget(self.budget_message)
        self.v_box1.addWidget(self.budget_status)

        self.v_box1.addStretch()
        self.v_box1.addWidget(self.message1)
        self.v_box1.addWidget(self.message2)
        self.v_box1.addWidget(self.mylineEdit)
        self.v_box1.addWidget(self.message3)    
        self.v_box1.addWidget(self.done)
        self.v_box1.addStretch()
        self.v_box1.addStretch()



        lay=QtWidgets.QHBoxLayout()



        
        lay.addLayout(self.v_box1)
        lay.addLayout(self.v_box)
 


        centwid.setLayout(lay)
        self.budget.clicked.connect(self.btn_click)
        self.done.clicked.connect(self.btn_click3)
        
        self.setCentralWidget(centwid)

        self.show()

    def btn_click(self):
      
        sender = self.sender()

        if sender.text() == 'Enter Budget' and self.le.text() != '':
            if self.toggle is True:
                print(self.le.text())
                budget = float(self.le.text())
                update_budget(budget)
                curr_budget = fetch_budget()
                curr_budget = curr_budget[0]
                self.budget_status.setText("Budget: " + str(curr_budget))
                self.le.hide()
                self.toggle = False
            else:
                self.toggle = True
                self.le.show()
        

    def btn_click1(self):
        sender = self.sender()
        item = sender.text()
        item = item.split('-')[0]
        item = item.strip()
        item, quantity = search_request_delete(item)
        print(str(quantity))
        if int(quantity) == 1:
           delete_request(item)
        else:
           reduce_quantity_scan(item)
           increase_quantity_item(item)
        self.restart_program()

    def btn_click3(self):
        text = 'Items:\n\n'
        total, items = fetch_items()
        for item in items:
            value = str(item[2])
            item = str(item[0]) + ' - ' + value  +'x'
            text+=item +'\n'
        text = text + '\n' + 'Total: ' + str(total)

        QtWidgets.QMessageBox.about(self, "Summary",text)
        clear_scan()
        update_budget(0)
        self.restart_program()

        #set the sample name variable
    def set_sample_name(self):
        self.sample_name = self.mylineEdit.text()
        print(self.sample_name)
        request = search_request(self.sample_name)
        if request is not False:
            item, value = search_request(self.sample_name)
            if int(value) == 0:
                value = ''
            print(str(item) + '-' + str(value))
            item_, quantity = search_request_delete_item(item)
            print(str(quantity))
            if quantity > 1:
                add_request(str(item), str(value))
                reduce_quantity_item(str(item))
                self.restart_program()
                self.startNew=1
            else:
                self.message3.setText("There's no stock for this item anymore")
                self.startNew=1              
        else:
            self.message3.setText("Item does not exist")
            self.startNew=1

    def delete_previous(self,text):
        if self.startNew:
            self.mylineEdit.setText(text[-1])
            self.startNew=0


    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    def restart_program(self):

    
            total, items = fetch_items()

            self.clearLayout(self.v_box)
                     

            for item in items:
                value = str(item[2])
                if int(value) == 0:
                    value = ''
                item = str(item[0]) + ' - ' + value  +'x'
                self.b3 = QtWidgets.QPushButton(item)
                self.b3.setSizePolicy(
                QtWidgets.QSizePolicy.Preferred,
                QtWidgets.QSizePolicy.Expanding)

                self.v_box.addWidget(self.b3)
                self.b3.clicked.connect(self.btn_click1)


            curr_budget = fetch_budget()
            curr_budget = curr_budget[0]
            self.message2.setText("Total: " + str(total))
            f = self.message2.font()
            f.setPointSize(10) # sets the size to 27
            f.setBold(True)
            self.message2.setFont(f)

            self.budget_status.setText("Budget: " + str(curr_budget))
            f = self.budget_status.font()
            f.setPointSize(10) # sets the size to 27
            f.setBold(True)
            self.budget_status.setFont(f)

            self.message3.setText(" ")


            if total > (curr_budget*70)/100:
                if total > curr_budget: 
                    status = "You are over budget!"
                    QtWidgets.QMessageBox.about(self, "Warning!!", "You are over budget!")
                else:
                    status = "You are close to over budgeting!"
                    QtWidgets.QMessageBox.about(self, "Caution!!", "You are close to over budgeting!")

            else:
                status = "Still in budget!"




   

app=QtWidgets.QApplication(sys.argv)

ex=window()
ex.setWindowTitle('POS System')
ex.setGeometry(100, 100, 800, 480)
sys.exit(app.exec_())
