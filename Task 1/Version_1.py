import pandas as pd

bk = pd.read_csv('books-en.csv', sep=';', encoding='latin-1')
count = len(bk[bk['Book-Title'].str.len()>30])

print(count)