# Beginner Level (Strings Fundamentals) 
# #Q1. Length of a String 
# '''Write a program that reads a string and prints its length. 
# o Input: "hello world" → Output: 11 
# Hint: Use len(s). '''

# s=str(input())
# print(len(s))

# #Q2.Uppercase & Lowercase 
# '''Convert the input string to uppercase and lowercase. 
# o Input: "Python3" → Output: "PYTHON3", "python3" 
# Hint: Methods: s.upper(), s.lower(). '''
# s=str(input())
# print(s.upper())
# print(s.lower())

#Q3. Count a Character 
'''Count how many times a given character appears in a string (case-sensitive). 
o Input: "banana", "a" → Output: 3 
Hint: Use s.count(ch). '''

# s = "banana"
# ch = "a"
# result = s.count(ch)
# print(result)  

#Q4.First & Last Character 
'''
Print the first and last character of a string; handle empty input. 
o Input: "drawer" → Output: First: d, Last: r 
Hint: Check empty with if not s; index via s[0] and s[-1]. '''

# s = input("Enter a string: ")

# if not s:
#     print("String is empty.")
# else:
#     print("First:", s[0], "Last:", s[-1])


#Q5. Check Substring Presence 
'''Check if a substring exists in a string. 
o Input: "data science", "science" → Output: True 
Hint: Use the in operator: sub in s.'''

# s=str(input())
# sub=input()
# if sub in s :
#     print(True)
# else:
#     print(False)

#Q6.Slice a String 
'''Print a substring from index start to end (exclusive). 
o Input: "programming", 3, 8 → Output: "gramm" 
Hint: Use slicing: s[start:end].'''

# s=input()
# print(s[3:8])

#Q7.Reverse a String 
'''Reverse the string. 
o Input: "Python" → Output: "nohtyP" 
Hint: Slicing trick: s[::-1]. '''

# s='python'
# print(s[::-1])

#Q8.. Replace Substring 
'''Replace all occurrences of a word with another (case-sensitive). 
o Input: "I love apples. Apples are great!", "apples", "oranges" 
o Output: "I love oranges. Apples are great!" 
Hint: s.replace(old, new) replaces exactly matching cases. '''

# s='I love apples. Apples are great'
# old='apples'
# new='oranges'
# print(s.replace(old,new))

#Q9.Split and Join 
'''Split a sentence on spaces and join with -. 
o Input: "split this sentence" → Output: "split-this-sentence" 
Hint: s.split() then "-".join(words). '''

# s="split this sentence"
# ch=s.split()
# new="-".join(ch)
# print(new)

#Q10.Strip Whitespace 
'''Remove leading and trailing spaces. 
o Input: "   padded text  " → Output: "padded text" 
Hint: Use s.strip(). '''

# s= "   padded text  "
# print(s.strip())


#Intermediate Level (More Involved String Tasks)

#Q11. Count Vowels & Consonants 
'''Count vowels and consonants (letters only; ignore digits/punctuation). 
o Input: "Hello, World! 123" → Output: Vowels: 3, Consonants: 7 
Hint: Iterate characters; check ch.isalpha(); membership test like ch.lower() in 
"aeiou". '''

# text = "Hello, World! 123"

# vowels = 0
# consonants = 0

# for ch in text:
#     if ch.isalpha():  # only letters
#         if ch.lower() in "aeiou":
#             vowels += 1
#         else:
#             consonants += 1

# print("Vowels:", vowels)
# print("Consonants:", consonants)



#Q12. Palindrome Check (Ignore Case & Non-alphanumerics) 
'''Determine if a string is a palindrome ignoring case and non-alphanumeric characters. 
o Input: "A man, a plan, a canal: Panama!" → Output: True 
Hint: Normalize with ''.join(ch.lower() for ch in s if ch.isalnum()); compare to 
its reverse. '''


# s = "A man, a plan, a canal: Panama!"
# s = ''.join(c.lower() for c in s if c.isalnum())
# print(s == s[::-1])

#Q13. Title Case (Manual) 
'''Convert a sentence to title case without using .title(). 
o Input: "hELLO wORLD from PYTHON" → Output: "Hello World From Python" 
Hint: Split into words; for each word: word[0].upper() + word[1:].lower() 
(guard empty words). '''

