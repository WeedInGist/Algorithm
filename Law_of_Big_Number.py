

var = list(map(int, input().split()))
N = var[0]
M = var[1]
K = var[2]
nums = list(map(int,input().split()))
nums.sort()
L=len(nums)
max=M//(K+1)
print(nums[L-1]*max*K+nums[L-2]*max+nums[L-1]*(M-max*(K+1)))