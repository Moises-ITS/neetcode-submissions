class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)] #[position, speed]
        pair.sort(reverse=True) #descending order
        fleets = 1
        prevTime = (target - pair[0][0]) / pair[0][1]
        #subtract target by highest starting position car and divide(/) by its speed = (floating point number)
        for i in range(1, len(pair)):
            currCar = pair[i] #[pos, speed]
            currTime = (target - currCar[0]) / currCar[1]
            if currTime > prevTime:
                fleets += 1
                prevTime = currTime
        return fleets
        
        
