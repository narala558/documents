# sname, cName, sym, ltp, dpname,
# coimax -> (strkprc, coi, coichgp),
# coichgp -> (strkprc, coi, coichgp),
# poimax -> (strkprc, poi, poichgp)
# poichp -> (strkprc, poi, poichgp)

import collections
import os.path
import pickle
import time

import requests


def get_stocks():
    fname = 'all.pkl'
    data = read_pickle(fname)
    if data:
        return data
    url = 'https://emt.edelweiss.in/emt-services/WatchList/GetGuestSymbols/1.0.1'
    data = '{"request":{"appID":"3353982b04323a3fad1287677da6a2db","requestType":"U","formFactor":"M","data":{"syLst":[],"wID":"-NFO"}}}'
    time.sleep(5)
    data = requests.get(url, data=data)
    data = data.json()
    write_pickle(fname, data)
    return data


def read_pickle(fname):
    if not os.path.exists(fname):
        return
    with open(fname, 'rb') as fh:
        data = pickle.load(fh)
    write_pickle(fname, data)
    return data


def write_pickle(fname, data):
    with open(fname, 'wb') as fh:
        pickle.dump(data, fh, protocol=2)


def get_stock_info(sname):
    fname = '{}.pkl'.format(sname)
    data = read_pickle(fname)
    if data:
        return data
    url = 'https://emt.edelweiss.in/emt-services/Market/OptionChainGuest/1.0.1'
    data = '{"request":{"appID":"3353982b04323a3fad1287677da6a2db","requestType":"U","formFactor":"M","data":{"aTyp":"OPTSTK","exp":"29 Jun 2017","uSym":"%s"}}}' % sname
    data = requests.get(url, data=data)
    data = data.json()
    write_pickle(fname, data)
    return data


def get_value(row, key):
    if key == 'cOIchgP':
        coi = float(row['cOI'])
        cchgoi = float(row['cChgOI'])
        if coi == cchgoi:
            value = coi * 100
        else:
            value = cchgoi / (coi - cchgoi)

    elif key == 'pOIchgP':
        coi = float(row['pOI'])
        cchgoi = float(row['pChgOI'])
        if coi == cchgoi:
            value = coi * 100
        else:
            value = cchgoi / (coi - cchgoi)

    else:
        value = float(row[key])

    return value


def get_max(data, key):
    m = None
    rdata = None
    for row in data:
        value = get_value(row, key)
        if not m or m < value:
            m = value
            rdata = row
        elif m == value:
            if key == 'cOIchgP':
                p_coi = rdata['cOI']
                if p_coi < row['cOI']:
                    rdata = row
            elif key == 'pOIchgP':
                p_poi = rdata['pOI']
                if p_poi < row['pOI']:
                    rdata = row

    if not rdata:
        rdata = collections.defaultdict(dict)
    return rdata


col = (
    'sname',
    'cm_stkprc', 'cm_coi',
    'cpm_stkprc', 'cpm_coi',
)
print(col)


stocks = get_stocks()
# print(stocks)
stocks = stocks['response']['data']['wlSym']

for stock in stocks:
    sname = stock['sName']
    cname = stock['cName']
    sym = stock['sym']
    dpname = stock['dpName']
    ltp = stock['ltp']

    try:
        data = get_stock_info(sname)
        data = data['response']['data']['opChn']
    except KeyError:
        continue

    info = get_max(data, key='cOI')
    cm_stkprc = info['stkPrc']
    cm_coi = info['cOI']

    info = get_max(data, key='cChgOI')
    cpm_stkprc = info['stkPrc']
    cpm_coi = info['cOI']

    info = get_max(data, key='pOI')
    pm_stkprc = info['stkPrc']
    pm_poi = info['pOI']

    info = get_max(data, key='pChgOI')
    ppm_stkprc = info['stkPrc']
    ppm_poi = info['pOI']

    print(
        sname,
        cm_stkprc, cm_coi,
        cpm_stkprc, cpm_coi,
        pm_stkprc, pm_poi,
        ppm_stkprc, ppm_poi,
    )

    # print(coi)
    # print(info)

# def get_max(data, ):


# coimax = get_max(data, key='coimax')


# data = requests.get()
