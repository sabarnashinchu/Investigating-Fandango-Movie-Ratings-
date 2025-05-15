import json
import re

def md_to_notebook(md_file, output_file):
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split the content into cells
    cells = []
    
    # Find all code blocks
    pattern = r'```python(.*?)```'
    code_blocks = re.findall(pattern, content, re.DOTALL)
    
    # Split the content by code blocks
    md_blocks = re.split(pattern, content, flags=re.DOTALL)
    
    # Create cells alternating between markdown and code
    for i, md_block in enumerate(md_blocks):
        if md_block.strip():  # If not empty
            cells.append({
                "cell_type": "markdown",
                "metadata": {},
                "source": md_block.strip().split('\n')
            })
        
        if i < len(code_blocks):  # If there's a code block following
            cells.append({
                "cell_type": "code",
                "metadata": {},
                "source": code_blocks[i].strip().split('\n'),
                "execution_count": None,
                "outputs": []
            })
    
    # Create notebook structure
    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.5"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    
    # Write the notebook to a file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1)
    
    print(f"Notebook created at {output_file}")

if __name__ == "__main__":
    md_to_notebook("notebook_content.txt", "Investigating_Fandango_Ratings.ipynb") 