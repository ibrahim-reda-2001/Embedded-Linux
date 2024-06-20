import requests
from pprint import pprint
import csv
from bs4 import BeautifulSoup
date=input("Enter the date in mm/dd/yyyy :").split()
url=requests.get(f"https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date={date}#")

def main(page):
soup=BeautifulSoup(page.content,"lxml")
matches_details=[]
#هنا انتا بتختار كل البطولات الا موجوده ف اليوم ده 
# بيكون موجود اكتر من ديف ممكن تكون ديف واحد بس  
#may be matchCard or matchsList
#find all scan all document but if u want only one use find () only
championship=soup.find_all("div",{'class':'matchCard'})  
#print(championship)
#بعد كدا محتاجين نطلع كل التفاصيل الا جوا الديف الكبير =>championship
#هنعمل فانكشن تطلع المعلومات دي و هتا الديف الكبير  
def match_information(championship):
    #اول حاجه هنجيبها عنوان البطوله
    #title is child number 0 (try and error) we need h2(in title in h2)
    #print(championship_title) #to try if it is 0 or 1
    championship_title=championship.contents[1].find('h2').text.strip()
    #all other information in untitle list
    #print(all_matches) #to try if it is 2 or 3
    all_matches_finish=championship.contents[3].find_all('div',{'class':'item finish liItem'})
    all_matches_future=championship.contents[3].find_all('div',{'class':'item future liItem'})
    all_matches_now=championship.contents[3].find_all('div',{'class':'item now liItem'})
    all_matchs=len(all_matches_finish)+len(all_matches_future)+len(all_matches_now)
    #print(all_matchs)
    for i in range (len(all_matches_finish)):
        #get teams names
        team_A=all_matches_finish[i].find('div',{'class':'teamA'}).text.strip()
        team_B=all_matches_finish[i].find('div',{'class':'teamB'}).text.strip()
        #get score
        match_result=all_matches_finish[i].find('div',{'class':'MResult'}).find_all('spans',{'class':'score'})
        score=f"{match_result[0].text.strip()}-{match_result[1].text.strip()}"
        #get match time
        match_time=all_matches_finish[i].find('div',{'class':'MResult'}).find_all('spans',{'class':'time'})
        matches_details.append=({"البطوله":championship_title,"الفريق الاول":team_A,"الفريق الثاني":team_B,"معاد المباراه ":match_time,"النتيجه":score})
    for i in range (len(all_matches_now)):
        #get teams names
        team_A=all_matches_now[i].find('div',{'class':'teamA'}).text.strip()
        team_B=all_matches_now[i].find('div',{'class':'teamB'}).text.strip()
        #get score
        match_result=all_matches_now[i].find('div',{'class':'MResult'}).find_all('spans',{'class':'score'})
        score=f"{match_result[0].text.strip()}-{match_result[1].text.strip()}"
        #get match time
        match_time=all_matches_now[i].find('div',{'class':'MResult'}).find_all('spans',{'class':'time'})
        matches_details.append=({"البطوله":championship_title,"الفريق الاول":team_A,"الفريق الثاني":team_B,"معاد المباراه ":match_time,"النتيجه":score}) 
    for i in range (len(all_matches_future)):
        #get teams names
        team_A=all_matches_future[i].find('div',{'class':'teamA'}).text.strip()
        team_B=all_matches_future[i].find('div',{'class':'teamB'}).text.strip()
        #get score
        match_result=all_matches_future[i].find('div',{'class':'MResult'}).find_all('spans',{'class':'score'})
        score=f"{match_result[0].text.strip()}-{match_result[1].text.strip()}"
        #get match time
        match_time=all_matches_future[i].find('div',{'class':'MResult'}).find_all('spans',{'class':'time'})
        matches_details.append=({"البطوله":championship_title,"الفريق الاول":team_A,"الفريق الثاني":team_B,"معاد المباراه ":match_time,"النتيجه":score})       
        
        
        
        
for i in range (len(championship)):
    match_information(championship[i])
     
#csv file
keys=matches_details[0].keys
with open('/home/ibrahim/Downloads','w')as output_file:
    dict_writer=csv.DictWriter(output_file,keys)
    dict_writer.writeheader()
    dict_writer.writerows(matches_details)
    print("file done")
           
        
