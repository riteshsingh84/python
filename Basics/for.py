# Write a program to print square of numbers between 1 to 5 except even numbers
for i in range(1,6):
    if i % 2==0:
        continue
        print ("Number is even, so skipping the number ",i)        
    else:
        print("Number is odd, so calculating square ",i*i)

# Write a program to find key using for and break
# key_location = input("Please enter location: ")

# location = ["garage","living","room","chair","closet"]

# for i in location:
#     if i == key_location:
#         print ("key is found in ",i)
#         break
#     else:
#         print("key is not found",i)

# exp  = [2340,2500,2600,2850.50,8976.25]
# total =0.0
# for x in range(len(exp)):
#     print ("Month:", (x+1),"Expense:",exp[x])
#     total = total + exp[x]

# print("Total Expense is: ", total)

#Program to write tables
# table= input("Please enter the number to the table you want to write: ")
# table=int(table)
# for x in range(table,(table*11),table):
#     print(x)


