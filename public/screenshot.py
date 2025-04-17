from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter

# Load the image again
image = Image.open(input_image_path).convert("RGBA")

# Sample background color
sample_area = image.crop((30, 20, 150, 60))
background_color = sample_area.getpixel((10, 10))

# Draw text with matching background color
draw = ImageDraw.Draw(image)

# Dynamic text box size adjustment for multiple lines
def draw_multiline_text(draw, text, position, font, max_width):
    lines = []
    width, height = draw.textsize(text, font)
    # Split text into multiple lines based on max width
    while width > max_width:
        text = text.rsplit(' ', 1)[0]
        lines.append(text)
        text = text.rsplit(' ', 1)[1]
        width, height = draw.textsize(text, font)
    lines.append(text)
    
    y_offset = 0
    for line in lines:
        draw.text((position[0], position[1] + y_offset), line, font=font, fill="black")
        y_offset += height
    return (position[0], position[1] + y_offset)

# Add the rectangle and text
rectangle_position = (30, 20, 150, 60)
text_position = (40, 30)
new_text = "Sample text for multiline support"
font_path = "path_to_font.ttf"
font = ImageFont.truetype(font_path, 20)

# Draw the rectangle and multiline text
draw.rectangle(rectangle_position, fill=background_color)
draw_multiline_text(draw, new_text, text_position, font, max_width=120)

# Add a border around the image
border_size = 10
image_with_border = ImageOps.expand(image, border=border_size, fill=background_color)

# Apply a filter (e.g., blur) to the image for added effect
image_with_border = image_with_border.filter(ImageFilter.GaussianBlur(radius=2))

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

print(f"Final image with border, watermark, and additional effects saved to: {output_final_image_path}")
