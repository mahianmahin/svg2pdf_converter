# svg2pdf


## Installation

To build the Container run

```bash
docker build -t <image_name> .
```


To generate the pdf into the Container
```bash
docker run --rm -it -v $(pwd):/app <image_name> python svg-converter-service.py
```


To run /bash the container
```bash
docker run --rm -it -v $(pwd):/app <image_name> /bin/bash
```

## Usage

>This software is written according to the given (sample.svg) svg template. It will not work with any other template.

>To use a custom font, just place a '.ttf' file at a time in the same directory as the script. The script will automatically install the font file and use it.

>Don't remove or rename 'sample.svg' or 'sample.json'file from the directory

>Just edit the json file's (sample.json) values for using different input.

>First, edit the 'sample.json' file according to your needs and then run the container. A pdf file named 'output.pdf' will be generated afterwards. If a pdf file already exists, it will be overwritten by the latest one.

>Don't change the key names of the json file

>Add the font files you want to use in the 'fonts' directory and it will get installed during docker image building 