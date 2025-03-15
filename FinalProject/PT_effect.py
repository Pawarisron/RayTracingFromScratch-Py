#Photo Effect
from PIL import Image
import numpy as np
import random

def add_grain(image_path, output_path, intensity=0.2):
    # Open Image
    image = Image.open(image_path)
    image = image.convert("RGB")
    
    # nummpy Array
    np_image = np.array(image)
    
    # add noise intensity (0 to 1)
    noise = np.random.normal(loc=0, scale=255 * intensity, size=np_image.shape)
    
    # Add the noise to the original image and clip values to range (0-255)
    noisy_image = np.clip(np_image + noise, 0, 255).astype(np.uint8)
    
    # Convert the noisy image back to PIL format and save
    noisy_image = Image.fromarray(noisy_image)
    noisy_image.save(output_path)