# Hum iss program mein ek password checker banayenge jo yeh sunchit karega ki humara password strong hai.

# Pehle user se ek password ka string input lijiye.
# Fir check kariye ki user ka password sakht hai ya nahi. Ek sakht password ko yeh sab rule follow karne chaiye:

# 1

# Kam se kam uski length 6 honi chaiye

# 2

# Jada se jada length 16 se jyada na ho

# 3

# Kam se kam ek dollar ka sign ($) hona chaiye

# 4

# Kam se kam password mein 2 ya 8 hona chaiye

# 5

# Password mein capital A ya capital Z hona chaiye

# Agar password yeh rules follow kar raha hai toh "Strong Password" print karo, nahi toh "Weak Password" type karo

char=(input("enter charecter"))
num=(input("enter num"))
specialchar=(input("enter special charecter"))
spw=char+num+specialchar
if char>="A" or char<="Z" and char>="a" or char<="z"  :
    # print(char)
    if num>="0" or num<="9":
    # print(num)
        if specialchar=="@" or specialchar=="$" or specialchar=="#":
            spw=char+num+specialchar
            if len(spw)==10:
                x=spw.split()
                print(x)
                print(spw)
                print("strong password")
            else:
                print("week password")


























# a=int(input("enter no"))
# b=int(input("entter no"))
# c=a*5+b*7
# print(c)































# a=int(input("enter no"))
# b=int(input("enter no"))
# c=a+b
# if c%2==0:
#     print("yes")
#     print(c)
# else:
#     print("no")
#     print(c)
    