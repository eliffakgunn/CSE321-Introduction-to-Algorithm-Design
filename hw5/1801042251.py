#CSE321 HW5 
#Elif Akgun 1801042251

#Q1

#Finds the cost of an optimal plan
def costOfOptimalPlan(NY,SF,M,n):
	costNY=NY[0] #if plan begins NY
	costSF=SF[0] #if plan begins SF
	costNY_temp=costNY #this variable for comparing after the costNY change

	#in for loop, for every iteration, whichever path is shorter selects that path
	#it decides which way it should come to the next index
	for i in range(1,n):
		costNY=NY[i]+min(costNY,costSF+M) 
		costSF=SF[i]+min(costSF,costNY_temp+M)
		costNY_temp=costNY

	optimalPlan=min(costNY, costSF)
	return optimalPlan

#Q2

#Sorts sessions by end times
def sortEnds(session): 
    return session[1]  

#Finds the optimal list of sessions with the maximum number of sessions
def optimalListOfSessions(sessions):
	optimalList=[] 
	i=0 #first session as 0 is selected
	optimalList.append(sessions[i])

	for j in range(1,len(sessions)): #0th element has already been added
		#you can be at only one session at the same time and you cannot leave any session before it is over
		if(sessions[i][1] <= sessions[j][0]): #check if sessions cross, select non-crossing sessions
			optimalList.append(sessions[j])
			i=j #continue from the session you have left
	return optimalList

#Q3

#Finds the subarrays of the given array  
def subarrays(arr,tempArr,newArr, i):    
    if (i == len(arr) and tempArr != []): #it does not append empty set
        newArr.append(tempArr)
    
    elif(i !=len(arr)): 
        subarrays(arr,tempArr,newArr,i + 1) #include element in the cuurent index      
        subarrays(arr,tempArr+[arr[i]],newArr,i + 1) #does not include element in the cuurent index

    return newArr

#Returns an array that includes the sum of subarrays elements
def sumOfSubarraysElements(arr,index,sum):
    if(index==len(arr)):
        return sum
    else:
        sum=sum+arr[index]
        return sumOfSubarraysElements(arr,index+1,sum)

#Checks whether there is a subset with the total sum of elements equal to zero
#If finds such a subset, then print the elements of that subset and terminates the function
def conditionalSubarray(arr,index):
    if(index==len(arr)):
    	return -1
    else:
        if(sumOfSubarraysElements(arr[index],0,0)==0):
        	return arr[index]
        return conditionalSubarray(arr,index+1)

#Q4

#Find an alignment between two strings with minimum cost.
def findAlignment(s1, s2, match_score, mismatch_score, gap_score):
    row=len(s1)
    col=len(s2)
    arr=([[0 for i in range (row+col+1)] for i in range (row+col+1)]) #matrix that holds the similarity between
                                                                      #arbitrary prefixes of the two sequences
    #intialize the first row and first column with i*gap_score 
    for i in range(row+col+1):
        arr[i][0] = i * gap_score
        arr[0][i] = i* gap_score  
    
    #fills the cells by the explanation in report file
    for i in range(1,row+1): 
        for j in range(1,col+1):    
            if (s1[i - 1] == s2[j - 1]):
                arr[i][j] = arr[i - 1][j - 1]+match_score
            else:
                arr[i][j] = max(max(arr[i - 1][j - 1] + mismatch_score, arr[i - 1][j] + gap_score) , 
                                arr[i][j - 1] + gap_score )
    
    length = row+col #length max be len(s1)+len(s2) when they dont include same latter
    
    i = row 
    j = col
    
    #pos1 and pos2 used for finding exact length
    pos1 = length
    pos2 = length 

    #alignment of sequence s1 and s2
    s1_last = (length + 1)*[0]
    s2_last = (length + 1)*[0] 

    #fill the s1_last and a2_last with ascii codes of sequence's letters
    while ( not (i == 0 or j == 0)):
        if (s1[i - 1] == s2[j - 1]):      
            s1_last[pos1] = ord(s1[i - 1]) 
            pos1=pos1-1
            s2_last[pos2] = ord(s2[j - 1]) 
            pos2=pos2-1
            i=i-1
            j=j-1 
        
        elif (arr[i - 1][j - 1] + mismatch_score == arr[i][j]): 
            s1_last[pos1] = ord(s1[i - 1]) 
            pos1=pos1-1
            s2_last[pos2] = ord(s2[j - 1] )
            pos2=pos2-1
            i=i-1 
            j=j-1  
        
        elif (arr[i - 1][j] + gap_score == arr[i][j]): 
            s1_last[pos1] = ord(s1[i - 1])
            pos1=pos1-1
            s2_last[pos2] = ord('_')
            pos2=pos2-1
            i=i-1 

        elif (arr[i][j - 1] + gap_score == arr[i][j]): 
            s1_last[pos1] = ord('_')
            pos1=pos1-1
            s2_last[pos2] = ord(s2[j - 1])
            pos2=pos2-1
            j=j-1  
        
    #continue fill the s1_last and s2_last 
    while (pos1 > 0): 
        if (i > 0):
            i=i-1
            s1_last[pos1] = ord(s1[i])
            pos1=pos1-1 
        else:
            s1_last[pos1] = ord('_')
            pos1=pos1-1 
     
    while (pos2 > 0):
        if (j > 0):
            j=j-1
            s2_last[pos2] = ord(s1[j])
            pos2=pos2-1
        else:
            s2_last[pos2] = ord('_' )
            pos2=pos2-1

    index = 1 #for finding which alignment begin
    #when both char are '_' this means that end of alignment and sequences start this index 
    for i in range(length,0,-1):
        if (chr(s2_last[i]) == '_' and chr(s1_last[i]) == '_'):
            index = i + 1 
            break

    print("\n")
    
    print("Alignment of sequences: ")
    for i in range(index,length+1):
        if(i!=length):
        	print(chr(s1_last[i]), end='')
        else:
        	print(chr(s1_last[i]))
 
    for i in range(index, length+1):
        if(i!=length):
        	print(chr(s2_last[i]), end='')
        else:
        	print(chr(s2_last[i]))

    #for row in arr:
    #	print(row) 


    print("The minimum cost of the alignment is ", end='')
    print(arr[row][col],end=".") 
    print("\n")
         
    return

