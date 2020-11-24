import sqlite3

class run_query():

	db_name = 'dbkiosco.db'

	def run_query(self, query, parameters = ()):
		with sqlite3.connect(self.db_name) as conn:
			cursor = conn.cursor()
			cursor.execute(query, parameters)
			result = cursor.fetchall()
			conn.commit()
			return result