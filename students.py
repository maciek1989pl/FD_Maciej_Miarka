students = {
    'Anna_Nowak': {'age': '23', 'PESEL': '00210112386', 'postal_code': '46127'},
    'Michał_Kowalski': {'age': '42', 'PESEL': '01210545620', 'postal_code': '52641'},
    'Julia_Wiśniewska': {'age': '38', 'PESEL': '02222978952', 'postal_code': '31552'},
    'Kacper_Wójcik': {'age': '19', 'PESEL': '03100732118', 'postal_code': '41004'},
    'Zuzanna_Kamińska': {'age': '25', 'PESEL': '04122165494', 'postal_code': '54331'},
    'Jakub_Lewandowski': {'age': '29', 'PESEL': '05101598726', 'postal_code': '37922'},
    'Natalia_Zielińska': {'age': '22', 'PESEL': '06110123452', 'postal_code': '23100'},
    'Szymon_Szymański': {'age': '52', 'PESEL': '07222956710', 'postal_code': '68221'},
    'Aleksandra_Dąbrowska': {'age': '41', 'PESEL': '08123176530', 'postal_code': '48056'},
    'Filip_Woźniak': {'age': '33', 'PESEL': '09101934594', 'postal_code': '00541'},
    'Amelia_Mazur': {'age': '23', 'PESEL': '10040523457', 'postal_code': '25119'},
    'Bartosz_Krawczyk': {'age': '26', 'PESEL': '11092987433', 'postal_code': '52077'},
    'Weronika_Król': {'age': '18', 'PESEL': '12062178920', 'postal_code': '43287'},
    'Mateusz_Jankowski': {'age': '28', 'PESEL': '13021500100', 'postal_code': '21651'},
    'Martyna_Piotrowska': {'age': '35', 'PESEL': '14123156439', 'postal_code': '22836'},
}

class Student:
    def __init__(self, pesel, age, name, postal_code):
        self.pesel = pesel
        self.age = age
        self.name = name
        self.postal_code= postal_code
        self.borrowed_books = []

        students[self.pesel] = self

    def borrow_book(self, book_title):
        if len(self.borrowed_books) >= 5:
            print(f"{self.name} nie może wypożyczyć więcej niż 5 książek.")
        else:
            self.borrowed_books.append(book_title)
            print(f"{self.name} wypożyczył książkę: {book_title}")

    def return_book(self, book_title):
        if book_title in self.borrowed_books:
            self.borrowed_books.remove(book_title)
            print(f"{self.name} oddał książkę: {book_title}")