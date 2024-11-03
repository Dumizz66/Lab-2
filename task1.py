from csv import reader


c = 0
with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
    file = reader(csvfile, delimiter=';')
    for row in file:
        if len(row[1]) > 30:
            c += 1

print(f"Книги, название которых содержит более 30 символов: {c}")