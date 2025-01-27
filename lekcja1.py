import socket #dzialanie w ogolnych uslugach sieciowych np tworzenie aplikacji sieciowych 
hostname = socket.gethostname() #pobieranie nazwy hosta 
print (f"hello {hostname}!") #wyswietlenie nazwy hosta 
name = input("Jak masz na imie? ") #pytanie o imie (pobranie danych od uzytkownika)
age = int(input("Ile masz lat? ")) #pytanie o wiek (pobranie danych od uzytkownika) int(input())- konwertuje na liczbe calkowita  
if age >= 18: #sprawdza czy warunek jest spelniony
    print("Jestes pelnoletni!")
else: #jesli warunek nie zostanie spelniony 
    print("Jestes niepelnoletni!")