firstname="  mahan"
secondname="   gowda"
fullname=firstname+" "+secondname
print(fullname)#concatination of string

message= "Warning!"
print(message*10)#printing 10 times of messge
print(message.replace("Warning! ","error"))
name='''"chandan said'hello'"
      dharshan said 'hi'
      '''
print(name)
print(len(message))#length of the string


name="mahan"
print(name[2:4])#slicing of string from forward
print(name[-2:-4])
'''slicing of string from backwards the index will be negativve from
                    #backwards'''               
print(name[::2])  #skipping the words
m="mahan is \n \t good boy"#escape sequences in string
print(m)
print(m.upper())