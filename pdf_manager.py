import os
from config import PDF_STORAGE_PATH

def ensure_pdf_directory_exists():
    """Ensure the PDF storage directory exists."""
    if not os.path.exists(PDF_STORAGE_PATH):
        os.makedirs(PDF_STORAGE_PATH)

def save_pdf(file_content, filename):
    """
    Save a PDF file to the specified directory.

    :param file_content: The binary content of the PDF file.
    :param filename: The filename under which to save the PDF.
    :return: The path to the saved PDF file.
    """
    ensure_pdf_directory_exists()
    full_path = os.path.join(PDF_STORAGE_PATH, filename)
    with open(full_path, 'wb') as pdf_file:
        pdf_file.write(file_content)
    return full_path

def get_pdf_path(filename):
    """
    Get the full path of a PDF file, if it exists.

    :param filename: The name of the PDF file.
    :return: The full path to the PDF file.
    """
    full_path = os.path.join(PDF_STORAGE_PATH, filename)
    if os.path.exists(full_path):
        return full_path
    else:
        return None

def delete_pdf(filename):
    """
    Delete a PDF file from the storage directory.

    :param filename: The name of the PDF file to delete.
    """
    full_path = get_pdf_path(filename)
    if full_path:
        os.remove(full_path)

# Example usage
if __name__ == "__main__":
    # Example of saving a PDF - in practice, `pdf_content` will come from a file upload or similar
    pdf_content = b"%PDF-1.4 example content"
    filename = "example.pdf"
    
    saved_path = save_pdf(pdf_content, filename)
    print(f"PDF saved to {saved_path}")

    # Example of retrieving a PDF path
    path = get_pdf_path(filename)
    if path:
        print(f"PDF path is {path}")
    else:
        print("PDF file does not exist.")

    # Optionally, delete the PDF
    # delete_pdf(filename)
    # print(f"PDF {filename} deleted.")
