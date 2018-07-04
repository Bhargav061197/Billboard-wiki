import requests
import pandas as pd
from bs4 import BeautifulSoup
import csv as csv
from date import date
a=date()


def songs():
    df = pd.DataFrame({
        "Fake": [0]
    })
    df = df.drop(columns="Fake")
    df = df.drop([0])
    df2 = df
    for it in a:
        print(it)
        url = "https://www.billboard.com/charts/hot-100/"+str(it)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,"html5lib")



        i = 1
        for (link ,link12) in zip(soup.findAll("h2", {"class": "chart-row__song"}),soup.findAll(class_="chart-row__artist")): # zip method helps us perform multiple pararllel for loops .
            href = link.string  #song name
            href1 = href.split()
            word1=combine(href1)
            x0=combine2(href1)
            url1 = "https://en.wikipedia.org/wiki/" + str(word1)
            href12 = link12.string
            split=href12.split()
            x1=combine2(split)
            x2 = word(x1)
            split2 = x2.split()
            href123=combine(split2)
            m1="_("
            m="_song)"
            url2=url1+str(m1)+str(href123)+str(m)
            c = test(url1)
            if c == 1:
                print(url1)

                df1 = pd.DataFrame({
                    "Song": [x0],
                    "Artist": [x2],
                    "Position": [i]
                })


                df4=urlx(url1, x0, x2,df1)


            if c != 1:

                test1 = test(url2)
                if test1 == 1:
                    print(url2)
                    df1 = pd.DataFrame({
                        "Song": [x0],
                        "Artist": [x2],
                        "Position": [i]
                    })


                    df4 = urlx(url2, x0, x2,df1)


                if test1 != 1:
                    m2="song)"
                    url3=url1+str(m1)+str(m2)
                    test3=test(url3)
                    if test3 == 1:
                        print(url3)
                        df1 = pd.DataFrame({
                            "Song": [x0],
                            "Artist": [x2],
                            "Position": [i]
                        })


                        df4= urlx(url3,x0,x2,df1)

            df2 = pd.concat([df4, df2], ignore_index=True)
            i = i + 1
    df2.to_csv("initial.csv")
    df2.fillna(0,inplace=True)

    df2 = df2.sort_values("Position")
    df2.drop_duplicates(subset='Song', keep="first", inplace=True)
    df2.set_index("Song", inplace=True)
    df2.to_csv("final.csv")





def combine2(word):
    x=" ".join(word)
    return x


def test(url1):
    source_code = requests.get(url1)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html5lib")
    for link1 in soup.findAll("a", {"title": "Single (music)"}):
        title1 = link1.string
        if title1 == "Single":
            return 1

def combine(word):
    x = "_".join(word)
    return x

def word(name):

    if "," in name:
        if "Featuring" in name:
            x = name.split(" Featuring", 1)[0]
            if "&" in x:
                return x.split(" &", 1)[0]
            else:
                return x
        else:
            return name.split(",", 1)[0]
    if "Featuring" in name:
        x=name.split(" Featuring", 1)[0]
        if "&" in x:
            return x.split(" &", 1)[0]
        else:
            return x
    if "&" in name:
        return name.split(" &", 1)[0]
    if "X" in name:
        return name.split(" X", 1)[0]
    else:
        return name


def urlx(url,x0,x1,df):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html5lib")

    df1 = getgenre(soup, df)

    df2 = getWriter(soup, df1)

    df3 = getproducer(soup,df2)


    return df3

def getgenre(soup,df):
    col=soup.findAll("td",{"class": "category hlist"})
    if len(col)==0:

        return df

    else:
        for link in soup.findAll("td", {"class": "category hlist"}):
            a=link.string
        if a==None:
            cols=str(col[0])
            under=BeautifulSoup(cols,"html5lib")
            if len(under.findAll("li")) == 0:
                x=under.a.string
                df1=pd.DataFrame({
                    x:[1]
                })
                df2 = pd.concat([df, df1], axis=1)

                return df2
            else:
                df1=pd.DataFrame({
                    "Fake":[0]
                })
                df1 = df1.drop(columns="Fake")
                df1=df1.drop([0])
                for i in under.findAll("li"):
                    x=i.a.string
                    df2=pd.Series(
                        [1],name=x
                    )

                    df1=pd.concat([df1,df2],axis=1)

                df1=pd.concat([df,df1],axis=1)


                return df1
        else:
            df1 = pd.DataFrame({
                a: [1]
            })
            df2 = pd.concat([df, df1], axis=1)

            return df2




def getWriter(soup,df):
    sample = "yes"
    for test in soup.findAll("a"):
        if test.string=="Songwriter(s)":
            sample=test.parent.parent.parent
        else:
            return df
    if sample=="yes":
        return df
    else:
        under1=BeautifulSoup(str(sample),"html5lib")
        df1 = pd.DataFrame({
            "Fake": [0]
        })
        df1 = df1.drop(columns="Fake")
        df1 = df1.drop([0])
        for x in under1.findAll("li"):
            if x.a == None:
                m=x.string
                df2 = pd.Series(
                    [1], name=m
                )
                df1=pd.concat([df1,df2],axis=1)
            else:
                m1=x.a.string

                df2 = pd.Series(
                    [1], name=m1
                )
                df1 = pd.concat([df1, df2], axis=1)
        df1 = pd.concat([df, df1], axis=1)

        return df1

def getproducer(soup,df):
    sample="yes"
    for test in soup.findAll("a"):
        if test.string=="Producer(s)":
            sample=test.parent.parent.parent
    if sample =="yes":
        return df
    under1=BeautifulSoup(str(sample),"html5lib")
    c=0
    df1 = pd.DataFrame({
        "Fake": [0]
    })
    df1 = df1.drop(columns="Fake")
    df1 = df1.drop([0])

    if len(under1.findAll("li"))==0:
         for x in under1.findAll("a"):
            c+=1
            if x.string!="Producer(s)":
                m=x.string

                df2 = pd.Series(
                    [1], name=m
                )
                df1 = pd.concat([df1, df2], axis=1)
         if c==1:
             str1 = str(under1)
             strx = (str1[str1.find("</span>") + 7:str1.find("</body>")]).strip()
             m1=strx

             df2 = pd.Series(
                 [1], name=m1
             )
             df1 = pd.concat([df1, df2], axis=1)
    else:
        for x in under1.findAll("li"):
            if (x.a==None):
                if(x.string==None):
                    break
                else:
                    m2=x.string

                    df2 = pd.Series(
                    [1], name=m2
                    )
                df1 = pd.concat([df1, df2], axis=1)
            else:
                m3=x.a.string
                df2 = pd.Series(
                    [1], name=m3
                )
                df1 = pd.concat([df1, df2], axis=1)
    df1 = pd.concat([df, df1], axis=1)
    return df1

songs()
