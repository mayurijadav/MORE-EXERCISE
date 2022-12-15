# Iss program ko run karo aur dekho ki numlist aur numlistsub20 ki value same aa rahi.
#  Iss code ko ais chane karo jisse hume num_list ki intial value bhi mil jaye.
# # Code Example

# def numbers_less_than_twenty(list):
#     counter = 0
#     while counter < len(list):
#         item = list[counter]
#         if item > 20:
#             list.remove(item)
#         else:
#             counter += 1
#         return list

# num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]

# num_list_sub_20 = numbers_less_than_twenty(num_list)

# print ("Initial list", num_list)
# print ("List that doesn't contain numbers greate than 20", num_list_sub_20)



def numbers_less_than_twenty(list):
    counter = 0
    while counter < len(list):
        item = list[counter]
        if item > 20:
            list.remove(item)
        else:
            counter += 1
        return list

num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]
new=[]
i=0
while i<len(num_list):
    if num_list[i]<=20:
        new.append(num_list[i])
    i+=1
print(new,"this is the list which doent have number greater than 20")

num_list_sub_20 = numbers_less_than_twenty(num_list)

print ("Initial list", num_list)
print ("List that doesn't contain numbers greate than 20", num_list_sub_20)
