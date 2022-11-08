# Jobstreet Scraper v0

Primary function is to scrape for specific job title or specific keyword, such as fresh graduate, in the description of job listings.

Warning : The urls are for the \*Malaysia Jobstreet site\*, **please change the urls accordingly** to fit your needs.

The output of this scraper is a text file containing a **dictionary** for each fitting job and contains the following information with their keys:
* jobstreet url - ```['link']```
* position - ```['title']```
* published date - ```['time']```
* description - ```['desc']```

This code was designed to work on Google Colab that has a timeout feature after a few hours unless there is an interaction on the webpage.
It will periodically save the results as text files to the desired path (usually Drive). After every iteration from the first, previous result text files will be deleted to save space.

# Usage

The main function is ```scrape_job()``` that takes 5 **required** and 1 ***non-required*** argument. In order these are:

* **timeout** - the amount of time, in seconds, for ```download_content()``` to obtain a url before timing out
* **sheet** - an empty list to store potential job information
* **total** - the total number of jobs to scrape over (to avoid long runtimes and repetitive scraping, this is to be done manually)
* **substring_list** - list of keywords to look for in the description of each job listing
* **path** - directory to save textfiles in
* ***keyword*** - specific job title, if no keyword is specified all job listings will be scraped

Note : A multithreaded version is currently in development but Colab does not support many of its features.
