class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # return the number of groups of cars the will arive to target
        # groups are made when a car catches up the a car infront
        # the behind car must reach the destination before or at the same time as the slowest group infront
        # start with the cars at farthest position
        # calculate every cars arival time and if it is faster than the car infront set it to be the same
        # else add one to the count of groups 
        if len(position) == 0:
            return 0
        cars = list(zip(position, speed))
        cars.sort(reverse = True)
        time = []
        count = 0
        for i in range(len(cars)):
            time.append((target - cars[i][0]) / cars[i][1])
            if (i != 0 and time[i] <= time[i - 1]):
                time[i] = time[i - 1]
            else:
                count += 1
        return count
