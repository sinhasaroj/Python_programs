class Stack:
    def __init__(self) -> None:
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self,ele):
        self.stack.append(ele)

    def pop_(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return -1

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return -1

s = Stack()

while True:
    print("PUSH")
    print("POP")
    print("PEEK")

    do = input("What operation you want to perform?")

    if do == "PUSH":
        ele = int(input("Enter the element you want to push."))
        s.push(ele)

    elif do == "POP":
        s.pop_()

        if ele == -1:
            print("Stack is empty.")
        else:
            print("The poped element is {}".format(ele))

    elif do == "PEEK":
        ele = s.peek()

        if ele == -1:
            print("Stack is empty.")
        else:
            print("The peeked element is {}".format(ele))
    else:
        break

    




