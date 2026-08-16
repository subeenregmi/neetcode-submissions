class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = list(zip(position, speed))
        pos_speed = sorted(pos_speed, key=lambda p: -p[0])

        stack = []

        for ps in pos_speed:
            if len(stack) == 0:
                stack.append(ps)
                continue
            else:
                head = stack[-1]
                head_time_to_dest = (target - head[0]) / head[1]
                current_time_to_dest = (target - ps[0]) / ps[1]

                if current_time_to_dest > head_time_to_dest:
                    stack.append(ps)

        return len(stack)