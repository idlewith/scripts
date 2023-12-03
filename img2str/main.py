import base64
import os
from html_utils import Html


def gen_image_html_full(index, image_name, image_content):
    string = f""" <h1>{image_name}</h1>
    <div id="{index}">
    
        <img class="clickable-image" 
        src="data:image/png;base64,{image_content}" 
        alt="Click me to fullscreen" onclick="showFullscreen(this.src)">
    
    </div>
    """
    return string


def image_to_text(file_path: str) -> str:
    with open(file_path, "rb") as image_file:
        encoded_image: bytes = base64.b64encode(image_file.read())
        encoded_image_str: str = encoded_image.decode("utf-8")
    return encoded_image_str


def get_image_files():
    folder = "images"
    filenames = os.listdir(folder)

    image_name_path_dict = {}
    dot = "."
    for index, filename in enumerate(filenames):
        filename_no_suffix = f"{index + 1}. filename"
        if dot in filename:
            filename_no_suffix = f"{index + 1}. {filename.split(dot)[0]}"

        image_path = os.path.join(folder, filename)
        image_name_path_dict.setdefault(filename_no_suffix, image_path)

    return image_name_path_dict


def gen_menu(index, filename):
    string = f"""
        <li><a href="#{index}" onclick="closeMenu()">{filename}</a></li>
    """
    return string


def main():
    image_name_path_dict = get_image_files()

    image_html_list = []
    menus = []
    for index, filename_image_path in enumerate(image_name_path_dict.items()):
        index = index + 1

        filename, image_path = filename_image_path
        encoded_text = image_to_text(image_path)

        menu = gen_menu(index, filename)
        menus.append(menu)

        image_html = gen_image_html_full(index, filename, encoded_text)
        image_html_list.append(image_html)

    html = Html()
    html_str = "".join(
        [
            html.prefix,
            "".join(menus),
            html.medium,
            "".join(image_html_list),
            html.suffix,
        ]
    )

    with open("img2str.html", "w", encoding="utf-8") as f:
        f.write(html_str)


if __name__ == "__main__":
    main()
