def average(nums):
    return sum(nums) / len(nums)


def clamp(x, lo, hi):
    return max(lo, min(x, hi))