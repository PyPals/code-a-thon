from bs4 import BeautifulSoup as bs
import urllib2, sys

url = 'http://www.tradingeconomics.com/currencies'
try:
    html = urllib2.urlopen(url).read()
    soup = bs(html, 'html.parser')
except Exception as err:
    print('Error: ', err)
    sys.exit()

tables = soup.findAll('table')

for i in range (1, len(tables)):
    table = tables[i]
    rows = table.findAll('tr')
    for row in rows:
        tds = row.findAll('td')
        if len(tds) > 3:
            title = tds[1].text.strip()
            ttl = list(title)
            ttl.insert(3, '-')
            title = "".join(ttl)
            rate = tds[2].text.strip()
            print title, rate