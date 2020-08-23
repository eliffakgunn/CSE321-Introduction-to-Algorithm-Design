#CSE321 HW3 
#Elif Akgun 1801042251

#Q3 

#Sorts the given array by insertion sort
def insertionSort(arr,count):
	for i in range(1,len(arr)):
		current=arr[i]
		position=i-1

		while(position>=0 and current<arr[position]):
			arr[position+1]=arr[position]
			position=position-1
			count=count+1

		arr[position+1]=current
		count=count+1
	
	return count

#Sorts the given array by quick sort
def quickSort(arr,low,high,count): 
   right=low
   left=high

   x=low; #pivot
   
   if(low<high):
      
      while(right<left):
         while(arr[right]<=arr[x] and right<high):
            right=right+1
         while(arr[left]>arr[x]):
            left=left-1
         if(right<left):
            arr[right], arr[left] = arr[left], arr[right]
            count=count+1
      
      arr[x], arr[left] = arr[left], arr[x]
      count=count+1

      return quickSort(arr,low,left-1,count)
      return quickSort(arr,left+1,high,count)

   return count

#Q4 

def findMedian(arr,k):
	l=0
	r=len(arr)-1

	while(l<=r):
		p=arr[l]

		i=l
		j=r+1

		while True:
			while True:
				i = i+1
				if(arr[i]>=p):
					break
			while True:
				j = j-1
				if(arr[j]<=p):
					break

			arr[i], arr[j]= arr[j], arr[i]
			
			if(i>=j):
				break

		arr[i], arr[j]= arr[j], arr[i]
		arr[l], arr[j]= arr[j], arr[l]

		if(j>k-1):
			r=j-1
		elif(j<k-1):
			l=j+1
		else:
			return arr[k-1]

#Q5

#Findt the subarrays of the given array  
def subarrays(arr,tempArr,newArr, i):    
    if (i == len(arr) and tempArr != []): #it does not append empty set
        newArr.append(tempArr)
    
    elif(i !=len(arr)): 
        subarrays(arr,tempArr,newArr,i + 1) #include element in the cuurent index      
        subarrays(arr,tempArr+[arr[i]],newArr,i + 1) #does notinclude element in the cuurent index

    return newArr
#Returns an array that includes the sum of subarrays elements
def sumOfSubarraysElements(arr,index,sum):
    if(index==len(arr)):
        return sum
    else:
        sum=sum+arr[index]
        return sumOfSubarraysElements(arr,index+1,sum)

#Returns an array that includes the multiplications of the subarrays
def multiplicationOfSubarraysElemenents(arr, index, mult):
    if(index==len(arr)):
        return mult
    else:
        mult=mult*arr[index]
        return multiplicationOfSubarraysElemenents(arr,index+1,mult)

#Returns an array that includes sum of subbarrays elements are bigger than or equal (min+max)*length/4
def conditionalSubarrays(arr,res,new,index):
    if(index==len(arr)):
    	return new
    else:
        if(sumOfSubarraysElements(arr[index],0,0)>=res):
        	new.append(arr[index])
        return conditionalSubarrays(arr,res,new,index+1)

#Returns an array that includes multiplications of conditional subarrays
def multiplicationOfConditionalSubarrays(arr,new,index):
    if(index==len(arr)):
        return new
    else:
        new.append(multiplicationOfSubarraysElemenents(arr[index],0,1))
        return multiplicationOfConditionalSubarrays(arr,new,index+1)

#returns the optimal subarray
def findOptimalSubarray(arr,new,index):
    if(index==len(arr)):
        return
    else:
        if(multiplicationOfSubarraysElemenents(arr[index],0,1) == min(new)):
            return arr[index]
        else:
            return findOptimalSubarray(arr,new,index+1)

def driver():
	arr1 = [5,4,7,8,1,3,11,10,23,2,6,22,0]
	arr2 = [5,4,7,8,1,3,11,10,23,2,6,22,0]

	print("\n")
	print("QUESTION 3")
	print("The array that will sort:")
	print(arr1)

	print("\n")
	print ("Number of count and sorted array with insertion sort:")      
	print(insertionSort(arr1,0))     
	print(arr1) 

	print("\n")
	print ("Number of count and sorted array with quick sort:")      
	print(quickSort(arr2,0,len(arr2)-1,0))     
	print(arr2) 

	####################################################

	print("\n")
	print("QUESTION 4")
	arr3=[7,13,5,81,29,41,1,3,2]
	print("The array that to be found its median:")
	print(arr3)
	print("Median of the array is:")
	print(findMedian(arr3,int(len(arr3)/2)+1))

	####################################################

	print("\n")
	print("QUESTION 5")

	arr4 = [2, 4, 7, 5, 22, 11]
	res=(min(arr4)+max(arr4))*len(arr4)/4 #sum(B)>=res
	
	subs=subarrays(arr4,[],[],0)
	print("The array that to be found its optimal subbaray:")
	print(arr4)
	

	sumArr=conditionalSubarrays(subs,res,[],0)  #sum>=36 olan subarrayler
	print("\n")
	print("The subbarrays that sum of elements are bigger or equal than (min+max)*length/4:")
	print(sumArr)

	new = multiplicationOfConditionalSubarrays(sumArr,[],0)
	print("\n")
	print("Optimal subarray:")
	newArr=findOptimalSubarray(sumArr, new ,0)
	newArr.sort(reverse = True)
	print(newArr)

driver()
	
	


