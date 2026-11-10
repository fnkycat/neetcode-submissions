class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        count = 0
        final_time = 0

        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(reverse=True)

        for position, speed in cars:
            time = (target - position) / speed

            if time > final_time:
                count+=1
                final_time = time

        return count

