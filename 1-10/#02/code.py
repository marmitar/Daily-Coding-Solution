def product_array_trivial(nums):
    product = 1
    for num in nums:
        product *= num

    return [product//num for num in nums]


def product_array_quadratic(nums):
    ans = []
    for i in range(len(nums)):
        ans.append(1)
        for j in range(len(nums)):
            if i != j:
                ans[i] *= nums[j]
    
    return ans


def product_array_linear(nums):
    direct = [1]
    inverse = [1]
    n = len(nums)

    for i in range(1, n):
        direct.append(direct[i-1] * nums[i-1])
        inverse.append(inverse[i-1] * nums[n-i])

    return [direct[i]*inverse[n-i-1] for i in range(n)]

print(product_array_linear([3, 2, 1]))
print(product_array_linear([1, 2, 3, 4, 5]))