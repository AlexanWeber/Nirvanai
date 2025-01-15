from PIL import ImageOps

# Reopen the original image to ensure a clean slate
image = Image.open(input_image_path)

# Sample the background color again from a wider area to ensure it's accurate
sample_area = image.crop((30, 20, 150, 60))  # Adjust coordinates for sampling
background_color = sample_area.getpixel((10, 10))  # Sample a pixel inside the area

# Redraw the text with a matching background color
draw = ImageDraw.Draw(image)
draw.rectangle(rectangle_position, fill=background_color)  # Use the sampled background color
draw.text(text_position, new_text, fill="black", font=font)  # Add the text on top

border_size = 10 
image_with_border = ImageOps.expand(image, border=border_size, fill=background_color)

# Add a watermark to the image
watermark_text = "Nirvanai AI"  
watermark_font_size = 15  
watermark_font = ImageFont.truetype(font_path, watermark_font_size) 

watermark_width, watermark_height = draw.textsize(watermark_text, font=watermark_font)
watermark_position = (
    image_with_border.width - watermark_width - 20,  
    image_with_border.height - watermark_height - 10,  
)

draw_with_border = ImageDraw.Draw(image_with_border)
draw_with_border.text(watermark_position, watermark_text, fill="gray", font=watermark_font)  

# Save the modified image
output_final_image_path = "/mnt/data/image_with_nirvanai_final_with_border.png"
image.save(output_final_image_path)
output_final_image_path

print(f"Final image with border and watermark saved to: {output_with_border_image_path}")
