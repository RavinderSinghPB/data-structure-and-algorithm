
def MedianOfArrays(array1, array2):
    #double answer;
    m = len(array1)
    n = len(array2)
    size = ((m+n)//2) +1
    #vector<int> temp_array(size);
    temp_array=[0]*size

    # // i is the pointer to integer vector temp_array
    # // j is the pointer to integer vector array1
    # // k is the pointer to integer vector array2
    # // only process the loop till we get to the median element
    #for(int i=0, j=0, k=0; i<size; i++)
    j=k=0
    for i in range(size):

        #// If array2 has reached its end
        if(k>n-1):

            temp_array[i]= array1[j];
            j+=1


        #// If array1 has reached its end
        elif (j>m-1):

            temp_array[i]= array2[k];
            k+=1


        #// If no array has reached its end pick the smaller element
        elif(array1[j] <= array2[k]):

            temp_array[i]= array1[j];
            j+=1

        elif(array1[j] > array2[k] ):

            temp_array[i]= array2[k]
            k+=1


    #// If m+n is even median is average of middle 2 elements
    if((m+n)%2 == 0):
        answer = (((temp_array[size-1] + temp_array[size-2]))/2)
        if int(answer)==answer:
            answer=int(answer)

    #// If m+n is odd median is middle elements
    else:
        answer = temp_array[size-1]

    return answer








# def MedianOfArrays(arr1,arr2):
#     print(*arr1,*arr2)
#     n1,n2=len(arr1),len(arr2)
#
#     print((n1+n2)%2)
#     if (n1+n2)%2!=0:
#         i,j=0,0
#         while i+j<((n1+n2)//2) and i<n1 and j<n2:
#             if arr1[i]>arr2[j]:
#                 j+=1
#             else:
#                 i+=1
#
#         # print(arr1[i],arr2[j],i,j)
#         if i+j==(n1+n2)//2:
#
#             if arr1[i]>arr2[j]:
#                 return arr2[j]
#             else:
#                 return arr1[i]
#
#         else:
#             if i==n1:
#                 remj=(n1+n2)//2-n1
#                 return arr2[remj]
#             else:
#                 return arr1[(n1+n2)//2-n2]
#
#     i,j=0,0
#
#     while i+j<((n1+n2)/2) and i<n1 and j<n2:
#         if i==n1 or j==n2:
#             if i==n1:
#                 remj=(n1+n1)//2-n1
#                 return (arr2[remj]+arr2[remj+1])/2
#             else:
#                 remi=(n1+n2)//2-n2
#                 return (arr1[remi]+arr1[remi+1])/2
#
#         if arr1[i]>arr2[j]:
#


    # if i==n1-1 or j==n2-1:
    #     if i==n1-1:
    #         return (arr2[j]+arr2[j+1])/2
    #     else:
    #         return (arr1[i]+arr1[i+1])/2
    # else:
    #     if arr1[i]>arr2[j]:
    #         return (arr2[j]+arr2[j+1])/2
    #     elif arr1[i]==arr2[j]:
    #         if arr1[i+1]>arr2[j+1]:
    #             return (arr2[j]+arr2[j+1])/2
    #         else:
    #             return (arr1[i]+arr1[i+1])/2
    #     else:
    #         return (arr1[i]+arr1[i+1])/2



'''
3
3 1 5 9
4 2 3 6 7
2 4 6
4 1 2 3 5
3 1 2 3
7 4 5 6 7 8 9 10 11
'''



if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        arr1=[int(x) for x in input().split()]
        arr2=[int(x) for x in input().split()]

        print(MedianOfArrays(arr1[1:],arr2[1:]))
