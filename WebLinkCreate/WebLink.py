import datetime
from selenium import webdriver
import bs4 as bs
import re
import smtplib
from os import sys, path


def create_log(_path, _searchText, _emailText, _count, _time, _urls):
    my_file = open(_path, "a")
    my_file.write(_searchText)
    my_file.write("URLs Searched: \n")
    for url in _urls:
        my_file.write(str(url)+"\n")

    # my_file.write("Found " + str(_count) + " Solicitations on " + str(_time) + "Link|" + i + "\n")
    my_file.write(_emailText)


def create_email(_text, _count, gmail_user, gmail_password, sent_from, to):
    """create and try to send email and create email_log_text"""
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    sys.path.append('C:\\Users\\Timothy\\Anaconda3\\lib\\site-packages\\IPython\\extensions')
    sys.path.append('C:\\Users\\Timothy\\.ipython')
    sys.path.append('C:\\Users\\Timothy')
    email_log_text = ''
    if _count != 0:
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, _text)
            server.close()
            email_log_text += 'Email Sent' + "\n"
        except:
            email_log_text += 'Something went wrong... Could not Send Email' + "\n"
    else:
        email_log_text += 'NO Email' + "\n"

    return email_log_text

def search_links(urlmin, time, _urls):
    """search provided urls and make links with urlmin and time stamp"""
    logtext = "Start Run on " + str(time) + "::\n"
    bodystr = ""
    urls = _urls
    totalCount = 0
    for i in urls:
        url = i
        browser = webdriver.Chrome("C:\\Users\\Timothy\\Documents\\GitHub\\webscraper2\\chromedriver.exe")
        browser.find_element_by_tag_name("body").send_keys("Keys.ESCAPE");
        browser.get(url)
        browser.implicitly_wait(2)
        try:
            myDynamicElement = browser.find_element_by_id("esbd-Results")
        except:
            print("no results")
        html_source = browser.page_source
        browser.quit()
        soup = bs.BeautifulSoup(html_source, 'html.parser')
        resulthtml = soup.find("div", {"id": "esbd-Results"})

        resulstsstr = str(resulthtml)
        if (resulstsstr != 'None'):
            results = resulthtml.get_text()
            res = [i.start() for i in re.finditer("window.open", resulstsstr)]
            searchstring2 = ';return false;'
            res1 = [i.start() for i in re.finditer(searchstring2, resulstsstr)]

            for x, y in zip(res, res1):
                resultlink = resulstsstr[x + 15:y - 2]
                logtext += (urlmin + resultlink + "\n")
                bodystr += (urlmin + resultlink + "\n")
            resultsCount = str(results).count("Solicitation ID:" + "\n")
            bodystr += str(resultsCount) + " Solicitations found for URL::" + str(url) + "\n"
        else:
            resultsCount = 0
        logtext += str(resultsCount) + " Solicitations found for URL::" + str(url) + "\n"

        totalCount += resultsCount
    return logtext, bodystr, totalCount

def mod_date():
    """get yesterday and current datetime"""
    time = datetime.datetime.now()-datetime.timedelta(1)
    year, month, day = str(datetime.datetime.date(time)).split("-")
    yday = str(int(day))
    if len(yday) == 1:
        yday = "0" + yday
    dayUse = str(month) + str(yday) + str(year)
    return dayUse, time


class UrlList:
    """create a list of urls from initial url, list of args with types"""
    def __init__(self, _urlmin, _lists, _type, _sDate):
        '''intialize'''
        self.urlLists = _lists
        self.urlmin = _urlmin
        self.types = _type
        self.sDate = _sDate
        self.retList = self.list_over()

    def __repr__(self):
        return str(self.retList)

    def __getitem__(self, item):
        return self.retList[item]

    def list_over(self):
        """run over list"""
        assert len(self.urlLists) == len(self.types)
        retList = []
        for l, m in zip(self.urlLists, self.types):
            tempList = self.parse_list(l, m)
            retList += tempList
        return retList

    def parse_list(self, _list, _type):
        """parse list"""
        outList = []
        if _type == "agency":
            for i in _list:
                oURL = self.create_url(self.urlmin, _agency=str(i), _startDate=self.sDate)
                outList.append(oURL)
        if _type == "nigp":
            for i in _list:
                oURL = self.create_url(self.urlmin, _nigp=str(i), _startDate=self.sDate)
                outList.append(oURL)
        return outList

    def create_url(self, _urlmin, _agency = "", _dateRange = "custom", _startDate = "", _endDate = "", _keySearch = "", _nigp = "", _status=1):
        """create url"""
        if _urlmin.endswith("/") or _urlmin.endswith("\\"):
            urlMin = _urlmin[:-1]
        else:
            urlMin = _urlmin
        if _agency != "":
            agency = "&agencyName=" + _agency
        else:
            agency = ""
        if _dateRange != "":
            dateRange = "&dateRange=" + _dateRange
        else:
            dateRange = ""
        if _startDate != "":
            startDate = "&startDate=" + _startDate
        else:
            startDate = ""
        if _endDate != "":
            endDate = "&endDate=" + _endDate
        else:
            endDate = ""
        if _keySearch != "":
            keySearch = "&keySearch=" + _keySearch
        else:
            keySearch = ""
        if _nigp != "":
            nigp = "&nigpClass=" + _nigp
        else:
            nigp = ""
        status = "&solStatus=1"
        urlFilter = "/esbd/filter=T" + agency + dateRange + startDate + endDate + keySearch + nigp + status
        url = urlMin + urlFilter
        return url
