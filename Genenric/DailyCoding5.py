

def cons(a,b):
    def pair(f):
        return f(a, b)
    return pair

def car(A):
    def getFirst(a,b):
        return a
    return A(getFirst)

def cdr(A):
    def getSecond(a,b):
        return b
    return A(getSecond)

temp = cons(3,4)
print(car(temp))
print(cdr(temp))
print("Done")