from functools import reduce

def main():
    lines = []

    with open('.\input.txt' ,'r') as f:
        lines = f.readlines()

    continue_search = True
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            word1 = lines[i].strip()
            word2 = lines[j].strip()
            continue_search = compare(word1, word2)

            if not continue_search:
                break
        if not continue_search:
            break

def compare(word1, word2):
    if len(word1) != len(word2):
        return True

    common_letters = ''
    diff = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            common_letters = common_letters + word1[i]
        else:
            diff = diff + 1

        if diff > 1:
            return True

    if diff == 1:
        print(common_letters)
        return False
    else:
        return True



if __name__ == '__main__':
    main()