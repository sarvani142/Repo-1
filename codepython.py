from flask import Flask, render_template_string

app = Flask(__name__)

# Simple HTML template with text and images
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Page with Images</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #f4f4f9;
            margin: 0;
            padding: 20px;
        }
        h1 {
            color: #333;
        }
        img {
            width: 300px;
            margin: 15px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
        }
        p {
            color: #555;
        }
    </style>
</head>
<body>
    <h1>Welcome to My Simple Page</h1>
    <p>This is a simple Flask page with images included.</p>
    <img src="https://picsum.photos/300/200" alt="Random Image 1">
    <img src="https://picsum.photos/301/200" alt="Random Image 2">
    <img src="https://picsum.photos/302/200" alt="Random Image 3">
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_template)

if __name__ == "__main__":
    app.run(debug=True)
