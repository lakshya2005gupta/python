    
def prime () :
    num = int(input("Enter a number: "))
    i = 2
    count = 0
    while i < num:
            if num % i == 0:
                count = count + 1
            i = i + 1

    if count == 0 and num > 1:
            print("Prime Number")
    else:
            print("Not a Prime Number")
prime()
ans = input("Do you want to check another number? (yes/no): ")
while ans.lower() == 'yes':
    prime() 
    ans = input("Do you want to check another number? (yes/no): ")

print("Exiting the program.")
    
