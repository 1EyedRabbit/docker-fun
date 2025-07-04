from flask import Flask, render_template_string
import random

app = Flask(__name__)

# Function to generate a random hex color
def get_random_color():
    return "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

@app.route('/')
def home():
    port = 8080  # You can adjust this port if needed, or retrieve from the environment
    color = get_random_color()
    return render_template_string("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Landing Page</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body, html {
            height: 100%;
            font-family: Arial, sans-serif;
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: {{ color }};
            transition: background-color 0.5s ease;
        }
        .container {
            text-align: center;
            color: white;
        }
        h1 {
            font-size: 2rem;
            margin-bottom: 10px;
        }
        p {
            font-size: 1.2rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to the Containerized Landing Page!</h1>
        <p>The container is running on port: {{ port }}</p>
    </div>
</body>
</html>
    """, port=port, color=color)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
