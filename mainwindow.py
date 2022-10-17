
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainwindow  import Ui_MainWindow
from particulas import Particula
from Lista import Lista


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.lista = Lista()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.inicio_pushButton.clicked.connect(self.click_agregar)
        self.ui.FINAL_pushButton.clicked.connect(self.click_final)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)

    @Slot()
    def click_mostrar(self):
        self.ui.salida.insertPlainText(str(self.lista))


    @Slot()
    def click_agregar(self):
        id = self.ui.ID_spinBox.value()
        origen_x = self.ui.ORIGEN_X_spinBox.value()
        origen_y = self.ui.ORIGEN_Y_spinBox.value()

        destino_x = self.ui.x_spinBox.value()
        destino_y = self.ui.y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        rojo = self.ui.rojo_spinBox.value()
        verde = self.ui.verde_spinBox.value()
        azul = self.ui.azul_spinBox.value()

        particula = Particula(id,origen_x,origen_y,destino_x,destino_y,velocidad,rojo,verde,azul)
        self.lista.agregar_inicio(particula)

    
    @Slot()
    def click_final(self):
        id = self.ui.ID_spinBox.value()
        origen_x = self.ui.ORIGEN_X_spinBox.value()
        origen_y = self.ui.ORIGEN_Y_spinBox.value()

        destino_x = self.ui.x_spinBox.value()
        destino_y = self.ui.y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        rojo = self.ui.rojo_spinBox.value()
        verde = self.ui.verde_spinBox.value()
        azul = self.ui.azul_spinBox.value()

        particula = Particula(id,origen_x,origen_y,destino_x,destino_y,velocidad,rojo,verde,azul)
        self.lista.agregar_final(particula)

    

        
