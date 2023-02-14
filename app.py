from flask import Flask, render_template

app = Flask(__name__)

#POSTS MOCK
post = [
    {
        "Titulo": "Post 1",
        "texto":"Meu primeiro post"
},
{       "Titulo": "Post 2","texto":"Olha eu aqui de novo"
    }
]

@app.route("/")
def exibir_entradas():
    return render_template("exibir_entradas.html",entradas = post)

