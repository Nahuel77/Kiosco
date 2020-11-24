import sys
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtGui, QtWidgets

import time
import sqlite3

from UI_Kiosco import Ui_MainWindow
from ui_functions import *

from ventas import Ventas
from cuentas import Cuentas
from run_query import run_query

class MainWindow(QMainWindow, Ventas, Cuentas, run_query):
  def __init__(self):
    QMainWindow.__init__(self)
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    self.hour = time.strftime('%H:%M')
    self.time = time.strftime('%d/%M/%Y')

    #### PAGES ###############################################################

    #### Ventas ##############################################################
    self.get_ventas()
    self.total_dia()
    self.ui.listaVentas.setColumnHidden(0, True)
    self.ui.btn_ventas.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_ventas))
    self.ui.btn_agregar.clicked.connect(self.add_venta)
    self.ui.btn_borrar.clicked.connect(self.delete_venta)
    self.ui.listaVentas.setColumnHidden(0, True)

    #### Cuentas ##############################################################
    self.get_cuentas()
    # self.ui.listaCuentas.cellClicked.connect(self.get_deudas)
    self.ui.listaCuentas.clicked.connect(self.get_deudas)
    self.ui.btn_agregardeuda.clicked.connect(self.agregar_deuda)
    self.ui.btn_cuentas.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_cuentas))

    #### Historial ############################################################
    self.ui.btn_historial.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_historial))

    #### Config ###############################################################
    self.ui.btn_configuracion.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_config))

        # MOVE WINDOW
    def moveWindow(event):
            # RESTORE BEFORE MOVE
      if UIFunctions.returnStatus() == 1:
        UIFunctions.maximize_restore(self)

            # IF LEFT CLICK MOVE WINDOW
      if event.buttons() == Qt.LeftButton:
        self.move(self.pos() + event.globalPos() - self.dragPos)
        self.dragPos = event.globalPos()
        event.accept()

        # SET TITLE BAR
    self.ui.title_bar.mouseMoveEvent = moveWindow

        ## ==> SET UI DEFINITIONS
    UIFunctions.uiDefinitions(self)


        ## SHOW ==> MAIN WINDOW
        ########################################################################
    self.show()

    ## APP EVENTS
    ########################################################################
  def mousePressEvent(self, event):
    self.dragPos = event.globalPos()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())