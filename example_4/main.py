class coin:
    def Fn(coins, target):
        d = [0] * (target + 1)
        d[0] = 1
        for coin in coins:
            for count in range(coin, target + 1):
                d[count] += d[count - coin]
        return d[target]

class longest:
    def Fn(x,y):
        m,n = len(x),len(y)
        d = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if x[i-1] == y[j - 1]: d[i][j] = d[i-1][j-1] + 1
                else: d[i][j] = max(d[i-1][j],d[i][j-1])
        return d[m][n]

if __name__ == "__main__":
    status = True;
    while(status):
        print("Select Exam [1]Coin [2]Longest OR [3-infinity]Exit")
        try :
            choose = int(input("Choose : "));
            if choose == 1:
                a = [1,2,5,10]
                target = 10
                print(coin.Fn(a,target))
            elif choose == 2:
                x  = "ABCDE"
                y = "BDCADE"
                print(longest.fn(x,y))
            else :
                status = False;
        except Exception :
            print("กรอกเลขเห้ย!")