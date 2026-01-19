from textnode import *
import os
import shutil
from markdown_to_html_node import markdown_to_html_node

def main():
    src = './static'
    dst = './public'
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)
    recursive(src, dst)
    generate_pages_recursive('content/', 'template.html', 'public/')

def recursive(src, dst):
    children = os.listdir(src)
    for child in children:
        if os.path.isfile(os.path.join(src, child)):
            shutil.copy(os.path.join(src, child), dst)
        else:
            if os.path.exists(os.path.join(dst, child)) == False:
                os.mkdir(os.path.join(dst, child))
            recursive(os.path.join(src, child), os.path.join(dst, child))
        
def extract_title(markdown):
    if markdown[0:2] != '# ':
        raise Exception("no title found")
    else:
        return markdown.split('\n')[0].strip('# ')

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as file:
        content = file.read()
    with open(template_path, 'r') as file:
        template = file.read()
    html_string = markdown_to_html_node(content).to_html()
    title = extract_title(content)
    result = template.replace('{{ Title }}', title)
    final_result = result.replace('{{ Content }}', html_string)
    directory = os.path.dirname(dest_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(dest_path, 'w') as file:
        file.write(final_result)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    old_files = os.listdir(dir_path_content)
    for file in old_files:
        if os.path.isfile(os.path.join(dir_path_content, file)):
            name, ext = os.path.splitext(file)        # e.g. "index.md" -> ("index", ".md")
            dest_path = os.path.join(dest_dir_path, name + ".html")
            generate_page(os.path.join(dir_path_content, file), template_path, dest_path)
        else:
            new_src_dir = os.path.join(dir_path_content, file)
            new_dest_dir = os.path.join(dest_dir_path, file)
            generate_pages_recursive(new_src_dir, template_path, new_dest_dir)


if __name__ == "__main__":
    main()