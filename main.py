print("=== Power Calculator ===")
n = int(input("Enter the number whose factorial you want to find: "))
multiplication=1

#Iterates for n+1 times: i=1 to n*1
for i in range(1, n+1):
    multiplication = multiplication * i
    print("\nMultiplication =", multiplication)