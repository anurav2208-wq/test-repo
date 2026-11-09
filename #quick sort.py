#quick sort
def quick_sort(lst,a,b):
    #base case
    if a>=b:
        return lst
    #recursive case
    p=partition(lst,a,b)
    quick_sort(lst,a,p-1)
    quick_sort(lst,p+1,b)


def partition(lst,low,high):
    pivot=lst[high]
    i=low-1
    for j in range(low,high):
        if lst[j]<pivot:
            i+=1
            lst[i],lst[j]=lst[j],lst[i]
    lst[i+1],lst[high]=lst[high],lst[i+1]
    return i+1

l=eval(input("enter a list:"))
print("the og list:",l)
quick_sort(l,0,len(l)-1)
print(l)

