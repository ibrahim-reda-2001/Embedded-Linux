import csv
from bs4 import BeautifulSoup
import string
data=open('html/main_8c.html','r')
html_content=data.read()
data.close()
#print(html_content)
soup=BeautifulSoup(html_content,'html.parser')
function_details=[]
all_function_title=soup.find_all('h2',{'class','memtitle'})
all_item=soup.find_all('div',{'class','memitem'})#this is important contain all info
for content in all_item:
    brief=content.find('div',{'class','memdoc'}).find('p').text
    #print(brief)
    parameters=content.find('table',{'class','params'}).find_all('td')
    parameter_list=[]
    for i in parameters:
        parameter_list.append(i.text)
    #print(parameter_list)
    return_val=content.find('div',{'class','memdoc'}).find('dl',{'class','section return'}).find('dd').text
    # print(return_val)
    function_details.append({
        'brief':brief,
        'parameters':parameter_list,
        'retturn':return_val
    })

# #print(function_details)
# for i in range(len(all_item)):
#     function_details[i]['parameters']=''.join(function_details[i]['parameters'])
# # print(function_details)
keys=function_details[0].keys()
with open('/home/ibrahim/Embedded Linux/01Python/lec4/task/doxygen/doxygen.csv','w') as doxygen_file:
    dictinory=csv.DictWriter(doxygen_file,keys)
    dictinory.writeheader()
    for i in range(len(all_item)):
        dictinory.writerow(function_details[i])
    print("doxygen file done bro .......")


    