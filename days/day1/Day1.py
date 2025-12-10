from BaseDay import BaseDay

class Day1(BaseDay):
    dial = 50
    counter_exact = 0
    counter_any_click = 0
    num_of_clicks = 0

    def get_result_part_one(self, prints=False):
        with open('days/day1/input.txt') as input_from_file:
            for input in input_from_file:
                if input[0] == 'L':
                    self.dial -= int(input[1:])

                elif input[0] == 'R':
                    self.dial += int(input[1:])

                self.dial %= 100
                if self.dial == 0:
                    self.counter_exact += 1

                if prints is True:
                    print(f"Dial after: {self.dial}, counter after: {self.counter_exact}")
        return self.counter_exact

    def get_result_part_two(self, prints=False):
        with open('days/day1/input.txt') as input_from_file:
            for input in input_from_file:
                move = int(input[1:])
                old_dial = self.dial

                if input[0] == 'L':
                    self.dial -= move
                    num_of_clicks = ((old_dial - 1) // 100) - ((self.dial - 1) // 100)

                elif input[0] == 'R':
                    self.dial += move
                    num_of_clicks = (self.dial // 100) - (old_dial // 100)

                self.dial %= 100
                self.counter_any_click += num_of_clicks

                if self.dial == 0:
                    self.counter_exact += 1

                if prints is True:
                    print(f"Dial after: {self.dial}, old counter after: {self.counter_exact}, new counter after: {self.counter_any_click}")
        return self.counter_any_click
