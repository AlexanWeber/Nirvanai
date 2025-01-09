# Reopen the original image to ensure a clean slate
image = Image.open(input_image_path)

# Sample the background color again from a wider area to ensure it's accurate
sample_area = image.crop((30, 20, 150, 60))  # Adjust coordinates for sampling
background_color = sample_area.getpixel((10, 10))  # Sample a pixel inside the area

# Redraw the text with a matching background color
draw = ImageDraw.Draw(image)
draw.rectangle(rectangle_position, fill=background_color)  # Use the sampled background color
draw.text(text_position, new_text, fill="black", font=font)  # Add the text on top

# Save the modified image
output_final_image_path = "/mnt/data/image_with_nirvanai_final.png"
image.save(output_final_image_path)
output_final_image_path