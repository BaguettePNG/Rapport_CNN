from PIL import Image

def autocrop_nonblack(input_path, output_path, resize_width=None):
    # Load image
    img = Image.open(input_path).convert("RGB")
    pixels = img.load()

    width, height = img.size

    # Find bounding box of all non-black pixels
    min_x, min_y = width, height
    max_x, max_y = 0, 0

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # consider pixel important if not nearly black
            if r > 10 or g > 10 or b > 10:
                min_x = min(min_x, x)
                max_x = max(max_x, x)
                min_y = min(min_y, y)
                max_y = max(max_y, y)

    # Crop to bounding box
    cropped = img.crop((min_x, min_y, max_x, max_y))

    # Resize if needed
    if resize_width:
        ratio = resize_width / cropped.width
        new_height = int(cropped.height * ratio)
        cropped = cropped.resize((resize_width, new_height), Image.LANCZOS)

    cropped.save(output_path)
    print("Image recadrée enregistrée :", output_path)


# Exemple d’utilisation
autocrop_nonblack(
    "/home/user/Documents/Polytech/ETN4/CCN/Rapport_CNN/RapportFinal/images/Simulation/Simu-3.png",
    "/home/user/Documents/Polytech/ETN4/CCN/Rapport_CNN/RapportFinal/images/Simulation/Simu-3-Rezize.png",
    resize_width=1200  # mettre None si tu veux juste crop
)
