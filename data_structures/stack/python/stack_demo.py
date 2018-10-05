class Stack():
   lst = []
   IsEmpty = False
   IsFull = False
   totalNumberOfElements = 0
   count = 0

   def __init__(self,length):
       self.lst = []
       self.totalNumberOfElements = length;
       print('initialize')

   def push(self,elem):
        print('push')
        if(len(self.lst)< self.totalNumberOfElements):
           self.count += 1
           self.lst.append(elem)
        else:
            self.IsFull = True
            print('Stack is Full')
       

   def pop(self):
        print('pop')
        self.count -= 1
        if(len(self.lst) <= 0):
            self.IsEmpty = True
            print('Stack is Empty')
        else:
            self.IsEmpty = False
            self.lst.pop()
        return 

   def peek(self):
        print('peek')
        if(len(self.lst) == 0):
            self.IsEmpty = True
            return print('Stack is Empty')
        else:
            elem = self.lst[len(self.lst)- 1]
            return elem

def main():
    myStack = Stack(5)
    myStack.push(3)
    myStack.push(4)
    myStack.push(1)
    myStack.push(3)
    myStack.push(5)
    myStack.push(23)
    print(myStack.IsEmpty)
    print(myStack.IsFull)
    myStack.peek()
    myStack.pop()
    myStack.pop()
    print(myStack.IsEmpty)
    print(myStack.IsFull)
    myStack.pop()
    myStack.pop()

if __name__ == "__main__":
    main()