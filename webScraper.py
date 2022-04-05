from bs4 import BeautifulSoup
import requests

line_break = '---------------------------'

def main():
    page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
    soup = BeautifulSoup(page.content, 'html.parser')
    print(page.content)
    print(soup.prettify()) #both of these return the page content
    print(line_break)
    print(soup.title) #you can add .prettify() for formatting
    print(line_break)
    elements_list = list(soup.children) #returns a list of all thhe elements inside the page
    print(elements_list)




if __name__ == '__main__':
    main()