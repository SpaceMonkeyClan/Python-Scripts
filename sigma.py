#!/usr/bin/env python
"""
This file demonstrates the use of sigma() on two different fucntions, f()
and g().
"""
def f(x):
	return 2*x + 1
	
def g(x):
	return (x - 1) * (x - 3)
	
def sigma(func, frm, to):
	result = 0;
	for i in range(frm, to+1):
		result += func(i)
	return result

sigma(f,2,4)
sigma(g,1,3)
