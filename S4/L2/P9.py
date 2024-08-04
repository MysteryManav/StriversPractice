# Book Allocation Problem: Allocate minimum no. of pages
def can_allocate_books(books, pages):
    students_required = 1
    pages_allocated = 0
    for book in books:
        if pages_allocated + book <= pages:
            pages_allocated += book
        else:
            students_required += 1
            pages_allocated = book
    return students_required

def book_allocation(books, students):
    n = len(books)
    if students > n:
        return -1

    lo = max(books)
    hi = sum(books)

    while lo <= hi:
        mid = (lo + hi)//2
        students_allocated = can_allocate_books(books, mid)
        if students_allocated > students:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo

books = [12, 34, 67, 90]
students = 2
print(book_allocation(books, students))
