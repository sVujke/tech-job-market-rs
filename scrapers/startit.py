from bs4 import BeautifulSoup
import requests, time
import scrape_lib

# f = open("C:/Users/vujke/Documents/GitHub/tech-job-market-rs/data/data.txt" ,"a")
# errorFile = open("C:/Users/vujke/Documents/GitHub/tech-job-market-rs/data/error.txt" ,"w")

# scraper methods

# methods for premium ads

# methods for standard ads
def get_position(ad):
    return ad[1].get_text()

# methods for mini ads
start = time.time()

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