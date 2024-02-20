#   https://www.hackerrank.com/test/3em71ltlfrk/questions/6sqmn1811gk



def truckTour(petrolpumps):
    positions=0
    fuel=0
    queue=[]
    for i in range(len(petrolpumps)):
        fuel+= petrolpumps[i][0] - petrolpumps[i][1]
        if fuel < 0 :
            fuel = 0 
            positions = i+1
    return positions


if __name__ == "__main__":
    n = int(input().strip())
    petrolpumps = []
    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))
    result = truckTour(petrolpumps)
    print (result)
