import re
import datetime

def main():
    records = []
    with open('input.txt', 'r') as file:

        for line in file.readlines():
            record = parse_line(line)
            records.append(record)

    dwarf_shift_count = {}
    dwarf_sleep_matrix = {}

    last_dwarf_id = 0
    last_fall_asleep_minute = 0
    # One all records have been parsed, they need to be ordered by the date
    for r in sorted(records, key=lambda x: x[0]):
        timestamp = r[0]
        begins_shift = r[3]
        falls_asleep = r[1]
        wakes_up = r[2]
        elf_id = r[4]

        if begins_shift:
            last_dwarf_id = elf_id

            # Increment shift count
            if last_dwarf_id in dwarf_shift_count:
                dwarf_shift_count[last_dwarf_id] += 1
            else:
                dwarf_shift_count[last_dwarf_id] = 1
                dwarf_sleep_matrix[last_dwarf_id] = [0 for i in range(60)] #Each item in the array will contain the count indicating how many time the elf have slept on this minute


        elif falls_asleep:
            if timestamp.hour == 0:
                last_fall_asleep_minute = timestamp.minute

        elif wakes_up:
            # now lets increment all of those minutes asleep
            for m in range(last_fall_asleep_minute, timestamp.minute):
                dwarf_sleep_matrix[last_dwarf_id][m] += 1


    sleep_record = -1
    biggest_snoozer = -1
    most_frequent_minute = -1
    # Find quard who slept most
    for dwarf in dwarf_sleep_matrix:
        total_slept = sum(dwarf_sleep_matrix[dwarf])
        if total_slept > sleep_record:
            sleep_record = total_slept
            biggest_snoozer = dwarf

            # Find the minute on which the elf sleeps most frequently
            records = dwarf_sleep_matrix[dwarf]
            most_frequent_minute = records.index(max(records))
        print(dwarf, sum(dwarf_sleep_matrix[dwarf]))

    print(biggest_snoozer, sleep_record, most_frequent_minute)
    print('Result: ', int(biggest_snoozer[1:]) * most_frequent_minute)



def parse_line(line):
    regex = re.compile(r'\[(\d{4}\-\d{2}\-\d{2})\s(\d{2}\:\d{2})\]\s(\b[\w]*\s(\#\d*)?.*)')
    result = regex.findall(line.strip())[0]

    # year, month, day = result[0].split('-')
    # hour, minute = result[1].split(':')

    timestamp = datetime.datetime(*map(lambda x: int(x), result[0].split('-')), *map(lambda x: int(x), result[1].split(':')))
    falls_asleep = 'falls asleep' == result[2]
    wakes_up = 'wakes up' == result[2]
    begins_shift = 'begins' in result[2]
    guard_id = result[3]

    # print(timestamp)
    # print(result)

    return (timestamp, falls_asleep, wakes_up, begins_shift, guard_id)

if __name__ == '__main__':
    main()