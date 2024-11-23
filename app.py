from flask import Flask, request, render_template_string

app = Flask(__name__)

# Main HTML templates
home_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Advocate for Better Assessments at SDSU</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f8f8f8;
            margin: 0;
            padding: 0;
            color: #333;
        }
        header {
            background: #b71c1c;
            padding: 20px;
            color: white;
            text-align: center;
        }
        header h1 {
            margin: 0;
        }
        .content {
            margin: 30px auto;
            max-width: 800px;
            text-align: left;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        .content h2 {
            color: #b71c1c;
        }
        button {
            padding: 10px 20px;
            color: white;
            background-color: #b71c1c;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #9a1515;
        }
        input[type="text"] {
            width: 100%;
            padding: 8px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 14px;
        }
        input[type="checkbox"] {
            margin-right: 8px;
        }
        footer {
            margin-top: 30px;
            text-align: center;
            font-size: 12px;
            color: #777;
        }
    </style>
</head>
<body>
    <header>
        <h1>Advocate for Better Assessments at SDSU</h1>
        <p>Generate a personalized letter to reduce multiple-choice tests.</p>
    </header>
    <div class="content">
        <h2>Select Your Reasons</h2>
        <form action="/generate" method="POST">
            <label><b>Choose Reasons:</b></label><br>
            <input type="checkbox" name="reason" value="Promotes Critical Thinking"> Promotes Critical Thinking<br>
            <input type="checkbox" name="reason" value="Encourages Deep Learning"> Encourages Deep Learning<br>
            <input type="checkbox" name="reason" value="Prepares Students for Real-World Problem Solving"> Prepares Students for Real-World Problem Solving<br>
            <input type="checkbox" name="reason" value="Reduces Test Anxiety"> Reduces Test Anxiety<br>
            <input type="checkbox" name="reason" value="Increases Fairness in Grading"> Increases Fairness in Grading<br>
            <input type="checkbox" name="reason" value="Encourages Creativity and Expression"> Encourages Creativity and Expression<br><br>

            <label><b>Your Name:</b></label><br>
            <input type="text" name="name" placeholder="Enter your name"><br>

            <label><b>Major:</b></label><br>
            <input type="text" name="major" placeholder="Enter your major"><br>

            <label><b>Year of Study:</b></label><br>
            <input type="text" name="year" placeholder="e.g., Freshman, Sophomore"><br><br>

            <button type="submit">Generate Letter</button>
        </form>
    </div>
    <footer>
        &copy; 2024 Advocate for Change | SDSU Inspired
    </footer>
</body>
</html>
"""

letter_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Your Personalized Letter</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f8f8f8;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: auto;
            text-align: center;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #b71c1c;
        }
        textarea {
            width: 100%;
            height: 300px;
            margin-top: 20px;
            padding: 10px;
            font-size: 14px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            padding: 10px 20px;
            color: white;
            background-color: #b71c1c;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #9a1515;
        }
        a {
            color: white;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Your Personalized Letter</h1>
        <textarea readonly>{{ letter }}</textarea><br>
        <button onclick="copyToClipboard()">Copy to Clipboard</button><br><br>
        <button><a href="https://www.sdsu.edu/feedback" target="_blank">Submit to SDSU Feedback Page</a></button>
    </div>
    <script>
        function copyToClipboard() {
            const textarea = document.querySelector('textarea');
            textarea.select();
            document.execCommand('copy');
            alert('Copied to clipboard!');
        }
    </script>
</body>
</html>
"""

# Flask routes
@app.route("/")
def home():
    return render_template_string(home_template)

@app.route("/generate", methods=["POST"])
def generate():
    reasons = request.form.getlist("reason")
    name = request.form.get("name", "A Concerned Student")
    major = request.form.get("major", "Your Major")
    year = request.form.get("year", "Your Year")

    # Generate letter content
    letter = f"Dear SDSU Administration,\n\n"
    letter += f"My name is {name}, a {year} majoring in {major}. I am writing to express my support for reducing the usage of multiple-choice tests at SDSU.\n\n"

    if reasons:
        letter += "Here are my reasons:\n"
        for reason in reasons:
            letter += f"- {reason}\n"
    else:
        letter += "I believe multiple-choice tests hinder students' ability to develop critical skills required in the real world.\n\n"

    letter += "Thank you for considering this request. I believe these changes can positively impact the learning environment at SDSU.\n\n"
    letter += "Sincerely,\n"
    letter += f"{name}"

    return render_template_string(letter_template, letter=letter)

if __name__ == "__main__":
    app.run(debug=False)
