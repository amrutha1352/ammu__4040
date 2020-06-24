def max_of_three(x,y,z):
	if(x>=y) and (x>=z):
		max=x
	elif(y>=x) and (y>=z):
		max=y
	else:
		max=z
	return max
	x=int(input("enter the value of x"))
	y=int(input("enter the value off y"))
	z=int(input("enter the value of z"))
	print(max_of_three(x,y,z))
				
			