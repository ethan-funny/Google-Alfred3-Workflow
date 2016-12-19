# -*- coding: utf-8 -*-
# 
# Copyright © 2016 ethan-funny (https://github.com/ethan-funny)
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2016-06-18
# Updated on 2016-12-19

import alfred
from alfred_google import gsearch


def process(query):
    """ Entry point
    :param query: query string
    :return:
    """
    if query:
        results = alfred_items_for_query(query)
        xml = alfred.xml(results)
        alfred.write(xml)


def alfred_items_for_query(query):
    index = 0
    alfred_results = []
    with open('port', 'r') as infile:
        port = int(infile.read())

    search_results = gsearch.search(query, port)
    for result in search_results:
        title = result.get('title', '').decode('utf-8')
        href = result.get('href', '').decode('utf-8')

        alfred_results.append(alfred.Item(
            title=title,
            subtitle=href,
            attributes={
                'uid': alfred.uid(index),
                'arg': title + ';' + href,
            },
            quicklookurl=href,
            icon='icon.png',
        ))

        index += 1

    return alfred_results


if __name__ == '__main__':
    try:
        query_str = ''.join(alfred.args())
    except:
        query_str = None

    process(query_str)
