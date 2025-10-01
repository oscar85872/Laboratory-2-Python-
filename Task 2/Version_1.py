import pandas as pd

bk = pd.read_csv('books-en.csv', sep=';', encoding='latin-1')
bk['Price'] = bk['Price'].str.replace(',','.')
bk['Price'] = pd.to_numeric(bk['Price'])

asd = True

while asd:
    author = input("Author's name: ").strip()
    
    results = bk[(bk['Book-Author'].str.lower() == author.lower()) & (bk['Price'] < 200)]
    
    print (results)

    while 1:
        respuesta = input("¿Continuar? [y/n]: ").lower()
        if respuesta in ['y', 'n']:
            if respuesta == 'y':
                break
            else:
                asd = False
                break
        else:
            print("Error: Debe ingresar 'y' o 'n'")
            