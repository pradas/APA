def interwoven(first_string, second_string, text):
    first_next_letter = first_string[0]
    first_length = len(first_string)
    pointer_first = 0
    first_completed = False

    second_next_letter = second_string[0]
    second_length = len(second_string)
    pointer_second = 0
    second_completed = False

    starting_pos = 0
    for index, letter in zip(range(len(text)), text):
        if first_completed and second_completed:
            return starting_pos
        if not pointer_first and not pointer_second:
            starting_pos = index
        if not first_completed and letter == first_next_letter:
            pointer_first += 1
            if pointer_first >= first_length:
                first_completed = True
            else:
                first_next_letter = first_string[pointer_first]
            continue
        if not second_completed and letter == second_next_letter:
            pointer_second += 1
            if pointer_second >= second_length:
                second_completed = True
            else:
                second_next_letter = second_string[pointer_second]
            continue

        first_next_letter = first_string[0]
        pointer_first = 0
        first_completed = False
        second_next_letter = second_string[0]
        pointer_second = 0
        second_completed = False

if __name__ == "__main__":
    res = interwoven("abac","bbc", "cabbabccdw")
    if res:
        print(res)
    else:
        print("No results found")