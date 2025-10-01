import pandas as pd
import random

bk = pd.read_csv('books-en.csv',sep=';', encoding='latin-1')
bibliography = []
for i in range(20):
    r = random.randint(0,9408)
    bibliography.append('{}. {} - {}'.format(bk.iloc[r]['Book-Author'],bk.iloc[r]['Book-Title'],bk.iloc[r]['Year-Of-Publication']))

with open (r'Task 3\bibliography.txt','w') as file:
    for linea in bibliography:
        file.write(linea + '\n')
print("File created")
