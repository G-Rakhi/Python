import heapq
def find_klarge(arr,k):
    arr=[- item for item in arr]
    heapq.heapify(arr)
    while k>0:
        s=heapq.heappop(arr)
        k=k-1
    return s*-1

arr=list(map(int, input().split()))
k=int(input())
ans=find_ksmall(arr,k)
print(ans)
