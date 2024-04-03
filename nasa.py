import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta
import random

def generate_unique_date(start_date, end_date, generated_dates):
	while True:
		random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
		if random_date not in generated_dates:
			generated_dates.add(random_date)
			return random_date

def fetch_and_save_image(generated_dates):
	print("Fetching image...")

	# Load environment variables
	load_dotenv()

	# Get the NASA API key from the environment variable
	nasa_api_key = os.getenv('NASA_API_KEY')

	# Generate a unique random date between 2022-01-01 and today's date
	start_date = datetime(2022, 1, 1)
	end_date = datetime.now()
	random_date = generate_unique_date(start_date, end_date, generated_dates)
	formatted_date = random_date.strftime('%Y-%m-%d')

	# Define the URL for the APOD (Astronomy Picture of the Day) endpoint with the random date
	apod_url = f"https://api.nasa.gov/planetary/apod?api_key={nasa_api_key}&date={formatted_date}"

	# Make a GET request to the APOD endpoint
	response = requests.get(apod_url)

	# Check if the request was successful
	if response.status_code == 200:
		# Parse the JSON response
		apod_data = response.json()

		# Determine if an HD image is available
		is_hd = 'hdurl' in apod_data

		# Get the URL of the high-definition image or fall back to the regular image
		image_url = apod_data.get('hdurl', apod_data.get('url'))

		# Check if the URL exists
		if image_url:
			# Download the image
			image_response = requests.get(image_url)

			# Check if the image download was successful
			if image_response.status_code == 200:
				# Create the Images directory if it doesn't exist
				if not os.path.exists('Images'):
					os.makedirs('Images')

				# Save the image to a file in the Images directory with the date in the filename
				# Append "HD" to the filename if the image is HD
				filename_suffix = "_HD" if is_hd else ""
				filename = f"Images/nasa_apod{filename_suffix}_{formatted_date}.jpg"
				with open(filename, 'wb') as image_file:
					image_file.write(image_response.content)
				print(f"Done. Image saved as '{filename}'")

				# Get the absolute path of the image file
				abs_filename = os.path.abspath(filename)

				# Open the image in the default file viewer
				os.startfile(abs_filename)
			else:
				print("Error downloading the image")
		else:
			print("Image URL not found in the response")
	else:
		print("Error fetching the APOD data")

def main():
	generated_dates = set()
	while True:
		fetch_and_save_image(generated_dates)
		answer = input("Would you like to generate another image? (Y/N): ").strip().upper()
		if answer != 'Y':
			break

if __name__ == '__main__':
	main()
