import b
def x():
    print('x')
    if __name__=="__main__":
        b.y()

import a
def y():
    print('y')
    if __name__=="__main__":
        a.x()
