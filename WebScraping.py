import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com/"

content = requests.get(url)
r = requests.get(url)		# r variable has all the HTML code
htmlContent = r.content		# r returns response so if we want the code we write r.content
#print(htmlContent)		    # printing the code

soup = BeautifulSoup(r.content, 'html.parser')
#print(soup.prettify())	# to print html in tree structure

#title = soup.title

#print(type(title)) #1. Tag
#print(type(title.string)) #2. NavigableString
#print(type(soup)) #3. BeautifulSoup
#4. Comment 

#get all the paragraphs from the page
#paras = soup.find_all('p')
#print(paras)

#anchors = soup.find_all('a')
#print(anchors)

# find first paragraph of page
#print(soup.find('p')) 

#find class of first paragraph
#print(soup.find('p')['class']) 

#get all tags with defined class
#print(soup.find_all("p", class_="lead"))

#get text from tags/soup
#print(soup.find('p').get_text())

#get all the links on the page
#print(soup.find_all('a')['href'])

#get all the links on the page
"""
anchors = soup.find_all('a')
all_links = set()
for link in anchors:
	if(link.get('href')!='#'):
		linkText = "https://codewithharry.com" + link.get('href')
		all_links.add(link)
		print(linkText) 
"""
navbarSupportedContent = soup.find(id='navbarSupportedContent')
print(navbarSupportedContent.contents)


###########################Description#######################################
1. Install Python, pip and VS Code
2. Set environment variables
3. open terminal in VS Code
4. in VS code terminal
	pip install requests
	pip install bs4
	pip install html5lib
{ // brackets are only to show code snippet
import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com/"
}
Step 1: Get the HTML
{
content = requests.get(url)
r = requests.get(url)		# r variable has all the HTML code
htmlContent = r.content		# r returns response so if we want the code we write r.content
#print(htmlContent)		# printing the code
}
Step 2: Parse the HTML
{
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())	# to print html in tree structure
}
#Get the title of the page
title = soup.title

Step 3: HTML Tree traversal
Commonly used type of objects:
{
#print(type(title)) #1. Tag
#print(type(title.string)) #2. NavigableString
#print(type(soup)) #3. BeautifulSoup
#4. Comment 
}


{
#get all the paragraphs tags from the page
paras = soup.find_all('p')
print(paras)

#get all the anchor tags from the page
anchors = soup.find_all('a')
print(anchors)


#find class of first paragraph
print(soup.find('p')['class']) 

#get all tags with defined class
print(soup.find_all("p", class_="lead"))

#get text from tags/soup
print(soup.find('p').get_text())

#get all the links on the page
anchors = soup.find_all('a')
all_links = set()
for link in anchors:
	if(link.get('href')!='#')
		linkText = "https://codewithharry.com" + link.get('href')
		all_links.add(link)
		print(linkText)

navbarSupportedContent = soup.find(id='navbarSupportedContent')
print(navbarSupportedContent)

#.contents - A tag's children are available as a list
#.children - A tag's children are available as a generator
#.strings  - Shows strings
#.parent   - to print parent tag
#.parents  - generator object to print parent tags
#.next_sibling  - To print next Sibling
#.parents  - 
for elem in navbarSupportedContent.contents:
	print(elem)

for item in navbarSupportedContent.stripped_strings:
	print(item)

for item in navbarSupportedContent.stripped_strings:
	print(item)

print(navbarSupportedContent.parent)  # to print parent tag

print(navbarSupportedContent.parents)  # to print parent tags

To print generator objects parent
for item in navbarSupportedContent.parents:
	print(item.name)

print(navbarSupportedContent.next_sibling.next_sibling)  # to print next sibling
print(navbarSupportedContent.previous_sibling.previous_sibling)  # to print previous sibling

#CSS selector
elem = soup.select('#loginModel')	#to print id loginModel
print(elem)

elem = soup.select('.modal-footer')	#to print list of modal footers
print(elem)
}
