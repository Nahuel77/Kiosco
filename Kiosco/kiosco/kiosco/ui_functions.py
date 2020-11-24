from main import *

GLOBAL_STATE = 0

class UIFunctions(MainWindow):

	def uiDefinitions(self):

		# Remove Title Bar
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)