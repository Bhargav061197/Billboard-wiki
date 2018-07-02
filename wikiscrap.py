import requests
from bs4 import BeautifulSoup


url = 'https://en.wikipedia.org/wiki/Too_Good_at_Goodbyes'
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text,"html5lib")


def getgenre(soup):
    col=soup.findAll("td",{"class": "category hlist"})
    if len(col)==0:
    	print("Nahi hai")
    else:
        cols=str(col[0])
        under=BeautifulSoup(cols,"html5lib")
        if len(under.findAll('li')) == 0:
        	print(under.a.string)
        else:
            for i in under.findAll('li'):
	            print(i.a.string)

def getWriter(soup):
    for test in soup.findAll("a"):
	    if test.string=="Songwriter(s)":
		    sample=test.parent.parent.parent
    under1=BeautifulSoup(str(sample),"html5lib")
    for x in under1.findAll('li'):
    	if x.a == None:
    		print(x.string)
    	else:
    		print(x.a.string)
def getproducer(soup):
	for test in soup.findAll("a"):
		if test.string=="Producer(s)":
			sample=test.parent.parent.parent
	under1=BeautifulSoup(str(sample),"html5lib")
	c=0
	if len(under1.findAll('li'))==0:
         for x in under1.findAll('a'):
            c+=1
            if x.string!="Producer(s)":
                print(x.string)
         if c==1:
             str1 = str(under1)
             strx = (str1[str1.find("</span>") + 7:str1.find("</body>")]).strip()
             print(strx)
	else:
	    for x in under1.findAll('li'):
		    if x.a==None:
			    print(x.string)
		    else:
			    print(x.a.string)


print("Genre")
getgenre(soup)
print("")
print("Writer")
getWriter(soup)  
print("")
print("Producer")
getproducer(soup)
