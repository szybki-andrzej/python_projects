from tkinter import *
import requests
import json


class CurrencyConvert:

    waluty = ["EUR","CAD","HKD","ISK","PHP","DKK","HUF","CZK","AUD",            #implementuje listę walut do wyboru dla użytkownika  
    "RON","SEK","IDR","INR","BRL","RUB","HRK","JPY","THB","CHF","SGD","PLN",
    "BGN","TRY","CNY","NOK","NZD","ZAR","USD","MXN","ILS","GBP","KRW","MYR"]
    

    def __init__(self, master):
    
        self.waluta1=StringVar(root)
        self.waluta1.set("przelicz z")
        self.list = OptionMenu(root, self.waluta1, *self.waluty)
        self.list.pack()

        self.waluta2=StringVar(root)
        self.waluta2.set("przelicz na")
        self.list = OptionMenu(root, self.waluta2, *self.waluty)
        self.list.pack()

        self.lbl = Label(master,text = "wpisz kwotę")
        self.lbl.pack()

        self.value = Entry(root)
        self.value.pack()

        self.button2 = Button(root, text = "Start", command = self.converter)
        self.button2.pack()

        self.result=Text(root, height=3, width= 70)
        self.result.pack()

        self.button = Button(root, text = "Koniec", command = self.quiter)
        self.button.pack()

    def converter(self):
        """Funkcja przypisana do przycisk <Start>"""

        try:
            url = "https://api.exchangeratesapi.io/latest"      
            r = requests.get(url, timeout=5)
            self.waluty = r.json()["rates"]     #nadpisuje tablicę z początku klasy tę pobraną ze strony

            a = self.value.get()
            b = self.waluta1.get()
            c = self.waluta2.get()
            kurs1 = self.waluty.get(b,None)
            kurs2 = self.waluty.get(c,None)
            self.saver()        #program pobrał najnowsze kursy, więc zapisuje je w pliku

            if b == "EUR":
                self.result.delete(1.0,END)     #usuwam wszystko co mogło zostać wpisane w polu result
                self.result.insert(INSERT, float(a)*(float(kurs2)))

            else:
                przelicznik = (float(kurs1))/(float(kurs2))
                self.result.delete(1.0,END)
                self.result.insert(INSERT, float(a)*(float(przelicznik)))

        except ValueError:
            self.result.delete(1.0,END)
            self.result.insert(INSERT, "Invalid value")

        except:     #gdy nie ma połączenia z internetem

            try:        #gdy nie ma połączenia z internetem ale istnieje plik z zapisanymi ostatnimi kursami walut

                js = open("lastrate.json", "rb")
                self.waluty = json.load(js)
                    
                a = self.value.get()
                b = self.waluta1.get()
                c = self.waluta2.get()
                kurs1 = self.waluty.get(b,None)
                kurs2 = self.waluty.get(c,None)
                self.saver()

                if b == "EUR":
                    self.result.delete(1.0,END)
                    self.result.insert(INSERT, "Connection Error\n" + str(float(a)*(float(kurs2))))

                else:
                    przelicznik = (float(kurs1))/(float(kurs2))
                    self.result.delete(1.0,END)
                    self.result.insert(INSERT, "Connection Error\n" + str(float(a)*(float(przelicznik))))

            except:     #gdy nie ma połączenia z internetem i nie istnieje plik

                self.result.delete(1.0,END)
                self.result.insert(INSERT, "Connection Error")
        

    def quiter(self):
        """Funkcja przypisana do <Koniec>"""
        exit(0)

    def saver(self):
        """Funkcja zapisująca tablicę walut do pliku .json"""
        
        with open("lastrate.json", "w") as js:
            json.dump(self.waluty, js)

    
if __name__ == "__main__":
    root = Tk()
    root.title("Konwerter walut")
    root.geometry("300x215")
    CurrencyConvert(root)
    root.mainloop()
