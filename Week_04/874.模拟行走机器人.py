class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dx, dy, x, y = 0, 1, 0, 0
        distance = 0
        obs_dict = {}
        for obs in obstacles:
            obs_dict[tuple(obs)] = 0
        for com in commands:
            if com == -2:
                dx, dy = -dy, dx
            elif com == -1:
                dx, dy = dy, -dx
            else:
                for j in range(com):
                    next_x = x + dx
                    next_y = y + dy
                    if (next_x, next_y) in obs_dict:
                        break
                    x, y = next_x, next_y
                    distance = max(distance, x*x + y*y)
        return distance