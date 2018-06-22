from random import randint
import re
import os
import sys


templates = [
	'Если автомат в момент t находится в состоянии "A", а входное воздействие равно "V", то следующее состояние будет равно "B".',
	'В момент времени t автомат перешел в состояние "A", и входное воздействие равно "V", то он перейдет в состояние "B".',
	'В момент времени t робот находится в состоянии "A", и при входном воздействии "V", он переходит в состояние "B".',
	'В момент t автомат пребывает в состоянии "A", и, получив воздействие "V", он перейдет в состояние "B".',
	'Если в момент времени t автомат находится в состоянии "A" при входном воздействии "V", то он перейдёт в состояние "B".',
  	'При пребывании автомата в состоянии "A" в момент времени t имея на входе воздействие "V", автомат сменит состояние на "B".',
]

def main():
	files = []
	for (dirpath, dirnames, filenames) in os.walk('temp/automat'):
	    files += filenames
	for f in files:
		lines = [ _.strip(" \n").strip(";") for _ in open('temp/automat/%s' % f).readlines() ]
		_tme = 0

		title = f.split('.')[0]
		img = f.split('.')[0] + ".png"
		print('\n\n== %s ==\n\n[[ %s ]]' % (title, img), file=sys.stderr)
		yield '== %s ==' % (title)
		yield '[[ %s ]]' % (img)
		n = 0
		y = ''
		for line in lines:
			try:
				_from, _to, _rel = [ _.strip() for _ in line.split(";") ]
			except ValueError:
				try:
					_from, _to = [ _.strip() for _ in line.split(";") ]
					_rel = '0'
				except ValueError:
					pass
			if _tme == 0:
				x = templates[0]
			else:
				x = templates[randint(0, len(templates))-1]
			y += x.replace('t', str(_tme)).replace('A', _from).replace('V', _rel).replace('B', _to)
			print(x, file=sys.stderr, end=' ')
			if n >= 3 and randint(1, 6) > 2:
				print(file=sys.stderr)
				yield y
				y = ''
				n = 0
			else:
				n += 1
			_tme += 1
		yield y
		print('\n',file=sys.stderr)


if __name__ == '__main__':
	rimg = re.compile('\\[\\[(.*)\\]\\]')
	rhh2 = re.compile('==(.*)==')
	for x in main():
		print(x)
		# if '[[' in x:
			# a = re.match(rimg, x).groups()[0].strip()
			# print('<figure><img style="width: 100%%" src="%s" /><figcaption>%s</figcaption></figure>' % (a,a))
		# elif '==' in x:
			# print('<h2>%s</h2>' % re.match(rhh2, x).groups()[0].strip())
		# else:
			# print('<p>%s</p>' % x)