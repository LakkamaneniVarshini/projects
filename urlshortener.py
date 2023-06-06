import pyshorteners

link=input("Enter link: ")

shortener = pyshorteners.Shortener()
x = shortener.tinyurl.short(link)
print("short link: ",x)