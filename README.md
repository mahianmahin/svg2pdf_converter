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

>This software depends on the given svg template. It will not work with any other template. 

>To use a custom font, just place a '.ttf' file in the same directory as the script. The script will automatically install the font file and use it.

>Don't remove or rename 'sample.svg' or 'sample.json'file from the directory

>Just edit the json file's values for using different data