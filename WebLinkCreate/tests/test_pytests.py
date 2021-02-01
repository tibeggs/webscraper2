import pytest
import WebLinkCreate as wbc
import datetime


class TestUrls:
    def test_urlList(self):
        testlist = [[1, 2, 3]]
        testtypes = ["agency"]
        urls = wbc.UrlList("link/", testlist, testtypes, "10052020")
        assert urls[0] == "link/esbd/filter=T&agencyName=1&dateRange=custom&startDate=10052020&solStatus=1"

    def test_urlList_m(self):
        testlist = [[1, 2, 3], ["a","b","c"]]
        testtypes = ["agency", "nigp"]
        urls = wbc.UrlList("link/", testlist, testtypes, "10052020")
        assert urls[0] == "link/esbd/filter=T&agencyName=1&dateRange=custom&startDate=10052020&solStatus=1"
        assert urls[3] == "link/esbd/filter=T&dateRange=custom&startDate=10052020&nigpClass=a&solStatus=1"

    def test_modDate(self):
        day_made, full = wbc.mod_date()
        time = datetime.datetime.now()
        year, month, day = str(datetime.datetime.date(time)).split("-")
        yday = str(int(day) - 1)
        if len(yday) == 1:
            yday = "0" + yday
        dayUse = str(month) + str(yday) + str(year)
        assert dayUse == day_made

    @pytest.mark.server
    def test_url_search(self):
        text, body, count = wbc.search_links("http://www.txsmartbuy.com/", datetime.datetime.now(), ['http://www.txsmartbuy.com/esbd/filter=T&dateRange=custom&startDate=08012020&endDate=10012020&solStatus=1'])
        assert count == 50

    @pytest.mark.server
    def test_send_email(self):
        gmail_user = 'pyecono@gmail.com'
        gmail_password = open("password.secret", "r").read()
        sent_from = gmail_user
        to = ['tibeggs@gmail.com', 'tbeggs@econometricainc.com']
        subject = 'WebScrape Result for test:'
        body = "body"
        email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)
        out_text = wbc.create_email(email_text, 1, gmail_user, gmail_password, sent_from, to)
        assert out_text == "Email Sent\n"

    def test_true(self):
        assert True
