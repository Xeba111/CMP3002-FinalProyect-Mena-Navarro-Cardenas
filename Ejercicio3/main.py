
def repeat_num(nums):
    visited = set()
    "visited={}"
    i = 0
    while nums[i]:
        if nums[i] in visited:
            return nums[i]

        visited.add(nums[i])
        i += 1

    return None
