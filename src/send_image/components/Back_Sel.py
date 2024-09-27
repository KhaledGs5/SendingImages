import os
import tkinter as tk
from tkinter import Button
from PIL import Image, ImageTk
from tkinter import filedialog

# class BackgroundSelector:
#     def __init__(self):
#         #self.folder_path = folder_path
#         self.root = tk.Tk()
#         self.root.title("Select Background Image")

#         # Initialize Canvas to display images in the folder
#         self.canvas = tk.Canvas(self.root, width=400, height=400)
#         self.canvas.pack(side="left", fill="both", expand=True, padx=10, pady=10)

#         # Add Scrollbar for Canvas
#         scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
#         scrollbar.pack(side="right", fill="y")

#         # Configure Canvas to use Scrollbar
#         self.canvas.configure(yscrollcommand=scrollbar.set)

#            # Create a frame to contain the images
#         self.image_frame = tk.Frame(self.canvas)
#         self.canvas.create_window((0,0), window=self.image_frame, anchor="nw")

#         # Bind mousewheel scrolling to canvas
#         self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

#         # Populate the frame with image thumbnails
#         self.populate_images()

#         # Variable to store the index of the selected image
#         self.selected_index = None

#     def populate_images(self):
#         # Get image files in the current directory
#         self.image_files = []
#         try:
#             for file in os.listdir():
#                 if file.endswith(('.png', '.jpg')):
#                     #image = Image.open(os.path.join(self.folder_path, file))
#                     self.image_files.append(file)
#         except FileNotFoundError as e:
#             print(f"Error: {e}")
            
#         #self.image_files = [file for file in os.listdir(self.folder_path) if file.endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif"))]
#         for i, file in enumerate(self.image_files):
#             # Load image
#             path = os.path.normpath(file)
#             image = Image.open(path)
#             # Resize image thumbnail
#             image.thumbnail((200, 200))
#             # Convert image to PhotoImage
#             photo = ImageTk.PhotoImage(image)
#             # Add image to Canvas
#             label = tk.Label(self.image_frame, image=photo)
#             label.image = photo  # Keep reference to prevent garbage collection
#             label.bind("<Button-1>", lambda event, index=i: self.select_image(event, index))
#             label.pack(anchor="w", padx=5, pady=5)

#     def select_image(self, event, index):
#         # Reset border of previously selected image
#         if self.selected_index is not None:
#             label = self.image_frame.children[f"!label{self.selected_index}"]
#             label.config(borderwidth=0)
#         # Update border of clicked image
#         label = event.widget
#         label.config(borderwidth=2, relief="solid")
#         self.selected_index = index
#         # Close the window after selecting an image
#         self.root.destroy()

#     def get_selected_image_path(self):
#         if self.selected_index is not None:
#             selected_filename = self.image_files[self.selected_index]
#             selected_image_path = os.path.abspath(selected_filename)
#             return selected_image_path
#         else:
#             return None

class BackgroundSelector:
    def __init__(self) :
          self.root = tk.Tk()
          self.root.title("Select Background Image")
          
    #     # # Create a Button widget to trigger the file dialog
    #     # self.my_btn = Button(self.root, text="Select Background", command=self.open)
    #     # self.my_btn.pack()
          #self.open()
          
          

    def open(self):
        
        self.filename = filedialog.askopenfilename(initialdir=r"C:\Users\HP\OneDrive\Bureau\pythonProject\Sending_Images\photo\photo_back",
                                                       title='select file',
                                                       filetypes=(("png files","*.png"),("jpg files","*.jpg"),("all the files","*.*")))
        
        return self.filename  
    def destroy_app(self):
         self.root.destroy() 

