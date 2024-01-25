def find_duplicates(nums):
    seen=set()
    duplicates=set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)
t=int(input())
l=list(map(int,input().split()))
r=find_duplicates(l)
print(r[0])