from bs4 import BeautifulSoup
import requests
import re
url = "http://195.220.111.166/copieHtml/re.html"
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")
blocks = soup.findAll('pre')
with open("outputs.txt", "a") as myfile:
    myfile.write("BLOCKS\n")
for block in blocks:
  with open("outputs.txt", "a") as myfile:
    myfile.write('\n' + block.text + '\n')
    myfile.write('*' * 50)
    print(block.text)
with open("outputs.txt", "a") as myfile:
    myfile.write("FUNCTIONS\n")
functions = soup.findAll("dt", {"class": "sig sig-object py"})
for function in functions:
  with open("outputs.txt", "a") as myfile:
    myfile.write('\n' + function.text + '\n')
    myfile.write('*' * 50)
# find functions with a regex as argument and print them
with open("outputs.txt", "a") as myfile:
    myfile.write("FUNCTIONS WITH REGEX AS ARGUMENT \n")
regex = re.compile(r"re\.(?P<function>\w+)\(.*\)")  
functionsWithRegex = soup.findAll(regex)
for function in functionsWithRegex:
  with open("outputs.txt", "a") as myfile:
    myfile.write('\n' + function.text + '\n')
    myfile.write('*' * 50)
