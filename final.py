from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import os
import uuid


def convert_pdf_to_images(pdf_path, output_dir):
    try:
        images = convert_from_path(pdf_path)

        image_paths = []
        for i, image in enumerate(images):
            image_name = f"{uuid.uuid4()}.jpeg"
            image_path = os.path.join(output_dir, image_name)
            image.save(image_path, 'JPEG')
            image_paths.append(image_path)

        return image_paths
    except Exception as e:
        print(f"Error converting PDF to images: {e}")
        return None


def extract_text_from_image(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        print(f"Error processing image: {e}")
        return None


if __name__ == "__main__":
    file_type = input("Do you want to upload a PDF or an Image? (pdf/image): ").strip().lower()

    output_dir = "./output_images"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if file_type == "pdf":
        pdf_path = input("Enter the path to the PDF file: ").strip()

        image_paths = convert_pdf_to_images(pdf_path, output_dir)

        if image_paths:
            for image_path in image_paths:
                print(f"Extracting text from {image_path}...")
                extracted_text = extract_text_from_image(image_path)

                if extracted_text:
                    print("Extracted Text:\n")
                    print(extracted_text)
                else:
                    print(f"Failed to extract text from {image_path}.")
        else:
            print("Failed to convert PDF to images.")

    elif file_type == "image":
        image_path = input("Enter the path to the image file: ").strip()

        print(f"Extracting text from {image_path}...")
        extracted_text = extract_text_from_image(image_path)

        if extracted_text:
            print("Extracted Text:\n")
            print(extracted_text)
        else:
            print(f"Failed to extract text from {image_path}.")

    else:
        print("Invalid option! Please choose either 'pdf' or 'image'.")
