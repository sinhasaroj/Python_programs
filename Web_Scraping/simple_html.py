from bs4 import BeautifulSoup

ITEM_HTML = """"
        <html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>HTML PARSER</title>
            </head>
            <body>
                <h1>This is a new file.</h1>
                <p class="subtitle">Numbers are created by numeric literals.</p>
                <p>Another paragraph without a class.</p>
                <ul>
                    <li>Chicken</li>
                    <li>Mutton</li>
                    <li>Fish</li>
                    <li>Eggs</li>
                    <li>Rice</li>
                </ul>
            
            </body>
        </html>
"""

simple_soup = BeautifulSoup(ITEM_HTML, 'html.parser')


def find_title():
    h1_tag = simple_soup.find('h1')
    print(h1_tag.string)


def find_list_items():
    list_items = simple_soup.find_all('li')
    list_content = [e.string for e in list_items]
    print(list_content)


def find_subtitle():
    paragraph = simple_soup.find('p', {"class": "subtitle"})
    print(paragraph.string)


def find_other_paragraphs():
    paragraphs = simple_soup.find_all('p')
    other_paragraph = [p.string for p in paragraphs if 'subtitle' not in p.attrs.get('class', [])]
    print(other_paragraph[0])


find_title()
find_list_items()
find_subtitle()
find_other_paragraphs()
