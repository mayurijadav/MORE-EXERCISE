# Ek number ka factorial 1 se leke uss number tak ke saare numbers ko ek saath multiply karke nikalta hai.

# Jaise 3 ka factorial 6 hai. Kyunki 1 * 2 * 3 ko calculate karke 6 aata hai

# 4 ka factorial 24 hai. Kyunki 1 * 2 * 3 * 4 ko calculate karke 24 aata hai

# Aise hi 7 ka factorial 5040 hai. Kyunki 1 * 2 * 3 * 4 * 5 * 6 * 7 ko calculate karke 5040 aata hai

# Ab aap ek program likhoge jo ki user se ek integer input lega aur fir uska factorial print karega. Agar user 3 dalega to 6 print karega, 7 dalega toh 5040 print karega aur aise hi dusre numbers ke lie.

a=int(input("enter the no"))
i=1
while i <=a:
    i+=1
print(i*i)