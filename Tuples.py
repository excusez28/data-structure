#create a tuple with different data types
tuplex = ("tuple",False,3.2,1)
print(tuplex)

#create a tuple
tuplex = (2,8,9,1,4,3)
print(tuplex)

#tuples are immutable, so you cannot add new elements
#using merge of tuples with the + operator, you can add elements and it will create a new tuple

tuplex = tuplex + (9,)
print(tuplex)

#counts the number of occurences of item 50 from a tuple
tuple1 = (20,50,10,70,40,60)
print(tuple1.count(50))

tuplex = (2,8,9,1,4,3)
#used tuple[start:stop] the start index is inclusive and the stop is index
_slice = tuplex[3:5]
#is exclusive
print(_slice)

_slice = tuplex[6:]
#if the start index isnt defined, is taken from the beginning of the tuple
print(_slice)

