from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, \
    QComboBox, QSizePolicy
from PyQt5.QtGui import QPixmap, QFont
from Bus_greedy import greedy
from Bus_A import A

class ProjectWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.contenedor = QWidget()

        self.lyt_main = QVBoxLayout()
        self.lyt_instruc = QHBoxLayout()
        self.lyt_coman = QHBoxLayout()
        self.lyt_ruta = QHBoxLayout()
        self.lyt_1 = QVBoxLayout()
        self.lyt_tabla = QVBoxLayout()
        self.lyt_2 = QVBoxLayout()

        self.lbl_instruc = QLabel()
        self.lbl_origen = QLabel()
        self.lbl_metodo = QLabel()
        self.lbl_destino = QLabel()
        self.lbl_ruta = QLabel()

        self.cmb_origen = QComboBox()
        self.cmb_metodo = QComboBox()
        self.cmb_destino = QComboBox()

        self.bot_buscar = QPushButton()

        self.lbl_image = QLabel()
        self.pixmap = QPixmap('ciudades.jpg')

        #self.bot_buscar.clicked.connect(self.busquedas)

        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('Busqueda Efectiva (BE)')

        self.lbl_instruc.setText('Bienvenidos a Busqueda Efectiva, con este programa podras encontrar la mejor ruta para '
                                 'viajar desde donde este hasta cualquier ciudad.\n' 'Selecciona tu ciudad de origen, tu ciudad '
                                 'destino y el método por el cual quieres hallar tu ruta.\n')
        self.lbl_instruc.setFont(QFont('CambriaMath',12))
        self.lbl_origen.setText('Origen')
        self.lbl_metodo.setText('Método')
        self.lbl_destino.setText('Destino')
        #self.lbl_ruta.setText('Tu ruta es:')
        self.lbl_image.setPixmap(self.pixmap)
        self.lbl_origen.setFixedWidth(50)
        self.lbl_metodo.setFixedWidth(50)
        self.lbl_destino.setFixedWidth(50)
        #self.lbl_ruta.setFixedWidth(80)
        self.lbl_instruc.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.lbl_origen.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.lbl_metodo.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.lbl_destino.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.lbl_ruta.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.lbl_image.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.cmb_origen.setFixedWidth(85)
        self.cmb_origen.addItems(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'M', 'N', '0', 'P', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z'])
        self.cmb_metodo.setFixedWidth(85)
        self.cmb_metodo.addItems(['Greedy', 'A*'])
        self.cmb_destino.setFixedWidth(85)
        self.cmb_destino.addItems(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'M', 'N', '0', 'P', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z'])
        self.cmb_origen.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.cmb_metodo.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.cmb_destino.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.bot_buscar.setFixedWidth(65)
        self.bot_buscar.setText('BUSCAR')
        self.bot_buscar.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.lyt_main.addLayout(self.lyt_instruc)
        self.lyt_main.addLayout(self.lyt_coman)
        self.lyt_main.addLayout(self.lyt_ruta)
        self.lyt_coman.addLayout(self.lyt_1)
        self.lyt_coman.addLayout(self.lyt_tabla)
        self.lyt_coman.addLayout(self.lyt_2)
        self.contenedor.setLayout(self.lyt_main)
        self.setCentralWidget(self.contenedor)

        self.lyt_instruc.addWidget(self.lbl_instruc)
        self.lyt_1.addWidget(self.lbl_origen)
        self.lyt_1.addWidget(self.cmb_origen)
        self.lyt_1.addWidget(self.lbl_metodo)
        self.lyt_1.addWidget(self.cmb_metodo)
        self.lyt_tabla.addWidget(self.lbl_image)
        self.lyt_2.addWidget(self.lbl_destino)
        self.lyt_2.addWidget(self.cmb_destino)
        self.lyt_2.addWidget(self.bot_buscar)
        self.lyt_ruta.addWidget(self.lbl_ruta)

        self.bot_buscar.clicked.connect(self.busquedas)

    def busquedas(self):
        ori = str(self.cmb_origen.currentText())
        des = str(self.cmb_destino.currentText())
        metodo = self.cmb_metodo.currentText()
        if metodo == 'Greedy':
            Bus = greedy(ori,des)
        else:
            Bus = A(ori,des)
        print(self.lbl_ruta.setText('Tu ruta es:\n'+ str(Bus)))

if __name__ == '__main__':
    app = QApplication([])
    window = ProjectWindow()
    window.show()
    app.exec_()
