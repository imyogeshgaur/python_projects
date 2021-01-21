#COMPLEX NUMBERS
z1=5+2j
z2=6+4j
print(z1+z2)
print(z1*z2)
print(z1-z2)
print(z1/z2)
print(type(z1))
#CONVERSIONt
d=10
e=complex(d)
f=float(d)
g=str(d)
print(d)
print(e)
print(f)
print(g)
#RANDOM
import random
print(random.randrange(1,10)) #print any random number betweem 1 to 9
print(random.random())
print()
#STRING SLICING
a="Yogesh Gaur"
print(a[4])
print(a[0:4]) #print character at index 0 to 3
print(a[0:len(a)]) #print wholw string
print(a.strip())#remove whitespaces from begning or end
print(a.lower())#convert all charachters to lowercase
print(a.upper())#convert all charachters to uppercase
print(a.split())#splits the string having spaces into substrings
x="esh"
print('q'in a)# in is used to check wheather the particular letter or group of letter is present in the string or not 
print(x in a)
x="Mukesh"
y="Gaur is"
qw="yogesh gaur"
c='15'
q=15
r=15.67
s='fjkb23'
print(x+y+c+"years old")#string to string concatenation
print(x+y+y.format(q)+'years old')#string to int/float/complex concatenation
f="give me {} i will give you {}" 
print(f.format(r,s))#float/complex concatenation
print(qw.capitalize())#Capitalise the first letter of the first word of the string
print(qw.title())#Capitalise the first letter of each word of the string
print(a.find('e',1,7))#find the index of a particular letter/word in a word/string
print(s.isalnum())#Check whether the string is alpha numeric or not
#MULTILINE STRING
b=''' Hello everyone my name is YOGESH GAUR 
   and i am a student of krishna engineering college 
   mohan nagar ghaziabad '''
print(b)
#Lists
fruits=['apple','mango','litchi','guvava',2]
fruits.append('pomogranate')#add any string/list at the end
fruits.extend('yogesh')#add any string/list seperated by letters
fruits.pop(4)#delete string/list at particular index
fruits.insert(3,'raspbery')#insert string/list at particular index
print(fruits)
#Tupple
car=("Lamborgini","Ferrari","BMW","Mercedes","BMW")
print(car)
print(car.index("BMW",0,3)) #find whether the value is present in a range or not
print(car.count("BMW"))#Count The number of occurance
bike=("Suzuki Hyerbusa","Kawaskai ninja HZ2")
print(type(bike))# It will print tupple when there is a comma in the each quatation
# del is used to delete any list,tupple
vechile=car+bike 
print(vechile) 
# sets
country={"India","USA","Germany","France"}#to add single value in the set
country.add("Nigeria")
print(country)
country.update(["North Korea","South Korea","Russia"])#to add more than one value in the set
print(country)
#remove()/discard() is used to remove an element from the set but if the element is not present in the set remove give error while discard will not give an error
#sets are unordered so pop() will remove any random element from the set
#clear() will make the set an empty set while delete() will delete the set
people={"Indians","Americans","Germans","French","Korean","Russian"}
world=country.union(people)#to combine two sets
print(world)
worlds=country.intersection(people)#to find common among two sets
print(worlds)
print(country.isdisjoint(people))#set1.isdisjoint(set2)=>set1-set2
#dictionary
smartphone1={
  "Processor":"Snapdragon 855+",
  "Camera":"64MP",
  "Display":"SuperAmoled",
  "Battery":"6000mAh"
}
print(smartphone1.get("Camera"))#return the value of the corresponding field
for x in smartphone1:
    print(x)#display the names/fields in the dictonary
    print(smartphone1[x])#display the values in the dictionary
#Nested Dictionary
RAM={
 "brand":"Kingston",
 "clockspeed":"2400Mhz"
 }
GPU={
     "gernation":"GDDR6",
     "clockspeed":"7800Mhz"
 }
Battery={
    "Type":"Lithium Polymer",
    "Backup":"14hrs"
}
Laptop={
    "RAM":RAM,
    "GPU":GPU,
    "Battery":Battery
}
for x in Laptop:
    print(x)
    print(Laptop[x])
#list(),tupple(),set() and dictionary() are in buiilt constructors used to make them 
#function
def yogesh():
    print(yogesh)
    pass #used to avoid any error
#Exception Handelling
aw=int(input("Enter the first number"))
bw=int(input("Enter the second number"))
try:
    print("Divide a by b gives ",aw/bw)
except:
    print("Division by 0 is not defined")
#lambda is used to make an anonymous fuction which is defined in one line
ex= lambda a,b,c : pow(b,2)-4*a*c 
print(ex(1,-1,2))
#class
class YOGESH:
      sub="Maths"
      age="19"
Y=YOGESH()
print(Y.sub)
print(Y.age)








