# Result Scraper

This project is a web application that allows users to scrape examination results for a specific range of roll numbers. The application is built using Flask for the backend and Selenium for web scraping. It currently supports results for the year 2024.

## Features

- Scrape results for a range of roll numbers.
- Supports both HSC and SSC education levels.
- Saves the results in a CSV file.
- User-friendly web interface for inputting data.

## Prerequisites

- Python 3.x
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)
- Flask
- Selenium

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/result-scraper.git
   cd result-scraper
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Download and install [ChromeDriver](https://sites.google.com/chromium.org/driver/) and ensure it's in your system's PATH.

## Usage

1. Start the Flask application:

   ```bash
   python get_result.py
   ```

2. Open your web browser and go to `http://localhost:5000`.

3. Fill out the form with the required information:
   - **Start Roll**: The starting roll number.
   - **End Roll**: The ending roll number.
   - **Name of the Candidate**: The candidate's name.
   - **Father's Name**: The candidate's father's name.
   - **Mother's Name**: The candidate's mother's name.
   - **Education Level**: Select either HSC or SSC.
   - **Year**: Enter the year (only 2024 is supported).

4. Click the "Submit" button to start scraping.

5. Once the scraping is complete, a CSV file named `result.csv` will be generated in the project directory.

## How It Works

- The application uses Selenium to automate the process of visiting the result website and entering roll numbers.
- It checks each roll number within the specified range and matches the candidate's name and father's name.
- The results are extracted and saved into a CSV file.

## Notes

- Ensure that the ChromeDriver version matches your installed Chrome browser version.
- The application currently only supports the year 2024.

## Troubleshooting

- If you encounter any issues with Selenium, ensure that your ChromeDriver is up to date and correctly installed.
- Check the console for any error messages that might indicate what went wrong.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.