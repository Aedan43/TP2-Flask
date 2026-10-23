# Journal de découverte — Maria CHEMLAL

## Mission 1 — Faire tourner Flask

**Ma découverte :** j’ai provoqué une erreur en ajoutant `+ 1` à un texte. Flask m’a montré où le code ne fonctionnait plus. En mode debug, il recharge aussi l’application après une modification. J’ai compris que ce mode m’aide pendant le développement, mais qu’il ne faut pas l’utiliser en production.

**Références :** Flask — [Installation](https://flask.palletsprojects.com/en/stable/installation/) ; Quickstart — [A Minimal Application](https://flask.palletsprojects.com/en/stable/quickstart/#a-minimal-application) et [Debug Mode](https://flask.palletsprojects.com/en/stable/quickstart/#debug-mode).

## Mission 2 — Comprendre les URL

**Ma découverte :** avec `<id>`, Flask reçoit l’identifiant comme du texte, alors que les identifiants de ma liste sont des nombres. La tâche n’était donc pas retrouvée. Avec `<int:id>`, Flask convertit l’identifiant en nombre. J’ai aussi compris qu’une tâche absente doit renvoyer une vraie erreur 404, pas seulement afficher un message « introuvable ».

**Références :** Flask Quickstart — [Variable Rules](https://flask.palletsprojects.com/en/stable/quickstart/#variable-rules) et [Redirects and Errors](https://flask.palletsprojects.com/en/stable/quickstart/#redirects-and-errors).

## Mission 3 — Afficher les tâches avec Jinja

**Ma découverte :** j’ai mis `<b>Important</b>` dans un titre, mais le navigateur a affiché les balises au lieu de mettre le texte en gras. J’ai compris que Jinja protège la page en affichant le contenu d’une variable comme du texte, et non comme du code HTML.

**Références :** Flask Quickstart — [Rendering Templates](https://flask.palletsprojects.com/en/stable/quickstart/#rendering-templates) ; Jinja — [Variables](https://jinja.palletsprojects.com/en/stable/templates/#variables) et [HTML Escaping](https://jinja.palletsprojects.com/en/stable/templates/#html-escaping).

## Mission 4 — Partager la mise en page

**Ma découverte :** j’ai utilisé `url_for('ajouter')` avant de créer la route `ajouter`. Flask a affiché une `BuildError` parce qu’il ne trouvait pas cette route. J’ai compris que le nom passé à `url_for` doit correspondre à une route existante. L’héritage de templates me permet ensuite de partager le menu entre les pages.

**Références :** Jinja — [Template Inheritance](https://jinja.palletsprojects.com/en/stable/templates/#template-inheritance) ; Flask Quickstart — [Static Files](https://flask.palletsprojects.com/en/stable/quickstart/#static-files).

## Mission 5 — Ajouter une tâche avec un formulaire

**Ma découverte :** sans redirection après l’envoi du formulaire, F5 me proposait de renvoyer le POST. J’ai compris qu’en redirigeant vers une page GET après l’ajout, l’actualisation ne renvoie pas le formulaire et n’ajoute pas la tâche une deuxième fois.

**Références :** Flask Quickstart — [HTTP Methods](https://flask.palletsprojects.com/en/stable/quickstart/#http-methods), [Accessing Request Data](https://flask.palletsprojects.com/en/stable/quickstart/#accessing-request-data) et [Redirects and Errors](https://flask.palletsprojects.com/en/stable/quickstart/#redirects-and-errors).

## Mission 6 — Utiliser les messages et la session

**Ma découverte :** après avoir modifié le cookie `session`, Flask ne l’a plus accepté et a repris le filtre par défaut. J’ai compris que Flask signe le cookie avec la clé secrète : si le contenu change, la signature ne correspond plus. Les messages flash permettent, eux, d’afficher un message après une redirection.

**Références :** Flask Quickstart — [Sessions](https://flask.palletsprojects.com/en/stable/quickstart/#sessions) et [Message Flashing](https://flask.palletsprojects.com/en/stable/quickstart/#message-flashing).

## Bonus — Renvoyer une réponse JSON

**Ma découverte :** en ouvrant `/api/taches`, j’ai vu la liste au format JSON. Flask peut transformer en réponse JSON les données renvoyées par une route.

**Référence :** Flask Quickstart — [About Responses](https://flask.palletsprojects.com/en/stable/quickstart/#about-responses).
