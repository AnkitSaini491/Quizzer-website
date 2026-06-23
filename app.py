from flask import Flask, request

app = Flask(__name__)

quizzes = {

"python":[
{
"question":"Who developed Python?",
"options":["Dennis Ritchie","Guido van Rossum","James Gosling","Bjarne Stroustrup"],
"answer":"Guido van Rossum"
},
{
"question":"Which keyword is used to define a function?",
"options":["function","def","fun","define"],
"answer":"def"
}
],

"c":[
{
"question":"Who developed C language?",
"options":["Dennis Ritchie","Guido van Rossum","James Gosling","Bjarne Stroustrup"],
"answer":"Dennis Ritchie"
},
{
"question":"Which symbol ends a statement in C?",
"options":[":",";","#","."],
"answer":";"
}
],

"dsa":[
{
"question":"Which data structure follows FIFO?",
"options":["Stack","Queue","Tree","Graph"],
"answer":"Queue"
},
{
"question":"Which data structure follows LIFO?",
"options":["Queue","Stack","Heap","Tree"],
"answer":"Stack"
}
],

"java":[
{
"question":"Who developed Java?",
"options":["James Gosling","Dennis Ritchie","Guido van Rossum","Bjarne Stroustrup"],
"answer":"James Gosling"
},
{
"question":"Java source code is compiled into?",
"options":["Machine Code","Bytecode","Assembly","Binary"],
"answer":"Bytecode"
}
]

}
def page(title, body):
    return f"""
<!DOCTYPE html>
<html>
<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>{title}</title>

<style>

*{{
margin:0;
padding:0;
box-sizing:border-box;
font-family:Segoe UI;
}}

body{{
background:linear-gradient(to bottom,#13002d,#040012);
color:white;
min-height:100vh;
}}

.container{{
width:90%;
max-width:1200px;
margin:auto;
padding:40px 20px;
}}

.logo{{
font-size:70px;
text-align:center;
}}

h1{{
font-size:60px;
text-align:center;
margin-top:10px;
}}

.subtitle{{
text-align:center;
color:#aaa;
margin-bottom:50px;
}}

.grid{{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
gap:25px;
}}

.card{{
background:#1a1037;
padding:30px;
border-radius:25px;
box-shadow:0 0 20px rgba(255,255,255,.08);
transition:.4s;
}}

.card:hover{{
transform:translateY(-8px);
}}

h2{{
margin-bottom:15px;
}}

button{{
width:100%;
padding:18px;
border:none;
border-radius:20px;
font-size:20px;
font-weight:bold;
cursor:pointer;
background:linear-gradient(to right,#8a2be2,#3a86ff);
color:white;
transition:.4s;
}}

button:hover{{
transform:scale(1.03);
}}

a{{
text-decoration:none;
}}

footer{{
margin-top:60px;
text-align:center;
color:#aaa;
}}

@media(max-width:768px){{

h1{{
font-size:42px;
}}

.logo{{
font-size:50px;
}}

}}

</style>

</head>

<body>

<div class="container">

{body}

<footer>

<br><br>

Designed & Developed by <b>ANKIT SAINI</b>

<br><br>

B.Tech IT Student at JMIT Radaur

<br><br>

Python | SQL | Cybersecurity

</footer>

</div>

</body>
</html>
"""


@app.route("/")
def home():

    return page(
        "Quizzer",

        """

<div class="logo">❓</div>

<h1>Quizzer</h1>

<div class="subtitle">
Test your programming knowledge
</div>


<div class="grid">

<div class="card">

<h2>🐍 Python Quiz</h2>

<p>Python fundamentals and programming.</p>

<br>

<a href="/quiz/python">

<button>Start Quiz</button>

</a>

</div>


<div class="card">

<h2>⚙️ C Quiz</h2>

<p>Learn C programming concepts.</p>

<br>

<a href="/quiz/c">

<button>Start Quiz</button>

</a>

</div>


<div class="card">

<h2>📚 DSA Quiz</h2>

<p>Data Structures and Algorithms.</p>

<br>

<a href="/quiz/dsa">

<button>Start Quiz</button>

</a>

</div>


<div class="card">

<h2>☕ Java Quiz</h2>

<p>Object Oriented Programming concepts.</p>

<br>

<a href="/quiz/java">

<button>Start Quiz</button>

</a>

</div>

</div>

"""
)
@app.route("/quiz/<topic>")
def quiz(topic):

    if topic not in quizzes:
        return "Quiz not found"

    questions = quizzes[topic]

    html = f"""

<div class="logo">❓</div>

<h1>{topic.upper()} Quiz</h1>

<form action="/result/{topic}" method="post">

"""

    for i, q in enumerate(questions):

        html += f"""

<div class="card">

<h2>{i+1}. {q['question']}</h2>

"""

        for option in q["options"]:

            html += f"""

<input type="radio"
name="q{i}"
value="{option}"
required>

{option}

<br><br>

"""

        html += "</div>"

    html += """

<button type="submit">

Submit Quiz

</button>

</form>

"""

    return page(topic, html)


@app.route("/result/<topic>", methods=["POST"])
def result(topic):

    questions = quizzes[topic]

    score = 0

    for i, q in enumerate(questions):

        answer = request.form.get(f"q{i}")

        if answer == q["answer"]:
            score += 1

    return page(
        "Result",

        f"""

<div class="logo">🏆</div>

<h1>Quiz Result</h1>

<div class="card">

<h2>Your Score</h2>

<h1>{score}/{len(questions)}</h1>

</div>

<div class="card">

<a href="/quiz/{topic}">

<button>

Play Again

</button>

</a>

<br><br>

<a href="/">

<button>

Back To Home

</button>

</a>

</div>

"""
    )


@app.route("/about")
def about():

    return page(
        "About",

        """

<div class="logo">ℹ️</div>

<h1>About Quizzer</h1>

<div class="card">

<h2>Quizzer</h2>

<p>

Quizzer is a professional quiz platform for
Python, C, Java and DSA.

</p>

</div>

<div class="card">

<h2>Developer</h2>

<p>

<b>ANKIT SAINI</b>

</p>

<br>

<p>

B.Tech IT Student at JMIT Radaur

</p>

<br>

<p>

Python | SQL | Cybersecurity

</p>

<br>

<p>

Email : as3126061@gmail.com

</p>

</div>

"""
    )


@app.route("/contact")
def contact():

    return page(
        "Contact",

        """

<div class="logo">📞</div>

<h1>Contact</h1>

<div class="card">

<h2>Email</h2>

<p>

as3126061@gmail.com

</p>

</div>

"""
    )


if __name__ == "__main__":
    app.run(debug=True)
    
