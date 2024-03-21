from PIL import Image


def combine_images_vertically(img_paths, spacing_reduction, output_path):
    images = [Image.open(img_path) for img_path in img_paths]
    widths, heights = zip(*(i.size for i in images))

    total_width = max(widths)
    total_height = sum(heights) - spacing_reduction * (len(images) - 1)

    new_image = Image.new('RGB', (total_width, total_height))

    y_offset = 0
    for img in images:
        new_image.paste(img, (0, y_offset))
        y_offset += img.size[1] - spacing_reduction

    new_image.save(output_path)

def combine_images_with_overlap(img_paths, overlap_amount, output_path):
    images = [Image.open(img_path) for img_path in img_paths]
    widths, heights = zip(*(i.size for i in images))

    total_width = max(widths)
    # Adjust total height calculation to account for overlap
    total_height = sum(heights) - overlap_amount * (len(images) - 1)

    new_image = Image.new('RGB', (total_width, total_height), (255, 255, 255))  # Assuming a white background

    y_offset = 0
    for img in images:
        new_image.paste(img, (0, y_offset))
        # Only move up by the height of the image minus the overlap amount for the next image
        y_offset += img.size[1] - overlap_amount

    new_image.save(output_path)

def combine_images_with_overlap_and_whitespace(img_paths, overlap_amount, whitespace_amount, output_path):
    images = [Image.open(img_path) for img_path in img_paths]
    widths, heights = zip(*(i.size for i in images))

    total_width = max(widths)
    # Adjust total height calculation to account for overlap and whitespace
    total_height = sum(heights) - overlap_amount * (len(images) - 1) + whitespace_amount * (len(images) - 1)

    new_image = Image.new('RGB', (total_width, total_height), (255, 255, 255))  # Assuming a white background

    y_offset = 0
    for i, img in enumerate(images):
        if i > 0:  # For all images after the first, add a band of whitespace
            # Create a band of whitespace
            whitespace = Image.new('RGB', (img.width, whitespace_amount), (255, 255, 255))
            new_image.paste(whitespace, (0, y_offset))
            y_offset += whitespace_amount
        new_image.paste(img, (0, y_offset))
        # Adjust y_offset for the next image, considering the overlap
        y_offset += img.size[1] - overlap_amount

    new_image.save(output_path, format='PNG', optimize=False)

# Example usage
major_path = 'random/figures/'
img_paths = [f'{major_path}heatmap_statistics_multihaz_multisec_fa_p_stage_3_fa_p_da_p.png',
             f'{major_path}heatmap_statistics_multihaz_multisec_fa_p_stage_3_fu_p_ds_p.png',]
# combine_images_vertically(img_paths, spacing_reduction=50, output_path='heatmap_statistics_multihaz_multisec.png')

# combine_images_with_overlap(img_paths, overlap_amount=500, output_path='heatmap_statistics_multihaz_multisec.png')
combine_images_with_overlap_and_whitespace(img_paths, overlap_amount=610, whitespace_amount=150, output_path='random/heatmap_statistics_multihaz_multisec.png')

img_paths = [f'{major_path}heatmap_interactions_multihaz_multisec_DamAgr_f_tot_revenue_agr.png',
             f'{major_path}heatmap_interactions_multihaz_multisec_DamAgr_f_tot_DamUrb_tot.png',
             f'{major_path}heatmap_interactions_multihaz_multisec_DamAgr_f_tot_DamShp_tot.png']

combine_images_with_overlap_and_whitespace(img_paths, overlap_amount=0, whitespace_amount=50, output_path='random/heatmap_interactions_multihaz_multisec.png')
