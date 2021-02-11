import string

# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)

txt = "Python is a great language for doing data analysis, primarily because of the fantastic ecosystem of data-centric Python packages. Pandas is one of those packages, and makes importing and analyzing data much easier. In this article, I have used Pandas to analyze data on Country Data.csv file from UN public Data Sets of a popular ‘statweb.stanford.edu’ website.As I have analyzed the Indian Country Data, I have introduced Pandas key concepts as below. Before going through this article, have a rough idea of basics from matplotlib and csv"

categories = {}

for c in txt:
    if c != ' ':
        if c in string.ascii_lowercase:
            key = 'lower'
        elif c in string.ascii_uppercase:
            key = 'upper'
        else:
            key = 'other'

        if key not in categories:
            categories[key] = set()

        categories[key].add(c)

print(categories)



