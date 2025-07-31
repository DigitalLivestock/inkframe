from PIL import Image, ImageDraw
import os
import sys
import random

class ImageHandler:
    def __init__(self, image_folder: str) -> None:
        self.folder_path: str = image_folder
        self.image_area = (0, 0, 600, 488)
        self.image_size = (600, 448)
        self.image_names: list[str] = []
        self.current_image_index: int = 0
        self.max_image_index: int = 0

        # Setup images and order:
        try:
            self.image_names = os.listdir(self.folder_path)
        except FileNotFoundError as e: 
            print(f"[ERROR] Directory not found - {e}")
            sys.exit(0)
        
        self.max_image_index = len(self.image_names) - 1

        # Shuffle images:
        random.shuffle(self.image_names)


    def get_next(self) -> Image:
        try:
            self.current_image_index: int = (self.current_image_index + 1) % self.max_image_index
            current_image_name: str = self.image_names[self.current_image_index]
            
        except IndexError:
            print("[ERROR] IndexError: setting index to 0")
            self.current_image_index = 0

        image_path: str = self.folder_path + current_image_name
        return image_path

    def shuffle(self) -> None:
        random.shuffle(self.image_names)


if __name__ == "__main__":
    image_folder_path = "~/inkframe/src/images/"
    
    test_image_handler = ImageHandler(i_folder=image_folder_path)
