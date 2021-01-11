# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import WebLinkCreate as wbc
from os import sys, path

def run_scrapper():
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    sys.path.append('C:\\Users\\Timothy\\Anaconda3\\lib\\site-packages\\IPython\\extensions')
    sys.path.append('C:\\Users\\Timothy\\.ipython')
    sys.path.append('C:\\Users\\Timothy')

    agencyList = [7547, 8164, 7877, 7857, 7957, 8247]
    nigpList = [91812, 91821, 91827, 91849, 91863, 91875, 91878, 91892, 91896, 94677, 96121, 96128]
    selectionList = [agencyList, nigpList]
    typesList = ["agency", "nigp"]
    minUrl = "http://www.txsmartbuy.com/"
    day_made, full = wbc.mod_date()
    urls = wbc.UrlList(minUrl, selectionList, typesList, day_made)
    text, emailbody, count = wbc.search_links(minUrl, full, urls)
    gmail_user = 'pyecono@gmail.com'
    gmail_password = 'Econo2020!'
    sent_from = gmail_user
    to = ['tibeggs@gmail.com', 'tbeggs@econometricainc.com', 'cholleyman@econometricainc.com',
          'iflores@econometricainc.com']
    subject = 'WebScrape Result for test ' + str(full)
    body = emailbody
    email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)
    out_text = wbc.create_email(email_text, count, gmail_user, gmail_password, sent_from, to)

    wbc.create_log("Log.txt", text, out_text, count, full, urls)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_scrapper()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
