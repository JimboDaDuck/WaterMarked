from PIL import Image, ImageDraw, ImageFont

def add_watermark(image_path, text, output_path):
    # Load the image
    image = Image.open(image_path)
    
    # Create a drawing object
    draw = ImageDraw.Draw(image)
    
    # Define the watermark text
    watermark_text = text
    
    # Define the font properties
    font = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", 30)  # You can replace "Arial.ttf" with the path to your desired font file
    
    # Calculate the watermark text size
    text_width, text_height = draw.textsize(watermark_text, font)
    
    # Calculate the position for the watermark (centered)
    x = (image.width - text_width) // 2
    y = (image.height - text_height) // 2
    
    # Calculate the position for the watermark (bottom left)
    margin = 10
    x = margin
    y = image.height - text_height - margin
    
    # Add the watermark to the image
    draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))
    
    # Save the image with the watermark
    image.save(output_path)
    print("Watermark added successfully!")

# Prompt the user for inputs
image_path = input("Enter the path to the image file: ")
text = input("Enter the watermark text: ")
output_path = input("Enter the output path for the watermarked image: ")

# Call the function to add the watermark
add_watermark(image_path, text, output_path)
