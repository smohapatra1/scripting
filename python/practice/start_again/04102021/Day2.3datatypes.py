# Instructions

#I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

#[https://waitbutwhy.com/2014/05/life-weeks.html](https://waitbutwhy.com/2014/05/life-weeks.html)

#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old. 

#It will take your current age as the input and output a message with our time left in this format:

#> You have x days, y weeks, and z months left. 

#Where x, y and z are replaced with the actual calculated numbers. 
number_of_years=input("Enter the years you wants to live: ")
years_as_age=int(number_of_years)
years_remaining= 90 - years_as_age
days_remaining= years_remaining * 365
weeks_remaining=years_remaining * 52
months_remaining=years_remaining * 30
print (f"You have {days_remaining} days, {months_remaining} months , {weeks_remaining} weeks from {number_of_years} years")
