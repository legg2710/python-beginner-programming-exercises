
def number_of_bottles():
    b = 99
    for i in range(0,100):
        if b == 2:
            print(str(b)+" bottles of milk on the wall, "+str(b)+" bottles of milk.")
            b = b-1
            print("Take one down and pass it around, "+str(b)+" bottle of milk on the wall.")
        elif b == 1:
            print(str(b)+" bottle of milk on the wall, "+str(b)+" bottle of milk.")
            b = b-1
            print("Take one down and pass it around, no more bottles of milk on the wall.")
        elif b == 0:
            print("No more bottles of milk on the wall, no more bottles of milk.")
            b = 99
            print("Go to the store and buy some more, "+str(b)+" bottles of milk on the wall.")
        else:
            print(str(b)+" bottles of milk on the wall, "+str(b)+" bottles of milk.")
            b = b-1
            print("Take one down and pass it around, "+str(b)+" bottles of milk on the wall.")
    
number_of_bottles()