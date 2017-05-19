"""
Automate the boring stuff ch 8
Create a program to load a text file and let users add their own text anywhere
the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the file

Example: The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected
by these events.
"""
mad_libs = open(r"C:\Users\michael.f.koegel\Documents\Python\MadLibs.txt", "r")
mad_read = mad_libs.read()
mad_content = mad_read.split()
print(mad_content)
mad_libs.close()


for i, j in enumerate(mad_content):
    if j == "ADJECTIVE":
        adjective = input("Please enter an adjective: ")
        mad_content[i] = adjective
    elif j == "NOUN":
        noun = input("Please enter an noun: ")
        mad_content[i] = noun
    elif j == "VERB.":
        verb = input("Please enter an verb: ")
        mad_content[i] = verb + "."
    elif j == "ADVERB":
        adverb = input("Please enter an adverb: ")
        mad_content[i] = adverb

print(" ".join(mad_content))
