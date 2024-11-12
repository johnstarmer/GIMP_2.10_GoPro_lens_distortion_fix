#!/usr/bin/env python

from gimpfu import *
import os

def batch_lens_distortion(input_folder, output_folder):
    # Iterate over all files in the folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.tif', '.bmp')):  # Add more extensions if needed
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, filename)

            # Open the image file
            image = pdb.gimp_file_load(input_file, input_file)
            drawable = image.active_layer

            # Apply Lens Distortion
            pdb.gimp_lens_distortion(image, drawable, 0.0, 0.0, 0.0, 0.0, -100.0)  # Adjust values as needed

            # Save the modified image
            pdb.gimp_file_save(image, drawable, output_file, output_file)

            # Clean up
            pdb.gimp_image_delete(image)

# Example Usage:
# input_folder = "~/Desktop/D_input"  # Path to input folder with images
# output_folder = "~/Desktop/D_output"  # Path to output folder

# batch_lens_distortion(input_folder, output_folder)
