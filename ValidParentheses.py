class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        index = 0
        for item in s:
            stack.append(item)
            print(len(stack))
        while index < len(stack):
            print(stack[index-1])
            if (stack[index] == "("):
                index += 1
                if(stack[index] == ")"):
                    return True
                else:
                    return False
            elif (stack[index] == "["):
                index += 1
                if (stack[index] == "]"):
                    return True
                else:
                    return False
            elif (stack[index] == "{"):
                index += 1
                if (stack[index] == "}"):
                    return True
                else:
                    return False
