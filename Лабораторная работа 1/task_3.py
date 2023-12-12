# TODO Найдите количество книг, которое можно разместить на дискете
diskette_capacity = 1.44 * 1024 * 1024  # в байтах
page_lines = 50
line_symbols = 25
total_symbols = 100 * page_lines * line_symbols
book_size = total_symbols * 4  # в байтах

books_on_diskette = diskette_capacity / book_size
print("Количество книг, помещающихся на дискету:", round(books_on_diskette))
