'''
Created on Feb 29, 2016

@author: Michael Koegel / mkoegel@gmail.com

Palindrome time!
'''
#need to import the string features to be able to
#find punctuation in our words / sentences
import string

#creating a function to check for palindromes
def palindrome(sentence):
    #need to remove all spaces, set the word to lower case
    sentence = sentence.lower().replace(" ", "")
    #defining the punctuation to use from our string import
    punct = set(string.punctuation)
    #removing all punctuation from our sentence
    sentence = ''.join(x for x in sentence if x not in punct)
    
    #if the sentence is the same as the sentence in reverse, print message
    if sentence == sentence[::-1]:
        #should show Palindrome with the sentence after it
        return ("Palindrome: %s" % (sentence))
    else: #if it isn't the same forwards and backwards
        #print a message stating that it isn't a palindrome
        return ("Not a Palindrome: %s" % (sentence))

#a couple print methods to test our methods.
print(palindrome("A man, a plan, a canal: panama"))
print(palindrome("tree, houses, are. cool'"))