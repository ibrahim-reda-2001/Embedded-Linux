import webbrowser
favourite_websites=["https://www.facebook.com/","https://www.youtube.com/","https://github.com/ibrahim-reda-2001/Embedded-Linux"]

def open_in_firefox(url):
    firefox_path=webbrowser.get('firefox')
    firefox_path.open(url)