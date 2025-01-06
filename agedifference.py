boyname=input("name>>")
boy_age=int(input("age>>"))
girlname=input("name>>")
girl_age=int(input("age>>"))
#using abs for absolute value if the girlage is more than boyage
age_difference=abs(boy_age - girl_age)
print(boyname+ " loves " +girlname)
print(".age difference="+str(age_difference))
print(f"{boyname} loves {girlname}.agedifference >>{age_difference}")