class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_lenght = 0
        window = []

        for i in s:
            while i in window:
                window.pop(0)
            window.append(i)
            

            # buscando el patron mas grande
            if len(window) > max_lenght: # si no se han repetido van para window, entonces si window ha logrado recolectar aunque sea mas de uno, significa que el max_lenght es ese tamano
                max_lenght = len(window)
        
        return max_lenght

'''
iteracion 1:
p not in window
window.append(p)
len(window) = 1 > max_lenght =0 -> max_lenght =1

iteracion 2:
w not in window
window.append(w)
len(window) = 2 > max_lenght =1 -> max_lenght =2

iteracion 3:
w in window -> entra el while
    pop(0) quita p -> window = ["w"]
    como w sigue en window no sale del while, se queda
    pop(0) quita w -> window = []
    sale del while ahora si
window.append("w")
len(window) = 1 > max_lenght=2 ? NO entonces -> max_lenght=2

Porque no se puede poner simplemente window = []?

porque si el s = dvdf cuando este eliminando el caracter repetido me voy a volar el v sin que este repetido. 

'''

        