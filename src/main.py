from copy_files import copy_files
from generate_page import generate_pages_recursive


dir_path_static = "./static"
dir_path_public = "./public"


def main():
    print("Copying static files to public directory...")
    copy_files(dir_path_static, dir_path_public)
    print("Generating pages...")
    generate_pages_recursive("./content", "./template.html", "./public")


main()
