#CSE321 HW4 
#Elif Akgun 1801042251

#Q1 b)

#This function converts a 2D array into the special array only if 
#it can be done with changing one single element in the array.
def specialArray(arr):
	signal=True
	for i in range(0,len(arr)-1):
		for j in range(0,len(arr[0])-1):
			if(arr[i][j]+arr[i+1][j+1]>arr[i][j+1]+arr[i+1][j]): #array is not special
				arr[i][j+1] = arr[i][j+1] + (arr[i][j]+arr[i+1][j+1] - (arr[i][j+1]+arr[i+1][j])) #add difference to arr[i][j+1] to make it special.
				signal=False 
	if(signal==False): #check again the array whether it is special
		return specialArray(arr) 
	else: #array is special now
		return arr


#Q1 c)

def findLeftMinElement(arr1, arr2) :

	for i in range(0,len(arr1[0:len(arr1):2])):
		arr2.append(LeftMin(arr1[0:len(arr1):2][i]))
	temp=1
	for j in range(0,len(arr1[1:len(arr1):2])):
		arr2.insert(temp,LeftMin(arr1[1:len(arr1):2][j]))
		temp=temp+2
	return arr2

def LeftMin(arr1):
	min=arr1[0]

	for i in range(0,len(arr1)):
		if(arr1[i]<min):
			min=arr1[i]
	return min

#Q2

#This function finds the kth element of the merged array of these two sorted arrays.
def findKthElement(arr1,arr2,k):
	m=len(arr1)
	n=len(arr2)

	if(k<1 or k>(m+n)):
		return -1
	if(m==0): #if arr1 is empty
		return arr2[k-1]
	if(n==0): #if arr2 is empty
		return arr1[k-1]
	if(k==1):
		return min(arr1[0], arr2[0])

	#arrays divided k/2 recursivly. So it check which is min; m(and n) or k/2
	temp1 = min(m, int(k/2)) 
	temp2 = min(n, int(k/2))

	if (arr1[temp1-1] < arr2[temp2-1]):
		newArr2=[]
		for i in range(temp1,m):
			newArr2.append(arr1[i])
		return findKthElement(newArr2,arr2,k-temp1) #returns function with the divided arr1 and arr2
	else:
		newArr2=[]
		for j in range(temp2,n):
			newArr2.append(arr2[j])
		return findKthElement(arr1,newArr2,k-temp2) #returns function with the arr1 and divided arr2 

#Q3

#This function finds maximum subarray sum in left psrt, 
#maximum subarray sum in right part and maximum subarray sum in crossing part 
def findMaxSub(arr, first, last) : 
	
	if (first==last) : 
		return arr[first] 

	#middle index 
	middle=int((first+last)/2)

	a=findMaxSub(arr, first, middle) #maximum subarray sum in left part 
	b=findMaxSub(arr, middle+1, last) #maximum subarray sum in right part
	c=findSumOfMaxCrossing(arr, first, middle, last,[]) #maximum subarray sum in crossing part

	return max(a,b,c)

#This function finds max sum of crossing part.
def findSumOfMaxCrossing(arr, first_, middle_, last_,new) : 
	
	leftOfMid= -99999 #we assume that it is infinity in the beginning
	rightOfMid= -99999 #we assume that it is infinity in the beginning
	temp3=0 #sum of elements from first element to middle element
	temp4=0 #sum of elements from middle element to last element
	
	for i in range(middle_, first_-1, -1) : #from middle to fist
		temp3 = temp3 + arr[i] 
		
		if (temp3 > leftOfMid) : #checks wheter new sum is bigger
			leftOfMid = temp3 
			new.append(arr[i])

	for i in range(middle_ + 1, last_ + 1) : #from middle to last
		temp4 = temp4 + arr[i] 
		
		if (temp4 > rightOfMid) :  #checks wheter new sum is bigger
			rightOfMid = temp4 
			new.append(arr[i])
			
	return leftOfMid+rightOfMid  #returns max sum of crossing part

#This function finds an array thats sum of elements is max sum.
#It starts 0th index and adds to sum elements that are in each indexes,
#If sum is max sum return this subarray.
def findMaxSubArray(arr,num):
	
	signal=True

	for j in range(0,len(arr)):
		sum=0
		newArr=[]
		for i in range(j,len(arr)):
			sum=sum+arr[i]
			newArr.append(arr[i])
			if(sum==num):
				signal=False 
				break
		if(signal==False):
			break	
	return newArr

#Q4	

#This function finds that whether given array is bipartite
#To do this it colors all adjacent vertices different colors
#-1 not colored, 1 first color, 0 second color
def isBipartite(arr,start):
	color=[-1]*len(arr) #colors are -1 in the beginning it means that vertices are not colored
	visited=[] #indicates the vertices wheter visited

	current=1
	color[start]=current #color first vertex to 1
	visited.append(start)

	#Like BFS, while visited is not empty keep running
	#It means that out of the while loop all vertices colored proper color (0 or 1)
	while(len(visited)!=0): #if vertices are visited
		#let edge(k,m)
		k=visited.pop()

		if(arr[k][k]==1): #if there is an edge that from vertex to same vertex itself
			return False

		for m in range(len(arr)):
			if(arr[k][m]==1 ): #if there is an edge from k to m
				if (color[k] == color[m]): #if color of vertex k and vertex m is same, this array is not bipartite
					return False
				elif(color[m]==-1): #if vertex m is not colored, color this vertex
					color[m]=current-color[k] #m colored other color
					visited.append(m) #m i visited
	return True

