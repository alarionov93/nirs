import re

p = '<text:p text:style-name="Standard">^text^</text:p>'
h1 = '<text:h text:style-name="Heading_20_1" text:outline-level="1">^section^ ^heading^</text:h>'
h2 = '<text:h text:style-name="Heading_20_2" text:outline-level="2">^section^.^subsection^ ^heading^</text:h>'
img = '<text:p text:style-name="Drawing">\
  <draw:frame \
    draw:style-name="fr1" \
    draw:name="^name^" \
    text:anchor-type="as-char" \
    svg:width="90%"  \
    draw:z-index="0">\
  <draw:image \
    xlink:href="^url^" \
    xlink:type="simple" \
    xlink:show="embed" \
    xlink:actuate="onLoad" \
    loext:mime-type="image/png"/>\
  </draw:frame>\
  <text:line-break/>Рисунок ^number^. ^name^ \
</text:p>'
code = '<text:p text:style-name="P2">^code^</text:p>\
<text:p text:style-name="Table">Листинг ^number^. ^text^</text:p>'

index = open('index.tpl', 'r').read()

def insert(to, data={}):
  for key,value in data.items():
     = to.replace('^%s^' % key, value)

  return to


