# Write a function called statistic which takes in a file name and returns a dictionary with the number
# of lines. words and characters in the file
import re


def statistics(file):
    with open(file, "r") as f:
        lines = f.readlines()

        f.seek(0)
        count_char = 0
        for x in lines:
            for y in x:
                count_char += 1

        f.seek(0)
        z = f.read()
        count_words = len(re.findall(r'\w+', z))

        return dict(lines=len(lines), words=count_words, characters=count_char)


print(statistics("story.txt"))
