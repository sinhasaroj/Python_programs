def insertion_sort(A):
    for i in range(1,len(A)):
        key = A[i]
        j = i-1

        while j>=0 and A[j]>key:
            A[j+1] = A[j]
            j=j-1

        A[j+1] = key

A = [12,2,123,4,678,54,32,23,1,90]
insertion_sort(A)

print(A)