#!/usr/bin/env python3
"""Small requests helper for web challenges."""

from urllib.parse import urljoin

import requests


# Cambia questo URL con l'endpoint della challenge.
BASE_URL = "http://127.0.0.1:8000/"


def make_session() -> requests.Session:
    """Crea una sessione pronta con header di base."""
    session = requests.Session()
    # Qui puoi aggiungere cookie, token o altri header comuni.
    session.headers.update({
        "User-Agent": "ctf-helper/1.0",
    })
    return session


def get(path: str, **kwargs) -> requests.Response:
    """GET con timeout e URL composto automaticamente."""
    return make_session().get(urljoin(BASE_URL, path.lstrip("/")), timeout=10, **kwargs)


def post(path: str, **kwargs) -> requests.Response:
    """POST con timeout e URL composto automaticamente."""
    return make_session().post(urljoin(BASE_URL, path.lstrip("/")), timeout=10, **kwargs)


if __name__ == "__main__":
    # Test minimo per vedere se il target risponde.
    response = get("/")
    print(response.status_code)
    print(response.text[:500])

# Uso: imposta `BASE_URL`, poi importa `get` e `post` nello script della challenge.
