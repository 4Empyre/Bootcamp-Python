def findChar(word_list, char):
    new_list = []
    for w in word_list:
        if w.find(char)!=-1:
            new_list.append(w)
    print(new_list)

word_list = ['hello','world','my','name','is','Anna']
char = 'o'
findChar(word_list, char)
