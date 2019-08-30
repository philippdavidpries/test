from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')



import scraperwiki
html=scraperwiki.scrape("https://www.walderbach.de/fileadmin/user_upload/Wahl/index.html")
print("Clickonthe...morelinktoseethewholepage")


 
import lxml.html
root=lxml.html.fromstring(html) #turnourHTMLintoanlxmlobject

tds=root.cssselect("mitBorderBottom zweite_spalte links") #getallthe<tdtags
for td in tds:
#  print lxml.html.tostring(td) # the full HTML tag
 print td.text # just the text inside the HTML tag
 
