'''
def isKPartitionPossibleRec(arr, subsetSum, taken,
                            subset, K, N, curIdx, limitIdx):
    if subsetSum[curIdx] == subset:

        """ current index (K - 2) represents (K - 1)  
        subsets of equal sum last partition will  
        already remain with sum 'subset'"""
        if (curIdx == K - 2):
            return 1

        # recursive call for next subsetition
        return isKPartitionPossibleRec(arr, subsetSum, taken,
                                       subset, K, N, curIdx + 1, N - 1)

        # start from limitIdx and include
    # elements into current partition
    for i in range(limitIdx, -1, -1):

        # if already taken, continue
        if (taken[i]):
            continue
        tmp = subsetSum[curIdx] + arr[i]

        # if temp is less than subset, then only
        # include the element and call recursively
        if (tmp <= subset):

            # mark the element and include into
            # current partition sum
            taken[i] = 1
            subsetSum[curIdx] += arr[i]
            nxt = isKPartitionPossibleRec(arr, subsetSum, taken,
                                          subset, K, N, curIdx, i - 1)

            # after recursive call unmark the element and
            # remove from subsetition sum
            taken[i] = 0
            subsetSum[curIdx] -= arr[i]
            if (nxt):
                return 1
    return 0


def isKPartitionPossible(arr, N, K):
    # If K is 1,
    # then complete array will be our answer
    if (K == 1):
        return 1

    # If total number of partitions are more than N,
    # then division is not possible
    if (N < K):
        return 0

    # if array sum is not divisible by K then
    # we can't divide array into K partitions
    sum = 0
    for i in range(N):
        sum += arr[i]
    if (sum % K != 0):
        return 0

    # the sum of each subset should be subset (= sum / K)
    subset = sum // K
    subsetSum = [0] * K
    taken = [0] * N

    # Initialize sum of each subset from 0
    for i in range(K):
        subsetSum[i] = 0

    # mark all elements as not taken
    for i in range(N):
        taken[i] = 0

    # initialize first subsubset sum as
    # last element of array and mark that as taken
    subsetSum[0] = arr[N - 1]
    taken[N - 1] = 1

    # call recursive method to check
    # K-substitution condition
    return isKPartitionPossibleRec(arr, subsetSum, taken,subset, K, N, 0, N - 1)

if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        N=int(input())
        arr=[int(x) for x in input().split()]
        k=int(input())

        if(isKPartitionPossible(arr, N, k)
'''

#Initial Template for Python 3

def isSubset( a, n, sum):
		if(sum==0):
		    return 1;
		elif(n==0 and sum!=0):
		    return 0
		if(a[n-1]>sum or a[n-1]==0):
		    return isSubset(a,n-1,sum);
		if(isSubset(a,n-1,sum-a[n-1])==1):
			a[n-1]=0;
			return 1;
		return isSubset(a,n-1,sum);

def isKPartitionPossible(a, n, k):

	sum=0;
# 	int flag;
# 	long mag, pnum;

	for i in range(n):

		sum+=a[i];


	if(sum%k!=0 or n<k):

		return 0;
	else:

		flag = 0 ;
		for i in range(k):
			if(isSubset(a,n,sum/k)==0):

				flag=1;
				return 0;
				# //if(flag==0)
				# //break;


		if(flag == 0):
		    return 1;

	return 1;


if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        N=int(input())
        arr=[int(x) for x in input().split()]
        k=int(input())

        print(isKPartitionPossible(arr, N, k))

