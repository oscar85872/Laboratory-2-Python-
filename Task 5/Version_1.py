import pandas as pd

bk = pd.read_csv('books-en.csv', sep=';', encoding='latin-1')
publishers = bk['Publisher'].unique()

print("List of publishers without repetitions: ")
print(publishers)

