from flask import Flask, render_template, request
app = Flask(__name__)
# Route for the homepage
@app.route('/')
def home():
   return render_template('index.html')
# Route to handle form submissions
@app.route('/submit', methods=['POST'])
def submit():
   name = request.form['name']
   email = request.form['email']
   message = request.form['message']
   # For now, just print the data to the console
   print(f"Message from {name} ({email}): {message}")
   # You can add logic to store data or send an email
   return "Thank you for your message!"
if __name__ == '__main__':
   app.run(debug=True)
