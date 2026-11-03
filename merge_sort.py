def merge_sort(lst):
    if len(lst)<=1:
        return lst
    mid=(len(lst)//2)
    print(lst)
    left=merge_sort(lst[:mid])
    right=merge_sort(lst[mid:])
    return merge(left,right)
def merge(l1,l2):
    if l1 ==[]:
        return l2
    if l2==[]:
        return l1
    if l1[0]<l2[0]:
        return [l1[0]]+ merge(l1[1:],l2)
    return [l2[0]]+ merge(l1,l2[1:])
l=eval(input('enter list:'))
c=merge_sort(l)
print(c)