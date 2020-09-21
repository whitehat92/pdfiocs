import pdfplumber
import sys
import re

file = sys.argv[1]

pdfdocument = pdfplumber.open(file)
c = range(len(pdfdocument.pages))
for x in c:
  pageObj = pdfdocument.pages[x]
  textpdf = pageObj.extract_text()
  hashes=re.findall(r'([a-fA-F\d]{32})', textpdf)
  urls=re.findall(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’])), textpdf)
  for hash in hashes:
    print(hash)
  for url in urls:
    print(url)
