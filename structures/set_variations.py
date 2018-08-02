l = ['spam', 'spam']
print (set(l))
print (set(l))
l1 = frozenset([1, 2, 3, 4, 5])
try:
    l1.add(1)
except:
    print ("Unable to add the element to the set")



