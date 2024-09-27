import os
from rembg import remove
from PIL import Image


class ImageProcessor:
    def __init__(self, input_path,back_path):
        self.input_path = input_path
        self.back_path = back_path
        self.img_name = input_path.split('/')[-1]
        self.output_dir =os.path.join("photo",'masked')
        self.original_dir =os.path.join("photo",'original')
        os.makedirs(self.original_dir, exist_ok=True)
        os.makedirs(self.output_dir, exist_ok=True)

    def process_image(self):
        img = Image.open(self.input_path)
        img.save(os.path.join(self.original_dir, self.img_name), format='jpeg')
        new_height = img.height / 2
        ratio = img.width / new_height
        new_width = int(new_height * ratio)
        img = img.resize((new_width, int(new_height)))
        output_path = os.path.join(self.output_dir, self.img_name)

        with open(output_path, 'wb') as f:
            input = open(os.path.join(self.original_dir, self.img_name), 'rb').read()
            subject = remove(input,
                             alpha_matting=True,
                             alpha_matting_background_threshold=500)
            f.write(subject)

        background_img = Image.open(self.back_path)
        background_img = background_img.resize((img.width, img.height))
        foreground_img = Image.open(output_path)
        background_img.paste(foreground_img, (0, 0), foreground_img)
        background_img.save(os.path.join(self.output_dir, 'background.jpg'), format='jpeg')


