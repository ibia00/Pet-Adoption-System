from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
import uuid

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# In-memory storage for pets
pets = [
    {
        'id': str(uuid.uuid4()),
        'name': 'Buddy',
        'type': 'dog',
        'age': 3,
        'adopted': False
    },
    {
        'id': str(uuid.uuid4()),
        'name': 'Whiskers',
        'type': 'cat',
        'age': 2,
        'adopted': False
    },
    {
        'id': str(uuid.uuid4()),
        'name': 'Charlie',
        'type': 'dog',
        'age': 5,
        'adopted': True
    }
]

@app.route('/')
def index():
    """Main page showing all pets with filtering options"""
    pet_type_filter = request.args.get('type', '')
    
    if pet_type_filter:
        filtered_pets = [pet for pet in pets if pet['type'].lower() == pet_type_filter.lower()]
    else:
        filtered_pets = pets
    
    # Get unique pet types for filter dropdown
    pet_types = list(set([pet['type'] for pet in pets]))
    
    return render_template('index.html', pets=filtered_pets, pet_types=pet_types, current_filter=pet_type_filter)

@app.route('/add_pet', methods=['POST'])
def add_pet():
    """Add a new pet"""
    name = request.form.get('name')
    pet_type = request.form.get('type')
    age = request.form.get('age')
    
    if not name or not pet_type or not age:
        flash('All fields are required!', 'error')
        return redirect(url_for('index'))
    
    try:
        age = int(age)
        if age < 0:
            flash('Age must be a positive number!', 'error')
            return redirect(url_for('index'))
    except ValueError:
        flash('Age must be a valid number!', 'error')
        return redirect(url_for('index'))
    
    new_pet = {
        'id': str(uuid.uuid4()),
        'name': name.strip(),
        'type': pet_type.strip().lower(),
        'age': age,
        'adopted': False
    }
    
    pets.append(new_pet)
    flash(f'Pet {name} has been added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/adopt_pet/<pet_id>')
def adopt_pet(pet_id):
    """Mark a pet as adopted"""
    pet = next((p for p in pets if p['id'] == pet_id), None)
    
    if pet:
        if pet['adopted']:
            flash(f'{pet["name"]} is already adopted!', 'info')
        else:
            pet['adopted'] = True
            flash(f'{pet["name"]} has been marked as adopted!', 'success')
    else:
        flash('Pet not found!', 'error')
    
    return redirect(url_for('index'))

@app.route('/delete_pet/<pet_id>')
def delete_pet(pet_id):
    """Delete a pet"""
    global pets
    pet = next((p for p in pets if p['id'] == pet_id), None)
    
    if pet:
        pets = [p for p in pets if p['id'] != pet_id]
        flash(f'{pet["name"]} has been removed from the system!', 'success')
    else:
        flash('Pet not found!', 'error')
    
    return redirect(url_for('index'))

# REST API Endpoints

@app.route('/api/pets', methods=['GET'])
def api_get_pets():
    """REST API: Get all pets"""
    return jsonify({
        'pets': pets,
        'total': len(pets),
        'available': len([p for p in pets if not p['adopted']]),
        'adopted': len([p for p in pets if p['adopted']])
    })

@app.route('/api/pets', methods=['POST'])
def api_add_pet():
    """REST API: Add a new pet"""
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    name = data.get('name')
    pet_type = data.get('type')
    age = data.get('age')
    
    if not name or not pet_type or age is None:
        return jsonify({'error': 'Missing required fields: name, type, age'}), 400
    
    try:
        age = int(age)
        if age < 0:
            return jsonify({'error': 'Age must be a positive number'}), 400
    except (ValueError, TypeError):
        return jsonify({'error': 'Age must be a valid number'}), 400
    
    new_pet = {
        'id': str(uuid.uuid4()),
        'name': str(name).strip(),
        'type': str(pet_type).strip().lower(),
        'age': age,
        'adopted': False
    }
    
    pets.append(new_pet)
    
    return jsonify({
        'message': 'Pet added successfully',
        'pet': new_pet
    }), 201

if __name__ == '__main__':
    print("Starting Pet Adoption System...")
    print("Access the web interface at: http://localhost:5000")
    print("API endpoints:")
    print("  GET  /api/pets - Get all pets")
    print("  POST /api/pets - Add a new pet")
    app.run(debug=True, host='0.0.0.0', port=5000)
