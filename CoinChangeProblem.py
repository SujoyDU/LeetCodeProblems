
import sys
coins = [1,3,5,10]
target = 12

minways = [13] * 15
minways[0]=0
print(minways)

for i in range(1,target+1):
    for j in coins:
        if j <= i:
            minways[i] = min(minways[i],minways[i-j]+1)

print(minways)

def coin_recursion(coin_list,target):
    if target == 0 : return 0
    res = sys.maxsize
    for i in coin_list:
        if i <= target:
            temp_res = coin_recursion(coin_list,target-i)+1
            if(temp_res < res) : res = temp_res

    return res

res = coin_recursion(coins,target)
if res>target:
    print(0)