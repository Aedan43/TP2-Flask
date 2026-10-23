
import os

from flask import Flask, abort, flash, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "0b3b75e53e383458c7260c27eea651802c622e421e467d91e24363274daf0603"
taches = [
    {"id": 1, "titre": "Réviser les décorateurs",
     "priorite": "haute", "terminee": False},
    {"id": 2, "titre": "Installer Flask",
     "priorite": "normale", "terminee": True},
    {"id": 3, "titre": "Lire la doc Jinja2",
     "priorite": "basse", "terminee": False},
]

@app.route("/")
def index():
    filtre = request.args.get("filtre")
    if filtre is None:
        filtre = session.get("filtre", "toutes")
    session["filtre"] = filtre

    if filtre == "actives":
        taches_filtrees = [t for t in taches if not t["terminee"]]
    elif filtre == "terminees":
        taches_filtrees = [t for t in taches if t["terminee"]]
    else:
        taches_filtrees = taches

    return render_template("taches.html", taches=taches_filtrees)


@app.route("/taches/<int:id>")
def tache(id):
    for t in taches:
        if t["id"] == id:
            return t["titre"]
    abort(404)


@app.route("/taches/ajouter", methods=["GET", "POST"])
def ajouter():
    if request.method == "POST":
        titre = request.form.get("titre", "").strip()
        priorite = request.form.get("priorite", "normale")

        if not titre or len(titre) > 80 or priorite not in ["basse", "normale", "haute"]:
            return render_template("ajouter.html")

        nouvel_id = max((t["id"] for t in taches), default=0) + 1
        taches.append({
            "id": nouvel_id,
            "titre": titre,
            "priorite": priorite,
            "terminee": False
        })
        flash("Tâche ajoutée")
        return redirect(url_for("index"))
    return render_template("ajouter.html")


@app.post("/taches/<int:id>/terminer")
def terminer(id):
    tache_a_terminer = next((t for t in taches if t["id"] == id), None)
    if tache_a_terminer is None:
        abort(404)

    tache_a_terminer["terminee"] = True
    return redirect(url_for("index"))


@app.post("/taches/<int:id>/supprimer")
def supprimer(id):
    tache_a_supprimer = next((t for t in taches if t["id"] == id), None)
    if tache_a_supprimer is None:
        abort(404)

    taches.remove(tache_a_supprimer)
    return redirect(url_for("index"))


@app.errorhandler(404)
def page_introuvable(erreur):
    return render_template("404.html"), 404


@app.route("/api/taches")
def api_taches():
    return taches
