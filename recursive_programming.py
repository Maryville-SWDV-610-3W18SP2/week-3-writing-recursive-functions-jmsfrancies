def changeBack(n):
    quarters = 25
    dimes = 10
    nickels = 5
    pennies = 1
    if n % quarters <= quarters:
       quarters = n//quarters
       print("{0} Quarters ".format(quarters))
       n = n - 25 * quarters
       if n % dimes <= dimes:
           dimes = n // dimes
           print("{0} Dimes".format(dimes))
           n = n - 10 * dimes
           if n % nickels <= nickels:
               nickels  = n // nickels
               print("{0} Nickels".format(nickels))
               n = n - 5 * nickels
               if n % pennies <= 1:
                 pennies = n // pennies
                 print("{0} Pennies".format(pennies))
                    
    
def main():
    n = int(input("Enter change that is less than 100 cents: "))
    if n <= 99 and n > 0:
       changeBack(n)
    else:
       print("Error: Enter a value between 1 and 99 ")

main()
            