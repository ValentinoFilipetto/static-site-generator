import os
from extract_markdown import extract_title
from markdown_to_html_node import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    print(f"Generating text {from_path} to {dest_path} using {template_path}")

    markdown_file = open(from_path)
    markdown = markdown_file.read()

    template_file = open(template_path)
    template = template_file.read()

    html_node = markdown_to_html_node(markdown)
    html_string = html_node.to_html()

    title = extract_title(markdown)

    rendered_html = template.replace("{{ Title }}", title).replace(
        "{{ Content }}", html_string
    )

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(rendered_html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for item in os.listdir(dir_path_content):
        if os.path.isfile(dir_path_content + f"/{item}"):
            generate_page(
                dir_path_content + f"/{item}",
                template_path,
                dest_dir_path + "/index.html",
            )
        else:
            generate_pages_recursive(
                dir_path_content + f"/{item}", template_path, dest_dir_path + f"/{item}"
            )
