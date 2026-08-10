class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while len(stack) != 0 and t > stack[-1][1]:
                prev_i, _ = stack.pop()
                output[prev_i] = i - prev_i

            stack.append((i, t))

        return output
                
