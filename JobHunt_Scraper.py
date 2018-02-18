#Author: Shyam Mohan Kriparamanan, andrew (skripara)
#Date : 2.17.2018
#This is programscrapes glassdoor site and retreives the job names, salaries, job histories for any of the keywords passed

import os
import sys
import requests
from bs4 import BeautifulSoup
import openpyxl
import re
import csv

def downloadStatsGlassDoor (url,i):
    '''
    Downloads the details of the search term passed
    :param url to search:
    :return: none
    '''

    liTotal = []

    headers = {'user-agent': 'Mozilla/5.0'}
    response = requests.get(url,headers=headers)
    if(response.status_code==200):
        soup = BeautifulSoup(response.text, "html.parser")

        totalJobs=""
        maindiv = soup.find("div",class_="pageContentWrapper").find("div").find("div").find("div").find("div",id="JobSearch").find("div").find("div",id="JobResults").find("section").find("article",id="MainCol").find("div")


        if maindiv.find("div", class_="hideHH", id="MainColSummary")!=None:
            divTemp = maindiv.find("div", class_="hideHH")
            if divTemp.find("p", class_="jobsCount")!=None:
                totalJobs = divTemp.find("p", class_="jobsCount").text


        if maindiv.find("ul",class_="jlGrid hover")!=None:
            if maindiv.find("ul",class_="jlGrid hover").find_all("li") !=None:
                listings = maindiv.find("ul",class_="jlGrid hover").find_all("li")

            for listing in listings:

                jobTitle=""
                jobLink=""
                employer = ""
                location = ""
                numberDaysAgo=""
                rating = ""
                salary=""
                salRange=""

                if listing.find("div",class_="logoWrap").find("span",class_="compactStars")!=None:
                    rating = listing.find("div",class_="logoWrap").find("span",class_="compactStars").text

                listing = listing.find("div").find_next_sibling()
                #if(listing["class"]!=['logoWrap']):

                if listing.find("div",class_="flexbox").find("div").find("a")!=None:
                    jobTitle = listing.find("div",class_="flexbox").find("div").find("a").text
                    jobLink= listing.find("div",class_="flexbox").find("div").find("a")["href"]

                if listing.find("div", class_="flexbox empLoc").find("div") != None:
                    employer = listing.find("div", class_="flexbox empLoc").find("div").text
                    location = listing.find("div", class_="flexbox empLoc").find("div").find("span").text
                    #numberDaysAgo= listing.find("div", class_="flexbox empLoc").find("span",class_="hideHH nowrap").find("span").text


                if listing.find("div",class_="flexbox").find("div").find("i")!=None:
                    salary= listing.find("div",class_="flexbox").find("div").find("i")["data-displayed-med-salary"]

                if listing.find("div",class_="flexbox").find("div").find("span",class_="green small")!=None:
                    salRange= listing.find("div",class_="flexbox").find("div").find("span",class_="green small").text

                liTotal.append(jobTitle+","+"https://www.glassdoor.com"+jobLink+","+employer+","+location+","+numberDaysAgo+","+rating+","+salary+","+salRange)
     #print(liTotal)
    return liTotal
    pass


def main():
    '''
    main entry to the program
    '''

    wb = openpyxl.Workbook()
    wb.create_sheet(index=0, title='glassdoor')

    #listInsert = ['jobTitle', 'JobLink', 'employer', 'location', 'numberDaysAgo', 'rating', 'salary', 'salRange']

    #Extract 10 pages of data
    print("Enter a job to search")
    search = input()
    # clean the search term to form the url
    searchTerm = search.replace(" ", "-")

    # url3="https://www.glassdoor.com/Job/marketing-manager-jobs-SRCH_KE0,17.htm"
    url=""


    try:

        masterList =['jobTitle,JobLink,employer,location,numberDaysAgo,rating,salary,salRange']
        for i in range(1,10):
            url=""

            if (i == 1):
                url = "https://www.glassdoor.com/Job/" + searchTerm + "-jobs-SRCH_KE0,17.htm"
            else:
                url="https://www.glassdoor.com/Job/" + searchTerm + "-jobs-SRCH_KE0,17_IP"+str(i)+".htm"
            print(url)

            l1=downloadStatsGlassDoor(url,i)
            masterList.extend(l1)

            print(l1)

        outF = open("myJobFileMarketingManager.csv", "w")
        for line in masterList:
            # write line to output file
            outF.write(line)
            outF.write("\n")
        outF.close()
        return





        #downloadStatsMonster("data scientist")
        #print(listInsert)
    except Exception as e:
        print(str(e))
        print("exception")
    finally:

        print("finally")

        print("Writing complete")
    pass


if __name__ == '__main__':
    os.chdir(os.path.dirname(sys.argv[0]))
    main()