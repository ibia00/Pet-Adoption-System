# 🐾 Pet Adoption System

A simple Flask web application for managing pet adoptions with RESTful API endpoints.

## 🚀 Features

### Web Interface
- **Add New Pet**: Add pets with name, type, and age
- **View All Pets**: Display all pets in an attractive card layout
- **Mark as Adopted**: Mark pets as adopted with a single click
- **Delete Pet**: Remove pets from the system
- **Filter by Type**: Filter pets by their type (dog, cat, etc.)
- **Statistics Dashboard**: View total, available, and adopted pets count

### REST API
- **GET /api/pets**: Returns all pets in JSON format with statistics
- **POST /api/pets**: Add a new pet using JSON data

## 📋 Requirements

- Python 3.7 or higher
- Flask 2.3.3

## 🛠️ Setup Instructions

### 1. Clone or Download
Download the project files to your local machine.

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python app.py
```

### 4. Access the Application
- **Web Interface**: http://localhost:5000
- **API Endpoint**: http://localhost:5000/api/pets

## 🌐 API Usage

### Get All Pets
```bash
curl -X GET http://localhost:5000/api/pets
```

**Response:**
```json
{
  "pets": [
    {
      "id": "uuid-string",
      "name": "Buddy",
      "type": "dog",
      "age": 3,
      "adopted": false
    }
  ],
  "total": 3,
  "available": 2,
  "adopted": 1
}
```

### Add New Pet
```bash
curl -X POST http://localhost:5000/api/pets \
     -H "Content-Type: application/json" \
     -d '{"name": "Rex", "type": "dog", "age": 4}'
```

**Response:**
```json
{
  "message": "Pet added successfully",
  "pet": {
    "id": "new-uuid-string",
    "name": "Rex",
    "type": "dog",
    "age": 4,
    "adopted": false
  }
}
```

## 📁 Project Structure

```
restfullPR/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── templates/
    └── index.html        # HTML template for web interface
```

## 🎯 Application Features

### Web Interface Features
1. **Modern Design**: Beautiful, responsive design with gradient backgrounds
2. **Flash Messages**: User feedback for all actions
3. **Form Validation**: Client and server-side validation
4. **Interactive Cards**: Hover effects and smooth animations
5. **Mobile Responsive**: Works on all device sizes

### Data Management
- **In-Memory Storage**: Uses Python list for simple data storage
- **Unique IDs**: Each pet gets a unique UUID identifier
- **Sample Data**: Comes with 3 sample pets pre-loaded

### Error Handling
- **Form Validation**: Validates all required fields
- **Age Validation**: Ensures age is a positive number
- **API Error Responses**: Proper HTTP status codes and error messages
- **User-Friendly Messages**: Clear feedback for all operations

## 🧪 Testing the Application

### Web Interface Testing
1. Open http://localhost:5000 in your browser
2. Try adding a new pet using the form
3. Test filtering pets by type
4. Mark a pet as adopted
5. Delete a pet

### API Testing with curl

**Test GET endpoint:**
```bash
curl -X GET http://localhost:5000/api/pets
```

**Test POST endpoint:**
```bash
curl -X POST http://localhost:5000/api/pets \
     -H "Content-Type: application/json" \
     -d '{"name": "Fluffy", "type": "cat", "age": 2}'
```

### API Testing with Python
```python
import requests
import json

# Get all pets
response = requests.get('http://localhost:5000/api/pets')
print(response.json())

# Add a new pet
new_pet = {
    "name": "Goldie",
    "type": "fish",
    "age": 1
}
response = requests.post(
    'http://localhost:5000/api/pets',
    headers={'Content-Type': 'application/json'},
    data=json.dumps(new_pet)
)
print(response.json())
```

## 🔧 Configuration

The application runs with the following default settings:
- **Host**: 0.0.0.0 (accessible from any IP)
- **Port**: 5000
- **Debug Mode**: Enabled for development

To change these settings, modify the `app.run()` call in `app.py`.

## 🚨 Important Notes

1. **Data Persistence**: Data is stored in memory and will be lost when the application restarts
2. **Security**: This is a demo application - use a proper secret key in production
3. **Database**: For production use, replace the in-memory list with a proper database
4. **Validation**: Additional validation may be needed for production use

## 🎉 Demo Data

The application comes with sample pets:
- **Buddy** (Dog, 3 years, Available)
- **Whiskers** (Cat, 2 years, Available)
- **Charlie** (Dog, 5 years, Adopted)

## 🐛 Troubleshooting

**Port already in use:**
```bash
# Kill process using port 5000
netstat -ano | findstr :5000
taskkill /PID <PID_NUMBER> /F
```

**Module not found:**
```bash
pip install Flask
```

**Template not found:**
Make sure the `templates/index.html` file exists in the correct location.

## 📝 License

This project is for educational purposes. Feel free to modify and extend as needed.

---

**Happy Pet Adopting! 🐕🐱🐰**
