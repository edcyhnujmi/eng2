#!python

import sys, codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

print("Content-Type: text/html")
print()
import cgi, os

form = cgi.FieldStorage()
listStrF = ''
currentPageE = ''
currentPageK = ''
currentPageEK = ''

if 'id' in form:
    pageId = form["id"].value
    if pageId == 'senEng':
        currentPageE = 'nav-item-current'
        senfileE = open('senEng', encoding='UTF8')
        listStr = senfileE.readlines()
        listStrF = ''
        for line in listStr:
            line = '<li>{sentences}</li>'.format(sentences=line)
            listStrF = listStrF + line
    elif pageId == 'senKor':
        currentPageK = 'nav-item-current'
        senfileK = open('senKor', encoding='UTF8')
        listStr = senfileK.readlines()
        listStrF = ''
        for line in listStr:
            line = '<li>{sentences}</li>'.format(sentences=line)
            listStrF = listStrF + line
    elif pageId == 'senEngKor':
        currentPageEK = 'nav-item-current'
        senK = open("senKor", encoding='UTF8')
        listStrK = senK.readlines()
        senK.close()

        listStrF = '\n'
        numSen = 468 #문장 개수에 따라 수정필요함!
        with open("senEng", encoding='UTF8') as fileE:
                for i, line in enumerate(fileE):
                    if i < numSen :
                        line = '<li>{sentences}</li>'.format(sentences=line)
                        listStrF = listStrF + line
                        listStrK2 = '<li class="noDots">{sentences}</li>'.format(sentences=listStrK[i])
                        listStrF = listStrF + listStrK2
                    else :
                        break

else:
    pageId = 'senEng'
    currentPageE = 'nav-item-current'
    senfileE = open('senEng', encoding='UTF8')
    listStr = senfileE.readlines()
    listStrF = ''
    for line in listStr:
        line = '<li>{sentences}</li>'.format(sentences=line)
        listStrF = listStrF + line

print('''<!doctype html>
<html>
<head>
    <title>{title}</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1, user-scalable=no" />
    <link href="sentencesStyle.css" rel="stylesheet" type="text/css" />
</head>
<body class="forMain">
    <div class="nav">
      <div class="nav-left-items" >
        <div class="nav-item {currentE}" onclick="location.href='sentences.py?id=senEng'" >eng</div>
        <div class="nav-item {currentK}" onclick="location.href='sentences.py?id=senKor'" >kor</div>
        <div class="nav-item {currentEK}" onclick="location.href='sentences.py?id=senEngKor'" >eng&kor</div>
      </div>
      <div class="nav-right-items">checkbox</div>

      <label class="switch">
        <input type="checkbox" onclick="PageMovement();">
        <span class="slider round"></span>
      </label>
    </div>
    <div class="text">
        <ul>
        {listStr}
        </ul>
    </div>
    <script src="sentences.js"></script>
</body>
</html>
'''.format(title=pageId, currentE=currentPageE, currentK=currentPageK, currentEK=currentPageEK, listStr=listStrF))
