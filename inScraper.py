#Indeed WebScraper
#1 July 2022
#Trista Smith
#Complete 7/4
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    indeed = f'https://www.indeed.com/jobs?q=python%20developer%20entry%20level&l=Remote&start={page}'
    r = requests.get(indeed, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_ = "slider_container")
    for list in divs:
        title = list.find('a').text.replace('\n', '')
        company = list.find('span', class_ = "companyName").text.replace('\n', '')
        summary = list.find('div', {'class' : "job-snippet"}).text.replace('\n', '')
        
        try:
            salary = list.find('span', class_ = "estimated-salary").text.replace('\n', '')   
        except:
            salary = ''
           
        job = {
            'Title': title,
            'Company': company,
            'Salary': salary,
            'Summary': summary
        }
        joblist.append(job)

        #print(title, company, salary, summary)
    return

joblist = []
for i in range(0, 200, 10):
    print(f'Getting page, {i}')
    c = extract(i)
    transform(c)
    df = pd.DataFrame(joblist)
    print(df.head())
    df.to_csv('jobs.csv')




    #last 24hrs, remote
    #https://www.indeed.com/jobs?q=python%20developer%20entry%20level&l=Remote&sc=0kf%3Aattr(DSQF7)%3B&fromage=1&vjk=5121460af85daa33