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

exp = "{}(){[]}(}"

if s.check(exp):
    print("Balanaced Expression")
else:
    print("Unbalanced Expression.")


