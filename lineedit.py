import sys
from PyQt5 import QtWidgets
from db_connection import search_request, fetch_items, add_request



class Window(QtWidgets.QWidget):

	def __init__(self):
		super().__init__()

		self.init_ui()

	def init_ui(self):

		total, items = fetch_items()
		print(str(total))

		self.le = QtWidgets.QLineEdit()
		self.b = QtWidgets.QPushButton('Clear')
		self.b2 = QtWidgets.QPushButton('Print')




		v_box = QtWidgets.QVBoxLayout()
		for item in items:
			item = str(item[0])

			self.b3 = QtWidgets.QPushButton(item)
			v_box.addWidget(self.b3)



		h_box = QtWidgets.QHBoxLayout()
		h_box.addWidget(self.le)
		h_box.addWidget(self.b)

		h_box.addWidget(self.b2)

		h_box.addLayout(v_box)


		self.setLayout(h_box)

		self.b.clicked.connect(self.btn_click)
		h_box.update()

		self.b2.clicked.connect(self.btn_click)



		self.show()

	def btn_click(self):
		sender = self.sender()
		if sender.text() == 'Print':
			item, value = search_request(self.le.text())
			print(str(item) + '-' + str(value))
			add_request(str(item), str(value))



		else:
			self.le.clear()



app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())