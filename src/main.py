from copy_files import copy_files
from generate_page import generate_page


dir_path_static = "./static"
dir_path_public = "./public"


def main():
    print("Copying static files to public directory...")
    copy_files(dir_path_static, dir_path_public)
    generate_page("./content/index.md", "./template.html", "./public/index.html")


main()
