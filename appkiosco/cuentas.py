from main import *

class Cuentas():

	db_name = 'dbkiosco.db'

	def get_cuentas(self):
		query = 'SELECT id_cuenta, nombre_cuenta FROM cuentas'
		db_rows = self.run_query(query)
		self.ui.listaCuentas.setColumnCount(2)
		self.ui.listaCuentas.setRowCount(len(db_rows))
		self.ui.listaCuentas.setHorizontalHeaderLabels(['Id', 'Nombre'])
		for row in range(len(db_rows)):
			for column in range(len(db_rows[0])):
				self.ui.listaCuentas.setItem(
					row,
					column,
					QTableWidgetItem(str(db_rows[row][column]))
				)

	def current_cuenta(self):
		if self.ui.listaCuentas.selectedItems():
			row = self.ui.listaCuentas.currentRow()
			return self.ui.listaCuentas.item(row, 0).text()

	def get_deudas(self):
		if self.current_cuenta():
			cell_id = self.current_cuenta()
			query = 'SELECT fecha_monto, horario_monto, monto_deuda, producto FROM deuda WHERE id_cuenta1 = ?'
			db_rows = self.run_query(query, (cell_id,))
			self.ui.listaDeudas.setColumnCount(4)
			self.ui.listaDeudas.setRowCount(len(db_rows))
			self.ui.listaDeudas.setHorizontalHeaderLabels(['Fecha', 'Horario', 'Monto', 'Producto'])
			for row in range(len(db_rows)):
				for column in range(len(db_rows[0])):
					self.ui.listaDeudas.setItem(
						row,
						column,
						QTableWidgetItem(str(db_rows[row][column]))
					)
			self.total_deuda()
		else:
			self.ui.listaDeudas.clear()
			self.ui.status_Cuenta.setText('Seleccione un nombre de cuenta')

	def agregar_deuda(self):
		if len(self.ui.montodeuda_entry.text()) != 0:
			cell_id = self.current_cuenta()
			query = 'INSERT INTO deuda VALUES(NULL, ?, ?, ?, ?, ?)'
			parameters = (
				self.time,
				self.hour,
				self.ui.montodeuda_entry.text(),
				self.ui.productodeuda_entry.text(),
				self.current_cuenta()
				)
			self.run_query(query, (parameters))
			self.get_deudas()
			self.ui.montodeuda_entry.clear()
			self.ui.productodeuda_entry.clear()
		elif not self.current_cuenta():
			self.ui.status_Cuenta.setText('Seleccione un nombre de cuenta')
		elif len(self.ui.montodeuda_entry.text()) == 0:
			self.ui.status_Cuenta.setText('Al menos el monto es requerido')

	def total_deuda(self):
		query = 'SELECT SUM(monto_deuda) FROM deuda'
		result = self.run_query(query)
		res = result[0]
		total = ''.join(str(v) for v in res)

		self.ui.total_deuda.setText('Deuda total: {}'.format(total))

	# revisar si la solucion es tonar el valor de current_cuenta de vuelta a cero

	def borrar_deuda(self):
		pass
