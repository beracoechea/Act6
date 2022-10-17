# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
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
        MainWindow.resize(532, 458)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.velocidad_spinBox = QSpinBox(self.groupBox)
        self.velocidad_spinBox.setObjectName(u"velocidad_spinBox")
        self.velocidad_spinBox.setMaximum(1000)

        self.gridLayout.addWidget(self.velocidad_spinBox, 5, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.azul_spinBox = QSpinBox(self.groupBox)
        self.azul_spinBox.setObjectName(u"azul_spinBox")

        self.gridLayout.addWidget(self.azul_spinBox, 8, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.azul_label = QLabel(self.groupBox)
        self.azul_label.setObjectName(u"azul_label")

        self.gridLayout.addWidget(self.azul_label, 8, 0, 1, 1)

        self.verde_spinBox = QSpinBox(self.groupBox)
        self.verde_spinBox.setObjectName(u"verde_spinBox")

        self.gridLayout.addWidget(self.verde_spinBox, 7, 1, 1, 1)

        self.ID_spinBox = QSpinBox(self.groupBox)
        self.ID_spinBox.setObjectName(u"ID_spinBox")

        self.gridLayout.addWidget(self.ID_spinBox, 0, 1, 1, 1)

        self.velocidad_label = QLabel(self.groupBox)
        self.velocidad_label.setObjectName(u"velocidad_label")

        self.gridLayout.addWidget(self.velocidad_label, 5, 0, 1, 1)

        self.inicio_pushButton = QPushButton(self.groupBox)
        self.inicio_pushButton.setObjectName(u"inicio_pushButton")

        self.gridLayout.addWidget(self.inicio_pushButton, 10, 0, 1, 2)

        self.y_label = QLabel(self.groupBox)
        self.y_label.setObjectName(u"y_label")

        self.gridLayout.addWidget(self.y_label, 4, 0, 1, 1)

        self.rojo_label = QLabel(self.groupBox)
        self.rojo_label.setObjectName(u"rojo_label")

        self.gridLayout.addWidget(self.rojo_label, 6, 0, 1, 1)

        self.FINAL_pushButton = QPushButton(self.groupBox)
        self.FINAL_pushButton.setObjectName(u"FINAL_pushButton")

        self.gridLayout.addWidget(self.FINAL_pushButton, 9, 0, 1, 2)

        self.x_spinBox = QSpinBox(self.groupBox)
        self.x_spinBox.setObjectName(u"x_spinBox")
        self.x_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.x_spinBox, 3, 1, 1, 1)

        self.rojo_spinBox = QSpinBox(self.groupBox)
        self.rojo_spinBox.setObjectName(u"rojo_spinBox")
        self.rojo_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.rojo_spinBox, 6, 1, 1, 1)

        self.mostrar_pushButton = QPushButton(self.groupBox)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")

        self.gridLayout.addWidget(self.mostrar_pushButton, 11, 0, 1, 2)

        self.y_spinBox = QSpinBox(self.groupBox)
        self.y_spinBox.setObjectName(u"y_spinBox")
        self.y_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.y_spinBox, 4, 1, 1, 1)

        self.ORIGEN_X_spinBox = QSpinBox(self.groupBox)
        self.ORIGEN_X_spinBox.setObjectName(u"ORIGEN_X_spinBox")

        self.gridLayout.addWidget(self.ORIGEN_X_spinBox, 1, 1, 1, 1)

        self.x_label = QLabel(self.groupBox)
        self.x_label.setObjectName(u"x_label")

        self.gridLayout.addWidget(self.x_label, 3, 0, 1, 1)

        self.verde_label = QLabel(self.groupBox)
        self.verde_label.setObjectName(u"verde_label")

        self.gridLayout.addWidget(self.verde_label, 7, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.ORIGEN_Y_spinBox = QSpinBox(self.groupBox)
        self.ORIGEN_Y_spinBox.setObjectName(u"ORIGEN_Y_spinBox")

        self.gridLayout.addWidget(self.ORIGEN_Y_spinBox, 2, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.salida = QPlainTextEdit(self.centralwidget)
        self.salida.setObjectName(u"salida")

        self.gridLayout_2.addWidget(self.salida, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 532, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"PARTICULAS", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ORIGEN X", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.azul_label.setText(QCoreApplication.translate("MainWindow", u"AZUL", None))
        self.velocidad_label.setText(QCoreApplication.translate("MainWindow", u"VELOCIDAD", None))
        self.inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"AGREGAR AL INICIO", None))
        self.y_label.setText(QCoreApplication.translate("MainWindow", u"DESTINO Y", None))
        self.rojo_label.setText(QCoreApplication.translate("MainWindow", u"ROJO", None))
        self.FINAL_pushButton.setText(QCoreApplication.translate("MainWindow", u"AGREGAR AL FINAL", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"MOSTRAR", None))
        self.x_label.setText(QCoreApplication.translate("MainWindow", u"DESTINO X", None))
        self.verde_label.setText(QCoreApplication.translate("MainWindow", u"VERDE", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ORIGEN Y", None))
    # retranslateUi

