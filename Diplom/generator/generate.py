import re
import os
import sys
# from PIL import Image

class Inserter(object):

  P = '<text:p text:style-name="Standard">^text^</text:p>'
  H1 = '<text:h text:style-name="Heading_20_1" text:outline-level="1">^section^ ^heading^</text:h>'
  H2 = '<text:h text:style-name="Heading_20_2" text:outline-level="2">^section^.^subsection^ ^heading^</text:h>'
  H3 = '<text:h text:style-name="Heading_20_3" text:outline-level="3">^section^.^subsection^.^subsubsection^ ^heading^</text:h>'
  IMG = '<text:p text:style-name="Drawing">\
    <draw:frame \
      draw:style-name="fr1" \
      draw:name="^name^" \
      text:anchor-type="as-char" \
      svg:width="90%"  \
      svg:height="^height^%"  \
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
  CODE = '<text:p text:style-name="P2">^code^</text:p>\
  <text:p text:style-name="Table">Листинг ^number^. ^name^</text:p>'
  TAB = '<text:tab/>'
  ENDL = '<text:line-break/>'

  img_cnt = 0
  tbl_cnt = 0
  h1_cnt = 0
  h2_cnt = 0
  h3_cnt = 0
  code_cnt = 0

  def __init__(self, filename):
    self.text = ''
    self.filename = filename
    self.index = open('index.tpl', 'r').read()

  def __del__(self):
    i = self._insert(self.index, {'insert':self.text})
    open(self.filename, 'w').write(i)

  def _insert(self, to, data):
    h = to
    for key,value in data.items():
      h1 = h.replace('^%s^' % key, str(value))
      h = h1

    return h

  def p(self, text):

    self.text += self._insert(self.P, {'text' : text})

  def img(self, name, url):
    # im = Image.open(url)
    # width, height = im.size
    # h = (height * 100) / (width * 1.5)
    h = 22
    self.img_cnt += 1
    abs_path = os.path.dirname(os.path.abspath(__file__))
    img_abs_path = '%s/%s' % (abs_path, name)
    self.text += self._insert(self.IMG, {'name':name.split('.')[0], 'number': self.img_cnt,  'url': img_abs_path, 'height': str(h)})

  def code(self, code = '', name = ''):
    code1 = code.replace('\n', self.ENDL).replace('\t', self.TAB)
    self.code_cnt += 1
    self.text += self._insert(self.CODE, dict(code=code1, number=number, name=name))

  def h0(self, heading):
    self.text += self._insert(self.H1, dict(section='', heading=heading))

  def h1(self, heading):
    self.h1_cnt += 1
    self.h2_cnt = 0
    self.h3_cnt = 0
    self.text += self._insert(self.H1, dict(section=self.h1_cnt, heading=heading))

  def h2(self, heading):
    self.h2_cnt += 1
    self.h3_cnt = 0
    self.text += self._insert(self.H2, dict(section=self.h1_cnt, subsection=self.h2_cnt, heading=heading))

  def h3(self, heading):
    self.h3_cnt += 1
    self.text += self._insert(self.H3, dict(section=self.h1_cnt, subsection=self.h2_cnt, subsubsection=self.h3_cnt, heading=heading))

def main():
  # index = open('index.tpl', 'r').read()
  # p1 = insert(p, {'text':'Привет, Даша!'})
  # img1 = insert(img, {'name': 'adfsdf sdf sd', 'url': 'sc.png', 'number': '1', })
  # code1 = insert(code, {'name': 'adfsdf', 'number': '1', 'code': 'def main(self):\n\ttest()'})
  # index1 = insert(index, {'insert': p1 + img1 + code1})

  lines = open(sys.argv[1], 'r').readlines()
  # print(lines)

  rimg = re.compile('\\[\\[(.*)\\]\\]')
  rhh0 = re.compile('\*\*(.*)\*\*')
  rhh1 = re.compile('==(.*)==')
  rhh2 = re.compile('===(.*)===')
  rhh3 = re.compile('====(.*)====')

  inserter = Inserter(filename=sys.argv[2])

  for x in lines:
    if '[[' in x:
      img_lnk = re.match(rimg, x).groups()[0].strip()
      inserter.img(img_lnk, img_lnk)
      # print('<figure><img style="width: 100%%" src="%s" /><figcaption>%s</figcaption></figure>' % (a,a))
    elif '====' in x:
      try:
        inserter.h3(re.match(rhh3, x).groups()[0].strip())
      except:
        print(x)
    elif '===' in x:
      inserter.h2(re.match(rhh2, x).groups()[0].strip())
    elif '==' in x:
      inserter.h1(re.match(rhh1, x).groups()[0].strip())
    elif '**' in x:
      inserter.h0(re.match(rhh0, x).groups()[0].strip())
    # elif '^$' in x:
      # inserter.code(code=, name=)   
    else:
      inserter.p(text=str(x))
  # inserter.code(code='class Привет():\n\ta = s', name='Code')
  # inserter.img(name='adfsdf sdf sd', url='sc.png', number='1')

if __name__ == '__main__':
  main()