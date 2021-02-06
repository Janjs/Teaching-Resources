from bs4 import BeautifulSoup
import requests
from datetime import datetime
import time

url = 'https://www.linkedin.com/jobs/search?keywords=Python&location=Matar%C3%B3%2C%20Catalonia%2C%20Spain&geoId=101156716&trk=public_jobs_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0'


def find_jobs():
    html_text = requests.get(url)
    html_text = html_text.text
    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all(
        'li', class_="result-card")

    for index, job_full in enumerate(jobs):
        link = job_full.a['href']

        job = job_full.find(
            'div', class_="result-card__contents job-result-card__contents")

        published_date = job.find('time')["datetime"]

        today = datetime.today().strftime('%Y-%m-%d')

        if published_date == today:
            try:
                company_name = job.find('a').text
            except:
                company_name = job.find('h4').text
            job_title = job.find('h3').text

            with open(f'jobs/{str(today) + " " +str(index)}.txt', 'w') as f:
                f.write(f'''
                Company Name: {company_name}
                Job title: {job_title}
                published at: {published_date}
                link: {link}
                ''')
            print(f'File saved: {index}')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)
