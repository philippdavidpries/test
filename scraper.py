import scraperwiki
html=scraperwiki.scrape("http://inmo.ie/6022")
print("Clickonthe...morelinktoseethewholepage")


 
import lxml.html
root=lxml.html.fromstring(html) #turnourHTMLintoanlxmlobject

tds=root.cssselect("td") #getallthe<tdtags
for td in tds:
#  print lxml.html.tostring(td) # the full HTML tag
 print td.text # just the text inside the HTML tag