# sentence = "hELLO wORLD from PYTHON"

# result = " ".join(
#     word[0].upper() + word[1:].lower() if word else ""
#     for word in sentence.split()
# )

# print(result)  

#Q14. Find All Indices of a Substring (Allow Overlaps) 
'''Return a list of starting indices where a substring occurs. 
o Input: s="aaaa", sub="aa" → Output: [0, 1, 2] 
Hint: Loop i from 0 to len(s) - len(sub); compare slices s[i:i+len(sub)].'''
# s = "aaaa"
# sub = "aa"

# indices = []

# for i in range(len(s) - len(sub) + 1):
#     if s[i:i+len(sub)] == sub:
#         indices.append(i)

# print(indices)  


#Q15. Character Frequency Dictionary 
'''Build a frequency dictionary for characters (case-insensitive, skip spaces). 
o Input: "Baa Baa Black Sheep" 
o Output (order may vary): {'b':3,'a':5,'l':1,'c':1,'k':1,'s':1,'h':1,'e':3,'p':1} 
Hint: Iterate for ch in s.lower(): and if ch != ' ': then count with a dict; 
dict.get(ch, 0)+=1. '''

# var="Baa Baa Black Sheep"

# s={}
# for ch in var.lower():
#     if ch !=" ": 
#         s[ch]=s.get(ch, 0) +1
# print(s)

#Q16.  Anagram Checker 
'''Check if two strings are anagrams (ignore spaces, punctuation, and case). 
o Input: "Listen", "Silent" → Output: True 
Hint: Normalize to letters with ch.isalpha() and lower(), then compare 
sorted(s1) vs sorted(s2) or frequency dicts. '''

# s1 = "Listen"
# s2 = "Silent"

# s1_clean = "".join(ch.lower() for ch in s1 if ch.isalpha())
# s2_clean = "".join(ch.lower() for ch in s2 if ch.isalpha())

# result = sorted(s1_clean) == sorted(s2_clean)

# print(result)  

#Q17.Compress Repeated Characters (RLE-lite) 
'''Compress runs of the same character as <char><count>. 
o Input: "aaabbcaaaa" → Output: "a3b2c1a4" 
Hint: Track current char and run length; flush when char changes or at the 
end.'''
# s = "aaabbcaaaa"

# result = ""
# count = 1

# for i in range(1, len(s) + 1):
#     if i < len(s) and s[i] == s[i - 1]:
#         count += 1
#     else:
#         result += s[i - 1] + str(count)
#         count = 1

# print(result)  


#Q18. Longest Word in a Sentence 
'''Find the longest word; if multiple, return the first. Consider words as alphabetic 
sequences. 
o Input: "Find the longest_word here!" → Output: "longest" 
Hint: Filter to letters using ''.join(ch for ch in token if ch.isalpha()); track max 
by length. '''

# s = "Find the longest_word here!"

# longest = ""

# for token in s.split():
#     # keep only alphabetic characters
#     word = "".join(ch for ch in token if ch.isalpha())
    
#     if len(word) > len(longest):
#         longest = word

# print(longest)  # longest

#Q19. Remove Duplicate Characters but Keep Order 
'''Remove duplicates while preserving the first occurrence order. 
o Input: "banana" → Output: "ban" 
Hint: Maintain a seen set; build result by adding chars not in seen. '''
# s = "banana"

# seen = set()
# result = ""

# for ch in s:
#     if ch not in seen:
#         seen.add(ch)
#         result += ch

# print(result)  # ban

#Q20.. Mask Email Username 
'''Mask all but the first and last character of the username with *; keep domain intact. 
o Input: "john.doe@example.com" → Output: "j******e@example.com" 
Hint: Split on '@'; for the left part, if length ≥ 2, keep first and last and 
replace middle with '*' * (len-2); if shorter, handle edge cases.'''
email = "john.doe@example.com"

# username, domain = email.split("@")

# if len(username) >= 2:
#     masked = username[0] + "*" * (len(username) - 2) + username[-1]
# else:
#     masked = username  # edge case (very short username)

# result = masked + "@" + domain

# print(result)  