import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):  # Стандартная инициализация
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Зарплатный калькулятор. Повременная форма оплаты труда')
        self.label_2.hide()
        self.label_3.hide()
        self.label_4.hide()
        self.label_5.hide()
        self.label_6.hide()
        self.label_7.hide()

        self.label.hide()
        self.label_8.hide()
        self.label_9.hide()

        self.comboBox_2.hide()

        self.textEdit.hide()
        self.textEdit_2.hide()
        self.textEdit_3.hide()
        self.textEdit_4.hide()
        self.textEdit_5.hide()
        self.textEdit_6.hide()
        self.textEdit_7.hide()
        self.textEdit_8.hide()
        self.pushButton_2.hide()
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.run_2)

    def run(self):

        if self.comboBox.currentText().replace(" ", "") == "ПОЧАСОВАЯ":

            self.label_2.show()
            self.label_3.show()
            self.label_4.hide()
            self.label_5.show()
            self.label_6.show()
            self.label_7.show()

            self.textEdit.show()
            self.textEdit_2.show()
            self.textEdit_3.hide()
            self.textEdit_4.show()
            self.textEdit_5.show()
            self.textEdit_6.show()
            self.pushButton_2.show()

            self.label.hide()
            self.label_8.hide()
            self.label_9.hide()
            self.textEdit_8.hide()
            self.comboBox_2.hide()
        elif self.comboBox.currentText().replace(" ", "") == "ПОМЕСЯЧНАЯ":
            self.label.show()
            self.label_2.hide()
            self.label_3.hide()
            self.label_4.hide()
            self.textEdit.hide()
            self.textEdit_2.hide()
            self.textEdit_3.hide()
            self.textEdit_7.show()
            self.pushButton_2.show()

            self.label_8.show()
            self.label_9.show()
            self.textEdit_8.show()
            self.comboBox_2.show()
            self.label_5.show()
            self.label_6.show()
            self.label_7.show()
            self.textEdit_4.show()
            self.textEdit_5.show()
            self.textEdit_6.show()
        elif self.comboBox.currentText().replace(" ", "") == "ПРЕМИАЛЬНАЯ":
            self.label_2.show()
            self.label_3.show()
            self.label_4.show()

            self.label_5.show()
            self.label_6.show()
            self.label_7.show()
            self.textEdit.show()
            self.pushButton_2.show()
            self.textEdit_2.show()
            self.textEdit_3.show()
            self.textEdit_4.show()
            self.textEdit_5.show()
            self.textEdit_6.show()

            self.label.hide()
            self.label_8.hide()
            self.label_9.hide()
            self.textEdit_8.hide()
            self.comboBox_2.hide()
            self.textEdit_7.hide()

    def run_2(self):
        self.textEdit_4.clear()
        self.textEdit_5.clear()
        self.textEdit_6.clear()
        if self.comboBox.currentText().replace(" ", "") == "ПОЧАСОВАЯ":
            try:
                stavka = float(self.textEdit.toPlainText())
                time_hours = int(self.textEdit_2.toPlainText())
                oklad = stavka * time_hours
                ndfl = oklad * 13 / 100
                sarplata = oklad - ndfl

                self.textEdit_4.setPlainText(str(f"{oklad} руб"))
                self.textEdit_5.setPlainText(str(f"{ndfl} руб"))
                self.textEdit_6.setPlainText(str(f"{sarplata} руб"))
            except ValueError:
                self.textEdit.setPlainText("Попробуйте еще раз.")
                self.textEdit_2.setPlainText("")

        elif self.comboBox.currentText().replace(" ", "") == "ПОМЕСЯЧНАЯ":
            try:
                oklad = float(self.textEdit_8.toPlainText())

                time_days = float(self.textEdit_7.toPlainText())
                month = self.comboBox_2.currentText().replace(" ", "")
                days = days_in_month(month)
                if 0 <= time_days <= days:
                        sarplata = (oklad * time_days) / days
                        ndfl = sarplata * 13 / 100
                        itog = sarplata - ndfl
                        self.textEdit_4.setPlainText(str(f"{oklad} руб"))
                        self.textEdit_5.setPlainText(str(f"{ndfl} руб"))
                        self.textEdit_6.setPlainText(str(f"{itog} руб"))
                else:
                    self.textEdit_8.clear()
                    self.textEdit_7.setPlainText(f"Попробуйте снова. Всего рабочих дней {days}.")
            except ValueError:
                self.textEdit_8.setPlainText("Попробуйте еще раз.")
                self.textEdit_7.setPlainText("")
        elif self.comboBox.currentText().replace(" ", "") == "ПРЕМИАЛЬНАЯ":
            try:
                stavka = float(self.textEdit.toPlainText())
                time_hours = int(self.textEdit_2.toPlainText())
                k = int(self.textEdit_3.toPlainText())
                oklad = stavka * time_hours * 1 + k / 100
                ndfl = oklad * 13 / 100
                sarplata = oklad - ndfl
                self.textEdit_4.setPlainText(str(f"{oklad} руб"))
                self.textEdit_5.setPlainText(str(f"{ndfl} руб"))
                self.textEdit_6.setPlainText(str(f"{sarplata} руб"))
            except ValueError:
                self.textEdit.setPlainText("Попробуйте еще раз")
                self.textEdit_2.setPlainText("")



def days_in_month(month_name):
    month_days = {
            'январь': 17,
            'февраль': 20,
            'март': 21,
            'апрель': 22,
            'май': 18,
            'июнь': 19,
            'июль': 23,
            'август': 21,
            'сентябрь': 22,
            'октябрь': 23,
            'ноябрь': 19,
            'декабрь': 17
        }

        # Переводим название месяца в нижний регистр для безопасного сравнения
    month_name_lower = month_name.lower()

        # Проверяем, есть ли такой месяц в словаре
    if month_name_lower in month_days:
        return month_days[month_name_lower]
    else:
        return None


def main():
    app = QApplication(sys.argv)
    wi = MyWidget()
    wi.show()
    sys.exit(app.exec())



if __name__ == '__main__':
    main()