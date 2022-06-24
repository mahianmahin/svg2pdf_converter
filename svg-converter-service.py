import json
import random

import cairosvg
from lxml import etree
import os 
from fontTools import ttLib


def svg_to_pdf():
	# scanning for the font file in the root dir
	for root, dirs, files in os.walk('./', topdown=False):
		for name in files:
			if '.ttf' in name:
				font = ttLib.TTFont(name)
				fontFamilyName = font['name'].getDebugName(1)

	# reading the svg template
	with open('sample.svg', 'rb') as file:
		svg_content = file.read()
		file.close()

	# reading the json file
	with open('sample.json', 'r') as json_file:
		json_data = json_file.read()
		json_file.close()

	dict = json.loads(json_data)

	# parsing the xml file for further operations
	root = etree.fromstring(svg_content)

	# injecting data 
	title = root.xpath('//*[@id="tspan48904"]')
	title[0].text = dict['text:title']

	# injecting data 
	subtitle = root.xpath('//*[@id="tspan41145"]')
	subtitle[0].text = dict['text:substitle']

	# injecting data 
	student_id = root.xpath('//*[@id="tspan41149"]')
	student_id[0].text = dict['text:student-id']

	description = root.xpath('//*[@id="text:instructions"]')

	# removing predefined template co-ordinates
	for item in description[0]:
		item.getparent().remove(item)

	count = 55
	split_string = [dict['text:instructions'][i:i+count] for i in range(0, len(dict['text:instructions']), count)]

	y_value = 136

	for item in split_string:
		random_id = "tspan" + str(random.randint(0000, 9999))
		tspan = etree.SubElement(description[0], "tspan")
		tspan.text = item
		tspan.set("id", random_id)
		tspan.set("x", "49")
		tspan.set("y", str(y_value))
		y_value = y_value + 6
	
	# setting up the font file
	title_box = root.xpath('//*[@id="text:title"]')
	title_box[0].attrib['style'] = f"font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:8.46667px;line-height:1.25;font-family:'{fontFamilyName}';-inkscape-font-specification:'{fontFamilyName}';text-align:start;white-space:pre;shape-inside:url(#rect38943);display:inline"
	
	# setting up the font file
	subtitle_box = root.xpath('//*[@id="tspan41145"]')
	subtitle_box[0].attrib['style'] = f"font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:4.46667px;line-height:1.25;font-family:'{fontFamilyName}';-inkscape-font-specification:'{fontFamilyName}';text-align:start;white-space:pre;shape-inside:url(#rect38943);display:inline"

	# setting up the font file
	id_box = root.xpath('//*[@id="text:student-id"]')
	id_box[0].attrib['style'] = f"font-size:4.9389px;line-height:1.25;font-family:'{fontFamilyName}';text-align:start;text-anchor:start;stroke-width:0.264583;-inkscape-font-specification:'{fontFamilyName}';font-weight:normal;font-style:normal;font-stretch:normal;font-variant:normal"
	
	# setting up the font file
	instructions_box = root.xpath('//*[@id="text:instructions"]')
	instructions_box[0].attrib['style'] = f"font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:4.9389px;line-height:1.25;font-family:'{fontFamilyName}';-inkscape-font-specification:'{fontFamilyName}';text-align:start;white-space:pre;shape-inside:url(#rect46297);display:inline;stroke-width:0.264583"

	# checking if the title is too big 
	if len(dict['text:title']) >= 26:
		# reducing the font size
		title_box[0].attrib['style'] = f"font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:4.46667px;line-height:1.25;font-family:'{fontFamilyName}';-inkscape-font-specification:'{fontFamilyName}';text-align:start;white-space:pre;shape-inside:url(#rect38943);display:inline"

	# converting the modified svg into pdf
	cairosvg.svg2pdf(bytestring=etree.tostring(root), write_to="output.pdf")

	print("[+] operation done")



svg_to_pdf()

