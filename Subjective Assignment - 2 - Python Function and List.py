#!/usr/bin/env python
# coding: utf-8

# # Assignments

# Q1. Write the Python function to get a string made of 4 copies of the last
# two characters of the specified string (length must be at least 2).
# 
#     Sample function and result :
#     insert-end ('Python') -> abababab
#     insert-end('Exercises') -> jkjkjkjk

# In[ ]:





# Q2. Write the python function to get a string made of its first three
# characters of a specified string. If the length of the string is less than 3
# then return the original string.
#     
#     Sample function and result :
#     first-three('ipy') -> ipy
#     first-three('python') -> pyt

# In[34]:


def stringmade(a):
    if len(a) < 3:
        print(a)
    else:
        result = (a[:3])
    return (result)


# In[41]:


print(stringmade('ABCDE'))


# Q3. Write the Python program to find smallest window that contains all
# characters of the given string?
# 
#     Original Strings:
#     asdaewsqgtwwsa
#     Smallest window that contains all characters of the said string:
#     Daewsqgt

# In[ ]:





# Q4. Write the Python program to count number of substrings from a
# given string of lowercase alphabets with exactly k distinct (given)
# characters?
# 
#     Input a string (lowercase alphabets): wolf
#     Input k: 4
#     Number of substrings with exactly 4 distinct characters: 1

# In[ ]:





# Q5. Write the Python program to count number of non-empty
# substrings of the given string?
# 
#     Input a string: w3resource
#     Number of substrings:
#     55

# In[54]:


print(len('w3resource'))


# In[55]:


def nonemptysubstrings(x): 
	a = len(x); 
	return int(a * (a + 1) / 2); 


# In[56]:


print(nonemptysubstrings("w3resource"))


# Q6. Write the Python program to count the number of strings where the
# string length is 2 or more, and first and last character are same
# from a given list of strings.
# 
#     Sample List : ['abc', 'xyz', 'wxw', '1331']
#     Expected Result: 2

# In[70]:


def first_char(a):
    x = 0
    for i in a:
        if len(i)>1 and i [0] == i[-1]:
            x +=1
    return x       


# In[71]:


print(first_char(['abc', 'xyz', 'wxw', '1331']))


# Q7. Write the Python program to get a list, sorted in increasing order by
# the last element in each tuple from the given list of non-empty
# tuples?
# 
#     Sample List - [ (2, 5), (1, 2), (4, 4), (2, 3), (2, 1) ]
#     Expected Result - [ (2, 1), (1, 2), (2, 3), (4, 4), (2, 5) ]

# In[ ]:





# Q8. Write the Python program to remove duplicates from a list?

# In[73]:


def duplicate(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b
a = [10,20,30,40,50,60,30,70,20]
print(duplicate(a))


# Q9. Write the Python program to find the list of words that are longer
# than n from a given list of words?

# In[74]:


def filter_long_words(n, str):
    list = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            list.append(x)
    return list	
print(filter_long_words(2, "what is name"))


# Q10. Write the Python program to print a specified list after removing the
# 0th, 4th, and 5th elements?
#     
#     Sample List - ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#     Expected Output - ['Green', 'White', 'Black']

# In[93]:


a = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
l = []
for i in a:
    if(a.index(i)) != 0 and (a.index(i)) != 4 and (a.index(i)) != 5:
        l.append(i)
print(l)


# Q11. Write the Python program to generate all permutations of a list in
# Python?

# In[ ]:





# Q12. Write the Python program to convert a pair of values into a sorted
# unique array?
#  
#     Original List- [ (1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10) ]
#     Sorted Unique Data- [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] 
# 

# In[105]:


a = [ (1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10) ]
b = []
for i in a:
      if i not in b:
            b.append(i)
print(b) 


# ## Great job!
