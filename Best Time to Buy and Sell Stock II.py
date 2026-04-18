import array

def stockmarket(prices):
    sum=0
    for i in range(1,len(prices)):
        val1=prices[i-1]
        val2=prices[i]
        if val1<val2:
            profit=val2-val1 
            sum+=profit
    return sum
if __name__=="__main__":
    prices=array.array('i',map(int,input("Enter Prices:").split()))
    print(stockmarket(prices))
