books = {
    'ID1': {'author': 'Fiodor Dostojewski', 'title': 'Zbrodnia i kara', 'year_of_release': '1866', 'pages': '576', 'amount': '3'},
    'ID2': {'author': 'George Orwell', 'title': 'Rok 1984', 'year_of_release': '1949', 'pages': '328', 'amount': '5'},
    'ID3': {'author': 'Michaił Bułhakow', 'title': 'Mistrz i Małgorzata', 'year_of_release': '1966', 'pages': '384', 'amount': '2'},
    'ID4': {'author': 'Jane Austen', 'title': 'Duma i uprzedzenie', 'year_of_release': '1813', 'pages': '432', 'amount': '5'},
    'ID5': {'author': 'J.R.R. Tolkien', 'title': 'Hobbit, czyli tam i z powrotem', 'year_of_release': '1937', 'pages': '310', 'amount': '1'},
    'ID6': {'author': 'Bolesław Prus', 'title': 'Lalka', 'year_of_release': '1890', 'pages': '680', 'amount': '6'},
    'ID7': {'author': 'Dan Brown', 'title': 'Kod Leonarda da Vinci', 'year_of_release': '2003', 'pages': '454', 'amount': '4'},
    'ID8': {'author': 'Andrzej Sapkowski', 'title': 'Wiedźmin: Ostatnie życzenie', 'year_of_release': '1993', 'pages': '288', 'amount': '7'},
    'ID9': {'author': 'Jonas Jonasson', 'title': 'Stulatek, który wyskoczył przez okno...', 'year_of_release': '2009', 'pages': '416', 'amount': '4'},
    'ID10': {'author': 'George R.R. Martin', 'title': 'Gra o tron', 'year_of_release': '1996', 'pages': '832', 'amount': '32'},
    'ID11': {'author': 'Antoine de Saint-Exupéry', 'title': 'Mały książę', 'year_of_release': '1943', 'pages': '96', 'amount': '5'},
    'ID12': {'author': 'Paulo Coelho', 'title': 'Alchemik', 'year_of_release': '1988', 'pages': '208', 'amount': '4'},
    'ID13': {'author': 'Aldous Huxley', 'title': 'Nowy wspaniały świat', 'year_of_release': '1932', 'pages': '311', 'amount': '8'},
    'ID14': {'author': 'Mario Puzo', 'title': 'Ojciec chrzestny', 'year_of_release': '1969', 'pages': '448', 'amount': '4'},
    'ID15': {'author': 'J.K. Rowling', 'title': 'Harry Potter i Kamień Filozoficzny', 'year_of_release': '1997', 'pages': '320', 'amount': '6'},
    'ID16': {'author': 'Carlos Ruiz Zafón', 'title': 'Cień wiatru', 'year_of_release': '2001', 'pages': '544', 'amount': '9'},
    'ID17': {'author': 'Stanisław Lem', 'title': 'Solaris', 'year_of_release': '1961', 'pages': '300', 'amount': '7'},
    'ID18': {'author': 'Ken Kesey', 'title': 'Lot nad kukułczym gniazdem', 'year_of_release': '1962', 'pages': '320', 'amount': '3'},
    'ID19': {'author': 'Stephen King', 'title': 'To', 'year_of_release': '1986', 'pages': '1138', 'amount': '2'},
    'ID20': {'author': 'J.D. Salinger', 'title': 'Buszujący w zbożu', 'year_of_release': '1951', 'pages': '277', 'amount': '3'},
    'ID21': {'author': 'Gustave Flaubert', 'title': 'Pani Bovary', 'year_of_release': '1857', 'pages': '384', 'amount': '3'},
    'ID22': {'author': 'Cormac McCarthy', 'title': 'Droga', 'year_of_release': '2006', 'pages': '241', 'amount': '5'},
    'ID23': {'author': 'Nicholas Sparks', 'title': 'Pamiętnik', 'year_of_release': '1996', 'pages': '224', 'amount': '9'},
    'ID24': {'author': 'Dan Brown', 'title': 'Inferno', 'year_of_release': '2013', 'pages': '624', 'amount': '3'},
    'ID25': {'author': 'Harper Lee', 'title': 'Zabić drozda', 'year_of_release': '1960', 'pages': '384', 'amount': '6'},
}

class Book:
    def __init__(self, book_id, author, title, year_of_release, pages, amount):
        self.book_id = book_id
        self.author = author
        self.title = title
        self.year_of_release = year_of_release
        self.pages = pages
        self.amount = amount
