import task2_module
#print("Favotite Websites : ")

for site in task2_module.favourite_websites:
    print (site)
    
url_to_open=input("Enter the favorite one ")

task2_module.open_in_firefox(url_to_open)