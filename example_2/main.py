from itertools import combinations as com_lib
from itertools import permutations
class exm1:
    def tsp():
        dist = [
            [0, 10, 15, 20],
            [10, 0, 35, 25],
            [15, 35, 0, 30],
            [20, 25, 30, 0]
        ]

        n = len(dist)             
        cities = list(range(n))     
        min_path = float('inf')      
        best_route = []              

        for perm in permutations(cities[1:]):
            current_path = 0
            k = 0                    
            route = [0]            

            for j in perm:
                current_path += dist[k][j]
                k = j
                route.append(j)

            current_path += dist[k][0]  
            route.append(0)

            print(f"Path {route} = {current_path}")

            if current_path < min_path:
                min_path = current_path
                best_route = route[:]
        print("="*10," Result ","="*10)
        print("\nเส้นทางที่สั้นที่สุด:", best_route)
        print("ระยะทางรวม:", min_path)
        print("="*30,)

class exm2:
    def viewer(e):
        print("="*10," Result ","="*10)
        for _ in e:
            print(_);
        print("="*30,)
    def ssp():
        print("Exam input ==> Enter Array : 1 2 3 4 5")
        try:
            data = input("Enter Array : ");
            array = list(map(int,data.split()));
            t = int(input("Enter T: "));
            result = [];
            lenght = len(array)
            for _ in range(lenght):
                for _in_ in com_lib(array,_):
                    if sum(_in_) == t :
                        result.append(list(_in_));
            exm2.viewer(result);
        except Exception:
            print("look Exam input")

if __name__ == "__main__":
    status = True;
    while(status):
        print("Select Exam [1]TSP [2]SSP OR [3-infinity]Exit")
        try :
            choose = int(input("Choose : "));
            if choose == 1:
                exm1.tsp()
            elif choose == 2:
                exm2.ssp()
            else :
                status = False;
        except Exception :
            print("กรอกเลขเห้ย!")
