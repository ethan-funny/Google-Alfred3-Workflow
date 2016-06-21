# -*- coding: utf-8 -*-
# 
# Copyright © 2016 ethan-funny (http://funhacks.net)
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2016-06-18
#


import socket
import urllib2
from re import match
from urllib import urlencode
from HTMLParser import HTMLParser

from PySocks import socks


class GoogleSearch:

    def __init__(self, query, port):

        self.query = query.encode('utf-8')
        self.url = u"http://www.google.com/search?" + urlencode({'q': self.query})
        self.header = 'Mozilla/5.001 (windows; U; NT4.0; en-US; rv:1.0) Gecko/25250101'
        self.SOCKS5_PROXY_HOST = '127.0.0.1' 
        self.SOCKS5_PROXY_PORT = port

    def get_html_source(self):
        html_source = ''

        try:
            if self.SOCKS5_PROXY_PORT == 0:
                request = urllib2.Request(self.url)
                request.add_header("User-Agent", self.header)
                html_source = urllib2.urlopen(request).read()
            else:
                socks.set_default_proxy(socks.SOCKS5, self.SOCKS5_PROXY_HOST, self.SOCKS5_PROXY_PORT)
                socket.socket = socks.socksocket
                request = urllib2.Request(self.url)
                request.add_header("User-Agent", self.header)
                html_source = urllib2.urlopen(request).read()
        except Exception as e:
            print e

        return html_source


class GoogleParser(HTMLParser):

    h3_flag = False
    a_flag = False
    b_flag = False
    title_part = ''

    def __init__(self):
        HTMLParser.__init__(self)
        self.result_info = []
        self.link = ''
        self.title = ''

    def handle_starttag(self, tag, attrs):
        if tag == 'h3' and attrs == [('class', 'r')]:
            self.h3_flag = True

        if tag == 'a' and self.h3_flag:
            self.a_flag = True

        if tag == 'b' and self.a_flag:
            self.b_flag = True

        if self.a_flag:
            for (key, value) in attrs:
                if key == 'href':
                    if value.startswith("/url?"):
                        m = match('/url\?(url|q)=(.+?)&', value)
                        if m and len(m.groups()) == 2:
                            href = urllib2.unquote(m.group(2))
                            self.link = href
                    else:
                        self.link = value

    def handle_endtag(self, tag):
        if tag == 'h3':
            self.h3_flag = False
        if tag == 'a' and self.a_flag:
            self.a_flag = False
            self.result_info.append({
                'title': self.title_part,
                'href': self.link
            })
            self.title_part = ''

    def handle_data(self, data):
        if self.a_flag:
            self.title_part += data


def search(query, port):
    google_search = GoogleSearch(query, port)
    page_source = google_search.get_html_source()

    google_parser = GoogleParser()
    google_parser.feed(page_source)
    google_parser.close()

    results = google_parser.result_info

    return results

if __name__ == '__main__':
    result_info = search('linux', 1234)
