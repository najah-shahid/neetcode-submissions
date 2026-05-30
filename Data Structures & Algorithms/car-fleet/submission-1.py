class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = list(zip(position, speed))
        pos_speed.sort()
        times = []
        stack = []
        for pos, spd in pos_speed:
            times.append((target - pos)/spd)
        for i in range(len(times) - 1, -1, -1):
            if stack and stack[-1] >= times[i]:
                continue
            stack.append(times[i])
        return len(stack)