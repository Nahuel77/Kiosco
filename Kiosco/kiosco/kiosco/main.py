import sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import *
from PySide2.QtCore import QFile
from PySide2 import QtCore, QtWidgets
import time

import sqlite3

GLOBAL_STATE = 0

class Kiosco(QMainWindow):

	db_name = 'dbk.db'

	def __init__(self):
		super(Kiosco, self).__init__()
		self.ui = QUiLoader().load(QFile('UI_Kiosco.ui'))
		self.get_ventas()

		# Set Ui Definitions
		UIFunctions.uiDefinitions(self)

		# fecha y hora
		self.hour = time.strftime('%H:%M')
		# interfaz ventas
		# inputs
		self.ingreso_entry = self.ui.ingreso_entry
		self.adicional_entry = self.ui.adicional_entry
		# botones
		self.ui.btn_agregar.clicked.connect(self.add_venta)
		self.ui.btn_borrar.clicked.connect(self.delete_venta)

		self.ui.listaVentas.setColumnHidden(0, True)

	def run_query(self, query, parameters = ()):
		with sqlite3.connect(self.db_name) as conn:
			cursor = conn.cursor()
			cursor.execute(query, parameters)
			result = cursor.fetchall()
			conn.commit()
		return result

	def get_ventas(self):
		query = 'SELECT id, horario, valor, adicional FROM ventas'
		db_rows = self.run_query(query)
		print()
		self.ui.listaVentas.setColumnCount(4)
		self.ui.listaVentas.setRowCount(len(db_rows))
		self.ui.listaVentas.setHorizontalHeaderLabels(['Id', 'Horario','Monto','Adicional'])
		for row in range(len(db_rows)):
			for column in range(len(db_rows[0])):
				self.ui.listaVentas.setItem(
					row,
					column,
					QTableWidgetItem(str(db_rows[row][column]))
				)

	def validation(self):
		return len(self.ui.ingreso_entry.text()) != 0

	def add_venta(self):
		if self.validation():
			query = 'INSERT INTO ventas VALUES(NULL, ?, ?, ?)'
			parameters = (
				self.hour,
				self.ui.ingreso_entry.text(),
				self.ui.adicional_entry.text()
				)
			self.run_query(query, parameters)
			self.ui.label_status.setText('Ingreso agregado')
			self.ingreso_entry.clear()
			self.adicional_entry.clear()
			self.get_ventas()
		else: self.ui.label_status.setText('Ingrese el valor de venta')

	def delete_venta(self):
		row = self.current_item()
		cell_id = self.ui.listaVentas.item(row, 0).text()
		query = 'DELETE FROM ventas WHERE id = ?'
		self.run_query(query, (cell_id, ))
		self.get_ventas()

	def current_item(self):
		if self.ui.listaVentas.selectedItems():
			row = self.ui.listaVentas.currentRow()
			self.ui.label_status.setText('')
			return row
		else: self.ui.label_status.setText('Seleccione un registro')

	def total_dia(self):
		pass

class UIFunctions(Kiosco):

	# Minimize Restore Func

	# UI Definitions
	def uiDefinitions(self):

		# Remove Title Bar
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground);


if __name__ == '__main__':
	app = QApplication(sys.argv)
	myapp = Kiosco()
	myapp.ui.show()
	sys.exit(app.exec_())