

import customtkinter as ctk 
import tkinter as tk
import requests
import io
import os
from PIL import Image, ImageTk
import shutil
import time
import base64

class TextToImageApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("532x632")
        self.title("Text to Image App")
        self.configure(bg='black')
        ctk.set_appearance_mode("dark") 

        # Create input box on the user interface 
        self.prompt = tk.Entry(self,width=512, font=("Arial", 15), fg="white", bg="black") 
        
        
        img = "generatedimage.jpg"
        # Create a placeholder to show the generated image
        self.img_placeholder = tk.Label(self, height=512, width=512, text="")
        
        
        # Create a button to trigger image generation
        self.generate_button = ctk.CTkButton(self,height=40, width=120,
                                              text_font=("Arial", 15), text_color="black",
                                                fg_color="white",text="Generate", command=self.generate)
        

        # Create a button to destroy the application
        self.destroy_button = ctk.CTkButton(self,height=40, width=120,
                                              text_font=("Arial", 15), text_color="black",
                                                fg_color="white",text="Finish", command=self.destroy_app)
        
        self.prompt.pack(pady=10)

        self.generate_button.pack(pady=10)

        self.destroy_button.pack(pady=10)

        self.img_placeholder.pack(pady=10)

        # Initialize API URL and headers
        self.API_URL = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"
        self.headers = {"Authorization": "Bearer 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"}

    def query(self, payload):
        response = requests.post(self.API_URL, headers=self.headers, json=payload)
        return response.content

    def generate(self):
        try:
            # Set the path for the generated image
            self.generated_image_path = "generatedimage.jpg"
        
            # Query for the image bytes
            payload = {"inputs": self.prompt.get()}
            image_bytes = self.query(payload)
            
            # Convert the image bytes to a PIL Image object
            image = Image.open(io.BytesIO(image_bytes))
            
            # Save the generated image
            image.save(self.generated_image_path)
            
            # Convert the PIL Image to a Tkinter PhotoImage
            self.img = ImageTk.PhotoImage(image)
            
            # Configure the image placeholder to display the generated image
            self.img_placeholder.configure(image=self.img)
            self.update_idletasks()
        except Exception as e:
        # Log any errors that occur
            print("Error:", e)
    def generate_unique_filename(self):
        self.timestamp = str(int (time.time()))
        filename = f"image_{self.timestamp}.jpg"
        return filename
    def destroy_app(self):
        # Check if image has been generated
        if self.generated_image_path is not None:
            # Move the generated image to the specified folder
            #save_folder = r"C:\Users\HP\OneDrive\Bureau\pythonProject\Sending_Images\photo_back" 
            save_folder = r"C:\Users\HP\OneDrive\Bureau\pythonProject\Sending_Images\photo\photo_back" # Replace with actual path
            os.makedirs(save_folder, exist_ok=True)
            filename = self.generate_unique_filename()
            save_path = os.path.join(save_folder, filename)
            shutil.move(self.generated_image_path, save_path)
            print("Image saved to:", save_path)
        else:
            print("No image generated")

        self.destroy()



