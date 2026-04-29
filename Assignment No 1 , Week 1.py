'''Use print, input, arithmetic operation, logical condition 
Be creative to show your skills in Python. 
Create separate file for each question 
Write question at the top of each file as comments of code.'''

#Q1.
''' write a program that converts a temperature from Celsius to Fahrenheit. (Formula: Fahrenheit = 
(Celsius * 9/5) + 32) '''

#sol.
# celsius=int(input("What is your temprture in skt?"))
# fahrenheit=((celsius * 9/5) + 32)
# print("temprature in sialkot in far is =", fahrenheit)

#Q2.
'''Calculate Area of a Rectangle'''
#sol
# length_of_rec= int(input("enter the lenght of an rectangle:"))
# width_of_rec=int(input("enter a width of an rectangle:"))
# area_of_rec=(length_of_rec * width_of_rec)
# print("area of rectangle is :",area_of_rec)

#Q3.
'''Calculate Compound Interest 
Use the formula: 
CI = P * (1 + R/100)**T - P 
Where P = principal, R = rate, T = time'''

# p = 1000  # Principal amount
# r = 5     # Annual interest rate (%)
# t = 3     # Time in years

# # Calculate Compound Interest
# ci = p * (1 + r / 100)**t - p

# print(f"Compound Interest:",ci)

#Q4.
'''Perimeter of a Rectangle - Take length and width as input and calculate the perimeter.'''

# len_of_rectangle=int(input("Enter a length of a rec:"))

# width_of_rectangle=int(input("Enter width of a recntangle :"))

# perimeter=2*(len_of_rectangle + width_of_rectangle)

# print("Pereimeter of a recnagle is = ", perimeter)


#Q5.
'''Average of Three Numbers - Input three numbers and print their average.'''
#sol.
# num_1=int(input("Enter a first num:"))
# num_2=int(input("Enter sec num:"))
# num_3=int(input("Enter third num:"))
# average=(num_1+num_2+num_3//3)
# print("Average of three numbers is =", average)


#Q6.
'''Square and Cube of a Number - Ask the user for a number and display its square and cube.'''

#sol.

# num = int(input("Enter a number: "))
# square = num ** 2
# cube = num ** 3
# print(f"\nSquare: {square}\nCube: {cube}")

#Q7.
''' Distribute Items Equally - You have n candies and k students. 
Write a program to find: 
how many candies each student gets 
how many are left '''

#sol.
# n = int(input("Enter number of candies: "))
# k = int(input("Enter number of students: "))

# each = n // k
# left = n % k

# print("Each student gets:", each)
# print("Candies left:", left)

#Q8.

'''Calculate Profit or Loss 
Input cost price and selling price. Display either: 
Profit and amount, or 
Loss and amount, or 
No Profit No Loss'''
#sol.
# cost_price = float(input("Enter cost price: "))
# selling_price = float(input("Enter selling price: "))

# if selling_price > cost_price:
#     profit = selling_price - cost_price
#     print("Profit:", profit)
# elif cost_price > selling_price:
#     loss = cost_price - selling_price
#     print("Loss:", loss)
# else:
#     print("No Profit No Loss")

#Q9.
''' Total Marks and Percentage 
Input marks of 5 subjects. Print: 
 Total marks 
 Percentage 
 Average '''

# m1 = float(input("Enter marks of subject 1: "))
# m2 = float(input("Enter marks of subject 2: "))
# m3 = float(input("Enter marks of subject 3: "))
# m4 = float(input("Enter marks of subject 4: "))
# m5 = float(input("Enter marks of subject 5: "))

# total = m1 + m2 + m3 + m4 + m5
# percentage = total / 5
# average = total / 5

# print("Total marks:", total)
# print("Percentage:", percentage)
# print("Average:", average)

#Q10.
''' Salary Calculator 
Input basic salary. Calculate: 
 HRA = 20% of basic 
 DA = 15% of basic 
 Total Salary = Basic + HRA + DA'''
#sol
# basic = float(input("Enter basic salary: "))
# hra = 0.20 * basic
# da = 0.15 * basic

# total_salary = basic + hra + da

# print("Basic Salary:", basic)
# print("HRA (20%):", hra)
# print("DA (15%):", da)
# print("Total Salary:", total_salary)

#Q11.
'''Age in Months and Days 
Input your age in years. Calculate and print age in: 
 Months 
 Days (approximate)'''

# age=int(input("Enter you'r age :"))
 
# age_in_motnhs= age * 12
# age_in_days=age * 365 

# print("age in months :",age_in_motnhs)
# print("age in days :", age_in_days)

#Q12.
'''Currency Converter (USD to PKR) 
Input amount in USD. Convert using a fixed exchange rate. '''

#sol.
# usd=int(input("USD $ ="))
# exchange_rate=280
# usd_to_pkr=usd*exchange_rate
# print("You have pkr :", usd_to_pkr)

#Q13.
'''Sum of First N Natural Numbers 
Input a number n, calculate sum of first n natural numbers. 
Formula: sum = n * (n + 1) / 2'''

#sol

# n=int(input("Natraul Number n="))
# sum=n*(n+1)/2
# print("sum of first:",n,"\nnatural number is :",int(sum))

#Q14.
'''Percentage of Correct Answers 
Input total questions and correct answers, and calculate the percentage score.'''
#sol
# total = int(input("Enter total questions: "))
# correct = int(input("Enter correct answers: "))

# percentage = (correct / total) * 100

# print("Your score is:", percentage, "%")

#Q15.
''' Speed, Distance, and Time 
Input distance and time, and calculate speed.'''
#sol
# distance=float(input("Enter distance in km:"))
# time=float(input("Enter Time in Hours:"))
# speed=distance/time
# print("Speed =",speed,"mph")

#Q16.
'''Calculate Body Mass Index (BMI) 
Input weight (kg) and height (m), then calculate: 
BMI = weight / (height ** 2)'''

# Weight=float(input("Enter your body weight:"))
# Height=float(input("Enter your Height: "))
# BMI=Weight//(Height ** 2)
# print(BMI)

#Q17.
''' Convert Minutes to Hours and Minutes 
Input number of minutes and convert to hours and remaining minutes. 
Example: 130 minutes → 2 hours 10 minutes'''

#Sol.
# number_of_min=int(input("Enter Number of minutes:"))
# Hours_and_Min=number_of_min/60
# print("Total Hours and minutes of given number is :",Hours_and_Min,"Hour and Min")

