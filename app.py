from flask import Flask, request

app = Flask(__name__)

questions = [
    {
        "question": "Who developed Python?",
        "options": ["Dennis Ritchie", "Guido van Rossum", "James Gosling", "Bjarne Stroustrup"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/* */", "--"],
        "answer": "#"
    },
    {
        "question": "Which keyword is used to define a function?",
        "options": ["function", "def", "fun", "define"],
        "answer": "def"
    }
]


@app.route("/")
def home():
    html = """
    <html>
    <head>
    <title>Quizzer</title>
    <style>
    body{
        background:#120022;
        color:white;
        font-family:Arial;
        text-align:center;
    }

    .box{
        width:80%;
        max-width:500px;
        margin:auto;
        background:#1d1038;
        padding:30px;
        border-radius:20px;
    }

    button{
        background:linear-gradient(to right,#8a2be2,#3a86ff);
        color:white;
        padding:15px;
        border:none;
        border-radius:15px;
        width:100%;
        font-size:20px;
    }
    </style>
    </head>

    <body>

    <h1>❓ Quizzer</h1>
    <h3>Test your Python knowledge</h3>

    <div class="box">

    <form action="/result" method="post">
    """

    for i, q in enumerate(questions):
        html += f"<h3>{q['question']}</h3>"

        for option in q["options"]:
            html += f"""
            <input type='radio' name='q{i}' value='{option}' required>
            {option}<br><br>
            """

    html += """
    <br>
    <button type="submit">Submit Quiz</button>
    </form>

    </div>

    <br><br>

    <h2>About</h2>

    <p>
    Designed & Developed by <b>ANKIT SAINI</b>
    </p>

    <p>
    B.Tech IT Student at JMIT Radaur
    </p>

    <p>
    Python | SQL | Cybersecurity
    </p>

    <p>
    Email : as3126061@gmail.com
    </p>

    </body>
    </html>
    """

    return html


@app.route("/result", methods=["POST"])
def result():
    score = 0

    for i, q in enumerate(questions):
        if request.form.get(f"q{i}") == q["answer"]:
            score += 1

    return f"""
    <html>
    <body style="background:#120022;color:white;text-align:center;font-family:Arial;">
    <h1>🏆 Quiz Result</h1>
    <h2>Your Score : {score}/{len(questions)}</h2>

    <a href="/" style="
    background:#3a86ff;
    color:white;
    padding:15px;
    text-decoration:none;
    border-radius:15px;">
    Play Again
    </a>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
