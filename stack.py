class Stack:
    def __init__(self):
        self.stack = []
    def add(self):
        n=int(input("how many values do you want to push into stack=="))
        for i in range(n):
            print((i+1) , "Enter the value")
            self.stack.append(input())
    def show(self):
        for x in self.stack:
            print(x)
    def remove(self):
        dup=set(self.stack)
        self.stack=list(dup)

AStack = Stack()
AStack.add()
AStack.show()
AStack.remove()
print("after remove the duplicate values")
AStack.show()