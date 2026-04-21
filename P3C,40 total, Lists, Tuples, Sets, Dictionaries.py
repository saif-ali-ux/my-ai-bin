#Part C — Python Sets (10 Intermediate-Level Questions)

#Q1.Given two sets, find elements that are in the first set but not the second.
#Tip: Use the - operator.
from ast import Compare


s={1,2,3,5,9,0}
s1={2,3,4,5}

print(s-s1)

#Q2. Find common items between three sets using intersection.
#Tip: Use set1 & set2 & set3.
s1={1,2,3,4}
s2={3,4,2}
s3={3,4,5,6}
p=s1 & s2 & s3
print(p)


#Q3. Given a sentence, return all unique words in lowercase.
#Tip: Split the string → lowercase → convert to set.
s=('WE are learning PYTHON from NEXSKILL')
unique_words=set(str.lower(s))
print(unique_words)

#Q4. Convert a list with duplicates into a set, then back to a sorted list.
#Tip: Use sorted(set(list)).
l=[1,2,3,4,5,6,7,8,9,1,2,3]
sorted_list=sorted(set(l))
print(sorted_list)

#Q5. Check if one set is a strict subset of another.
#Tip: Use < operator.
S1={1,2,3}
S2={1,2,3,4,5}
print(S1 < S2)


#Q6.Use a set comprehension to collect all squares of numbers from 1–15 that are divisible by 3.
#Tip: Write {x*x for x in ... if x % 3 == 0}.
squares={x*x for x in range(1,16) if x % 3 == 0}
print(squares)

#Q7. Count how many duplicate values exist in a list using sets.
#Tip: Compare lengths: len(list) - len(set(list)).
l=[1,2,3,4,5,6,7,8,9,1,2,3]
print(len(l)- len(set(l)))

#Q8. Write a program to remove all vowels from a string using a set.
#Tip: Use a vowel set and filter characters.
s='NEXSKILL'
vowels={'a','e','i','o','u'}
result=''.join(ch for ch in s if ch.lower() not in vowels)
print(result)

#Q9.Find the symmetric difference between two sets.
#Tip: Use the ^ operator.
s={1,5,9,7}
s2={2,5,9,8}
print(s^s2)

#Q10. Check if two strings are anagrams(contains same characters) using set comparison (unique characters only).
#Tip: Compare set(str1) with set(str2).
str1='listen'
str2='silent'
print(set(str1) == set(str2))
