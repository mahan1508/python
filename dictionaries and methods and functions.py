dictionary={
    "key1":'value  1 '  ,
    'key2':'value  2 '  ,
    'key3':'value  3 ' 
}
dictionary2={
    'key11':'value11',
    'key12':'value12',
    'key13':'value13'
    }#dictionary will be entered into flower braces{}
print(dictionary.get('key10',"not found"))
print(type(dictionary))#show the type of the dictionary
dictionary['key4']='value 4'
print('updatiing....')#updating the value of keey1
print(dictionary.keys())
print(dictionary.values())
dictionary.update(dictionary2)#combaining two dictionary
dictionary['key1']='value10'#changing the value of key1
dictionary.pop('key4')#key4 will be deleted
print(dictionary)