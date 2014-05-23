#!/usr/bin/env python
#-*- coding:utf-8 -*-
import requests
from lxml import etree
from datetime import datetime
import re
from sqlalchemy.exc import IntegrityError
from bangumi import app, db
from bangumi.models import Torrent


KTXP_RSS = 'http://bt.ktxp.com/rss-sort-1.xml'
MONTH_DICT = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
              'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
REG = r'<[^>]*>'


def pubdate_to_date(pubdate):
    splitted_pubdate = pubdate.split(' ')
    year = int(splitted_pubdate[3])
    month = MONTH_DICT[splitted_pubdate[2]]
    day = int(splitted_pubdate[1])
    [hour, minute, second] = [int(i) for i in splitted_pubdate[4].split(':')]
    return datetime(year, month, day, hour, minute, second)


def crawl_ktxp_rss():
    r = requests.get(KTXP_RSS)
    page = r.text
    page = page.encode(r.encoding)
    dom = etree.fromstring(page)
    items = dom.xpath('//item')
    for item in items:
        title = item.xpath('title')[0].text
        link = item.xpath('link')[0].text
        enclosure = item.xpath('enclosure/@url')[0]
        pubdate = pubdate_to_date(item.xpath('pubDate')[0].text)
        description = re.sub(REG, '', item.xpath('description')[0].text)
        torrent = Torrent(title=title, link=link, enclosure=enclosure, pub_date=pubdate, description=description)
        db.session.add(torrent)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            break
        except Exception as e:
            print e
            db.session.rollback()

if __name__ == '__main__':
    crawl_ktxp_rss()
    print 'Finished successfully!'