# 9 March 2023
# Assignment 7
# Dustin Cooksey
# This project takes a users entry and verifies it to be a
# non negative number, then displays the even, odd, and 
# fibonacci sequence of numbers for the users entry.


import pandas as pd
import numpy as np

while True:
    n = int(input("Enter an non-negative integer number: "))
    try:
        num = int(n)
        if num > 0:
            break
        else:
            print("Integer must be greater than 0")
    except ValueError:
        print("Please input an integer")

header_names = ["Even" , "Odd", "Fibonacci"]

even = []
odd = []
fibo = [0,1]

for i in range(n):
  even.append(2*i)
  odd.append(2*i+1)
  if i > 1: fibo.append(fibo[i-2]+fibo[i-1])

dict = {"Even": even , "Odd": odd, "Fibonacci": fibo}

df = pd.DataFrame(dict)

print(df)