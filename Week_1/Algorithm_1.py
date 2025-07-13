

class Algorithm :
    def Majority(data):
        n = len(data);
        n2 = n/2;
        for i in range(n):
            c = 0;
            for j in range(n):
                if(data[i] == data[j]):
                    c=c+1;

                if(c>=n2):
                    return True;
        if(i==n-1):
            return False;

            