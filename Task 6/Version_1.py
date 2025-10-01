import pandas as pd

bk = pd.read_csv('books-en.csv',sep=';',encoding='latin-1')
bk_ordered = bk.sort_values('Downloads', ascending=False)

print('The 20 most popular books(number of downloads)')
for i in range(20):
    print("{}. ".format(i+1) +'\t' + bk_ordered.iloc[i]['Book-Title'] + ' '*(100-len(bk_ordered.iloc[i]['Book-Title'])),end='')
    print(bk_ordered.iloc[i]['Downloads'])