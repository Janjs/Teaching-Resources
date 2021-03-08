from bs4 import BeautifulSoup
import requests

url = "https://www.linkedin.com/jobs/search?keywords=Python%20%28Programming%20Language%29&location=Matar%C3%B3%2C%20Catalonia%2C%20Spain&geoId=101156716&trk=public_jobs_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0"

pagina_web = requests.get(url)
pagina_web_text = pagina_web.text

soup = BeautifulSoup(pagina_web_text, 'lxml')

jobs = soup.find_all('div', class_="result-card__contents job-result-card__contents")


for job in jobs:
    try:
        job_title = job.h3.text
        company_name = job.find('a', class_="result-card__subtitle-link job-result-card__subtitle-link")
        company_name = company_name.text

        print("Feina: "+job_title)
        print("Empresa: "+company_name)
        print("------------")
    except:
        print("No s'ha pogut obtenir informació.")