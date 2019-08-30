import scraperwiki
html=scraperwiki.scrape("http://inmo.ie/6022")
print("Clickonthe...morelinktoseethewholepage")


 
importlxml.html
root=lxml.html.fromstring(html) #turnourHTMLintoanlxmlobject

tds=root.cssselect('td') #getallthe<tdtags
fortdintds:
print lxml.html.tostring(td) # the full HTML tag
print td.text # just the text inside the HTML tag


