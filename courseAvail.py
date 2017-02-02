import requests
import smtplib
import tkinter
import tempfile

#top = tkinter.Tk()
#top.mainloop()

def classavail(url):
    link = courseavail


    f = requests.get(link)
    unparsedLines = []
    unparsedLines = f.text.split(',')
    
    for item in unparsedLines:
        if("has_seats" in item):
            seatdata = item
            availability = seatdata.strip()[-2:-1]
            if (availability == '1'):
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
                   "Subject: Course Availability",
                   "",
                   text
                   ])
    server.sendmail("test.geromeyabut@gmail.com", "test.geromeyabut@gmail.com", msg)
    server.quit()

############################

School = input("Enter school code, i.e. COEN\n")
Number = input("Enter course code, i.e. 10\n")

course = School + " " + Number

"""courseavail = "https://www.scu.edu/apps/ws/courseavail/classes/3840/ugrad/COEN%20177" """

courseavail = "https://www.scu.edu/apps/ws/courseavail/classes/3840/ugrad/" + School + "%20" + str(Number)
print(courseavail)



while(1):
    if(classavail(courseavail) == 1):
        print("class is available\n")
        print("if class becomes unavailable, will notify\n")
        while( classavail(courseavail) == 1):
            if(classavail(courseavail)==0):
                text = "Class "+ course + " is now unavailable"
                sendMail(text)
                print(text)
                break

    if(classavail(courseavail) == 0):
        print("class is unavailable\n")
        print("If class becomes available, will notify\n")
        while(classavail(courseavail) == 0):
            if(classavail(courseavail)==1):
                text = "Class "+ course + " is now available"
                sendMail(text)
                print(text)
                break

