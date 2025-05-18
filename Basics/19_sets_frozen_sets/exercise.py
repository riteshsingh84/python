"""
1. Create any set anf try to use frozenset(setname).

"""
colors = {"red", "green", "blue", "yellow"}
print("check type of colors",type(colors)) # check type of colors

frozen_colors = frozenset(colors)
print("check type of frozen_colors",type(frozen_colors)) # check type of frozen_colors

print("print Colors and Frozen set of colors:", colors,frozen_colors)

colors.add("purple")

# frozen_colors.add("purple")  # This will raise an AttributeError because frozenset is immutable
print("print Colors and Frozen set of colors after adding purple:", colors,frozen_colors)   

"""
2. Find the elements in a given set that are not in another set
"""
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

print("set1:", set1)
print("set2:", set2)

difference_set1_set2 = set1 - set2
print("Difference between set1 and set2 using operator is: ", difference_set1_set2)
print("Difference between set1 and set2 using (difference) method: ", set1.difference(set2))
 
difference_set2_set1 = set2 - set1
print("Difference between set2 and set1 using operator is: ", difference_set2_set1)
print("Difference between set2 and set2 using (difference) method: ", set2.difference(set1))



