import os


def install_fonts():
	# scanning for the font file in the root dir
	for root, dirs, files in os.walk('./fonts/', topdown=False):
		for name in files:
			if '.ttf' in name:
				os.system(f"install -m644 {name} /usr/share/fonts/")
				print(f"[+] Font {name} installed...")


install_fonts()
