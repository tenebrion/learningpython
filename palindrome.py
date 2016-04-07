'''
Created on Feb 29, 2016

@author: Michael Koegel / mkoegel@gmail.com

Palindrome time!
'''
#need to import the string features to be able to
#find punctuation in our words / sentences
import string
import time

start_time = time.time()


def palindrome(sentence):
    """
    Simple method to filter out spaces and punctuation and check if
    the sentence is a palindrome
    :param sentence: user generated sentence
    :return:
    """
    sentence = sentence.lower().replace(" ", "")
    punct = set(string.punctuation)
    sentence = ''.join(x for x in sentence if x not in punct)
    
    # if the sentence is the same as the sentence in reverse, print message
    if sentence == sentence[::-1]:
        return "Palindrome: {}".format(sentence)
    else:
        return "Not a Palindrome: {}".format(sentence)

# a couple print methods to test our methods.
print(palindrome("A man, a plan, a canal: panama"))
print(palindrome("tree, houses, are. cool'"))
end_time = time.time()
total_time = (end_time - start_time)
print("Completed in {} seconds".format(total_time))