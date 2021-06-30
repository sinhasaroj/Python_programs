class Stack:
    def __init__(self) -> None:
        self.stack = []

    def check(self,exp):
        for i in range(len(exp)) :
            if exp[i] == '(' or exp[i] == '{' or exp[i] == '[':
                self.stack.append(exp[i])

            if len(self.stack) == 0:
                return False

            if exp[i] == ')':
                char = self.stack.pop()
                if char != '(':
                    return False

            if exp[i] == "}":
                char = self.stack.pop()
                if char != '{':
                    return False

            if exp[i] == "]":
                char = self.stack.pop()
                if char != '[':
                    return False


        if len(self.stack):
            return False
        else:
            return True
            

s = Stack()

exp = "{}(){[]}(}"  # returns False

if s.check(exp):
    print("Balanaced Expression")
else:
    print("Unbalanced Expression.")


# Another Approach:

# def isValid(exp):
    
#     stack = []
#     opening = '({['
#     closing = ')}]'

#     for char in exp:
#         if char in opening:
#             stack.append(char)
        
#         if char in closing:
#             if len(stack) == 0:
#                 return False

#             elif closing.index(char) != opening.index(stack.pop()):
#                 return False

#     return len(stack) == 0

# exp = '()' returns True

# print(isValid(exp))







