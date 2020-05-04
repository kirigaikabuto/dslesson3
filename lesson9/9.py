
def add():
    print("Hello world it is ADD")
    main()

def remove():
    print("Hello world it is Remove")
    main()
    
def main():
    print("[1]Add")
    print("[2]Remove")
    num = int(input())
    if num == 1:
        add()
    elif num == 2:
        remove()

main()
