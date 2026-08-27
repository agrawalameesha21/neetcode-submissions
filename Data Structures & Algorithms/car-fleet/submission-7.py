class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort by position
        sorted_pairs = sorted(zip(position, speed), reverse=True)
        position, speed = map(list, zip(*sorted_pairs))
        
        # each iteration till target exceeded
        time = []
        for index, n in enumerate(position):
            time.append(((target - n)/speed[index]))

        fleets = []
        for index, n in enumerate(time):
            if len(fleets) == 0: 
                fleets.append(n)
            elif n > fleets[len(fleets) - 1]: 
                fleets.append(n)

        return len(fleets)
