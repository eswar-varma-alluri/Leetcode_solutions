class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        total_time = 0
        current_floor = 0
        
        for req in requests:
            total_time += abs(req - current_floor)
            current_floor = req
            
        return total_time