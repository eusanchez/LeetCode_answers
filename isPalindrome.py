# Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # -> bool means it will return a bool as an answer
        return str(x) == str(x)[::-1]

# #sequence[start:stop:step]
# start: The index to begin slicing (inclusive).
# stop: The index to stop slicing (exclusive).
# step: The interval at which elements are taken (can be positive or negative).


# word = "hello"
# reversed_word = word[::-1]
# print(reversed_word)  # Output: "olleh"

# nums = [1, 2, 3, 4, 5]
# reversed_nums = nums[::-1]
# print(reversed_nums)  # Output: [5, 4, 3, 2, 1]


        