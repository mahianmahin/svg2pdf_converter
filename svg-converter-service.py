import json
import random

import cairosvg
from lxml import etree
import os 
from fontTools import ttLib


def svg_to_pdf():
	# reading the svg template
	with open('sample2.svg', 'rb') as file:
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
	# title = root.xpath('//*[@id="tspan48904"]')
	title = root.xpath('//*[@id="tspan7647"]')
	title[0].text = dict['text:title']

	# injecting data 
	# subtitle = root.xpath('//*[@id="tspan41145"]')
	subtitle = root.xpath('//*[@id="tspan41145"]')
	subtitle[0].text = dict['text:substitle']

	# injecting data 
	# student_id = root.xpath('//*[@id="tspan41149"]')
	student_id = root.xpath('//*[@id="tspan41149"]')
	student_id[0].text = dict['text:student-id']
	
	student_id = root.xpath('//*[@id="tspan41149-2"]')
	student_id[0].text = dict['text:student-id-2']

	description = root.xpath('//*[@id="text:instructions"]')

	# removing predefined template co-ordinates
	for item in description[0]:
		item.getparent().remove(item)

	count = 40
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
	
	# # setting up the font file
	title_box = root.xpath('//*[@id="text:title"]')
	# title_box[0].attrib['style'] = f"font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:8.46667px;line-height:1.25;font-family:'{fontFamilyName}';-inkscape-font-specification:'{fontFamilyName}';text-align:start;white-space:pre;shape-inside:url(#rect38943);display:inline"

	# checking if the title is too big 
	if len(dict['text:title']) >= 20:
		print(len(dict['text:title']))
		# reducing the font size
		previous_style = title_box[0].attrib['style']
		title_box[0].attrib['style'] = f"{previous_style}; font-size:4.46667px;"

	# converting the modified svg into pdf
	cairosvg.svg2pdf(bytestring=etree.tostring(root), write_to="output.pdf")

	print("\n[+] Conversion done!")



svg_to_pdf()

