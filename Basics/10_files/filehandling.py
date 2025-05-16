"""
This is sample program to work with file.

File Open Modes:
1. r - Opens file for reading only. Throws error if file does not exist.
2. w - Opens file for writing only. If file doesn't exist then it will create new one. if it exist then it will overwrite it.
3. r+ - Opens file for both reading and writing. Throws error if file does not exist.
4. w+ - Opens file for both reading and writing. If file doesn't exist then it will create new one. if it exist then it will overwrite it.
5. a - Opens file in append mode. Whatever you write to file will get appended and original content will not be overwritten.
"""

# Opening a file in writable mode, This will always overwrite the file content
f = open("C://Ritesh//Work//R_AND_D//AI//Python//Exercise//Basics//data//funny.txt","w")

# Writing string into text file
f.write("I love python.")

# closing the text file
f.close()

# Opening a file in writable mode, This will always not overwrite the file content, but append it
f = open("C://Ritesh//Work//R_AND_D//AI//Python//Exercise//Basics//data//funny.txt","a")

# Writing string into text file in new line
f.write("\nI love javascript.")
f.write("\nI love C#.")

# closing the text file
f.close()


# Opening a new file in writeable mode to copy the content and wordcount line by line.
f_write = open("C://Ritesh//Work//R_AND_D//AI//Python//Exercise//Basics//data//funny_wc.txt","w")

# Opening a file in readable mode using with statement. If you open the file using with statement then there is no need to close the file explicitly 
with open("C://Ritesh//Work//R_AND_D//AI//Python//Exercise//Basics//data//funny.txt","r") as f_read:
    # Reading the content from file line by line.
    for line in f_read:
        words = line.split(' ') # Splitting the words with space.
        f_write.write("Wordcount:" + str(len(words)) + " " + line) # Writing the data line by line in new file.

# closing the text file
f_write.close()

# Checking if file is really closed or not
print("f_read is closed: ", f_read.closed)
print("f_write is closed: ", f_read.closed)


