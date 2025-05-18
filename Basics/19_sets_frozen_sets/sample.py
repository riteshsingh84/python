# create a set 
basket   = {'apple', 'orange', 'banana', 'pear', 'kiwi','apple','banana','mango'}

print(type(basket)) # check type of basket
print("Fruits in basket: ",basket) # {'banana', 'kiwi', 'orange', 'pear', 'apple','mango'}

# Another way to create a set
fruit_basket = set() # create an empty set
print(type(fruit_basket)) # check type of fruit_basket
# add elements to the set
fruit_basket.add('apple')
fruit_basket.add('orange') 
fruit_basket.add('banana')
# add duplicate element
fruit_basket.add('banana') # this will not add a duplicate element
print("Fruits in new fruit_basket: ",fruit_basket) # {'banana', 'orange', 'apple'}

# remove element from the set
fruit_basket.remove('banana') # remove 'banana' from the set
print("Fruits in new fruit_basket after removing banana: ",fruit_basket) # {'orange', 'apple'}
# remove element from the set using discard
fruit_basket.discard('apple') # remove 'banana' from the set
print("Fruits in new fruit_basket after removing apple using discard: ",fruit_basket) # {'orange'}

fruit_basket.add('kiwi') 
fruit_basket.add('pear')
fruit_basket.add('cherry') 

# check if element is in the set
if 'kiwi' in fruit_basket:
    print("Kiwi is in the fruit_basket") # Kiwi is in the fruit_basket  
else:
    print("Kiwi is not in the fruit_basket")

# check if element is not in the set
if 'banana' not in fruit_basket:
    print("Banana is not in the fruit_basket") # Banana is not in the fruit_basket  

# check length of the set
print("Length of the fruit_basket: ",len(fruit_basket)) # Length of the fruit_basket:  3

# iterate through the set
for fruit in fruit_basket:
    print("Fruit in fruit_basket: ",fruit) # Fruit in fruit_basket:  orange, Fruit in fruit_basket:  kiwi, Fruit in fruit_basket:  pear

frozen_basket = frozenset(basket) # create a frozen set
print("check type of frozen_basket",type(frozen_basket)) # check type of frozen_basket
print("Fruits in frozen_basket: ",frozen_basket) # Fruits in frozen_basket:  frozenset({'banana', 'kiwi', 'orange', 'pear', 'apple'})

# list of all fruits in both basket and fruit_basket
union_basket = basket.union(fruit_basket) # union of two sets
all_fruits = basket | fruit_basket # another way to find union
print("Union of basket and fruit_basket: ",union_basket,all_fruits) # Union of basket and fruit_basket:  {'banana', 'kiwi', 'orange', 'pear', 'apple', 'mango'}

# list of fruits which is present in both basket and fruit_basket
intersection_basket = basket.intersection(fruit_basket) # intersection of two sets
common_fruits = basket & fruit_basket # another way to find intersection
print("Intersection of basket and fruit_basket: ",intersection_basket,common_fruits) # Intersection of basket and fruit_basket:  {'kiwi', 'orange', 'pear', 'apple'}

# list of fruits in basket not in fruit_basket
difference_basket = basket.difference(fruit_basket) # difference of two sets
print("Difference of basket and fruit_basket: ",difference_basket) # Difference of basket and fruit_basket:  {'banana', 'mango'}

# list of fruits in fruit_basket not in basket
difference_fruit_basket = fruit_basket - basket # difference of two sets. Another way to find difference
print("Difference of fruit_basket and basket: ",difference_fruit_basket) 

# Check if fruit_basket is a subset of basket
if fruit_basket < basket:
    print("fruit_basket is a subset of basket") # fruit_basket is a subset of basket
else:
    print("fruit_basket is not a subset of basket")

# Check if all_fruits is a superset of fruit_basket
if all_fruits > fruit_basket:
    print("all_fruits is a superset of fruit_basket") # all_fruits is a superset of fruit_basket            
    
# clear the set
fruit_basket.clear() # clear the set
print("Fruits in new fruit_basket after clearing: ",fruit_basket) # Fruits in new fruit_basket after clearing:  set()

# check if set is empty
if not fruit_basket:
    print("fruit_basket is empty") # fruit_basket is empty


