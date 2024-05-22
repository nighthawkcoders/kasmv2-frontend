import os
from datetime import datetime
import shutil

# Define the directories
pdf_dir = 'pdfs'
documents_dir = '_documents'
base_url = '/kasmv2-frontend'  # Adjust this to your actual base URL

# Create the _documents directory if it doesn't exist
os.makedirs(documents_dir, exist_ok=True)

# Function to clean the _documents directory
def clean_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

# Clean the _documents directory
clean_directory(documents_dir)

# Loop through each PDF in the pdf_dir
for pdf_filename in os.listdir(pdf_dir):
    if pdf_filename.endswith('.pdf'):
        # Define the title and paths
        title_with_date = os.path.splitext(pdf_filename)[0]
        # Extract the date and title from the filename
        date_str, title = title_with_date[:10], title_with_date[11:]
        date = datetime.strptime(date_str, '%Y-%m-%d').strftime('%Y-%m-%d')

        pdf_path = f"{base_url}/{pdf_dir}/{pdf_filename}"
        markdown_filename = os.path.join(documents_dir, f'{title}.md')

        # Create the content for the Markdown file
        content = f"""---
layout: document
title: "{title}"
pdf: "{pdf_path}"
date: {date}
---

<embed src="{{{{ page.pdf }}}}" width="100%" height="600px" type="application/pdf">
"""

        # Write the content to the Markdown file
        with open(markdown_filename, 'w') as f:
            f.write(content)

        print(f'Created {markdown_filename}')
