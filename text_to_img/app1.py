from googletrans import Translator
from pathlib import Path
import torch
from diffusers import StableDiffusionPipeline
from transformers import  pipeline , set_send
import matplotlib.pyplot as plt
from flask import Flask , jsonify, render_template,request
import os
import time

app = Flask(__name__)

def get_translation(text,dest_lang):
    translator = Translator()
    translated_text = translator.translate(text, dest=dest_lang)
    return translated_text.text

class CFG:
    seed:42
    if torch.cuda.is_available():
        device = "cuda"
        generator = torch.Generator(device).manual_seed(seed)

    else:
        device = "cpu" 
        generator = torch.Generator(device).manual_seed(seed)   
    
    image_gen_step = 35
    image_gen_model_id = "stabilityai/stable-diffusion-2"
    image_gen_size = (500,500)
    image_gen_guidance_scale = 9
    prompt_gen_model_id = "gpt3"
    prompt_dataset_size  = 6
    prompt_gen_max_length = 12


def get_model(hugging_token):
    image_gen_model = StableDiffusionPipeline.from_pretrained(
        CFG.image_gen_model_id,
        revision="fp16",use_auth_token = hugging_token,guidance_scale=9)

    image_gen_model = image_gen_model.to(CFG.device)
    return image_gen_model

def generate_image(prompt,model):
    image = model(
        prompt,num_inference_steps = CFG.image_gen_step,
        generator = CFG.generator,
        guidance_scale = CFG.image_gen_guidance_scale
    ).image[0]
    image = image.resize(CFG.image_gen_size)
    return image

@app.route("/")

def home():
    return render_template("index.html")


def save_image(image):
    save_folder = 'static'
    os.makedirs(save_folder,exist_ok=True)
    filename = generate_unique_filename()
    image_path = os.path.join(save_folder, filename)
    image.save(image_path)
    print("image saved at this path",image_path)
    return image_path

def generate_unique_filename():
    timestamp = str(int (time.time()))
    filename = f"image_{timestamp}.jpg"
    return filename

@app.route("/generate",methods=["POST"])
def generate():
    prompt = request.form.get('prompt')
    hugging_token = request.form.get('auth_token')
    print(prompt)
    Translation = get_translation(prompt,"en")
    print(Translation)
    img = generate_image(Translation,get_model(hugging_token))
    #save the image locally
    save_path = save_image(img)
    #create a Json response
    response={
        'prompt':prompt,
        'image_path':save_path
    }
    return jsonify(response)