from flask import Flask, render_template, request, jsonify
from coffee_logic import recommend_coffee

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/recommend')
def recommend_page():
    return render_template('recommend.html')
@app.route('/menu')
def menu():
    return render_template('menu.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    result = recommend_coffee(
        data['age'],
        data['weight'],
        data['sleep_hours'],
        data['study_hours'],
        data['caffeine_tolerance']
    )   
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
