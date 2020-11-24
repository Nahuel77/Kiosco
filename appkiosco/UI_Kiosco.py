# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_Kiosco.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.window_layout = QVBoxLayout(self.centralwidget)
        self.window_layout.setSpacing(0)
        self.window_layout.setObjectName(u"window_layout")
        self.window_layout.setContentsMargins(10, 10, 10, 10)
        self.window = QFrame(self.centralwidget)
        self.window.setObjectName(u"window")
        self.window.setEnabled(True)
        self.window.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(15, 12, 41, 255), stop:1 rgba(48, 43, 99, 255));\n"
"border-radius:10px;")
        self.window.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.window)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.window)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setEnabled(True)
        self.title_bar.setMinimumSize(QSize(0, 40))
        self.title_bar.setMaximumSize(QSize(16777215, 50))
        self.title_bar.setStyleSheet(u"background-color: none;")
        self.title_bar.setFrameShape(QFrame.StyledPanel)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 5, 0, 0)
        self.frame_title = QFrame(self.title_bar)
        self.frame_title.setObjectName(u"frame_title")
        font = QFont()
        font.setFamily(u"JasmineUPC")
        font.setPointSize(17)
        self.frame_title.setFont(font)
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_title)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 0, 0, 0)
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        font1 = QFont()
        font1.setFamily(u"Levenim MT")
        font1.setPointSize(14)
        self.label_title.setFont(font1)
        self.label_title.setStyleSheet(u"color: rgb(0, 212, 212)")

        self.verticalLayout_2.addWidget(self.label_title)


        self.horizontalLayout.addWidget(self.frame_title)

        self.frame_btns = QFrame(self.title_bar)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMaximumSize(QSize(100, 16777215))
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(70, 10, 16, 16))
        self.btn_close.setMinimumSize(QSize(16, 16))
        self.btn_close.setMaximumSize(QSize(17, 17))
        self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_close.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 0, 0, 150);\n"
"}")
        self.btn_minimize = QPushButton(self.frame_btns)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setGeometry(QRect(40, 10, 16, 16))
        self.btn_minimize.setMinimumSize(QSize(16, 16))
        self.btn_minimize.setMaximumSize(QSize(17, 17))
        self.btn_minimize.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_minimize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	background-color: rgb(85, 255, 127);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(58, 255, 127, 150);\n"
