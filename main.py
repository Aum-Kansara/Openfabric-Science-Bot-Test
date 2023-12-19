from bs4 import BeautifulSoup
# from dotenv import load_dotenv
# from os import getenv
import requests
# load_dotenv()

# API_KEY=getenv("API_KEY")
# SEARCH_ENGINE_ID=getenv("SEARCH_ENGINE_ID")


# search_query="What is gravity?" 

# url="https://www.googleapis.com/customsearch/v1"

# params={
#     'q':search_query,
#     'key':API_KEY,
#     'cx':SEARCH_ENGINE_ID,
# }

# response=requests.get(url,params=params)
# results=response.json()['items']

# for item in results:
#     print(item['link'])


link="https://spaceplace.nasa.gov/what-is-gravity/en/"
res=requests.get(link)
soup=BeautifulSoup(res.text,features='html.parser')

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())

# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)    

print(text)

