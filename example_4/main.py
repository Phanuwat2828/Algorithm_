

class exam4:
    def coin():
        pass
    def longgest():
        pass


if __name__ == "__main__":
    status = True;
    while(status):
        print("Select Exam [1]Coin [2]Longest OR [3-infinity]Exit")
        try :
            choose = int(input("Choose : "));
            if choose == 1:
                exam4.coin()
            elif choose == 2:
                exam4.longgest();
            else :
                status = False;
        except Exception :
            print("กรอกเลขเห้ย!")