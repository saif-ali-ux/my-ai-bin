# #Part D — Python Dictionaries (10 Beginner Questions)
# #Q1.Create a dictionary {'name': 'Ali', 'age': 25} and print the name.
# #Tip: Use d['name'].
# m_dic={
#     'name':'ali',
#     'age':25
# }
# print(m_dic['name'])


# #Q2.Add key 'city': 'Lahore' to a dictionary.
# #Tip: Use assignment: d['city'] = 'Lahore'.
# my_dic={}
# my_dic['city']='Lahor'
# print(my_dic)

# #Q3.Change 'age' in {'name': 'Ali', 'age': 25} to 30.
# #Tip: Assign a new value: d['age'] = 30.
# m_dic={
#     'name':'ali',
#     'age':'25'
# }
# print(m_dic)
# m_dic['age']=30
# print(m_dic)

# #Q4.Delete key 'age' from a dictionary.
# #Tip: Use del d['age'].
# d={
#     'name':'saif',
#     'age':'25'
# }
# print(d)
# del d['age']
# print(d)

# #Q5.Check if key 'salary' exists in a dictionary.
# #Tip: Use in operator.
# s={}
# print('salry' in s)


# #Q6. Print all keys from {'a': 1, 'b': 2}.
# #Tip: Use d.keys().
# g={
#     'a':1,
#     'b':2
# }
# print(g)
# s=g.keys()
# print(s)

# #Q7.Print all values from a dictionary.
# #Tip: Use d.values().
# g={
#     'a':1,
#     'b':2
# }
# print(g)
# s=g.values()
# print(s)

# #Q8.Iterate and print key‑ value pairs from {'x': 10, 'y': 20}.
# #Tip: Use for k, v in d.items()
# g={
#     'x': 10, 
#     'y': 20
# }

# for k, v in g.items():
#     print(k, v)


# #Q9.Use get() to safely read key 'score' from an empty dictionary.
# #Tip: Use d.get('score', default_value).
# d={}
# c=d.get('score', 89)
# print(c)

# #Q10. Create a dictionary from two lists: keys = ['a','b'], values = [1,2].
# #Tip: Use dict(zip(keys, values)).
# keys = ['a', 'b']
# values = [1, 2]

# result = dict(zip(keys, values))
# print(result)