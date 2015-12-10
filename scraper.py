from bs4 import BeautifulSoup
import requests, time

f = open("C:/Users/vujke/Documents/GitHub/tech-job-market-rs/data/data.txt" ,"a")
errorFile = open("C:/Users/vujke/Documents/GitHub/tech-job-market-rs/data/error.txt" ,"w")

#list of skills
skills = ['java','.net', 'c','frontend','android','ios','qa','linux','js','php','python','ruby','game-dev']

skills_dict = {
'java':'',
'.net':'',
 'c':'',
 'frontend':'',
 'android':'',
 'ios':'',
 'qa':'',
 'linux':'',
 'js':'',
 'php':'',
 'python':'',
 'ruby':'',
 'game-dev':''}

#base URL
url="http://startit.rs/poslovi/"

for skill in skills:

	response = requests.get(url+skill)
	print url+skill
	#check status code
	if response.status_code != requests.codes.ok:
		print 'status code not ok'
		break

	#try:
		#read response content
	result = response.content

			#make BeautifulSoup object
	soup = BeautifulSoup(result, 'html.parser')

			#find the demand

	title = soup.h1.get_text()

	        # find the length of the word before the number
	text_length = len(title)

	demand = title
	        #demand = title[text_length:]
	skills_dict[skill] = demand

	f.write(skills_dict[skill]+"\t")

    #except Exception as e:
      #      errorFile.write("Error on line: "+str(x)+"********"+str(e)+"**********"+"\n")
     #       pass

f.write("\n")
