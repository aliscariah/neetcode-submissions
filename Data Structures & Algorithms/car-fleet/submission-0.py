class Solution:
    def carFleet(self, target: int, pos: List[int], speed: List[int]) -> int:
        
        cars=sorted(zip(pos,speed),reverse=True)
        fleet=0
        fastest=0
        for pos,spd in cars:
            t=(target-pos)/spd
            if t>fastest:
                fleet+=1
                fastest=t
        return fleet                        