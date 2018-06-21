import re
# from PIL import Image

class Inserter(object):

  P = '<text:p text:style-name="Standard">^text^</text:p>'
  H1 = '<text:h text:style-name="Heading_20_1" text:outline-level="1">^section^ ^heading^</text:h>'
  H2 = '<text:h text:style-name="Heading_20_2" text:outline-level="2">^section^.^subsection^ ^heading^</text:h>'
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
      h1 = h.replace('^%s^' % key, value)
      h = h1

    return h

  def p(self, text):
    self.text += self._insert(self.P, {'text' : text})

  def img(self, name, url, number):
    # im = Image.open(url)
    # width, height = im.size
    # h = (height * 100) / (width * 1.5)
    h = 22
    self.text += self._insert(self.IMG, {'name':name, 'url':url, 'number':number, 'height': str(h)})

  def code(self, code = '', number = '1', name = ''):
    h = code.replace('\n', self.ENDL).replace('\t', self.TAB)
    self.text += self._insert(self.CODE, dict(code = h, number = number, name = name))

  def h1(self, **kwargs):
    self.text += self._insert(self.H1, kwargs)

  def h2(self, **kwargs):
    self.text += self._insert(self.H2, kwargs)

def main():
  # index = open('index.tpl', 'r').read()
  # p1 = insert(p, {'text':'Привет, Даша!'})
  # img1 = insert(img, {'name': 'adfsdf sdf sd', 'url': 'sc.png', 'number': '1', })
  # code1 = insert(code, {'name': 'adfsdf', 'number': '1', 'code': 'def main(self):\n\ttest()'})
  # index1 = insert(index, {'insert': p1 + img1 + code1})
  inserter = Inserter(filename='index1.fodt')
  inserter.p(text='Привет, Даша!')
  inserter.code(code='class Привет():\n\ta = s', number='1', name='Code')
  inserter.img(name='adfsdf sdf sd', url='sc.png', number='1')

if __name__ == '__main__':
  main()