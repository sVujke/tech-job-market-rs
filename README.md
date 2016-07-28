# Tech Job Market of Serbia

## Data Set

The data has been scraped from a popular Serbian website [Startit](http://startit.rs/poslovi/) since December 14th, 2016.
The scraper was written using the [Beutiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) library. 

The process of data collection is automated with a python script which is hosted on an [Amazon Elastic Compute
Cloud (EC2)](https://aws.amazon.com/ec2/) and is scheduled to run every day at 5:00 PM (CET). The script counts the number of job adverts
with the following tags: java, .net, c, php, js/javascript, python, ruby, android, ios, game-dev, qa, frontend and linux.

##Line Chart - Overall demand for IT skills 

![Overal demand for IT Skills](https://raw.githubusercontent.com/sVujke/tech-job-market-rs/master/img/overall.PNG "Overall demand for IT skills ")
