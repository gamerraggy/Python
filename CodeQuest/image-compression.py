nums= []

cases2 = int(input().rstrip())
for j in range(cases2):
    nums.clear()
    cases = int(input().rstrip())
    for i in range(cases):
        line = float(input().rstrip())
        nums.append(line)

    maxNum = max(nums)
    minNum = min(nums)

    for i in range(len(nums)):
        print(round((nums[i]-minNum)/(maxNum-minNum)*255))
