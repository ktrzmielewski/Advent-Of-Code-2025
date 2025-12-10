import time
from BaseDay import BaseDay


class Day2(BaseDay):
    prints = True

    def get_result_part_one(self, prints=False):
        self.prints = prints
        with open('days/day2/input.txt') as file:
            for input in file:
                ranges = input.split(',')

        bounds = [range.split('-') for range in ranges]

        sum = 0
        start = time.time()
        for lower_bound, upper_bound in bounds:
            for i in range(int(lower_bound), int(upper_bound)+1):
                skip_i = False

                if i > 1000000000:
                    i_str = str(i)
                    if i_str[:5] == i_str[5:]:
                        sum += i
                        skip_i = True
                    if skip_i:
                        continue
                if i > 10000000:
                    i_str = str(i)
                    if i_str[:4] == i_str[4:]:
                        sum += i
                        skip_i = True
                    if skip_i:
                        continue
                if i > 100000:
                    i_str = str(i)
                    if i_str[:3] == i_str[3:]:
                        sum += i
                        skip_i = True
                    if skip_i:
                        continue
                if i > 1000:
                    i_str = str(i)
                    if i_str[:2] == i_str[2:]:
                        sum += i
                        skip_i = True
                    if skip_i:
                        continue
                if 10 < i < 100:
                    i_str = str(i)
                    if i_str[0] == i_str[1]:
                        sum += i
                        skip_i = True
                    if skip_i:
                        continue

        end = time.time()
        if prints:
            print("Elapsed:", end - start, "seconds")
            print(sum)

        return sum

    def get_result_part_two(self, prints=False):
        self.prints = prints

        with open('days/day2/input.txt') as file:
            for input in file:
                ranges = input.split(',')

        bounds = [range.split('-') for range in ranges]
        sum2 = 0
        start = time.time()

        for lower_bound, upper_bound in bounds:

            for i in range(int(lower_bound), int(upper_bound)+1):
                i_str = str(i)
                skip_i = False

                if (len(i_str)) == 10:
                    # check 1/2
                    if i_str[:5] == i_str[5:]:
                        self.print_sequence_and_number_if_needed(i_str[:5], i_str, lower_bound, upper_bound)
                        sum2 += i
                        skip_i = True
                    # check 1/5
                    if not skip_i and all(i_str[0:2] == i_str[i:i+2] for i in range(2, len(i_str), 2)):
                        self.print_sequence_and_number_if_needed(i_str[:2], i_str, lower_bound, upper_bound)
                        sum2 += i
                        skip_i = True
                    # check 1/10
                    if self.check_for_1_letter_sequence(skip_i, i_str):
                        self.print_sequence_and_number_if_needed(i_str[0], i_str, lower_bound, upper_bound)
                        sum2 += i
                        skip_i = True
                    if skip_i:
                        continue
                if (len(i_str)) == 9:
                    # check 1/3
                    if all(i_str[0:3] == i_str[i:i+3] for i in range(3, len(i_str), 3)):
                        self.print_sequence_and_number_if_needed(i_str[:3], i_str, lower_bound, upper_bound)
                        sum2 += i
                        skip_i = True
                    # check 1/9
                    if self.check_for_1_letter_sequence(skip_i, i_str):
                        self.print_sequence_and_number_if_needed(i_str[0], i_str, lower_bound, upper_bound)
                        sum2 += i
                        skip_i = True
                    if skip_i:
                        continue
                if (len(i_str)) == 8:
                    # 1/2
                    if i_str[:4] == i_str[4:]:
                        self.print_sequence_and_number_if_needed(i_str[:4], i_str, lower_bound, upper_bound)
                        sum2 += i
                        skip_i = True
                    # 1/4
                    if not skip_i and all(i_str[0:2] == i_str[i:i + 2] for i in range(2, len(i_str), 2)):
                        self.print_sequence_and_number_if_needed(i_str[:2], i_str, lower_bound, upper_bound)
                        sum2 += i
                        skip_i = True
                    # 1/8
                    if self.check_for_1_letter_sequence(skip_i, i_str):
                        self.print_sequence_and_number_if_needed(i_str[0], i_str, lower_bound, upper_bound)
                        sum2 += i
                        skip_i = True
                    if skip_i:
                        continue

                if (len(i_str)) == 7:
                    if self.check_for_1_letter_sequence(skip_i, i_str):
                        print(f"i_str: {i_str[0]}, i: {i}, for range: {lower_bound},{upper_bound}")
                        sum2 += i
                        skip_i = True
                    if skip_i:
                        continue

                if (len(i_str)) == 6:
                    # 1/2
                    if i_str[:3] == i_str[3:]:
                        self.print_sequence_and_number_if_needed(i_str[:3], i_str, lower_bound, upper_bound)
                        sum2 += i
                        skip_i = True
                    # 1/3
                    if not skip_i and all(i_str[0:2] == i_str[i:i+2] for i in range(2, len(i_str), 2)):
                        self.print_sequence_and_number_if_needed(i_str[:2], i_str, lower_bound, upper_bound)
                        sum2 += i
                        skip_i = True
                    # 1/6
                    if self.check_for_1_letter_sequence(skip_i, i_str):
                        self.print_sequence_and_number_if_needed(i_str[0], i_str, lower_bound, upper_bound)
                        sum2 += i
                        skip_i = True
                    if skip_i:
                        continue

                if (len(i_str)) == 5:
                    if self.check_for_1_letter_sequence(skip_i, i_str):
                        self.print_sequence_and_number_if_needed(i_str[0], i_str, lower_bound, upper_bound)
                        sum2 += i
                        skip_i = True
                    if skip_i:
                        continue

                if (len(i_str)) == 4:
                    # check 1/2
                    if i_str[:2] == i_str[2:]:
                        self.print_sequence_and_number_if_needed(i_str[:2], i_str, lower_bound, upper_bound)
                        sum2 += i
                        skip_i = True
                    if self.check_for_1_letter_sequence(skip_i, i_str):
                        self.print_sequence_and_number_if_needed(i_str[0], i_str, lower_bound, upper_bound)
                        sum2 += i
                        skip_i = True
                    if skip_i:
                        continue

                if (len(i_str)) == 3:
                    if all(char == i_str[0] for char in i_str):
                        self.print_sequence_and_number_if_needed(i_str[0], i_str, lower_bound, upper_bound)
                        sum2 += i
                        skip_i = True
                    if skip_i:
                        continue

                if (len(i_str)) == 2:
                    if self.check_for_1_letter_sequence(skip_i, i_str):
                        self.print_sequence_and_number_if_needed(i_str[0], i_str, lower_bound, upper_bound)
                        sum2 += i
                        skip_i = True
                    if skip_i:
                        continue

        end = time.time()
        if prints:
            print("Elapsed:", end - start, "seconds")
            print(sum2)
        return sum2

    def check_for_1_letter_sequence(self, skip_i, number):
        return not skip_i and all(char == number[0] for char in number)

    def print_sequence_and_number_if_needed(self, seq, number, lower_bound, upper_bound):
        if self.prints:
            print(f"i_str: {seq}, i: {number}, for range: {lower_bound},{upper_bound}")