import json
import random

import cairosvg
from lxml import etree


def svg_to_pdf():
	with open('sample.svg', 'rb') as file:
		svg_content = file.read()
		file.close()

	with open('sample.json', 'r') as json_file:
		json_data = json_file.read()
		json_file.close()

	dict = json.loads(json_data)

	root = etree.fromstring(svg_content)

	title = root.xpath('//*[@id="tspan48904"]')
	title[0].text = dict['text:title']

	subtitle = root.xpath('//*[@id="tspan41145"]')
	subtitle[0].text = dict['text:substitle']

	student_id = root.xpath('//*[@id="tspan41149"]')
	student_id[0].text = dict['text:student-id']

	description = root.xpath('//*[@id="text:instructions"]')

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
	
	print(etree.tostring(description[0]))
	
	title_box = root.xpath('//*[@id="text:title"]')
	title_box[0].attrib['style'] = "font-size:4; font-family:Montserrat"

	if dict['text:title'] >= 26:
		title_box[0].attrib['style'] = "font-size:5;"

	cairosvg.svg2pdf(bytestring=etree.tostring(root), write_to="output.pdf")

	print("[+] operation done")



svg_to_pdf()

