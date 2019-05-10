import sys
from PyQt5 import QtWidgets, QtGui



def window():
		app = QtWidgets.QApplication(sys.argv)
		w = QtWidgets.QWidget()

		b= QtWidgets.QPushButton(w)
		l = QtWidgets.QLabel(w)


		b.setText("Clear")
		l.setText("Items Cleared")

		h_box = QtWidgets.QVBoxLayout()
		h_box.addStretch()
		h_box.addWidget(l)
		h_box.addWidget(b)
		h_box.addStretch()



		v_box = QtWidgets.QVBoxLayout()
		v_box.addWidget(b)
		v_box.addWidget(l)

		w.setLayout(h_box)




		w.setWindowTitle('POS System')
		w.setGeometry(100, 100, 800, 480)



		b.move(400,240)
		l.move(100, 100)

		w.show()
		sys.exit(app.exec_())

window()