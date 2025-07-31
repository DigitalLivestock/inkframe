from inky.auto import auto
from PIL import Image, ImageDraw

from sensor_handler import SensorHandler

class DisplayHandler:
    def __init__(self):
        self.display = auto()
        self.draw = None
        self.current_image: Image
        self.current_hud = None
        self.hud_on = True
        self.hud_text: str = ""

    def toggle_hud(self):
        self.hud_on = not self.hud_on

    def set_hud_text(self, text: str):
        self.hud_text = text

    def set_hud(self):
        pos_size = (self.display.resolution[0] - 110, self.display.resolution[1] - 45, self.display.resolution[0], self.display.resolution[1])
        self.draw.rectangle(pos_size, fill="white", outline=None, width=1)

        self.draw.multiline_text(
            xy = (pos_size[0] + 5, pos_size[1] + 5), 
            text=self.hud_text,
            fill="black",
            font=None, 
            anchor='la', 
            spacing=4, 
            align='left', 
            direction=None, 
            features=None,
            language=None, 
            stroke_width=0, 
            stroke_fill=None, 
            embedded_color=False,
            font_size=14
        )

    def set_image(self, image_path: str):
        
        try:
            with Image.open(image_path) as image:
                self.current_image = image.resize(self.display.resolution)
                self.draw = ImageDraw.Draw(self.current_image)
                if self.hud_on:
                    self.set_hud()
                
                self.display.set_image(self.current_image)

        except FileNotFoundError:
            print(f"[ERROR] The image file at {image_path} was not found.")
        except Exception as e:
            print(f"[ERROR] An error occurred: {e}")