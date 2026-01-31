'''Write a code find the give number is Amstrong or not'''

while True:
    def is_Armstrong(num):
        digits = len(str(num))
        temp = num
        total = 0

        while temp > 0:
            digit = temp % 10
            total += digit ** digits
            temp //= 10

        return total == num
    '''
    num = int(input("Enter a number: "))
    print(num,"is An Armstrong Number" if is_Armstrong(num) else "Not An Armstrong")
    '''
    
    #Range Some Number To Some Number
    def get_Armstrong(start,end):
        res=""
        for i in range(st,end+1):
            if is_Armstrong(i):
                res=res+str(i)+"|"
        return res

    st=int(input("Enter Starting Number:"))
    ed=int(input("Enter Ending Number:"))

    print(get_Armstrong(st,ed))
    opt=input("Do You Want to Repeat y|n:")
    if opt == 'n':
        break




