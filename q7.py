# Socho aapke paas 2 lists hain. Aapne aisa code likhna hain jisse ek nayi list banne jisme inn dono lists ke woh item hone chaiye ho dono list mein aa rahe hain. Socho aapki do list yeh hain:
# Code Example

# list1 = [1, 342, 75, 23, 98]
# list2 = [75, 23, 98, 12, 78, 10, 1]

# Inn dono list se aapki nayi list yeh banni chaiye:
# Code Example

# new_list = [1, 23, 75, 98]

# Iss nayi list mein sirf 1, 75 aur 98 isliye hain kyunki aur koi bhi items dono lists mein nahi aa rahi. Dusri saari items ya toh pehli list mein aa rahi hai ya dusri mein.

list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
i=0
newlist=[]
while i<len(list2):
    if list2[i] in list1:
        newlist.append(list2[i])
    i+=1
print(newlist)



 
list1 = [75, 23, 98, 12, 78, 10, 1]
list2= [1, 342, 75, 23, 98]
i=0
newlist=[]
while i<len(list1):
    if list1[i] in list2:
        newlist.append(list1[i])
    i+=1
print(newlist)









# list1 = [1,2,3,4,5,6]
# list2 = [2,3,1,0,6,7]
# i=0
# a=[]
# while i<len(list1):
#     if list1[i] not in list2:
#         a.append (list1[i])
#     i+=1
# print(a)
