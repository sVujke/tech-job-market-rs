from bs4 import BeautifulSoup
import requests, time
from os import path
from datetime import date
import scrape_lib
import mongo_lib
import pprint

start = time.time()

# methods for PREMIUM and STANDARD ads
# PARAMETER po is a single ad div
def get_city(po):
    firm_city = po.find_all('div',class_="listing-ime-firme")
    city = firm_city[1].get_text()
    #print city
    city = city.split(' ')[3:]
    #print city
    cities = ""
    #print ' '.join(city)
    #for c in city:
    #    print "EVO: ", c
    #    cities = cities+str(c).encode('utf8')
    return ' '.join(city)
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

def get_tags_list(ad):
    tag_list = []
    tags = ad[3:]
    for tag in tags:
        t = tag.get_text().lower()
        tag_list.append(t)
    return tag_list

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


def get_tags_list_s(ad):
    tag_list = []
    tags = ad[2:]
    for tag in tags:
        t = tag.get_text().lower()
        tag_list.append(t)
    return tag_list

# general methods
def current_date_str():
    d = date.today()
    d = d.strftime("%d/%m/%y")
    return d

def make_ad_list(ads, type):

    ads_list = []
    i = 0
    for ad in ads:
            ad_dict = {}
            add = ad.find_all('a')
            ad_dict['date'] = current_date_str()
            ad_dict['ad_type'] = type
            #print get_position(add)
            ad_dict['position'] = get_position(add)
            ad_dict['firm'] = get_firm(add)
            #print get_city(ad)
            ad_dict['city'] = get_city(ad).encode('utf-8')
            ad_dict['tags'] = get_tags_list(add)
            #print unicode(ad_dict, 'utf-8')
            #print unicode(ad_dict, 'utf-8').encode('utf-8')
            ads_list.append(ad_dict)
            #print standard_adds_list
            #i = i+1
            #print i
    return ads_list


def make_ad_list_s(ads, type):

    ads_list = []
    i = 0
    for ad in ads:
            ad_dict = {}
            add = ad.find_all('a')
            ad_dict['date'] = current_date_str()
            ad_dict['ad_type'] = type
            #print get_position(add)
            ad_dict['position'] = get_position_s(add)

            ad_dict['firm'] = get_firm_s(ad)
            #print get_city(ad)
            ad_dict['city'] = get_city_s(add).encode('utf-8')
            ad_dict['tags'] = get_tags_list_s(add)
            #print unicode(ad_dict, 'utf-8')
            #print unicode(ad_dict, 'utf-8').encode('utf-8')
            ads_list.append(ad_dict)
            #print standard_adds_list
            #i = i+1
            #print i
    return ads_list
#def find_ads(css_class_name):
#    return soup.find_all("div", class_="css_class_name")
#base URL
url="http://startit.rs/poslovi/"


response = requests.get(url)

result = response.content

soup = BeautifulSoup(result, 'html.parser')

premium_ads = soup.find_all("div", class_="listing-oglas-premium")
standard_ads = soup.find_all("div", class_="listing-oglas-standard")
mini_ads = soup.find_all("div", class_="oglas-mini")

# making lists of dictionaries
premium_ads = make_ad_list(premium_ads, "premium ads")
standard_ads = make_ad_list(standard_ads, "standard ads")
mini_ads = make_ad_list_s(mini_ads, "mini ads")

#print "PREMIUM ADS: ",make_ad_list(premium_ads, "premium ads")
#print"""
#
#
#
#
#"""
#print "STANDARD ADS: ",make_ad_list(standard_ads, "standard ads")
#print"""
#
#
#
#
#"""
#print "MINI ADS: ",make_ad_list_s(mini_ads, "mini ads")

#
#
# mongoDB
#
#

db, collection =mongo_lib.connect_client('jobs_db','job_posts')
#collection.insert(premium_ads)


collection.insert(premium_ads)
collection.insert(standard_ads)
collection.insert(mini_ads)

query_set = collection.find()
print query_set.count()

#for i in query_set:
#    pprint.pprint(i)

#collection.remove()

time = time.time()-start
scrape_lib.print_time(time)