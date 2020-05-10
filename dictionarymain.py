d1={
    'harshit':{'age':'21','email':'harshitvasisth@gmail.com'},
    'devansh':{'age':'18','email':'d201601411@gmail.com'},
   }
for i,j in d1.items():
    print('\n' + "users :" + str(i))
    for name,value in j.items():
        print('\t'+ str(name)+' : '+ str(value))
