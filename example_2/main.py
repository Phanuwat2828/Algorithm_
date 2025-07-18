



class exm1:
    pass
class exm2:
    
    def ssp():
        data = input("Enter Array : ");
        array = list(map(int,data.split()));
        t = int(input("Enter T: "));
        lenght = len(array)
        for _ in range(lenght):
            for _in_ in range(lenght):
                if((array[_]+array[_in_]) == t):
                    print(array[_],",",array[_in_]," : ",t)
exm2.ssp();

