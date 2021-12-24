import time

def sort(nums: list):
    for sort_idx in range(0, len(nums)):
        min_idx = sort_idx
        min_num = nums[sort_idx]
        for cmp_idx in range(sort_idx+1, len(nums)):
            cmp_num = nums[cmp_idx]

            if min_num > cmp_num:
                min_num = cmp_num
                min_idx = cmp_idx

        if min_idx is not sort_idx:
            nums[sort_idx], nums[min_idx] = nums[min_idx], nums[sort_idx]
        
        # print(nums)
    
    
if __name__ == "__main__":
    nums = [3, 4, 2, 1, 22, 25, 12, 10, 5, 120, 0]
    
    start = time.perf_counter_ns()
    sort(nums)
    print(f"Time taken: {time.perf_counter_ns()-start}")
    
    print(f"Sorted list: {nums}")
