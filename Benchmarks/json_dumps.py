import json
import sys

import six
from six.moves import xrange
import timeit


EMPTY = ({}, 2000)
SIMPLE_DATA = {'key1': 0, 'key2': True, 'key3': 'value', 'key4': 'foo',
               'key5': 'string'}
SIMPLE = (SIMPLE_DATA, 1000)
NESTED_DATA = {'key1': 0, 'key2': SIMPLE[0], 'key3': 'value', 'key4': SIMPLE[0],
               'key5': SIMPLE[0], six.u('key'): six.u('\u0105\u0107\u017c')}
NESTED = (NESTED_DATA, 1000)
HUGE = ([NESTED[0]] * 1000, 1)

CASES = ['EMPTY', 'SIMPLE', 'NESTED', 'HUGE']


def bench_json_dumps(data):
    for obj, count_it in data:
        for _ in count_it:
            json.dumps(obj)


def bench():
    cs=', '.join(CASES)
    if cs:
        cases = []
        for case in cs.split(','):
            case = case.strip()
            if case:
                cases.append(case)
        if not cases:
            print("ERROR: empty list of cases")
            sys.exit(1)
    else:
        cases = CASES

    data = []
    for case in cases:
        obj, count = globals()[case]
        data.append((obj, xrange(count)))

    bench_json_dumps(data)

def time():
    t=timeit.timeit(bench,number=350)
    return t
