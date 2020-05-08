a = "welcome"
b = "to"
c = "the"
d = "Hotel"
e = "California"

list1 = [d, e]
print ("list1 " + str(list1))

list2 = [a, b, c]
list3 = list1 + list2
print ("list3" + str(list3))

list4 = list3[4:1:-1]
print ("list4" + str(list4))
list5 = []
list4.reverse ()

for x in range (0, len(list4)):
    list5.append(list4[x])

list5.insert(3,list1)
print ("list5 " + str(list5))

f ="Plenty"
g ="of"
h ="room"
i ="at"

list6 = [f, g, h, i]
list6.append (c)
print ("list6 " + str(list6))

x = 0
list7 = []
for item in list3:
    if item[x] != "t":
        list7.append(item)
print ("list7 " + str(list7))

list8 = 2 * list6
list8.remove("at")
print ("list8" + str(list8))
