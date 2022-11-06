import sys

from PyQt6.QtWidgets  import QMainWindow, QApplication
from Calculadora import Ui_Calculadora

class MainWindow(QMainWindow, Ui_Calculadora):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)

        self.texto_conta = ""

        def add_num(num):
            if str(self.texto_conta) != "":
                self.display_1.setText("")
                self.display_2.setText("0")
                self.texto_conta = ""
            texto_inicial = self.display_2.text()
            if texto_inicial[-1] == '0' and len(texto_inicial) == 1:
                self.display_2.setText(num)
            else:
                self.display_2.setText(texto_inicial + num)
            self.btn_ac.setText("CE")

        def add_ponto(pt):
            texto_inicial = self.display_2.text()
            if not "." in texto_inicial:
                self.display_2.setText(texto_inicial + pt)
                self.btn_ac.setText("CE")

        def deletar():
            if self.btn_ac.text() == "AC":
                self.display_1.setText("")
                self.display_2.setText("0")
            else:
                texto_inicial = self.display_2.text()
                texto_inicial = texto_inicial[:-1]
                if texto_inicial == "":
                    texto_inicial = "0"
                    self.btn_ac.setText("AC")
                self.display_2.setText(texto_inicial)

        def add_sinais(sinal):
            texto_inicial_1 = self.display_1.text()
            texto_inicial_2 = self.display_2.text()
            if texto_inicial_1 == "":
                self.display_1.setText(f"{texto_inicial_2} {sinal}")
            elif texto_inicial_1[-1] in ["%", ")"]:
                self.display_1.setText(f"{texto_inicial_1} {sinal}")
            else:
                self.display_1.setText(f"{texto_inicial_1} {texto_inicial_2} {sinal}")
            self.display_2.setText("0")

        def add_pc():
            texto_inicial_1 = self.display_1.text()
            texto_inicial_2 = self.display_2.text()
            if texto_inicial_2 != "0":
                if texto_inicial_1 != "":
                    self.display_1.setText(f"{texto_inicial_1} {texto_inicial_2}%")
                else:
                    self.display_1.setText(f"{texto_inicial_2}%")
                self.display_2.setText("0")

        def add_ap_fp(p):
            texto_inicial_1 = self.display_1.text()
            texto_inicial_2 = self.display_2.text()
            if p == "(":
                if texto_inicial_1 != "":
                    if texto_inicial_1[-1] != ")":
                        self.display_1.setText(f"{texto_inicial_1} {p}")
                else:
                    self.display_1.setText(f"{p}")
            else:
                if texto_inicial_1[-1] != ")":
                    self.display_1.setText(f"{texto_inicial_1} {texto_inicial_2} {p}")
                    self.display_2.setText("0")
                else:
                    self.display_1.setText(f"{texto_inicial_1} {p}")

        def calcular():
            texto_inicial_1 = self.display_1.text()
            texto_inicial_2 = self.display_2.text()
            if texto_inicial_1 != "":
                if texto_inicial_1[-1] in ["+", "×", "−", "÷"]:
                    self.texto_conta = f"{texto_inicial_1} {texto_inicial_2}"
                else:
                    self.texto_conta = f"{texto_inicial_1}"
                self.display_1.setText(self.texto_conta)
                self.texto_conta = self.texto_conta.replace("%", "/100")
                self.texto_conta = self.texto_conta.replace(" ", "")
                self.texto_conta = self.texto_conta.replace("×", "*")
                self.texto_conta = self.texto_conta.replace("+", "+")
                self.texto_conta = self.texto_conta.replace("−", "-")
                self.texto_conta = self.texto_conta.replace("÷", "/")

                try:
                    texto_inicial_2 = eval(f"{self.texto_conta}")
                    if float.is_integer(float(texto_inicial_2)):
                        self.display_2.setText(f"{int(texto_inicial_2)}")
                    else:
                        self.display_2.setText(f"{texto_inicial_2}")
                except:
                    print(texto_inicial_2)
                    self.display_2.setText("Erro na conta!")
                self.btn_ac.setText("AC")
            

        self.btn_0.clicked.connect(lambda: add_num(self.btn_0.text()))
        self.btn_1.clicked.connect(lambda: add_num(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: add_num(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: add_num(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: add_num(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: add_num(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: add_num(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: add_num(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: add_num(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: add_num(self.btn_9.text()))

        self.btn_ponto.clicked.connect(lambda: add_ponto(self.btn_ponto.text()))

        self.btn_ac.clicked.connect(deletar)

        self.btn_mais.clicked.connect(lambda: add_sinais(self.btn_mais.text()))
        self.btn_menos.clicked.connect(lambda: add_sinais(self.btn_menos.text()))
        self.btn_mp.clicked.connect(lambda: add_sinais(self.btn_mp.text()))
        self.btn_div.clicked.connect(lambda: add_sinais(self.btn_div.text()))

        self.btn_pc.clicked.connect(add_pc)

        self.btn_ap.clicked.connect(lambda: add_ap_fp(self.btn_ap.text()))
        self.btn_fp.clicked.connect(lambda: add_ap_fp(self.btn_fp.text()))

        self.btn_igual.clicked.connect(calcular)


if __name__ == "__main__":
    qt = QApplication(sys.argv)
    view = MainWindow()
    view.show()
    qt.exec()