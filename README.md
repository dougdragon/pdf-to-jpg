# PDF to JPG
This script converts PDF files to JPG images. If the PDF file(s) contain more than 1 page, an image will be created for each page.

The script uses the following packages:
- [pypdfium2==4.30.0](https://github.com/pypdfium2-team/pypdfium2/tree/4.30.0)
- [pillow==10.4.0](https://github.com/python-pillow/Pillow/tree/10.4.0)

## To install dependencies
```bash
pip install -r requirements.txt
```

## To run
1. Place PDF files into the `input` directory
2. Run **script.py**:
    ```bash
    python3 script.py
    ```
3. The script will convert the PDF files to JPG images and create a ZIP file containing all the images
