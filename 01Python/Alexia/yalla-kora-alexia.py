import requests
from pprint import pprint
import csv
from bs4 import BeautifulSoup
import datetime
def get_date():
    return datetime.datetime.now().strftime("%m/%d/%Y")

date = get_date()
url = requests.get(f"https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date={date}#")

def main(page):
    soup = BeautifulSoup(page.content, "lxml")
    matches_details = []
    #هنا انتا بتختار كل البطولات الا موجوده ف اليوم ده 
    # بيكون موجود اكتر من ديف ممكن تكون ديف واحد بس  
    #may be matchCard or matchsList
    #find all scan all document but if u want only one use find () only

    championship = soup.find_all("div", {'class': 'matchCard'})
    #print(championship)
    #بعد كدا محتاجين نطلع كل التفاصيل الا جوا الديف الكبير =>championship
    #هنعمل فانكشن تطلع المعلومات دي و هتا الديف الكبير

    def match_information(championship):
        #اول حاجه هنجيبها عنوان البطوله
        #title is child number 0 (try and error) we need h2(in title in h2)
        #print(championship_title) #to try if it is 0 or 1
        championship_title = championship.contents[1].find('h2').text.strip()
        #all other information in untitle list
        #print(all_matches) #to try if it is 2 or 3
        all_matches_finish = championship.contents[3].find_all('div', {'class': 'item finish liItem'})
        all_matches_future = championship.contents[3].find_all('div', {'class': 'item future liItem'})
        all_matches_now = championship.contents[3].find_all('div', {'class': 'item now liItem'})

        for match in all_matches_finish:
            team_A = match.find('div', {'class': 'teamA'}).text.strip()
            team_B = match.find('div', {'class': 'teamB'}).text.strip()
            match_result = match.find('div', {'class': 'MResult'}).find_all('span', {'class': 'score'})
            score = f"{match_result[0].text.strip()}-{match_result[1].text.strip()}"
            match_time = match.find('div', {'class': 'MResult'}).find('span', {'class': 'time'}).text.strip()
            matches_details.append({"البطوله": championship_title, "الفريق الاول": team_A, "الفريق الثاني": team_B, "معاد المباراه ": match_time, "النتيجه": score})

        for match in all_matches_now:
            team_A = match.find('div', {'class': 'teamA'}).text.strip()
            team_B = match.find('div', {'class': 'teamB'}).text.strip()
            match_result = match.find('div', {'class': 'MResult'}).find_all('span', {'class': 'score'})
            score = f"{match_result[0].text.strip()}-{match_result[1].text.strip()}"
            match_time = match.find('div', {'class': 'MResult'}).find('span', {'class': 'time'}).text.strip()
            matches_details.append({"البطوله": championship_title, "الفريق الاول": team_A, "الفريق الثاني": team_B, "معاد المباراه ": match_time, "النتيجه": score})

        for match in all_matches_future:
            team_A = match.find('div', {'class': 'teamA'}).text.strip()
            team_B = match.find('div', {'class': 'teamB'}).text.strip()
            match_result = match.find('div', {'class': 'MResult'}).find_all('span', {'class': 'score'})
            score = f"{match_result[0].text.strip()}-{match_result[1].text.strip()}"
            match_time = match.find('div', {'class': 'MResult'}).find('span', {'class': 'time'}).text.strip()
            matches_details.append({"البطوله": championship_title, "الفريق الاول": team_A, "الفريق الثاني": team_B, "معاد المباراه ": match_time, "النتيجه": score})

    for champ in championship:
        match_information(champ)
        #csv 

    keys = matches_details[0].keys()
    with open('/home/ibrahim/Downloads/matches_details.csv', 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(matches_details)
        print("file done")

main(url)