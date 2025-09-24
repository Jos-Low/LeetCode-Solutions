list1 = ["Shogun","Piatti","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# Example testcase

dup = []
minindex = []
for n in range(len(list1)):
  if list1[n] in list2:
    for x in range(len(list2)):
      if list2[x] == list1[n]:
        index = x + n
        minindex.append(index)
        if index>minindex[0]:
          continue
        elif index<minindex[0]:
          dup.clear()
          dup.append(list1[n])
        else:  
          dup.append(list1[n])

# Print to test
print(minindex)
print(dup)
