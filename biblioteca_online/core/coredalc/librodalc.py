from core.models import Libro

def get_book_by_ispn(ispn) -> Libro:
    libro = Libro.objects.filter(ispn=ispn).first()
    return libro
