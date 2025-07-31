import time
import configparser
import schedule

from button_handler import InkyButtonHandler
from image_handler import ImageHandler
from sensor_handler import SensorHandler
from display_handler import DisplayHandler


def main() -> None:
    print("[INFO] Setting things up...")

    config = configparser.ConfigParser()
    config.read('config.ini')

    change_interval: int = int(config.get('General', 'photo_change_interval_sec'))
    image_folder_path: str = config.get('General', 'image_folder_path')

    inky_image_handler = ImageHandler(image_folder=image_folder_path)
    inky_button_handler = InkyButtonHandler()
    inky_display_handler = DisplayHandler()
    inky_sensor_handler = SensorHandler()

    def update_display():
        print("[DEBUG] Updating image...")

        # Update temp/hum data:
        try:
            sensor_data = inky_sensor_handler.get_sample()
            hud_text = f"Temp: {sensor_data.temperature} °C\nHum: {sensor_data.humidity} %"
            inky_display_handler.set_hud_text(text=hud_text)
        except RuntimeError as e:
            print(f"[ERROR] RuntimeError: sensor - {e}")

        # Update image and HUD if active:
        inky_button_handler.disable_buttons()
        inky_display_handler.set_image(inky_image_handler.get_next())
        inky_display_handler.display.show() # Blocking until display not busy
        inky_button_handler.enable_buttons()

    update_display()

    schedule.every(change_interval).seconds.do(update_display)

    while True:

        schedule.run_pending()

        if inky_button_handler.is_event():
            button_event = inky_button_handler.get_event()
            inky_button_handler.clear_event_queue() # One event at a time
            
            print("[DEBUG] Button event: " +  button_event)
            
            # Next photo:
            if button_event == "A":
                print("[DEBUG] Moving to next image")
                update_display()

            # Re-shuffle:
            elif button_event == "B":
                print("[DEBUG] Re-shuffling images")
                inky_image_handler.shuffle()
                
            # TMP
            elif button_event == "C":
                pass

            # Toggle HUD:
            elif button_event == "D":
                inky_display_handler.toggle_hud()
                print(f"[DEBUG] Toggled hud_on={inky_display_handler.hud_on}")

        time.sleep(0.5)


if __name__ == "__main__":
    
    main()
 
