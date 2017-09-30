# This script prompts the user for a file to decipher, generates a table of letter frequencies and then
# attempts to solve it by replacing most common encrypted characters with the most frequently used 
# characters in english text.


import operator


# main function
def crack_text():
    global filename  # probably not secure, look into it

    while True:
        try:
            filename = input("Enter filename: ").strip()
            counts = read_count(filename)
            break
        except IOError:
            print("File " + filename + " does not exist.")

    freq_dict = compute_freq(counts)
    sorted_counts = sort_to_list(freq_dict)
    print_freq(sorted_counts)
    cracker = generate_cracker(sorted_counts)
    decrypt_file(cracker, filename)

    return cracker


# reads file, returns a list of character counts
def read_count(filename):
    infile = open(filename, "r")

    counts = 26 * [0]  # create and initialize counts
    for line in infile:
        # invoke the count_letters function
        count_letters(line.lower(), counts)

    infile.close()

    return counts


# create frequency dictionary
def compute_freq(counts):
    freq_dict = {}
    for i in range(len(counts)):
        if counts[i] != 0:
            freq_dict[chr(ord('a') + i)] = counts[i]

    return freq_dict


# sort and return as list
def sort_to_list(dictionary):
    _sorted = sorted(dictionary.items(), key=operator.itemgetter(1))

    return _sorted


def print_freq(sorted_list):
    for i in range(len(sorted_list) - 1, -1, -1):
        print(sorted_list[i][0], "\t", sorted_list[i][1])


def generate_cracker(sorted_list):
    # compare frequency of encrypted letters to natural letter frequency
    text_frequency = []
    for i in range(len(sorted_list) - 1, -1, -1):
        text_frequency.append(sorted_list[i][0])
    letter_frequency = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u',
                        'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z']

    # use pairwise dict constructor zip to make a code cracker
    cracker = dict(zip(text_frequency, letter_frequency))

    return cracker


def decrypt_file(cracker, filename):
    file1 = open(filename, 'r')
    file2 = open("cracked.txt", 'w')
    for line in file1:
        process_code(line, cracker, file2)
    file1.close()
    file2.close()


def count_letters(line, counts):
    for ch in line:
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1


def process_code(line, cracker, file):

    for ch in line:
        if ch in cracker.keys():
            file.write(cracker[ch])
        else:
            file.write(ch)

crack_text()
