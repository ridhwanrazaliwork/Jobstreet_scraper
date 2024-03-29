from bs4 import BeautifulSoup as sp 
import requests,re,math,time,os

#attempt at obtaining url content
#time in number of seconds until timeout
def download_content(url,time):
    timeout = time*4
    for i in range(timeout):
        page = requests.get(url)
        if page != None:
            return page.content
        elif i == timeout-1:
            return None
        else:
            time.sleep(0.25)
            continue

#refer readme file
def scrape_job(timeout,sheet,total,substring_list,path,keyword=''):
    for pages in range(1,math.ceil(total/30)+1):
        if keyword == '':        
            url = 'https://www.jobstreet.com.my/en/job-search/job-vacancy/{}/?ojs=1'.format(pages)
        else:
            url = 'https://www.jobstreet.com.my/en/job-search/{}-jobs/{}'.format(keyword,pages)
        #extract page
        page = download_content(url,timeout)
        #catch failure
        if page == None:
            print('Page',pages,'failed to download.')
            continue
        #parse with BS
        soup = sp(page,'html.parser')
        #find specific class that identifies the job listings
        job = soup.find('div',class_="sx2jih0 zcydq8bm").find('div',class_='sx2jih0')
        for jobs in job :
                #obtain info
                link_job = jobs.find('h1',class_='sx2jih0 zcydq84u _18qlyvc0 _18qlyvc1x _18qlyvc3 _18qlyvca').a.get('href')
                job_title = jobs.find('h1',class_='sx2jih0 zcydq84u _18qlyvc0 _18qlyvc1x _18qlyvc3 _18qlyvca').a.text
                pub = jobs.find('time',class_='sx2jih0 zcydq84u').text
                url1 = 'https://www.jobstreet.com.my{}'.format(link_job)
                #extract page
                page1 = download_content(url1,timeout)
                #parse with BS
                soup1 = sp(page1,'html.parser')
                #find specific class that identifies the job listings
                try:
                    temp = soup1.find('div',class_="sx2jih0 zcydq86q zcydq86v zcydq86w").find("span",'sx2jih0 zcydq84u _18qlyvc0 _18qlyvc1x _18qlyvc1 _18qlyvca').text
                    a = any(substring in temp for substring in substring_list)
                    if a:
                        sheet.append([{'link':'https://www.jobstreet.com.my'+link_job,'title':job_title,'time':pub,'desc':temp}])
                except:
                    continue
        #to save as
        filename = path + 'p%s.txt' % (str(pages))
        #to remove previous
        prev_filename = path + 'p%s.txt' % (str(pages-1))
        #save sheet items to new txt file
        with open(filename,'w') as fp:
            for item in sheet:
                fp.write("%s\n" % item)
        #remove older txt file
        if os.path.exists(prev_filename):
            os.remove(prev_filename)
        else:
            print("First txt saved.")
        print('Completed page',(pages),'with',len(sheet),'candidates found.',(math.ceil(total/30)-pages),'page(s) left.')

keyword = 'data-analyst' #optional
substring_list = ['fresh graduate','Fresh graduate','Fresh graduates','fresh graduates']
sheet,total,timeout = [],60,3
path = '/content/drive/MyDrive/'
print("Started...")
scrape_job(timeout,sheet,total,substring_list,path)
