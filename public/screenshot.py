from PIL import Image, ImageDraw, ImageFont, ImageOps

# Load the image again
image = Image.open(input_image_path).convert("RGBA")

# Sample background color
sample_area = image.crop((30, 20, 150, 60))
background_color = sample_area.getpixel((10, 10))

# Draw text with matching background color
draw = ImageDraw.Draw(image)
draw.rectangle(rectangle_position, fill=background_color)
draw.text(text_position, new_text, fill="black", font=font)

# Add a border around the image
border_size = 10
image_with_border = ImageOps.expand(image, border=border_size, fill=background_color)

# Create a transparent watermark layer
watermark_text = "Nirvanai AI"
watermark_font_size = 15
watermark_font = ImageFont.truetype(font_path, watermark_font_size)

# Create a new transparent image for watermark
watermark_layer = Image.new("RGBA", image_with_border.size, (255, 255, 255, 0))
draw_watermark = ImageDraw.Draw(watermark_layer)

# Calculate watermark position
watermark_width, watermark_height = draw_watermark.textsize(watermark_text, font=watermark_font)
watermark_position = (
    image_with_border.width - watermark_width - 20,
    image_with_border.height - watermark_height - 10,
)

# Add watermark with transparency
watermark_color = (128, 128, 128, 150)  # Gray with transparency
draw_watermark.text(watermark_position, watermark_text, fill=watermark_color, font=watermark_font)

# Merge watermark layer with the image
final_image = Image.alpha_composite(image_with_border.convert("RGBA"), watermark_layer)

# Save the final image
output_final_image_path = "/mnt/data/image_with_nirvanai_final_with_border.png"
final_image.save(output_final_image_path)

print(f"Final image with border and watermark saved to: {output_final_image_path}")
