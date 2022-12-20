from bs4 import BeautifulSoup  # pip install beautifulsoup4
import requests  # pip install requests
import re  # pip install regex
url = "http://195.220.111.166/copieHtml/re.html"  # url of the page to scrap
html_content = requests.get(url).text  # get the html content
# parse the html content with beautifulsoup and lxml parser (pip install lxml)
soup = BeautifulSoup(html_content, "lxml")
# find all the blocks of code in the page (pre tag) and store them in a list of called blocks
blocks = soup.findAll('pre')
with open("outputs.txt", "a") as myfile:  # open a file called outputs.txt in append mode and store it in a variable called myfile (a is for append mode which means that the file will be created if it doesn't exist and if it does exist, the new content will be added to the end of the file)
    # write the string "BLOCKS" in the file outputs.txt
    myfile.write("BLOCKS\n")
for block in blocks:  # for each block in the list of blocks
    # open the file outputs.txt in append mode and store it in a variable called myfile
    with open("outputs.txt", "a") as myfile:
        # write the text of the block in the file outputs.txt
        myfile.write('\n' + block.text + '\n')
        myfile.write('*' * 50)  # write 50 * in the file outputs.txt
        print(block.text)  # print the text of the block
# open the file outputs.txt in append mode and store it in a variable called myfile
with open("outputs.txt", "a") as myfile:
    # write the string "FUNCTIONS" in the file outputs.txt
    myfile.write("FUNCTIONS\n")
# find all the functions in the page (dt tag with class sig sig-object py) and store them in a list of called functions
functions = soup.findAll("dt", {"class": "sig sig-object py"})
for function in functions:  # for each function in the list of functions
    # open the file outputs.txt in append mode and store it in a variable called myfile
    with open("outputs.txt", "a") as myfile:
        # write the text of the function in the file outputs.txt
        myfile.write('\n' + function.text + '\n')
        myfile.write('*' * 50)  # write 50 * in the file outputs.txt
# find functions with a regex as argument and print them
# open the file outputs.txt in append mode and store it in a variable called myfile
with open("outputs.txt", "a") as myfile:
    # write the string "FUNCTIONS WITH REGEX AS ARGUMENT" in the file outputs.txt
    myfile.write("FUNCTIONS WITH REGEX AS ARGUMENT \n")
# regex to find functions with a regex as argument
regex = re.compile(r"re\.(?P<function>\w+)\(.*\)")
# find all the functions with a regex as argument and store them in a list of called functionsWithRegex
functionsWithRegex = soup.findAll(regex)
for function in functionsWithRegex:  # for each function in the list of functionsWithRegex
    # open the file outputs.txt in append mode and store it in a variable called myfile
    with open("outputs.txt", "a") as myfile:
        # write the text of the function in the file outputs.txt
        myfile.write('\n' + function.text + '\n')
        myfile.write('*' * 50)  # write 50 * in the file outputs.txt
