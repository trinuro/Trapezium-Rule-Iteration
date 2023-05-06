# This is a project I did on 27/5/2022. Time is from 2:30 pm to 3:20 pm.
# I did this for my semester 2 Math T Project
from __future__ import division
import math

def trapezium(f, n, a, b):
	'''
        f- function [f(x)]
        n- number of trapeziums
        a- lower limit
        b- upper limit
        Returns definite integral of f(x) from range a to b
	'''
	h = (b-a)/n
	area = 0.5*h
	sum_y = f(a)+f(b)

	part_sum = 0

	for i in range(1, n):
		part_sum += f(a+h*i)

	sum_y += 2*part_sum
	area *= sum_y

	return area

def f(x):
	return (math.sin(x**2))

# main function
n= 6
while n<21:

	a = 0
	b = 0.5
	h = (b-a)/n
	#print the values of f(a) from a to b correct to 6 dp
	print(" x | f(x)")
	print("f({:4f}):".format(a),round(f(a), 6))
	for i in range(1,n):
		print("f({:4f}):".format(a+h*i),round(f(a+h*i), 6))
	print("f({:4f}):".format(b),round(f(b), 6))

	# print output correct to 5 dp
	output = trapezium(f, n, a, b)
	print("Number of trapezium is ", n)
	print("Total area is: ", round(output, 5), "(Correct to 5 decimal places)\n")

	n +=2
