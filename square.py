def sum_of_squ(n):
	sum=0
	for i in range (1,n+1):
		sum=sum+(i*i)
		return sum
		n=int(input("enter the value of n"))
		print(sum_of_squ(n))