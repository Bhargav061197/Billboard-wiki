import datetime
def date():
    start = datetime.datetime.strptime("01-01-2016", "%d-%m-%Y")
    end = datetime.datetime.strptime("01-01-2018", "%d-%m-%Y")
    date_generated = [start + datetime.timedelta(days=x) for x in range(1, (end-start).days)]
    a=[]
    for (date,i) in zip(date_generated,range(1,731)):
        if i%350==0:
            a.append(date.strftime("%Y-%m-%d"))

    return a

