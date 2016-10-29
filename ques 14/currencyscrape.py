from bs4 import BeautifulSoup as bs
import urllib2, sys

from flask import Flask, render_template, redirect, request, jsonify

url = 'http://www.tradingeconomics.com/currencies'

def scrape():
    print "Please wait while it scrapes"
    try:
        html = urllib2.urlopen(url).read()
        soup = bs(html, 'html.parser')
    except Exception as err:
        print('Error: ', err)
        sys.exit()

    tables = soup.findAll('table')
    currs = []
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
                currs.append({'title':title, 'rate':rate})
                # print title, rate
    return currs

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('curr.html', details = scrape())

if __name__ == '__main__':
    app.run(port = 3000)