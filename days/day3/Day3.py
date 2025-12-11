from BaseDay import BaseDay


class Day3(BaseDay):
    def get_result_part_one(self, prints=False):
        banks = []
        with open('days/day3/input.txt') as file:
            for line in file:
                banks.append([int(num) for num in line.strip()])


        sum_max_joltage = 0
        size = len(banks[0])
        bank_num = 0
        for bank in banks:

            right_ptr, left_ptr = bank[size-1], bank[size-2]
            max_joltage = -1
            for index, digit in reversed(list(enumerate(bank))):

                if prints:
                    print(f"Right ptr at: {right_ptr}, left ptr at: {left_ptr}, current max: {max_joltage}")

                potential_max = left_ptr * 10 + right_ptr
                if right_ptr < left_ptr:
                    right_ptr = left_ptr

                if index is not 0:
                    left_ptr = bank[index-1]
                    if index == size - 1:
                        left_ptr = bank[index - 2]

                if potential_max > max_joltage:
                    max_joltage = potential_max

            if prints:
                print(f"Max: {max_joltage} for bank: {bank_num}")

            bank_num += 1
            sum_max_joltage += max_joltage

        print(sum_max_joltage)