#Q5	

#This function manages a warehouse
def manageWarehouse(arr1,f1,l1,arr2,f2,l2,new):

	if(f1==l1): #after division, if there is one element
		#it can goes to len(price)-1 
		if(f2 != len(arr2)-1): 
			return arr2[f2+1]-arr1[f1] #calculation of gain
		else:
			return

	mid1=int((f1+l1)/2) #middle index of arr1(cost)
	mid2=int((f2+l2)/2) #middle index of arr2(price)

	#divides the arrays into two part
	a=manageWarehouse(arr1,f1,mid1,arr2,f2,mid2,new)
	b=manageWarehouse(arr1,mid1+1,l1,arr2,mid2+1,l2,new)

	#appends all gains
	if(a!=None):
		new.append(a)
	if(b!=None):	
		new.append(b)

#This function finds best day to buy the goods.
def bestDay(arr):
	max=arr[1]
	new=[]
	for i in range(len(arr)):
		if(arr[i]!=None and max<arr[i]):
			max=arr[i]
			for j in range(len(new)):
				new.pop()
			new.insert(0,i)
		elif(arr[i]!=None and max==arr[i]):
			new.append(i)
	return new

#This report if there is no day to make money
def doesItMakeMoney(arr):
	temp=0
	for i in range(len(arr)):
		if(arr[i]!=None and (arr[i]<0 or arr[i]==0)):
			temp=temp+1
	if (temp==len(arr)-1):
		return True
	return False


#Driver function
def driver():

	print("\n")
	print("QUESTION 1.b")

	arr1=[[37,23,22,32], [21,6,7,10],[53,34,30,31],[32,13,9,6],[43,21,15,8]]

	print("An array that is not special:")
	for i in range(len(arr1)):
		print(arr1[i])

	print("\n")
	print("Converted array:")
	for i in range(len(arr1)):
		print(specialArray(arr1)[i])

	print("\n")
	print("QUESTION 1.c")

	print("An array that is special:")
	for i in range(len(arr1)):
		print(arr1[i])	

	print("\n")
	print("Leftmost minimum element in each row:")	
	print(findLeftMinElement(arr1,[]))

	print("\n")
	print("QUESTION 2")

	arr2 = [1,12,18,19,26,31] 
	arr3 = [18,27,28,30] 

	print("Two sorted arrays that will merge:")
	print("arr1= ", arr2)
	print("arr2= ", arr3)
	print("5. element is:",findKthElement(arr2, arr3,5))

	print("\n")
	print("QUESTION 3")
	
	arr4 = [5, -6, 6, 7, -6, 7, -4, 3] 
	arr4_1=[-5,3,-7,9,8,1,-2,-5]

	print("An array thats will find maximum contiguous sum subarray:")
	print(arr4)
	maxSum = findMaxSub(arr4, 0, len(arr4)-1) 
	print("Maximum contiguous sum: ", maxSum)
	print("Contiguous subset having the largest sum: ",findMaxSubArray(arr4,maxSum)) 

	print("\n")

	print("Another array thats will find maximum contiguous sum subarray:")
	print(arr4_1)
	maxSum = findMaxSub(arr4_1, 0, len(arr4_1)-1) 
	print("Maximum contiguous sum: ", maxSum)
	print("Contiguous subset having the largest sum: ",findMaxSubArray(arr4_1,maxSum)) 
	
	print("\n")
	print("QUESTION 4")

	arr5= [ [ 0, 1, 1, 1 ], [ 1, 0, 1, 0 ], [ 1, 1, 0, 1 ], [ 1, 0, 1, 0 ] ] #not bipartite
	arr6=[[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0] ] #bipartite 
	#arr7=[[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]] #bipartite

	print("An array that is not bipartite:")
	for i in range(len(arr5)):
		print(arr5[i])
	print("Is this array is bipartite?")
	if(isBipartite(arr5,0)):
		print("Yes.")
	else:
		print("No.")

	print("\n")

	print("Another array that is bipartite:")
	for i in range(len(arr6)):
		print(arr6[i])
	print("Is this array bipartite?")
	if(isBipartite(arr6,0)):
		print("Yes.")
	else:
		print("No.")

	print("\n")
	print("QUESTION 5")

	cost1=[5,11,2,21,5,7,8,12,13,None]
	price1=[None,7,9,5,21,7,13,10,14,20]
	gain1=[None]

	print("Cost=", cost1)
	print("Price=", price1)

	manageWarehouse(cost1,0,len(cost1)-1,price1,0,len(price1)-1,gain1)
	print("Gain=",gain1)
		
	if(doesItMakeMoney(gain1)):
		print("There is no day to make money.")
	else:
		print("Best day(s) to buy the goods: ", bestDay(gain1))

	print("\n")

	cost2=[6,5,5,None]
	price2=[None,5,5,5]
	gain2=[None]

	print("Cost=", cost2)
	print("Price=", price2)

	manageWarehouse(cost2,0,len(cost2)-1,price2,0,len(price2)-1,gain2)
	print("Gain=",gain2)
		
	if(doesItMakeMoney(gain2)):
		print("There is no day to make money.")
	else:
		print("Best day(s) to buy the goods: ", bestDay(gain2))


	print("\n")


driver()