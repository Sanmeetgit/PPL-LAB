x = "coep"
a = 3
if x == 0:
	raise Exception("x should be positive only")
if a == 1:
	raise ZeroDivisionError("Divided by zero---not possible")
if not type(x) is int:
	raise TypeError("Only integer entries allowed")
