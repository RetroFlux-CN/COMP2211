import os
import zipfile


def unzip_file(zip_path, extract_to):
	"""
	Extracts a ZIP file to the specified directory.

	Parameters:
		zip_path (str): Path to the ZIP file.
		extract_to (str): Directory where the contents will be extracted.

	Returns:
		None
	"""
	# Check if the provided ZIP file exists
	if not os.path.exists(zip_path):
		raise FileNotFoundError(f"The file {zip_path} does not exist.")
	# Create the target directory if it doesn't exist
	os.makedirs(extract_to, exist_ok=True)

	# Open the ZIP file in read mode
	with zipfile.ZipFile(zip_path, 'r') as zip_ref:
		zip_ref.extractall(extract_to)
		print(f"Extracted all files to: {extract_to}")