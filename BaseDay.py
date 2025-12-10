import os

class BaseDay():
    def solve_and_get_results(self):
        return isinstance(self.get_result_part_one(), int) and isinstance(self.get_result_part_two(), int)
