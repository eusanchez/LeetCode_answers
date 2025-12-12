# Given an array of integers arr, return true if and only if it is a valid mountain array.

# Recall that arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 

# Example 1:

# Input: arr = [2,1]
# Output: false
# Example 2:

# Input: arr = [3,5,5]
# Output: false
# Example 3:

# Input: arr = [0,3,2,1]
# Output: true

class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
      top_element = max(arr)
      left_side = arr[:arr.index(top_element)]
      right_side = arr[arr.index(top_element)+1:]

      if not left_side or right_side:
        return False

      #check neighbors
      if left_side[-1] >= top_element or right_side[0] >= top_element:
        return False

      #check if left side is decreasing
      for i in range(len(left_side)-1):
        if left_side[i] > left_side[i+1]:
          return False

      #check if right side is increasing
      for i in range(len(right_side)-1):
        if right_side[i] <= right_side[i+1]:
          return False

      return True


  
