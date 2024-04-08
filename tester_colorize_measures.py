from PIL import Image, ImageOps
from Paper3_v1.scripts.utilities.design_choices.main_dashboard_design_choices import MEASURE_COLORS, MEASURE_NUMBERS

def colorize_logos(logo_path,colour, new_logo_path):
    # Load the image
    original_image = Image.open(logo_path)

    # Convert the image to grayscale
    gray_image = ImageOps.grayscale(original_image)

    # Colorize the image - the example here colorizes the image to light blue
    # The first tuple defines the original color (black in grayscale),
    # and the second tuple defines the target color in (R, G, B) format.
    colorized_image = ImageOps.colorize(gray_image, black="white", white=colour)

    # Now you can save the colorized image or use it directly in Plotly
    colorized_image.save(new_logo_path)

# Continue to add this colorized image to your Plotly figure

for measure in MEASURE_NUMBERS:
    image_path = f'Paper3_v1/data/logos/{measure}.png'
    colour = MEASURE_COLORS[str(MEASURE_NUMBERS[measure])]
    colorize_logos(image_path, colour, f'Paper3_v1/data/logos/colorized/{measure}.png')
