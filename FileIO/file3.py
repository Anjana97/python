f=open("word_count")
dict={}
for lines in f:
    words=lines.rstrip(".\n").split(" ")
    for word in words:
        word=word.rstrip(",")
        if word not in dict:
            dict[word]=1
        else:
            dict[word]+=1
for k,v in dict.items():
    print(k,v)

lst=[10,20,30,40,50,100]
print(max(lst))
highest=max(dict,key=dict.get)