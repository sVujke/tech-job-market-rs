from bs4 import BeautifulSoup
import requests, time

start = time.time()

f = open("data.txt" ,"a")
errorFile = open("error.txt" ,"w")

f.write(time.strftime("%d/%m/%Y,"))

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

	t = soup.h1.get_text()

	first_letter = skill[0]

	title = str(t).rstrip()

	index = title.index(first_letter)

	title = title[index:]
	        # find the length of the word before the number
	text_length = len(skill)

	demand = title

	demand = title[text_length:]

	skills_dict[skill] = demand

	#print len(skills_dict[skill])
	
	f.write(skills_dict[skill] +",")

    #except Exception as e:
      #      errorFile.write("Error on line: "+str(x)+"********"+str(e)+"**********"+"\n")
     #       pass

f.write("\n")

time = time.time()-start

if(time > 60):
	print 'It took', time/60, 'minutes.'
else: 
	print 'It took', time, 'seconds.'
