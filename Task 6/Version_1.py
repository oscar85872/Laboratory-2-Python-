import pandas as pd

bk = pd.read_csv('books-en.csv',sep=';',encoding='latin-1')
bk_ordered = bk.sort_values('Downloads', ascending=False)

print('The 20 most popular books(number of downloads)')
for i in range(20):
    print("{}. ".format(i+1) +'\t' + bk_ordered['Book-Title'].iloc[i] + ' '*(100-len(bk_ordered['Book-Title'].iloc[i])),end='')
    print(bk_ordered['Downloads'].iloc[i])