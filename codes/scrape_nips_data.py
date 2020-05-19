# -*- coding: utf-8 -*-
"""
Created on Mon May 11 21:10:00 2020

@author: tneha
"""


import requests
import pandas as pd
from bs4 import BeautifulSoup


def scrape_161718(year):
    
    url = "https://neurips.cc/Conferences/"+year+"/Schedule?bySubject=#bySubjectArea"

    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    l = soup.find(id = 'bySubjectForm')
    
    values = l.find_all('input', type = 'checkbox')
    values = [v["value"] for v in values]
    
    labels = l.find_all('label')
    #values = [int(re.sub('id', '', label['for'])) for label in labels]
    
    
    df = []
    
    for i, value in enumerate(values):
        
        url = "https://neurips.cc/Conferences/"+year+"/Schedule?bySubject=&selectedSubject="+value+"#bySubjectArea"
        
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        
        k = soup.find_all('div', class_ = 'maincard narrower Poster')
        
        for item in k:
            
            title = item.find('div', class_ = "maincardBody").text
            
            #link = item.find('a', class_ = "btn btn-default btn-xs href_PDF")['href'] 
            link = item.find('a', class_ = "btn btn-default btn-xs href_PDF")
            if link is not None:
                link = link['href']
                            
                response2 = requests.get(link)
                
                if response2.status_code == 404:
                    
                    abstract = "paper link not found"
                    pdf_link = "paper link not found"
                    
                else:
                    
                    soup2 = BeautifulSoup(response2.text, "html.parser")
                    
                    abstract = soup2.find('p', class_ = 'abstract').text
                    
                    m = soup2.find('div', class_="main wrapper clearfix")
                    pdf_link = "http://papers.nips.cc"+m.find_all('a')[1]['href']
                
                doc = {
                        'title': title,
                        'abstract': abstract,
                        'pdf_link': pdf_link,
                        'year': int(year),
                        'track': labels[i].text.strip()
                            }
                
                df.append(doc)
            else:
                continue
    
    return pd.DataFrame(df)


def scrape_19():

    url = "https://neurips.cc/Conferences/2019/ScheduleMultitrack2?text=&session=&event_type=Poster&day="
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    l = soup.find_all('div', class_ = 'event-title')
    
    df = []
    
    for item in l:
        
        url = "https://neurips.cc" + item.a['href']
        track = item.a['title']
        
        response = requests.get(url)
        
        soup1 = BeautifulSoup(response.text, "html.parser")
        
        papers = soup1.find_all('div', class_ = 'event-title')
        
        for paper in papers:
            
            link = "https://neurips.cc" + paper.a['href']
            
            #extract paper metadata
            title = paper.a['title']
            
            #reuqest the paper url to get paper metadata
            response = requests.get(link)
            soup2 = BeautifulSoup(response.text, "html.parser")
            
            pdf_link = soup2.find('a', class_ = 'btn btn-default btn-xs href_PDF')['href']
            
            response = requests.get(pdf_link)
            
            soup3 = BeautifulSoup(response.text, "html.parser")
            
            abstract = soup3.find('p', class_ = 'abstract').text
            
            doc = {
                    'track': track,
                    'title': title,
                    'year': 2019,
                    'abstract': abstract,
                    'pdf_link': pdf_link
                    }
            
            df.append(doc) 
            
    #return the list of dicts as a dataframe    
    return pd.DataFrame(df)
            
        
    
        
def main():
    
    data = []
    
    #for 2016-2018 call scrape_161718
    for y in ['2016', '2017', '2018']:        
        data.append(scrape_161718(y))
    
    #for 2019 call scrape_19
    data.append(scrape_19())
     
    #merge the data for all years and write it to a csv
    data = pd.concat(data)    
    data.to_csv("nips_scraped.csv", index= False)
        
        

if __name__ == '__main__':
    main()       