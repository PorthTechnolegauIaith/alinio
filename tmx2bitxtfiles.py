import codecs
from lxml import etree 
from xml.etree import ElementTree as ET
from argparse import ArgumentParser

def convert(source_file, file_en, file_cy):

	tree=etree.parse(source_file)
	tus=tree.xpath('//tu')

	print (len(tus))

	focy = codecs.open(file_cy, "w", "utf8")
	foen = codecs.open(file_en, "w", "utf8")

	for tu in tus:
	#	print (ET.tostring(tu))

		segs=tu.xpath('.//tuv/seg/text()')
	
		if (len(segs) == 2):

			en = segs[0].replace('\n','').replace('\r','')
			cy = segs[1].replace('\n','').replace('\r','')
		
			if ( len(en)>1 and len(cy) > 1):	

				print (en)

				foen.write("\n" + en)
				focy.write("\n" + cy)

	focy.close()
	foen.close()


if __name__ == '__main__':

	parser = ArgumentParser(description="Trosi ffeiliau TMX i ddwy ffeil")

	parser.add_argument('-s', '--source-tmx', dest="source_file", required=True, help="Ffeil testun Saesneg")
	parser.add_argument('-e', '--english', dest="file_en", required=True, help="Ffeil testun Saesneg")
	parser.add_argument('-c', '--cymraeg', dest='file_cy', required=True, help="Ffeil testun Cymraeg")

	#args = parser.parse_args()
	args = vars(parser.parse_args())

	try:
		#args.func(**vars(args))
		convert(args['source_file'], args['file_en'], args['file_cy'])
	except Exception as e:
		print(e)

