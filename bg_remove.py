from io import BytesIO

import streamlit as st
from PIL import Image
from rembg import remove

from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
# from htbuilder.funcs import rgba, rgb


st.set_page_config(layout="wide", page_title="Image Background Remover")

st.write("## Conveniently remove backgrounds from your images!")
st.write(
    ":alien: Upload an image and watch as this AI magically removes the background. Full quality images can be downloaded from the sidebar on the left."
)
st.sidebar.write("## Upload and download :gear:")

# Create the columns
col1, col2 = st.columns(2)

# Download the fixed image


def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

# Package the transform into a function


def fix_image(upload):
    image = Image.open(upload)
    col1.write("Original Image :camera:")
    col1.image(image)

    fixed = remove(image)
    col2.write("Fixed Image :wrench:")
    col2.image(fixed)
    st.sidebar.markdown("\n")
    st.sidebar.download_button(
        "Download the fixed image", convert_image(
            fixed), "fixed.png", "image/png"
    )


# Create the file uploader
my_upload = st.sidebar.file_uploader(
    "Upload an image", type=["png", "jpg", "jpeg"])

# Fix the image!
if my_upload is not None:
    fix_image(upload=my_upload)
else:
    fix_image("./eagle.png")


# Footer
def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)


def layout(*args):

    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
    </style>
    """

    style_div = styles(
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        text_align="center",
        # height="60px",
        # opacity=0.6
    )

    style_hr = styles(
    )

    body = p()
    foot = div(style=style_div)(hr(style=style_hr), body)

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)
        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)


def footer():
    myargs = [
        "<b>Made with ❤ by</b> ",
        link("https://www.wmouton.vercel.app/", " WMouton"),
        br(),
    ]
    layout(*myargs)

# def footer():
#     myargs = [
#         "<b>Made with ❤ by</b> ",
#         link("https://www.wmouton.vercel.app/", " WMouton"),

#         " using: Python 3.10 ",
#         link("https://www.python.org/", image('https://i.imgur.com/ml09ccU.png',
#                                               width=px(18), height=px(18), margin="0em")),
#         ", Streamlit ",
#         link("https://streamlit.io/", image('https://streamlit.io/images/brand/streamlit-mark-color.svg',
#                                             width=px(24), height=px(25), margin="0em")),
#         br(),
#     ]
#     layout(*myargs)


if __name__ == "__main__":
    footer()
