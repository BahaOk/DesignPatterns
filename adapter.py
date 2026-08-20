class OldPrinter:
    def print_text(self):
        print("Yazdırılıyor...")


class Printer:
    def print(self):
        pass


class PrinterAdapter(Printer):

    def __init__(self, old_printer):
        self.old_printer = old_printer

    def print(self):
        self.old_printer.print_text()


old_printer = OldPrinter()
printer = PrinterAdapter(old_printer)
printer.print()
"""
uyumsuz iki sınıfın birlikte çalışabilmesini sağlamak için araya bir printer dönüştürücü sınıf koyarak 
eski printer ile güncel printerı birbirine uyumlu hale getirdik.
"""