"}")

        self.horizontalLayout.addWidget(self.frame_btns)


        self.verticalLayout.addWidget(self.title_bar)

        self.content_bar = QFrame(self.window)
        self.content_bar.setObjectName(u"content_bar")
        self.content_bar.setStyleSheet(u"background-color: none;")
        self.content_bar.setFrameShape(QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.content_bar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(15, 0, 15, 0)
        self.frame_menus = QFrame(self.content_bar)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setMinimumSize(QSize(150, 0))
        self.frame_menus.setMaximumSize(QSize(150, 16777215))
        self.frame_menus.setFrameShape(QFrame.StyledPanel)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.btn_ventas = QPushButton(self.frame_menus)
        self.btn_ventas.setObjectName(u"btn_ventas")
        self.btn_ventas.setGeometry(QRect(20, 60, 111, 41))
        font2 = QFont()
        font2.setFamily(u"Latha")
        font2.setPointSize(15)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.btn_ventas.setFont(font2)
        self.btn_ventas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ventas.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 150), stop:1 rgba(0, 170, 255, 150));\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.btn_cuentas = QPushButton(self.frame_menus)
        self.btn_cuentas.setObjectName(u"btn_cuentas")
        self.btn_cuentas.setGeometry(QRect(20, 120, 111, 41))
        self.btn_cuentas.setFont(font2)
        self.btn_cuentas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cuentas.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 150), stop:1 rgba(0, 170, 255, 150));\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.btn_historial = QPushButton(self.frame_menus)
        self.btn_historial.setObjectName(u"btn_historial")
        self.btn_historial.setGeometry(QRect(20, 180, 111, 41))
        self.btn_historial.setFont(font2)
        self.btn_historial.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_historial.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 150), stop:1 rgba(0, 170, 255, 150));\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.btn_configuracion = QPushButton(self.frame_menus)
        self.btn_configuracion.setObjectName(u"btn_configuracion")
        self.btn_configuracion.setGeometry(QRect(20, 450, 111, 41))
        self.btn_configuracion.setFont(font2)
        self.btn_configuracion.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_configuracion.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 150), stop:1 rgba(0, 170, 255, 150));\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_3.addWidget(self.frame_menus)

        self.frame_pages = QFrame(self.content_bar)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 0)
        self.pages_widget = QStackedWidget(self.frame_pages)
        self.pages_widget.setObjectName(u"pages_widget")
        font3 = QFont()
        font3.setFamily(u"Latha")
        font3.setPointSize(14)
        self.pages_widget.setFont(font3)
        self.pages_widget.setStyleSheet(u"background-color: none;")
        self.page_ventas = QWidget()
        self.page_ventas.setObjectName(u"page_ventas")
        self.listaVentas = QTableWidget(self.page_ventas)
        self.listaVentas.setObjectName(u"listaVentas")
        self.listaVentas.setGeometry(QRect(30, 70, 231, 501))
        font4 = QFont()
        font4.setFamily(u"Levenim MT")
        font4.setPointSize(12)
        self.listaVentas.setFont(font4)
        self.listaVentas.setFocusPolicy(Qt.StrongFocus)
        self.listaVentas.setStyleSheet(u"QTableWidget {	\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(27, 55, 83);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, "
                        "170, 255, 255));\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color:  qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	padding: 3px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}")
        self.listaVentas.setFrameShape(QFrame.VLine)
        self.listaVentas.setFrameShadow(QFrame.Sunken)
        self.listaVentas.setLineWidth(2)
        self.listaVentas.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.listaVentas.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listaVentas.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.listaVentas.horizontalHeader().setDefaultSectionSize(77)
        self.listaVentas.horizontalHeader().setHighlightSections(False)
        self.listaVentas.verticalHeader().setVisible(False)
        self.listaVentas.verticalHeader().setHighlightSections(False)
        self.label_ventas = QLabel(self.page_ventas)
        self.label_ventas.setObjectName(u"label_ventas")
        self.label_ventas.setGeometry(QRect(40, 30, 181, 31))
        font5 = QFont()
        font5.setFamily(u"Levenim MT")
        font5.setPointSize(14)
        font5.setBold(False)
        font5.setWeight(50)
        self.label_ventas.setFont(font5)
        self.label_ventas.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.label_ingreso = QLabel(self.page_ventas)
        self.label_ingreso.setObjectName(u"label_ingreso")
        self.label_ingreso.setGeometry(QRect(310, 30, 171, 31))
        self.label_ingreso.setFont(font1)
        self.label_ingreso.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.label_adicional = QLabel(self.page_ventas)
        self.label_adicional.setObjectName(u"label_adicional")
        self.label_adicional.setGeometry(QRect(310, 140, 231, 31))
        self.label_adicional.setFont(font1)
        self.label_adicional.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.btn_agregar = QPushButton(self.page_ventas)
        self.btn_agregar.setObjectName(u"btn_agregar")
        self.btn_agregar.setGeometry(QRect(310, 260, 121, 41))
        self.btn_agregar.setFont(font3)
        self.btn_agregar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agregar.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 150), stop:1 rgba(0, 170, 255, 150));\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.btn_borrar = QPushButton(self.page_ventas)
        self.btn_borrar.setObjectName(u"btn_borrar")
        self.btn_borrar.setGeometry(QRect(310, 340, 121, 41))
        self.btn_borrar.setFont(font3)
        self.btn_borrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_borrar.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 150), stop:1 rgba(0, 170, 255, 150));\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_dia = QLabel(self.page_ventas)
        self.label_dia.setObjectName(u"label_dia")
        self.label_dia.setGeometry(QRect(300, 520, 271, 41))
        self.label_dia.setFont(font1)
        self.label_dia.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.ingreso_entry = QLineEdit(self.page_ventas)
        self.ingreso_entry.setObjectName(u"ingreso_entry")
        self.ingreso_entry.setGeometry(QRect(300, 70, 261, 41))
        self.ingreso_entry.setFont(font1)
        self.ingreso_entry.setStyleSheet(u"QLineEdit {\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, 						x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 			255, 255));\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.528, y1:1, x2:0.522, y2:0.596227, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"}")
        self.adicional_entry = QLineEdit(self.page_ventas)
        self.adicional_entry.setObjectName(u"adicional_entry")
        self.adicional_entry.setGeometry(QRect(300, 180, 261, 41))
        self.adicional_entry.setFont(font1)
        self.adicional_entry.setStyleSheet(u"QLineEdit {\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, 						x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 			255, 255));\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.528, y1:1, x2:0.522, y2:0.596227, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"}")
        self.label_status = QLineEdit(self.page_ventas)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setGeometry(QRect(310, 430, 261, 41))
        self.label_status.setFont(font1)
        self.label_status.setCursor(QCursor(Qt.ArrowCursor))
        self.label_status.setFocusPolicy(Qt.NoFocus)
        self.label_status.setAcceptDrops(False)
        self.label_status.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"color: rgb(0, 170, 255);")
        self.pages_widget.addWidget(self.page_ventas)
        self.page_config = QWidget()
        self.page_config.setObjectName(u"page_config")
        self.label_3 = QLabel(self.page_config)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 30, 91, 31))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.label_4 = QLabel(self.page_config)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 100, 601, 151))
        font6 = QFont()
        font6.setFamily(u"Latha")
        font6.setPointSize(12)
        self.label_4.setFont(font6)
        self.label_4.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.email = QLineEdit(self.page_config)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(140, 30, 291, 41))
        self.email.setFont(font1)
        self.email.setStyleSheet(u"QLineEdit {\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, 						x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 			255, 255));\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.528, y1:1, x2:0.522, y2:0.596227, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"}")
        self.pages_widget.addWidget(self.page_config)
        self.page_historial = QWidget()
        self.page_historial.setObjectName(u"page_historial")
        self.historial_ventas = QTableWidget(self.page_historial)
        self.historial_ventas.setObjectName(u"historial_ventas")
        self.historial_ventas.setGeometry(QRect(400, 70, 231, 211))
        self.historial_ventas.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.historial_ventas.setStyleSheet(u"QTableWidget {	\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(27, 55, 83);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, "
                        "170, 255, 255));\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color:  qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	padding: 3px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}")
        self.calendarWidget = QCalendarWidget(self.page_historial)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(70, 80, 256, 183))
        self.label = QLabel(self.page_historial)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(410, 30, 151, 31))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.label_2 = QLabel(self.page_historial)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(410, 290, 151, 31))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.historial_fiado = QTableWidget(self.page_historial)
        self.historial_fiado.setObjectName(u"historial_fiado")
        self.historial_fiado.setGeometry(QRect(400, 330, 231, 151))
        self.historial_fiado.setStyleSheet(u"QTableWidget {	\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(27, 55, 83);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, "
                        "170, 255, 255));\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color:  qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	padding: 3px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}")
        self.pages_widget.addWidget(self.page_historial)
        self.page_cuentas = QWidget()
        self.page_cuentas.setObjectName(u"page_cuentas")
        font7 = QFont()
        font7.setPointSize(8)
        self.page_cuentas.setFont(font7)
        self.listaCuentas = QTableWidget(self.page_cuentas)
        self.listaCuentas.setObjectName(u"listaCuentas")
        self.listaCuentas.setGeometry(QRect(30, 130, 231, 191))
        self.listaCuentas.setStyleSheet(u"QTableWidget {	\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(27, 55, 83);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, "
                        "170, 255, 255));\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color:  qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	padding: 3px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}")
        self.listaCuentas.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.listaCuentas.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listaCuentas.setDragDropOverwriteMode(False)
        self.listaCuentas.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.listaCuentas.horizontalHeader().setMinimumSectionSize(31)
        self.listaCuentas.horizontalHeader().setDefaultSectionSize(115)
        self.listaCuentas.horizontalHeader().setStretchLastSection(True)
        self.listaCuentas.verticalHeader().setVisible(False)
        self.listaCuentas.verticalHeader().setDefaultSectionSize(35)
        self.listaCuentas.verticalHeader().setHighlightSections(False)
        self.listaDeudas = QTableWidget(self.page_cuentas)
        self.listaDeudas.setObjectName(u"listaDeudas")
        self.listaDeudas.setGeometry(QRect(340, 130, 431, 191))
        self.listaDeudas.setStyleSheet(u"QTableWidget {	\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(27, 55, 83);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, "
                        "170, 255, 255));\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color:  qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	padding: 3px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}")
        self.listaDeudas.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.listaDeudas.horizontalHeader().setStretchLastSection(True)
        self.listaDeudas.verticalHeader().setVisible(False)
        self.listaDeudas.verticalHeader().setHighlightSections(False)
        self.label_nuevacuenta = QLabel(self.page_cuentas)
        self.label_nuevacuenta.setObjectName(u"label_nuevacuenta")
        self.label_nuevacuenta.setGeometry(QRect(40, 400, 151, 31))
        self.label_nuevacuenta.setFont(font1)
        self.label_nuevacuenta.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.label_borrarcuenta = QLabel(self.page_cuentas)
        self.label_borrarcuenta.setObjectName(u"label_borrarcuenta")
        self.label_borrarcuenta.setGeometry(QRect(40, 30, 161, 31))
        self.label_borrarcuenta.setFont(font1)
        self.label_borrarcuenta.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.btn_buscarcuenta = QPushButton(self.page_cuentas)
        self.btn_buscarcuenta.setObjectName(u"btn_buscarcuenta")
        self.btn_buscarcuenta.setGeometry(QRect(220, 70, 41, 41))
        self.btn_buscarcuenta.setFont(font3)
        self.btn_buscarcuenta.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_buscarcuenta.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 150), stop:1 rgba(0, 170, 255, 150));\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_agregardeuda = QLabel(self.page_cuentas)
        self.label_agregardeuda.setObjectName(u"label_agregardeuda")
        self.label_agregardeuda.setGeometry(QRect(350, 30, 161, 31))
        self.label_agregardeuda.setFont(font1)
        self.label_agregardeuda.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.btn_agregardeuda = QPushButton(self.page_cuentas)
        self.btn_agregardeuda.setObjectName(u"btn_agregardeuda")
        self.btn_agregardeuda.setGeometry(QRect(730, 70, 41, 41))
        self.btn_agregardeuda.setFont(font3)
        self.btn_agregardeuda.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agregardeuda.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 150), stop:1 rgba(0, 170, 255, 150));\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_pago = QLabel(self.page_cuentas)
        self.label_pago.setObjectName(u"label_pago")
        self.label_pago.setGeometry(QRect(350, 400, 141, 31))
        self.label_pago.setFont(font1)
        self.label_pago.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.btn_nuevacuenta = QPushButton(self.page_cuentas)
        self.btn_nuevacuenta.setObjectName(u"btn_nuevacuenta")
        self.btn_nuevacuenta.setGeometry(QRect(220, 440, 41, 41))
        self.btn_nuevacuenta.setFont(font3)
        self.btn_nuevacuenta.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_nuevacuenta.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 150), stop:1 rgba(0, 170, 255, 150));\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.btn_pagodeuda = QPushButton(self.page_cuentas)
        self.btn_pagodeuda.setObjectName(u"btn_pagodeuda")
        self.btn_pagodeuda.setGeometry(QRect(600, 440, 41, 41))
        self.btn_pagodeuda.setFont(font3)
        self.btn_pagodeuda.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pagodeuda.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 150), stop:1 rgba(0, 170, 255, 150));\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.btn_borrarcuenta = QPushButton(self.page_cuentas)
        self.btn_borrarcuenta.setObjectName(u"btn_borrarcuenta")
        self.btn_borrarcuenta.setGeometry(QRect(30, 520, 231, 41))
        self.btn_borrarcuenta.setFont(font3)
        self.btn_borrarcuenta.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_borrarcuenta.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 150), stop:1 rgba(0, 170, 255, 150));\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.btn_pagocompleto = QPushButton(self.page_cuentas)
        self.btn_pagocompleto.setObjectName(u"btn_pagocompleto")
        self.btn_pagocompleto.setGeometry(QRect(340, 520, 301, 41))
        self.btn_pagocompleto.setFont(font3)
        self.btn_pagocompleto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pagocompleto.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 150), stop:1 rgba(0, 170, 255, 150));\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.buscarcuenta_entry = QLineEdit(self.page_cuentas)
        self.buscarcuenta_entry.setObjectName(u"buscarcuenta_entry")
        self.buscarcuenta_entry.setGeometry(QRect(30, 70, 171, 41))
        self.buscarcuenta_entry.setFont(font1)
        self.buscarcuenta_entry.setStyleSheet(u"QLineEdit {\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, 						x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 			255, 255));\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.528, y1:1, x2:0.522, y2:0.596227, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"}")
        self.montodeuda_entry = QLineEdit(self.page_cuentas)
        self.montodeuda_entry.setObjectName(u"montodeuda_entry")
        self.montodeuda_entry.setGeometry(QRect(340, 70, 171, 41))
        self.montodeuda_entry.setFont(font1)
        self.montodeuda_entry.setStyleSheet(u"QLineEdit {\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, 						x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 			255, 255));\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.528, y1:1, x2:0.522, y2:0.596227, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"}")
        self.pagodeuda_entry = QLineEdit(self.page_cuentas)
        self.pagodeuda_entry.setObjectName(u"pagodeuda_entry")
        self.pagodeuda_entry.setGeometry(QRect(340, 440, 241, 41))
        self.pagodeuda_entry.setFont(font1)
        self.pagodeuda_entry.setStyleSheet(u"QLineEdit {\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, 						x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 			255, 255));\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.528, y1:1, x2:0.522, y2:0.596227, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"}")
        self.nuevacuenta_entry = QLineEdit(self.page_cuentas)
        self.nuevacuenta_entry.setObjectName(u"nuevacuenta_entry")
        self.nuevacuenta_entry.setGeometry(QRect(30, 440, 171, 41))
        self.nuevacuenta_entry.setFont(font1)
        self.nuevacuenta_entry.setStyleSheet(u"QLineEdit {\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, 						x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 			255, 255));\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.528, y1:1, x2:0.522, y2:0.596227, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"}")
        self.status_Cuenta = QLabel(self.page_cuentas)
        self.status_Cuenta.setObjectName(u"status_Cuenta")
        self.status_Cuenta.setGeometry(QRect(30, 340, 301, 41))
        font8 = QFont()
        font8.setFamily(u"Leelawadee")
        font8.setPointSize(14)
        self.status_Cuenta.setFont(font8)
        self.status_Cuenta.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.productodeuda_entry = QLineEdit(self.page_cuentas)
        self.productodeuda_entry.setObjectName(u"productodeuda_entry")
        self.productodeuda_entry.setGeometry(QRect(540, 70, 171, 41))
        self.productodeuda_entry.setStyleSheet(u"QLineEdit {\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, 						x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 			255, 255));\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.528, y1:1, x2:0.522, y2:0.596227, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"}")
        self.total_deuda = QLabel(self.page_cuentas)
        self.total_deuda.setObjectName(u"total_deuda")
        self.total_deuda.setGeometry(QRect(340, 340, 331, 41))
        self.total_deuda.setFont(font1)
        self.total_deuda.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.pages_widget.addWidget(self.page_cuentas)

        self.verticalLayout_4.addWidget(self.pages_widget)


        self.horizontalLayout_3.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.content_bar)

        self.credits_bar = QFrame(self.window)
        self.credits_bar.setObjectName(u"credits_bar")
        self.credits_bar.setMaximumSize(QSize(16777215, 30))
        self.credits_bar.setStyleSheet(u"background-color: none;")
        self.credits_bar.setFrameShape(QFrame.NoFrame)
        self.credits_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.credits_bar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_label_credits = QFrame(self.credits_bar)
        self.frame_label_credits.setObjectName(u"frame_label_credits")
        self.frame_label_credits.setFrameShape(QFrame.StyledPanel)
        self.frame_label_credits.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_label_credits)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 0, 0, 0)
        self.label_credits = QLabel(self.frame_label_credits)
        self.label_credits.setObjectName(u"label_credits")
        font9 = QFont()
        font9.setFamily(u"Levenim MT")
        self.label_credits.setFont(font9)
        self.label_credits.setStyleSheet(u"color: rgb(128, 102, 168);")

        self.verticalLayout_3.addWidget(self.label_credits)


        self.horizontalLayout_2.addWidget(self.frame_label_credits)

        self.frame_grip = QFrame(self.credits_bar)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(30, 30))
        self.frame_grip.setMaximumSize(QSize(30, 30))
        self.frame_grip.setStyleSheet(u"padding: 5px;")
        self.frame_grip.setFrameShape(QFrame.StyledPanel)
        self.frame_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_grip)


        self.verticalLayout.addWidget(self.credits_bar)


        self.window_layout.addWidget(self.window)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages_widget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"Kiosco", None))
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
        self.btn_ventas.setText(QCoreApplication.translate("MainWindow", u"Ventas", None))
        self.btn_cuentas.setText(QCoreApplication.translate("MainWindow", u"Cuentas", None))
        self.btn_historial.setText(QCoreApplication.translate("MainWindow", u"Historial", None))
        self.btn_configuracion.setText(QCoreApplication.translate("MainWindow", u"Config", None))
        self.label_ventas.setText(QCoreApplication.translate("MainWindow", u"Ventas:", None))
        self.label_ingreso.setText(QCoreApplication.translate("MainWindow", u"Nuevo ingreso:", None))
        self.label_adicional.setText(QCoreApplication.translate("MainWindow", u"Informaci\u00f3n adicional:", None))
        self.btn_agregar.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.btn_borrar.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.label_dia.setText(QCoreApplication.translate("MainWindow", u"Total del d\u00efa:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"E-Mail:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"La aplicaci\u00f3n Kiosco, generara un respaldo de modo online de la base de datos en cada inicio. Dicho respaldo se enviara al e-mail registrado.", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ventas:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Fiado:", None))
        self.label_nuevacuenta.setText(QCoreApplication.translate("MainWindow", u"Nueva cuenta:", None))
        self.label_borrarcuenta.setText(QCoreApplication.translate("MainWindow", u"Buscar cuenta:", None))
        self.btn_buscarcuenta.setText(QCoreApplication.translate("MainWindow", u"Ok", None))
        self.label_agregardeuda.setText(QCoreApplication.translate("MainWindow", u"Agregar deuda:", None))
        self.btn_agregardeuda.setText(QCoreApplication.translate("MainWindow", u"Ok", None))
        self.label_pago.setText(QCoreApplication.translate("MainWindow", u"Pago:", None))
        self.btn_nuevacuenta.setText(QCoreApplication.translate("MainWindow", u"Ok", None))
        self.btn_pagodeuda.setText(QCoreApplication.translate("MainWindow", u"Ok", None))
        self.btn_borrarcuenta.setText(QCoreApplication.translate("MainWindow", u"Borrar cuenta", None))
        self.btn_pagocompleto.setText(QCoreApplication.translate("MainWindow", u"Pago completo", None))
        self.status_Cuenta.setText("")
        self.total_deuda.setText("")
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"App desarrollada por Nahuel Calcara. \u00a9", None))
    # retranslateUi

