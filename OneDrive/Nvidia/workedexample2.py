#Problem 2: Given a list nums and a number k, find the largest sum of any k numbers in a row
# k = size of the window, find the largest numebr

# variables:
# nums
# k

def list_nums(nums, k):
    window_sum = sum(nums[:k])   # sum of the first k numbers
    best = window_sum            # remembers the biggest sum

    for i in range(k, len(nums)):    # i is the position of the number entering
        enter = nums[i]
        leave = nums[i - k]

        window_sum = window_sum - leave + enter
        best = max(best, window_sum)

    return best                  # outside the loop: runs after every window is checked

print(list_nums([2, 1, 5, 1, 3, 2], 3))   # 9