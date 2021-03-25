def staircase(n):
    count = n - (n-1)
    for i in range(0,n):
        printer(count,n)
        count += 1
    
def printer(count,n):
    print_string = ""
    for i in range(0,n-count):
        print_string += " "
    for i in range(0,count):
        print_string += "#"
    print(print_string)
