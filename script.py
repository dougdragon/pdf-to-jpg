"""Generates a zip file containing jpg images of PDF files"""
import os
import shutil
from datetime import datetime
import pypdfium2 as pdfium


INPUT_DIR = 'input'
OUTPUT_DIR = 'output'
generated_jpg_files = []

def remove_image_files():
    """Remove the generated image files"""
    print('Removing generated image files')
    os.chdir(OUTPUT_DIR)
    files_list = os.listdir(os.getcwd())
    for filename in files_list:
        try:
            os.remove(filename)
        except Exception as e:
            print(f'Unable to remove "{filename}": {e}')
    print('Generated files removed.')

# Create a list of PDF file names in the input directory
input_directory = os.path.join(os.getcwd(), INPUT_DIR)
pdf_file_names = [
    f for f in os.listdir(input_directory) \
        if os.path.isfile(os.path.join(input_directory, f)) \
            and f.endswith('.pdf')
]
print(f'File names collected: {len(pdf_file_names)}')
print('Converting to JPG now...')
# Loop over the file names in the list generating a jpg file for each and saving
# them in the output directory
start_time = datetime.now()
for file_name in pdf_file_names:
    input_file_path = os.path.join(os.getcwd(), INPUT_DIR, file_name)
    output_file_name = f'{file_name.split(".pdf")[0]}'
    pdf = pdfium.PdfDocument(input_file_path)
    for i in range(len(pdf)):
        page = pdf[i]
        image = page.render().to_pil()
        image.save(
            os.path.join(
                os.getcwd(),
                OUTPUT_DIR,
                f'{output_file_name}_{i}.jpg'
            )
        )
        # Add the generated JPG file name to a list
        generated_jpg_files.append(output_file_name)
print('JPG files generated.')
try:
    print('Now adding to zip file...')
    zip_file_name = f'{datetime.now().strftime("%Y-%m-%d")}_pdf_to_jpg'
    shutil.make_archive(
        zip_file_name,
        'zip',
        os.path.join(os.getcwd(), OUTPUT_DIR)
    )
    print(f'Zip file created: {os.path.join(os.getcwd(), zip_file_name)}')
    remove_image_files()
except Exception as e:
    print(f'Error creating zip file: {e}')
finally:
    total_time_in_seconds = (datetime.now() - start_time).total_seconds()
    if total_time_in_seconds > 60:
        print(f'Total time: {datetime.now() - start_time}')
    else:
        print(f'Total seconds: {(datetime.now() - start_time).total_seconds()}')
