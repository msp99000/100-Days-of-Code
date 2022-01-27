'''

You are given a string.Your task is to count the frequency of letters of the string and print the letters in descending order of frequency.

'''


word = input()
dct = {}
for i in word:
    dct[i] = dct.get(i,0) + 1

dct = sorted(dct.items(),key=lambda x: (-x[1],x[0]))
for i in dct:
    print(i[0],i[1])
