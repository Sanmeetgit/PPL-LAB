
try:
	import ppl
except ImportError:
	print("No such module exists. Can't be imported")
except NameError:
	print("x is not defined")
except ZeroDivisionError:
	print("Can't divide by zero")
except:
	print("Something else Error has occured ")
else:
	print("No error occured")
finally:
	print("This is finally block")
