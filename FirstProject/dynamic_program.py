#!/usr/bin/env python3

def twoSum(nums, target):
        saved_nums = {}
        count = 0
        for value in nums:
            saved_nums[count] = value
            compliment = target - value
            if compliment in saved_nums.values() and get_key(compliment, saved_nums) != count:
                return [get_key(compliment, saved_nums), count]
            count += 1

def get_key(val, my_dict):
    for key, value in my_dict.items():
         if val == value:
             return key
 
    return "key doesn't exist"






if __name__ == "__main__":
    print(twoSum([7, 32, 500, 4, 20, 18], 50))
