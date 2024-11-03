import xml.dom.minidom as minidom
def conv(item):
    if item.count(',') == 0:
        return int(item)
    else:
        item = item.replace(',','.')
        return float(item)


xml_file = open('currency.xml' , 'r', encoding = 'windows - 1251')
xml_data = xml_file.read()
dom = minidom.parseString(xml_data)
dom.normalize()
elements = dom.getElementsByTagName('Valute')
dictionary = []
value = ''
for node in elements:
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == 'Value':
             value = child.firstChild.data
             dictionary.append (value)
for i in range(len(dictionary)):
 dictionary [i] = conv(dictionary[i])
average = sum(dictionary) / len(dictionary)
average = round (average, 2)

print(average)
xml_file.close()