# input ka use kar ke 3 alag variables mein 3 integers ka input lein. Input lene ke baad inn 3 mein se sabse bade number ko print karo
a=int(input("enter no"))
b=int(input("enter no"))
c=int(input("enter no"))
if a>b and a>c:
    print(a,"is greater")
elif b>a and b>c:
    print(c,"is greater")
elif c>a and c>b:
    print(c,"is greater")
else:
    print("somthing is wrong")