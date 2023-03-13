
# Gerekli kitaplıkları içe aktarma
import csv
import datetime
import os.path
from os import path

# “Menu.txt” dosyasını oluşturma
with open('Menu.txt', 'w') as menu_file:
    menu_file.write('\nLütfen Bir Pizza Tabanı Seçiniz:\n'
                     '1: Klasik\n'
                     '2: Margarita\n'
                     '3: Türk Pizza\n'
                     '4: Sade Pizza\n\n'
                     've seçeceğiniz sos:\n'
                     '11: Zeytin\n'
                     '12: Mantarlar\n'
                     '13: Keçi Peyniri\n'
                     '14: Et\n'
                     '15: Soğan\n'
                     '16: Mısır\n\n'
                     'Teşekkür ederiz!\n')


# Üst sınıf oluşturma “pizza”
class Pizza:
    def __init__(self):
        self.description = "Hatalı Pizza"

    def get_description(self):
        return self.description

    def get_cost(self):
        pass


# Alt sınıf oluşturma “pizza”
class Klasik(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Klasik Pizza"
        self.cost = 15.0

    def get_cost(self):
        return self.cost


class Margarita(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Margarita Pizza"
        self.cost = 17.5

    def get_cost(self):
        return self.cost


class TurkPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Türk Pizza"
        self.cost = 20.0

    def get_cost(self):
        return self.cost

class SadePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Sade Pizza"
        self.cost = 18.0

    def get_cost(self):
        return self.cost


# Üst sınıf oluşturma “Decorator”
class Decorator(Pizza):
    def __init__(self, component):
        super().__init__()
        self.component = component

    def get_cost(self):
        return self.component.get_cost() + self.cost

    def get_description(self):
        return self.component.get_description() + ' ' + self.description


# Alt sınıf oluşturma “Decorator”
class Zeytin(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Zeytin"
        self.cost = 2.0



class Mantarlar(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Mantarlar"
        self.cost = 2.5


class KeciPeyniri(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Keçi Peyniri"
        self.cost = 3.0


class Et(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Et"
        self.cost = 4.0


class Sogan(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Soğan"
        self.cost = 1.5


class Misir(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Mısır"
        self.cost = 1.5


# Main fonksiyonunu oluşturma
def main():
    # Print menu
    with open('Menu.txt', 'r') as menu_file:
        print(menu_file.read())

    # Pizza için kullanıcıdan input alma
    pizza = None
    while not pizza:
        pizza_choice = input("Lütfen bir pizza seçin (1-4): ")
        if pizza_choice == "1":
            pizza = Klasik()
        elif pizza_choice == "2":
            pizza = Margarita()
        elif pizza_choice == "3":
            pizza = TurkPizza()
        elif pizza_choice == "4":
            pizza = SadePizza()
        else:
            print("Hatalı pizza seçimi, lütfen tekrar deneyin.")
    
    # Sos için kullanıcıdan input alma
    sauce_choice = input("Lütfen bir sos seçin (11-16): ")

    while sauce_choice not in ["11", "12", "13", "14", "15", "16"]:
        print("Hatalı sos seçimi, lütfen tekrar deneyin.")
        sauce_choice = input("Lütfen bir sos seçin (11-16): ")
        
    if sauce_choice == "11":
        pizza = Zeytin(pizza)
    elif sauce_choice == "12":
        pizza = Mantarlar(pizza)
    elif sauce_choice == "13":
        pizza = KeciPeyniri(pizza)
    elif sauce_choice == "14":
        pizza = Et(pizza)
    elif sauce_choice == "15":
        pizza = Sogan(pizza)
    elif sauce_choice == "16":
        pizza = Misir(pizza)
    
    # Pizzanın ücretini hesaplama
    total_cost = pizza.get_cost()

    # Kullanıcıdan bilgilerini alma
    name = input("Lütfen adınızı girin: ")
    id_number = input("Lütfen kimlik numaranızı girin: ")
    card_number = input("Lütfen kredi kartı numaranızı girin: ")
    card_password = input("Lütfen kredi kartı şifrenizi girin: ")

    # Sipariş zamanını kaydetme
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Siparişi Orders_Database.csv dosyasına kaydetme
    with open("Orders_Database.csv", mode="a", newline="") as file:

    # Orders_Database.csv dosyasındaki kolon isimlerini belirleme
        column_names = ["Müşteri Adı", "TC Kimlik Numarası", "Kredi Kartı Numarası", "Kart Şifresi", "Pizza Seçimi", "Ücret", "Sipariş Zamanı"]
        writer = csv.writer(file)

        # Dosyanın boş olup olmadığını kontrol etme
        if path.exists("Orders_Database.csv") and os.stat("Orders_Database.csv").st_size != 0:
            writer.writerow([name, id_number, card_number, card_password, pizza.get_description(), total_cost, timestamp])
        else:
            writer.writerow(column_names)
            writer.writerow([name, id_number, card_number, card_password, pizza.get_description(), total_cost, timestamp])

    # Sipariş mesajını ekranda yazdırma
    print("Siparişiniz için teşekkür ederiz Sevgili "+ name +
          ".\nToplam sipariş tutarınız $" + str(total_cost) +
          ".\nPizzanız çok yakında hazır olacak!")

if __name__ == "__main__":
    main()
