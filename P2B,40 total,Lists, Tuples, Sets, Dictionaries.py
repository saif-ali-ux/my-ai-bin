# #Part B — Python Tuples (10 Intermediate-Level Questions)
# #Q1. Convert the list [1, 2, 3, 4] into a tuple and then unpack it into four variables.
# #Tip: Use tuple() and simple unpacking.
# l= [1, 2, 3, 4]
# t=tuple(l)
# a,b,c,d=t
# print(t)

# #Q2.2. Given t = (('a', 1), ('b', 2), ('c', 3)), create a list of all second elements.
# #Tip: Use a comprehension: x[1].
# t = (('a', 1), ('b', 2), ('c', 3))
# result = [x[1] for x in t]
# print(result)

# #Q3. Write a function that returns multiple values (sum, min, max) using a tuple.
# #Tip: Return (..., ..., ...) and unpack later
# def calculate_stats(numbers):
#     return sum(numbers), min(numbers), max(numbers)
# nums = [10, 5, 8, 20]

# total, minimum, maximum = calculate_stats(nums)

# print("Sum:", total)
# print("Min:", minimum)
# print("Max:", maximum)


# #Q4. Combine two tuples (1, 2, 3) and (4, 5) then convert the result to a list.
# #Tip: Use + to join them.
# t1 = (1, 2, 3)
# t2 = (4, 5)

# result = list(t1 + t2)
# print(result)


# #Q5.Given a tuple of numbers, find the element with the highest frequency.
# #Tip: Loop through unique items using set(t).
# t = (1, 2, 2, 3, 3, 3, 4)

# max_count = 0
# most_frequent = None

# for num in set(t):
#     count = t.count(num)
#     if count > max_count:
#         max_count = count
#         most_frequent = num

# print(most_frequent)

# #Q6.Check if two tuples contain the same elements regardless of order.
# #Tip: Compare sorted(tuple) values.
# t1 = (1, 2, 3)
# t2 = (3, 2, 1)

# print(sorted(t1) == sorted(t2))

# #Q7.. Extract the last three items from a tuple using slicing.
# #Tip: Use negative indexing: t[-3:].
# t = (1, 2, 3, 4, 5)
# result=t[-3:]
# print(result)

# #Q8:Concatenate a tuple with itself three times (repeat operation).
# #Tip: Use tuple * 3.
# t = (1, 2, 3)
# results = t * 3
# print(results)

# #Q9.Convert a nested tuple) ((1,2),(3,4)) into a flat tuple (1,2,3,4).
# #Tip: Use a comprehension inside tuple().
# t= ((1,2),(3,4))
# result = tuple(item for subtuple in t for item in subtuple)
# print(result)

# #Q10.Store coordinates in tuples and calculate the Manhattan distance.
# #Tip: Use absolute difference formula: abs(x1-x2) + abs(y1-y2).
# def manhattan_distance(coord1, coord2):
#     return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])
# point1 = (3, 4)
# point2 = (1, 2)
# distance = manhattan_distance(point1, point2)
# print("Manhattan Distance:", distance)
