"""
Dr. Seuss's Green Eggs and Ham

Create a program that reads through the story and makes the letter i uppercase
any time it should be. (Make sure to change it when it's used in sam-I-am's
name too.)
Have your program make a new file, and have it write out the story correctly.
Print out how many errors were corrected.
When you're finished, you should have corrected this many errors.
"""
count = 0
# opening the file and referencing it by my_file name
with open("green_eggs_and_ham.txt") as my_file:
    content = my_file.readlines()

# I need to loop through each line and then each char
for line in content:
    for char in line
        # looking for every i, including those in words
        if "i" in char:
            # instructions call for a count of fixed I's
            count += 1
            # I don't know if there is a better way to fix
            # both style I's at once
            content = [i.replace("i ", "I ") for i in content]
            content = [i.replace("-i-", "-I-") for i in content]

# writing the results to a new file so I don't contaminate
# the source file
with open("green_eggs_and_ham_NEW.txt", "w") as new_file:
    new_file.writelines(content)

#just for quick reference on the screen
print(content)
print(count)