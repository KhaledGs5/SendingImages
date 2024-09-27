from src.send_image.components.Back_Sel import BackgroundSelector
from src.send_image.components.image_process import ImageProcessor
from src.send_image.components.send import Send_Email
from src.send_image.components.user_interface import UserInterface
from text_to_img.app import TextToImageApp
from tkinter import messagebox
import time


class SendPipeline:
    def __init__(self,file_path):
        #self.folder_path = folder_path
        self.file_path = file_path

    def main(self):
        answer = messagebox.askyesno("Confirmation", "Would you like to proceed with TextToImage?")
        if answer :
            app = TextToImageApp()
            app.mainloop()
            time.sleep(1)
           
        selector = BackgroundSelector()
        selected_image_path = selector.open()
        selector.destroy_app()
        processor = ImageProcessor(self.file_path,selected_image_path)
        processor.process_image()
        email_interface = UserInterface()
        email_interface.mainloop()
        email_to = email_interface.email_to
        send_email = Send_Email(email_to)
        send_email.send_email()
