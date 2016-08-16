"""
Write three functions:
sort1(langauges)
sort2(languages)
sort3(langauges)
Goal: Print exactly the below w/ three functions:
1:
    Arabic
    English
    Koine Greek
    Latin
    Romanian
    C++
    JavaScript
    Python
    R
2:
    R
    C++
    Latin
    Arabic
    Python
    English
    Romanian
    JavaScript
    Koine Greek
3:
    JavaScript
    R
    Latin
    Python
    Romanian
    Koine Greek
    English
    Arabic
    C++
"""
languages = {'JavaScript': 'P',
             'Arabic': 'N',
             'R': 'P',
             'Python': 'P',
             'C++': 'P',
             'Koine Greek': 'N',
             'Latin': 'N',
             'Romanian': 'N',
             'English': 'N'}

from operator import itemgetter, attrgetter

# def sort1(d):
#     lst = sorted(sorted(d), key=d.__getitem___)
#     print("1:")
#     for x in lst:
#         print("\t"+x)
# sort1(languages)

def sort1b(d):
    import operator
    lst = sorted(sorted(d.items()), key=operator.itemgetter(1))
    print("sort 1: ")
    for language, type_ in lst:
        print("\t"+language)

sort1b(languages)

def sort2(d):
    lst = sorted(d, key=len)
    print("Sort 2:")
    for item in lst:
        print("\t" + item)
sort2(languages)

def sort3(d):
    lst = sorted(sorted(d), key=last_char, reverse=True)
    print("Sort 3:")
    for item in lst:
        print("\t" + item)

def last_char(string):
    return string[-1].lower()

sort3(languages)

