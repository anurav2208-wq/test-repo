def bubblesort(lst,n):
    for i in range(n-1):
        for j in range(n-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]

def selectionsort(lst,n):
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if lst[j]<lst[min_index]:
                min_index=j
        lst[i],lst[min_index]=lst[min_index],lst[i]
        print(lst)

def insertionsort(lst,n):
    for i in range(1,n):
        key=lst[i]
        j=i-1
        while j>=0 and lst[j]>key:
            lst[j+1]=lst[j]
            j-=1
        lst[j+1]=key


l=eval(input("enter a list:"))
print("the og list:",l)
insertionsort(l,len(l))
print("the sorted lst:",l)



