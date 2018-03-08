#coding:utf-8
from __future__ import print_function, unicode_literals

import sys
import os
import re

from workflow import Workflow
from workflow.notify import notify

log = None

def main(wf):
    query = sys.argv[1]
    log.info(query)

    handle(query)

def handle(query):
    query = unicode(query, 'utf-8')

    validQuery = False
    for rule in RULES:
        if re.match(rule, query) is not None:
            validQuery = True
            break
    if not validQuery:
        notify('Error', query + ' is not a valid configuration!')
        return

    query.replace(r'\s+', ' ')
    kvPair = query.split(' ')

    key = kvPair[0]
    val = kvPair[1]

    wf.store_data(key, val)
    notify('Set Configuration Successfully', 'Set ' + key + " to " + val + " complete!")

if __name__ == '__main__':
    wf = Workflow()
    log = wf.logger
    sys.exit(wf.run(main))