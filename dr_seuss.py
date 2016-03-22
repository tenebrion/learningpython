"""
Dr. Seuss's Green Eggs and Ham

Create a program that reads through the story and makes the letter i uppercase
any time it should be. (Make sure to change it when it's used in sam-I-am's
name too.)
Have your program make a new file, and have it write out the story correctly.
Print out how many errors were corrected.
When you're finished, you should have corrected 84 errors.
"""
count = 0
# opening the file and referencing it by my_file name
with open(r"C:\Users\michael.f.koegel\Documents\GitHub\learningpython\green_eggs_and_ham.txt") as my_file:
    content = my_file.readlines()

# I need to loop through each line and then each char
for line in content:
    for char in line:
        # I don't know if there is a better way to fix
        # both style I's at once
        content = [i.replace("i ", "I ") for i in content]
        content = [i.replace("-i-", "-I-") for i in content]

# quick count of all capital "I's" to see what was modified
# There may be a way to tie it into the previous loops,
# but I'm not sure how
for a_line in content:
    for a_char in a_line:
        if a_char == "I":
            count += 1

# writing the results to a new file so I don't contaminate
# the source file
with open("green_eggs_and_ham_NEW.txt", "w") as new_file:
    new_file.writelines(content)

# just for quick reference on the screen
print(content)
print(count)
