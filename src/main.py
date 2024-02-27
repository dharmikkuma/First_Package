import numpy as np  


class calculator():
    
    def sum(a, b):
        answer = a + b

        return answer
    
    def mul(a, b):
        answer = a * b

        return answer

    def dev(a, b):
        if b == 0:
            return print("devision by zero")
        answer = a/ b

        return answer
    
    def sub(a, b):
        answer = a - b

        return answer