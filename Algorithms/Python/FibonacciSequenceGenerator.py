import decimal
#define function for generator
def fibonacciGenerator(orderNumber):
    if orderNumber < 2:
        return orderNumber
    else:
        return fibonacciGenerator(orderNumber-1) + fibonacciGenerator(orderNumber-2)#algorithm
#get number from end user and convert to decimal
getNumber = decimal.Decimal(input('ENTER AN INTEGER OR DECIMAL NUMBER  \n '))
#print response and repeat for the rest of the numbers in the sequence
while getNumber >=0:
    answer = fibonacciGenerator(getNumber)
    print(answer)
    getNumber += 1
