# Flask Web Application for Data Transformation

## Overview

This repository contains a Flask-based web application designed for a college assignment. It integrates a Flask backend with a visually appealing webpage using the W3.css framework to enhance the user experience. The application includes functionalities for form handling, data transformation, and dynamic data display.

## Features

1. **Stylish Homepage**:
   - Displays a visually enhanced landing page using W3.css.

2. **User Input Handling**:
   - Accepts user input through a form.
   - Dynamically displays the submitted data on a new page in a table format.

3. **CSV to JSON Conversion**:
   - Converts data from a CSV file into JSON format.
   - Outputs the JSON data as a response and saves it locally.

4. **JSON Dashboard**:
   - Presents JSON data in a user-friendly table format on a webpage.

5. **Video Demonstration**:
   - A video demo showcasing the application is available [here](https://drive.google.com/file/d/1j9u981QZAPuDGM3XHq75npsVRHADeHTu/view?usp=sharing).

## Project Structure

- **`static/`**:
  - Contains static files (CSS, images) used in the application.
- **`templates/`**:
  - `index.html`: Homepage template.
  - `form.html`: Template for user input form.
  - `user.html`: Template to display user-submitted data.
  - `api_call.html`: Template to display JSON data in a table.
- **`allegiance.csv`**: Input CSV file.
- **`app.py`**: Main Flask application script.
- **`converted_books.json`**: Output JSON file after conversion.

## Prerequisites

- Python 3.x
- Flask (`pip install flask`)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/kevincogan/Flask_College_Assignment.git
   cd Flask_College_Assignment
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   python app.py
   ```

4. **Access the Application**:
   Open your browser and navigate to `http://localhost:8082`.

## Endpoints

### 1. `/` (Homepage)
- Displays the main landing page of the application.

### 2. `/formtest` (Form Submission)
- Accepts user input via a form (name field).
- Redirects to a user-specific page displaying the input.

### 3. `/<usr>` (User Page)
- Displays the user-submitted data in a table format.

### 4. `/allegiances` (CSV to JSON Conversion)
- Converts `allegiance.csv` into `converted_books.json`.
- Outputs the JSON data as a response.

### 5. `/allegiancedashboard` (JSON Dashboard)
- Displays the JSON data from `converted_books.json` in a table format on a webpage.

## How It Works

1. **Form Handling**:
   - User submits their name via the form.
   - Flask redirects to a user-specific page displaying the submitted data.

2. **CSV to JSON Conversion**:
   - The `allegiances` endpoint reads the `allegiance.csv` file.
   - Converts it to JSON format using Python's `csv` and `json` libraries.
   - Writes the JSON data to `converted_books.json`.
   - Outputs the JSON data as a response.

3. **JSON Dashboard**:
   - The `allegiancedashboard` endpoint renders the JSON data from `converted_books.json` into a table format using an HTML template.

## Example Input and Output

### Form Submission
**Input**:
```
Name: Kevin
```

**Output**:
A user-specific page displaying:
```
Name: Kevin
```

### CSV to JSON Conversion
**Input File (`allegiance.csv`)**:
```csv
Name,House,Role
Jon Snow,Stark,Lord Commander
Daenerys Targaryen,Targaryen,Queen
```

**Output JSON (`converted_books.json`)**:
```json
[
  {
    "Name": "Jon Snow",
    "House": "Stark",
    "Role": "Lord Commander"
  },
  {
    "Name": "Daenerys Targaryen",
    "House": "Targaryen",
    "Role": "Queen"
  }
]
```

**Displayed Table**:
| Name               | House      | Role             |
|--------------------|------------|------------------|
| Jon Snow           | Stark      | Lord Commander   |
| Daenerys Targaryen | Targaryen  | Queen            |

## Contribution

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes and push them to your fork.
4. Open a pull request describing your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

Explore this Flask-based college assignment with enhanced web design and functionality!

