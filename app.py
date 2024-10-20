from selenium import webdriver
from selenium.webdriver.common.by import By
from flask import Flask, render_template, request, jsonify, send_file
import csv  
import os
import time
from selenium.webdriver.chrome.options import Options
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    global driver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    driver = webdriver.Chrome(options=chrome_options)
    data = {
        'start_roll': request.form['start_roll'],
        'end_roll': request.form['end_roll'],
        'candidate_name': request.form['candidate_name'],
        'fathers_name': request.form['fathers_name'],
        'mothers_name': request.form['mothers_name'],
        'education_level': request.form['education_level'],
        'year_name': request.form['year_name']
    }
    
    try:
          # Initialize WebDriver here (don't reassign to None)
        start = int(data["start_roll"])
        end = int(data["end_roll"])
        name_of_student = data["candidate_name"].upper()
        name_of_a_parent = data["fathers_name"].upper()

        # Only 2024 is available for now
        urls = [
            "https://hscresult.bise-ctg.gov.bd/h1624/individual/index.php", 
            "https://sresult.bise-ctg.gov.bd/s24/individual/index.php"
        ]

        for i in range(start, end + 1):
            if data["education_level"] == "HSC":
                driver.get(urls[0])
            elif data['education_level'] == "SSC":
                driver.get(urls[1])
            time.sleep(1)  # Wait for page to load

            input_field = driver.find_element(By.ID, 'roll')
            input_field.send_keys(i)
            button = driver.find_element(By.ID, 'button2')
            button.click()
            time.sleep(2)  # Wait for results to load

            all_infos = driver.find_elements(By.CLASS_NAME, 'cap_lt')
            for info in all_infos:
                if info.text == name_of_student and all_infos[2].text == name_of_a_parent:
                    all_texts = [element.text for element in all_infos]

                    # Assuming the order of elements in all_texts matches the desired columns
                    name, city, fathers_name, group, mothers_name, session, registration_no, student_type, college_name, status, gpa = all_texts[:11]
                    subjects_and_numbers = ','.join(all_texts[11:])

                    # Define the header
                    header = [
                        "Name", "City", "Father's Name", "Group", "Mother's Name", "Session", 
                        "Registration No", "Student Type", "College Name", "Status", "GPA", "Subjects and Numbers"
                    ]

                    # Check if the file exists and is empty
                    file_exists = os.path.isfile("result.csv")
                    is_empty = os.stat("result.csv").st_size == 0 if file_exists else True

                    with open("result.csv", "w", newline='') as file:
                        writer = csv.writer(file)
                        
                        # Write the header if the file is empty
                        if is_empty:
                            writer.writerow(header)
                        
                        # Write the data row
                        writer.writerow([
                            name, city, fathers_name, group, mothers_name, session, registration_no, 
                            student_type, college_name, status, gpa, subjects_and_numbers
                        ])
                    break
            

    except Exception as e:
        print(f"Error: {e}")

    return jsonify({"message": "Data submitted successfully!"}), 200
@app.route('/download_csv')
def download_csv():
    # Ensure the CSV file is generated and available at this path
    path_to_csv = 'result.csv'  # Adjust the path if necessary
    return send_file(path_to_csv, as_attachment=True, download_name='result.csv')

if __name__ == "__main__":
    app.run(debug=True)
