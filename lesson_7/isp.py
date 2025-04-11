from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print_doc(self):
        pass

class Scannable(ABC):
    @abstractmethod
    def scan_doc(self):
        pass

class Printer(Printable):
    def print_doc(self):
        print("Printing document...")

class Scanner(Scannable):
    def scan_doc(self):
        print("Scanning document...")