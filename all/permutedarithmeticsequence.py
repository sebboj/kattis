def arith(nums):
    diff = abs(nums[0]-nums[1])
    p = 0
    while p < len(nums)-1:
        if abs(nums[p]-nums[p+1]) != diff:
            return False
        else:
            p += 1
    return True

cas = int(input())
for z in range(cas):
    lit = input().split(" ")
    lit.remove(lit[0])
    lit = [int(n) for n in lit]
    if arith(lit):
        print("arithmetic")
    else:
        lit.sort()
        if arith(lit):
            print("permuted arithmetic")
        else:
            print("non-arithmetic")