# Define a function named count that takes a single parameter. The parameter is a string. 
# The string will contain a single word divided into syllables by hyphens, such as these:
# "met-a-phor"
# "ter-min-a-tor"
# Your function should count the number of syllables and return it.

def count(string):
    syllabes = string.count("-") + 1
    print(syllabes)
    return syllabes

count("Al-go-rit-mo")