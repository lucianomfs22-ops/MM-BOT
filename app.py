from flask import Flask, render_template_string

app = Flask(__name__)

# HTML simples de demonstração
html = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>HORIZON MM</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #0f0f0f;
            color: #fff;
            text-align: center;
            padding: 50px;
        }
        img {
            width: 200px;
            border-radius: 15px;
        }
        a {
            display: inline-block;
            margin-top: 20px;
            padding: 10px 20px;
            background: #5865F2;
            color: white;
            text-decoration: none;
            border-radius: 10px;
        }
        a:hover {
            background: #4752C4;
        }
    </style>
</head>
<body>
    <h1>🚀 Bem-vindo à Horizon MM!</h1>
    <p>Aqui temos middleman confiável por um preço super barato!</p>
    <img src="https://cdn.discordapp.com/attachments/1412843907871543311/1416166331962757170/file_00000000ce54622f9c17ded6cda5f09e.png" alt="Logo">
    <br>
    <a href="https://discord.gg/horizontrades" target="_blank">Entrar no Discord</a>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