#Q5

#Calculates the sum of the array with the minimum number of operations
def sumOfArray(arr):
	numberOfOperation=0 #number of operation
	while(len(arr)>1): #keep summing to there is a element in array
		arr.sort() #firstly sort the array because more smaller two elements are summing
		sum=arr[0]+arr[1]
		#pop the summing elements
		arr.pop(0) 
		arr.pop(0)
		arr.insert(0,sum) #insert new addition to array
		numberOfOperation=numberOfOperation+sum

	print("Sum of array is: ", arr[0])
	print("Number of operation is: ", numberOfOperation)

#Driver function
def driver():

	print("\n")
	print("QUESTION 1")

	print("Operating costs are:")

	NY=[1,3,20,30] 
	SF=[50,20,2,4]
	M=10

	print("NY=",NY)
	print("SF=", SF)
	print("Moving cost M= ", M)
	print("\n")
	print("The cost of optimal plan: ")
	print(costOfOptimalPlan(NY,SF,M,len(NY)))

	####################################################

	print("\n")
	print("QUESTION 2")

	sessions=[[8,10],[2,5], [1,3], [3,4], [11,12], [0,7], [5,9]]

	print("List of sessions:")
	print(sessions)
	print("\n")

	sessions.sort(key=sortEnds) #firstly sorts the list
	print("Sorted list:")
	print(sessions)
	print("\n")

	print("The optimal list of sessions with the maximum number of sessions:")
	print(optimalListOfSessions(sessions))

	####################################################
	
	print("\n")
	print("QUESTION 3")

	S1=[-1, 6, 4, 2, 3, -7, -5]
	
	print("A set of integer that to be found its subset with the total sum ")
	print("of elements equal to zero:")
	print(S1)
	print("\n")

	subs=subarrays(S1,[],[],0)
	subset=conditionalSubarray(subs,0)

	if(subset==-1):
		print("There is no subset with the total sum of elements equal to zero.")
	else:
		print("A subset with the total sum of elements equal to zero:")
		print(subset)

	print("\n")
	S2=[-1, 6, 4, 2]
	
	print("Another set of integer that to be found its subset with the total sum ")
	print("of elements equal to zero:")
	print(S2)
	print("\n")

	subs=subarrays(S2,[],[],0)
	subset=conditionalSubarray(subs,0)

	if(subset==-1):
		print("There is no subset with the total sum of elements equal to zero.")
	else:
		print("A subset with the total sum of elements equal to zero:")
		print(subset)
	
	####################################################

	print("\n")
	print("QUESTION 4")

	s1="TREE" 
	s2="DEER"

	s3="GEBZE"
	s4="GEBZE"

	s5="ABCD"
	s6="EFGH"
 
	match_score= 2
	mismatch_score = -2
	gap_score = -1

	print("Test1:")

	print("Sequnece 1: ", end="")
	print(s1)

	print("Sequnece 2: ", end="")
	print(s2)
	
	findAlignment(s1, s2, match_score, mismatch_score, gap_score)

	print("Test2:")
	
	print("Sequnece 1: ", end="")
	print(s3)

	print("Sequnece 2: ", end="")
	print(s4)
	
	findAlignment(s3, s4, match_score, mismatch_score, gap_score)

	print("Test3:")
	
	print("Sequnece 1: ", end="")
	print(s5)

	print("Sequnece 2: ", end="")
	print(s6)
	
	findAlignment(s5, s6, match_score, mismatch_score, gap_score)

	####################################################

	print("\n")
	print("QUESTION 5")
	
	arr=[7,3,4,9,2,1]

	print("An array of integers to calculate the sum of its elements: ")
	print(arr)
	sumOfArray(arr)
	print("\n")


driver()