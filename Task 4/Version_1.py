from xml.dom.minidom import parse

file = parse('currency.xml')

diccionary = {}

numcode = file.getElementsByTagName('NumCode')
charcode = file.getElementsByTagName('CharCode')

for i in range(len(numcode)):
    diccionary[charcode[i].firstChild.data]= numcode[i].firstChild.data   
print(diccionary)
