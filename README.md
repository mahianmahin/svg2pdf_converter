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
docker run --rm -it -v $(pwd):/app <image_name> python svg-converter-service.py
```
