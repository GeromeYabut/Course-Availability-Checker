import requests
import smtplib
import tkinter

#top = tkinter.Tk()
#top.mainloop()

"""
def classavail(url):
    link = url
    f = requests.get(link)
    seatsLine = []
    for line in f:
        if("seats" in str(line)):
            seatsLine = line

    seatsLine = str(seatsLine).split(',')
    seatsLine = str(seatsLine[0]).split(':')
    #print(seatsLine[1][1])
    if(int(seatsLine[1][1]) == 1 ):
        return 1
    else:
        return 0
"""

def classavail(url):
    link = courseavail

    f = requests.get(link)
    unparsedLines = []
    for line in f:
        if ("has_seats" in str(line)):
            unparsedLines.append(line)
#print(len(unparsedLines))
#print(unparsedLines)

    parse2 = []

    for item in unparsedLines:
        parse2.append(str(item).split(','))

    seatdata = ''

    for item in parse2:
        for data in item:
            if("has_seats" in data):
                seatdata = data
                availability = seatdata.strip()[-2:-1]
                return 1
    return 0



def sendMail(text):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("test.geromeyabut@gmail.com", "Yabuttim3")

    msg = "\r\n".join([
                   "From: test.geromeyabut@gmail.com",
                   "To: test.geromeyabut@gmail.com",
                   "Subject: Just a message",
                   "",
                   text
                   ])
    server.sendmail("test.geromeyabut@gmail.com", "test.geromeyabut@gmail.com", msg)
    server.quit()


School = input("Enter school code, i.e. COEN\n")
Number = input("\nEnter course code, i.e. 10\n")

"""courseavail = "https://www.scu.edu/apps/ws/courseavail/classes/3840/ugrad/COEN%20177" """

courseavail = "https://www.scu.edu/apps/ws/courseavail/classes/3840/ugrad/" + School + "%20" + str(Number)
print(courseavail)



while(1):
    if(classavail(courseavail) == 1):
        print("class is available\n")
        print("if class becomes unavailable, will notify\n")
        while( classavail(courseavail) == 1):
            if(classavail(courseavail)==0):
                text = "Class is now unavailable"
                sendMail(text)
                print(text)
                break

    if(classavail(courseavail) == 0):
        print("class is unavailable\n")
        print("If class becomes available, will notify\n")
        while(classavail(courseavail) == 0):
            if(classavail(courseavail)==1):
                text = "Class is now available"
                sendMail(text)
                print(text)
                break

