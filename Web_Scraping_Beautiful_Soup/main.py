from bs4 import BeautifulSoup

with open("homepage.html") as html_file:
    content = html_file.read()
    # print(content)
    soup = BeautifulSoup(content, 'lxml')
    all_card_headings = soup.find_all('h5')
    for heading in all_card_headings:
        # print(heading)
        print(heading.text)
    # print(all_card_headings)
    # print(soup.find('a'))

    course_card = soup.find_all('div', class_="card")
    for card in course_card:
        course_name = card.h5.text
        course_body = card.p
        course_price = card.a.text.split()[-1]
        print(course_name)
        # print(course_body)
        # print(course_price)

        data = f'{course_name} is the course name and price is {course_price}'
        print(data)
    # print(course_card)

