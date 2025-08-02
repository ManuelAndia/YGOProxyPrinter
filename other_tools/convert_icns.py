#%% Imports
from PIL import Image
import os
import subprocess

#%% Parameters
app_name = "YGOProxyPrinter"
input_png = r"../img/logo-96.ico"
output_name = f"{app_name}.icns"

#%% Functions
def create_icns(input_png, output_icns):
    sizes = [
        (16, 16, "icon_16x16.png"),
        (32, 32, "icon_16x16@2x.png"),
        (32, 32, "icon_32x32.png"),
        (64, 64, "icon_32x32@2x.png"),
        (128, 128, "icon_128x128.png"),
        (256, 256, "icon_128x128@2x.png"),
        (256, 256, "icon_256x256.png"),
        (512, 512, "icon_256x256@2x.png"),
        (512, 512, "icon_512x512.png"),
        (1024, 1024, "icon_512x512@2x.png"),
    ]
    
    # Create iconset directory
    iconset_dir = f"{app_name}.iconset"
    os.makedirs(iconset_dir, exist_ok=True)
    
    # Generate all sizes
    img = Image.open(input_png)
    for w, h, name in sizes:
        resized = img.resize((w, h), Image.LANCZOS)
        resized.save(os.path.join(iconset_dir, name))
    
    # Convert to ICNS (requires WSL or Linux tools)
    try:
        subprocess.run(["png2icns", output_icns] + 
                      [os.path.join(iconset_dir, f) for f in os.listdir(iconset_dir)],
                      check=True)
        print(f"Successfully created {output_icns}")
    except FileNotFoundError:
        print("png2icns not found. Install icnsutils in WSL or use another method.")

#%% Do the work
if __name__=="__main__":
    create_icns(input_png, output_name)