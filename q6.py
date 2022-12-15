# Socho aapko paas ek list hai jisme kuch values baar baar aa rahi hain. 
# Ek aisa code likho jisse aap ek nayi list banayein jisme iss list ki items ek ek baar hi aaye. Jaise:
a=["mayu","pratu","mayu","pratu","raje","vir"]
i=0
b=[]
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    i+=1
print(b)
