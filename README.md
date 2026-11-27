# OnlineBookStorePython
This is a web-based bookstore application developed for a database management class project.
The application uses Flask for the web interface and SQLite for storing bookstore information.
Users can view books, choose between buying and renting books.

## Project Overivew


## Requirements
The following software is required:
- Python 3.0 or newer
- pip
- Flask
- SQLite

## Installation: 
### Step 1. Download or clone the project
```
git clone <repository-url>
cd OnlineBookStorePython
```

### Step 2. Upgrade pip

Windows:
```bash
py -m pip install --upgrade pip
```

macOS/ Linux:
```bash
python3 -m pip install --upgrade pip
```

### Step 3. Create the virtual environment:
Windows:
```bash
py -m venv venv
```

macOS/ Linux:
```bash
python3 -m venv venv
```

### Step 4. Activate the virtual environment
Windows:
```bash
venv\Scripts\activate
```

macOS/ Linux:
```bash
source venv/bin/activate
```

### Step 5. Install Flask (project dependency)
```bash
pip install flask
```

### Step 6. Running the application
Windows:
```bash
python database.py
python app.py
```
macOS/ Linux:
```bash
python3 database.py
python3 app.py
```
Open the following address in a web browser:
```bash
http://127.0.0.1:5000
```

### Step 7. Stopping the application
Press Ctr + C

### Troubleshooting
If Flask is not found, make sure the virtual environment is activated and run:
```bash
pip install flask
```
If the database is missing or corrupted, delete bookstore.db and initialize it again:
```bash
python3 database.py
```


