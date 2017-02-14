z = int(input())
o = input().split(" ")
nums = []
for i in range(z):
    nums.append(int(o[i]))
nums.sort()
p = 0
while p < len(nums)-1:
    if nums[p] == nums[p+1]:
        nums.remove(nums[p])
    else:
        p += 1
link = False
lit = ""
n = 0
last = 0
k = 0
while n < len(nums)-1:
    if nums[n]+1 == nums[n+1] and not link:
        lit += str(nums[n])
        last = nums[n+1]
        n += 1
        link = not link
    elif nums[n]+1 == nums[n+1] and link:
        last = nums[n+1]
        k += 1
        n += 1
    elif nums[n]+1 != nums[n+1] and link:
        if k > 0:
            lit += "-" +str(last) + " "
            link = not link
            n += 1
        else:
            lit += " " +str(last) + " "
            link = not link
            n += 1
        k = 0
    elif nums[n]+1 != nums[n+1] and not link:
        lit += str(nums[n]) + " "
        n += 1
if k > 0 and last == nums[-1]:
    lit += "-"+str(nums[-1])
elif link:
    lit += " " + str(nums[-1])
else:
    lit += str(nums[-1])
print(lit)







