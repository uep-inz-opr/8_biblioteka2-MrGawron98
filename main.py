class LibraryException(Exception):
    pass

class Library(list):

    def __init__(self):
        super(Library, self).__init__()

    def add_book(self, author, title, year):
        self.append({"author": author, "title": title, "year": year, "reader": "NN"})

    def get_uniques(self):
        return list(set([(book['title'], book['author']) for book in self]))

    def get_uniques_count(self):
        uniques = self.get_uniques()
        result = []
        for book in uniques:
            count = []
            for e in self:
                if e['title'] == book[0] and e['author'] == book[1]:
                    count.append(e)
            result.append((book[0], book[1], len(count)))
        return sorted(result, key = lambda x: x[0])

    def wypozycz(self, title, reader):
        success = False
        if len(self) == 0:
            raise LibraryException("Biblioteka pusta")
        count = 0
        for book in self:
            if book['reader'] == reader:
                count += 1
        if count <= 3:
            for book in self:
                if book['title'] == title and book['reader'] == "NN":
                    book['reader'] = reader
                    success = True
                    break
                if book['title'] == title and book['reader'] == reader:
                    raise LibraryException("Czytelnik już ma tę książkę")
            if not success:
                raise LibraryException("Książka nie jest dostępna")
        else:
            raise LibraryException("Czytelnik ma już 3 książki")


    def oddaj(self, title, reader):
        success = False
        if len(self) == 0:
            raise LibraryException("Biblioteka pusta")
        for book in self:
            if book['title'] == title and book['reader'] == reader:
                book['reader'] = "NN"
                success = True
                break
        if not success:
            raise LibraryException("Czytelnik nie posiada takiej książki")

    def print_library(self):
        print(self)


bib = Library()

n = int(input())

result = []

for i in range(n):
    query = eval(input())
    if len(query) == 4:
        bib.add_book(query[2], query[1], query[3])
        result.append(True)
    elif len(query) == 3:
        action = query[0]
        reader = query[1]
        title = query[2]
        if action == "wypozycz":
            try:
                bib.wypozycz(title, reader)
                result.append(True)
            except LibraryException:
                result.append(False)
        elif action == "oddaj":
            try:
                bib.oddaj(title, reader)
                result.append(True)
            except LibraryException:
                result.append(False)
    #bib.print_library()
for value in result:
    print(value)



































# class Biblioteka:
#
#     def __init__(self, lista_ksiazek = [], egzemplarze = [], czytelnicy = []):
#         self.lista_ksiazek = lista_ksiazek
#         self.egzemplarze = egzemplarze
#         self.czytelnicy = czytelnicy
#
#     def dodaj_egzemplarz_ksiazki(self, tytul, autor, rok):
#         k1 = Ksiazka(tytul, autor)
#         if k1 not in self.lista_ksiazek:
#             self.lista_ksiazek.append(k1)
#         e1 = Egzemplarz(rok_wydania=rok, tytul=tytul, autor=autor)
#         self.egzemplarze.append(e1)
#         for ksiazka in self.lista_ksiazek:
#             if ksiazka == k1:
#                 ksiazka.ile += 1
#
#     def wypisz_ksiazki(self):
#         result = []
#         for e in self.lista_ksiazek:
#             wynik = (e.tytul, e.autor, self.egzemplarze.count(e))
#             result.append(wynik)
#
#         result = sorted(result, key = lambda x: x[0])
#         for r in result: print(r)
#
#     def dzialaj(self, query):
#         action = query[0]
#         if len(query) == 3:
#             nazwisko = query[1]
#             ksiazka = query[2]
#         elif len(query) == 4:
#             tytul = query[1]
#             autor = query[2]
#             rok = query[3]
#
#         if action == "dodaj":
#             self.dodaj_egzemplarz_ksiazki(tytul, autor, rok)
#             return True
#
#         elif action == "wypozycz":
#             czytelnik = Czytelnik(nazwisko)
#             if czytelnik not in self.czytelnicy:
#                 self.czytelnicy.append(czytelnik)
#             for e in self.egzemplarze:
#                 if e.tytul == ksiazka:
#                     self.egzemplarze.remove(e)
#                     self.get_czytelnik_by_name(nazwisko).append(e)
#                     break
#                 else:
#                     return False
#             return True
#
#         elif action == "oddaj":
#             czytelnik = Czytelnik(nazwisko)
#             if czytelnik not in self.czytelnicy:
#                 return False
#
#
#
#
#     def get_czytelnik_by_name(self, name):
#         for czytelnik in self.czytelnicy:
#             if czytelnik.name == name:
#                 return czytelnik
#         return None
#
#
# class Ksiazka:
#
#     def __init__(self, tytul, autor, ile = 0):
#         self.tytul = tytul
#         self.autor = autor
#         self.ile = ile
#
#     def __eq__(self, other):
#         if isinstance(other, Ksiazka):
#             return self.tytul == other.tytul and self.autor == other.autor
#         return False
#
# class Egzemplarz(Ksiazka):
#
#     def __init__(self, rok_wydania, tytul, autor, wypozyczony=False):
#         super().__init__(tytul, autor)
#         self.rok_wydania = rok_wydania
#         self.wypozyczony = wypozyczony
#
# class Czytelnik:
#
#     def __init__(self, nazwisko, wypozyczone = []):
#         self.nazwisko = nazwisko
#         self.wypozyczone = wypozyczone
#
#     def __eq__(self, other):
#         if isinstance(other, Czytelnik):
#             return self.nazwisko == other.nazwisko
#         return False
#
# #########################################################
# bib = Biblioteka()
#
# n = int(input())
#
# for i in range(n):
#     query = eval(input())
#     bib.dzialaj(query)
#
