#
'''

'''

def findMinimumCost(string):
	# Write your code here.
	if (len(string)%2)!=0:
		return -1
   
	else:
		stack = []
		for i in string:
			if i=='{':
				stack.append(i)
			else:
				if len(stack)>0:
					top = stack[-1]
					if top == '{':
						stack.pop()
					else:
						stack.append(i)
				else:
					stack.append(i)
		a,b = 0,0
		for i in stack:
			if i=='{':
				a+=1
			else:
				b+=1
		return ((a+1)//2) + ((b+1)//2)
			    
	
	
if __name__ == "__main__":
    string = "}}}}}{"
    print(findMinimumCost(string))