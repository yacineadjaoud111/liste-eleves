from flask import Flask, render_template_string

app = Flask(__name__)

# Liste des élèves — ajoutez votre ligne ici
eleves = [
    {"prenom": "Loïc", "nom": "Dumont", "github": "loic-prof"},
    {"prenom": "Yacine", "nom": "Adjaoud", "github": "loic-prof"},
]

TEMPLATE = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Liste des élèves</title>
    <style>
        body { font-family: sans-serif; max-width: 600px; margin: 40px auto; padding: 0 20px; }
        h1 { border-bottom: 2px solid #333; padding-bottom: 8px; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th { background: #333; color: white; padding: 10px; text-align: left; }
        td { padding: 10px; border-bottom: 1px solid #ddd; }
        tr:hover { background: #f5f5f5; }
        a { color: #0066cc; text-decoration: none; }
        a:hover { text-decoration: underline; }
        .count { color: #666; font-size: 0.9em; margin-top: 10px; }
    </style>
</head>
<body>
    <h1>Liste des élèves</h1>
    <table>
        <thead>
            <tr>
                <th>Prénom</th>
                <th>Nom</th>
                <th>GitHub</th>
            </tr>
        </thead>
        <tbody>
            {% for eleve in eleves %}
            <tr>
                <td>{{ eleve.prenom }}</td>
                <td>{{ eleve.nom }}</td>
                <td>
                    <a href="https://github.com/{{ eleve.github }}" target="_blank">
                        @{{ eleve.github }}
                    </a>
                </td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    <p class="count">{{ eleves|length }} élève(s) inscrit(s)</p>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(TEMPLATE, eleves=eleves)


if __name__ == "__main__":
    app.run(debug=True)
