# 方法1：哈希表
def two_sum2(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
    return []

# 方法2：双指针
def two_sum(nums, target):
    nums_with_index = [(num, i) for i, num in enumerate(nums)]
    nums_sorted = sorted(nums_with_index, key=lambda x: x[0])
    left, right = 0, len(nums_sorted)-1
    while left < right:
        current_sum = nums_sorted[left][0] + nums_sorted[right][0]
        if current_sum == target:
            return [nums_sorted[left][1], nums_sorted[right][1]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

# 测试用例
test_cases = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1])
]

# 主函数
if __name__ == "__main__":
    print("测试两种two_sum实现方法:")
    for nums, target, expected in test_cases:
        print(f"\n输入: nums={nums}, target={target}")
        
        # 测试哈希表方法
        result1 = two_sum2(nums, target)
        print(f"哈希表方法结果: {result1}")
        print(f"是否正确: {result1 == expected}")
        
        # 测试双指针方法
        result2 = two_sum(nums, target)
        print(f"双指针方法结果: {result2}")
        print(f"是否正确: {result2 == expected}")