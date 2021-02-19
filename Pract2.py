def heapif(arr,n,i):
    largest = i
    l=2*i+1
    r=2*i+2

    if l<n and arr[i]<arr[l]:
        largest=l

    if r<n and arr[largest]<arr[r]:
        largest =r

    if largest !=i:
        arr[i],arr[largest]=arr[largest],arr[i]

        heapif(arr,n,largest)
        
def heapSort(arr):
    n =len(arr)

    for i in range(n,-1,-1):
        heapif(arr,n,i)

    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapif(arr,i,0)

arr=[12,11,13,5,6,7]
heapSort(arr)
n=len(arr)
print("Sort array is")
for i in range(n):
    print("%d" %arr[i])
