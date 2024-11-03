from csv import reader


RED = '\u001b[41m'
LIGHT_GREEN = '\u001b[42m'
YELLOW = '\u001b[43m'
END = '\u001b[0m'


# Поиск по автору
def conv(item):
    if item.count(',') == 0:
        return int(item)
    else:
        item = item.replace(',','.')
        return float(item)


while True:
    count = 0
    request = input("Enter a request: ")
    if request.lower() == 'stop':
        print("Thank you for using!")
        break
    else:
        with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
            file = reader(csvfile, delimiter=';')
            for row in file:
                lower_case = row[2].lower()
                index = lower_case.find(request.lower())
                if index != -1:
                    if 150 <= conv(row[6]):
                        count +=1
                        print(
                            f"{row[1]} "
                            f"(Author: {row[2]})"
                        )

        if count == 0:
            print('Nothing found.')