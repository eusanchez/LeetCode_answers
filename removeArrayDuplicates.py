# Remove Duplicates from Sorted Array

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.

# Return k.

class Solution:
    def removeDuplicates (self, nums: List[int]) -> int:
        lista = []
        for i in nums:
            if i not in lista: 
                lista.append(i)

        for j in range(len(lista)):
            nums ［j］ = lista ［j］
            
        return len(lista)


# Fast Solution

# class Solution:
    # def removeDuplicates(self, nums: List[int]) -> int:
        # k = 1
        # for i in range(1, len(nums)): 
            # if nums[i] != nums[k-1]: # ex: if i[0] != i[1] -> 0 != 2 
                # nums[k] = nums[i] # i[1] = i [1]
                # k += 1
        # return k
        
