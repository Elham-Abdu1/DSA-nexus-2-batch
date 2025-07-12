def split_and_join(line):
    list_words = line.split(" ")
    conc_string = "-".join(list_words)
    return conc_string

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
