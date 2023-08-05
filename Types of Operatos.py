# #Relational operators:
# >  >=   <   <=

#Equality operators:
# == !=

name1 = "monika"

name2 = "titi"   #Lexicographical order  - Dictionary (ascending to descending order)

print(name1>name2)

print(name2>name1)

print(name1==name2)

print(name1!=name2)

print("hi hello")

print("hi \thello")

print("hi \nhello")

print("i'm fine")

print("i\'m fine")


#Constants

MAX_ATTEMPTS = 3

#Assignment Operators

#+=   -=  *=   /=   //=   %=   **=

no = 10
#no = no+1  #no+=1

no+=5
print(no)

no*=2   #no= no*2
print(no)

#Ternary Operators (conditional operators)

#no1= 10, no2 = 20, no3 =30

no1, no2, no3 = 10, 20, 30

no3 =30 if no1>no2 else 40

print(no3)

#Membership Operators

# in , not in

sen = "Today is friday"
print("o" in sen)

print("h" in sen)

print("h" not in sen)

print("o" not in sen)

print("Today" in sen)

print("today" in sen)

print("Today" not in sen)

print("Today" in sen)

#Operators chaining

print(100<200)

print(100>200)

print(100<200<300)

print(100<500<200)

#Bitwise Operators

# (#  &  ~  ^  |  >>  <<)

print(4&5)
print(4|5)
print(4^5)
 no = 10
print(~no)
print(10<<2)
print(40>>2)

#LOgical operators

#and, or and not

print(5 or 4)

result= True

result2= not result

print(result)

print(result2)


#modules

def biggest(n1, n2):
    if n1>n2:
        print(n1, "is greater")
    else:
        print(n1, "is greater")

no1 = int(input("enter no: "))
no1 = int(input("enter no2: "))
biggest(no1, no2)