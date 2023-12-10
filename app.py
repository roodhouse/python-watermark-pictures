from tkinter import *  # noqa: F403
import requests
import io
import random
from os import getenv
from dotenv import load_dotenv
from PIL import Image, ImageTk

load_dotenv()

UNSPLASH = getenv('UNSPLASH')

# get random image
response = requests.get(url=f'https://api.unsplash.com/photos/?client_id={UNSPLASH}')
response.raise_for_status()

data = response.json()

random_image = random.choice(data)

random_image_link = random_image['urls']['small']

print(random_image_link)

window = Tk()
window.title("Watermark")

# download image
image_data = requests.get(random_image_link).content
# create pil image object
pil_image = Image.open(io.BytesIO(image_data))

width, height = pil_image.size
canvas = Canvas(width=width, height=height)  # noqa: F405

print(f"Width: {width}, Height: {height}")
# convert pil image object to photoimage
tk_image = ImageTk.PhotoImage(pil_image)
# display on canvas
canvas.create_image(0, 0, anchor='nw', image=tk_image)
canvas.pack()

window.mainloop()