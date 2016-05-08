from bs4 import BeautifulSoup
import requests, time
import scrape_lib

start = time.time()

# f = open("C:/Users/vujke/Documents/GitHub/tech-job-market-rs/data/data.txt" ,"a")
# errorFile = open("C:/Users/vujke/Documents/GitHub/tech-job-market-rs/data/error.txt" ,"w")

# scraper methods

# methods for PREMIUM and STANDARD ads
# PARAMETER po is a single ad div
def get_city(po):
    firm_city = po.find_all('div',class_="listing-ime-firme")
    city = firm_city[1].get_text()
    city = city.split(' ')[3:]
    cities = ""
    for c in city:
        cities = cities+str(c)
    return cities
# PARAMETER ad is a list of all <a> tags
def get_position(ad):
    return ad[1].get_text()

def get_firm(ad):
    return ad[2].get_text()

def get_tags(ad):
    tags = ad[3:]
    tag_str = ""
    for tag in tags:
        tag_str = tag_str + str(tag.get_text())+" "
    tag_str = tag_str.lower()
    return tag_str
# methods for MINI ads
def get_city_s(ad):
    return ad[1].get_text()

def get_position_s(ad):
    return ad[0].get_text()

def get_tags_s(ad):
    tags = ad[2:]
    tag_str = ""
    for tag in tags:
        tag_str = tag_str + str(tag.get_text())+" "
    tag_str = tag_str.lower()
    return tag_str

def get_firm_s(po):
    return po.find('div',class_="oglas-mini-header").get_text()


#base URL
url="http://startit.rs/poslovi/"


response = requests.get(url)

result = response.content

soup = BeautifulSoup(result, 'html.parser')

l = soup.h1.get_text()
print len(l)

k = soup.find_all("div", class_="listing-oglas-premium")
print k[0].h1.get_text()
	# response = requests.get(url+skill)
	# print url+skill
	# #check status code
	# if response.status_code != requests.codes.ok:
	# 	print 'status code not ok'
	# 	break
    #
	# #try:
	# 	#read response content
	# result = response.content
    #
	# 		#make BeautifulSoup object
	# soup = BeautifulSoup(result, 'html.parser')
    #
	# 		#find the demand
    #
	# title = soup.h1.get_text()
    #
	#         # find the length of the word before the number
	# text_length = len(title)
    #
	# demand = title
	#         #demand = title[text_length:]
	# skills_dict[skill] = demand
    #
	# f.write(skills_dict[skill]+"\t")

    #except Exception as e:
      #      errorFile.write("Error on line: "+str(x)+"********"+str(e)+"**********"+"\n")
     #       pass

#f.write("\n")

time = time.time()-start
scrape_lib.print_time(time)