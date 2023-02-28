# Exercise 1
# Reverse the list below in-place using an in-place algorithm. Reverse the strings at the same time.
# two pointer
words = ['this' , 'is', 'a', 'sentence', '.']
def reverse(words):
    left = 0
    right = len(words) - 1
    while left <= right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1
    return words
print(reverse(words))

# Exercise 2
# Create a function that counts how many distinct words are in the string below, then outputs a dictionary with the words as the key and the value as the amount of times that word appears in the string. Should output:
# {'a': 5,
#  'abstract': 1,
#  'an': 3,
#  'array': 2, ... etc...
a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'
def distint_words(a_text):
    words = a_text.split()
    dist_dict = {}
    for word in words:
        if word in dist_dict:
            dist_dict[word] += 1
        else:
            dist_dict[word] = 1
    return dist_dict
print(distint_words(a_text))

# Exercise 3
# Write a program to implement a Linear Search Algorithm. 
# Hint: Linear Searching will require searching a list for a given number. 
nums_list = [10,23,45,70,11,15]
target = 70
def lin_search(nums_list, target):
    for i in range(len(nums_list)):
        if nums_list[i] == target:
            return i
    return -1
print(lin_search(nums_list,target))
# If number is not present return -1
# (I know I probably didn't need the print statement but I still wasn't getting an output after returning -1)