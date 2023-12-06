import tkinter as tk
import customtkinter as ctk 

from PIL import ImageTk
from authtoken import auth_token
from PIL import Image

import torch
from torch import autocast
from diffusers import StableDiffusionPipeline 
from transformers import CLIPImageProcessor

import torch
print(torch.cuda.is_available())
print(torch.version.cuda)


# Create the app
app = tk.Tk()
app.geometry("532x632")
app.title("Stable Bud") 
ctk.set_appearance_mode("dark") 

# prompt = ctk.CTkEntry(height=40, width=512, text_font=("Arial", 20), text_color="black", fg_color="white") 
prompt = ctk.CTkEntry(
    app,
    height=40,
    width=512,
    font=("Arial", 20),
    text_color="black",
    fg_color="white"
)
prompt.place(x=10, y=10)

# lmain = ctk.CTkLabel(height=512, width=512)
lmain = ctk.CTkLabel(app, height=512, width=512)
lmain.place(x=10, y=110)

modelid = "CompVis/stable-diffusion-v1-4"
device = "cuda"
# device = "cpu"
# pipe = StableDiffusionPipeline.from_pretrained(modelid, revision="fp16", torch_dtype=torch.float16, use_auth_token=auth_token)
pipe = StableDiffusionPipeline.from_pretrained(modelid, variant="fp16", torch_dtype=torch.float16, use_auth_token=auth_token) 

pipe.to(device) 

def generate1(): 
    with autocast(device): 
        image = pipe(prompt.get(), guidance_scale=8.5)["sample"][0]
    
    image.save('generatedimage.png')
    img = ImageTk.PhotoImage(image)
    lmain.configure(image=img) 

def generate(): 
    with autocast(device): 
        generated_image = pipe(prompt.get(), guidance_scale=8.5)["sample"][0]
    
    generated_image.save('generatedimage.png')
    
    img = ImageTk.PhotoImage(generated_image)
    
    lmain.configure(image=img)
    lmain.image = img

# trigger = ctk.CTkButton(height=40, width=120, text_font=("Arial", 20), text_color="white", fg_color="blue", command=generate) 
trigger = ctk.CTkButton(app,
    height=40, width=120,
    font=("Arial", 20),  # Set the font directly using 'font' argument
    text_color="white", fg_color="blue",
    command=generate
)
trigger.configure(text="Generate") 
trigger.place(x=206, y=60) 

app.mainloop()