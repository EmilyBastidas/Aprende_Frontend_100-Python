"""
Aplicación simple de ReactPy integrada con FastAPI
"""

from fastapi import FastAPI
from reactpy import component, html
from reactpy.backend.fastapi import configure


@component
def Navbar():
    return html.nav(
        {"class": "navbar navbar-expand-lg navbar-black bg-black"},
        html.a(
            {"class": "navbar-brand", "href": "#"},
            html.img({
                "src": "https://previews.123rf.com/images/wannasak/wannasak2308/wannasak230800399/211315790-cat-with-sunglasses-vector-illustration-of-a-cat-in-sunglasses-on-a-colorful-background.jpg",
                "width": "50",
                "alt": "Logo"
            })
        ),

        html.ul(
            {"class": "navbar-nav ml-auto "},
            html.li(
                {"class": "nav-item "},
                html.a({"class": "nav-link text-light", "href": "#"})
            ),
            html.li(
                {"class": "nav-item "},
                html.a({"class": "nav-link text-light", "href": "#"})
            ),
            html.li(
                {"class": "nav-item "},
                html.a({"class": "nav-link text-light", "href": "#"})
            ),
            html.li(
                {"class": "nav-item "},
                html.a({"class": "nav-link text-light", "href": "#"})
            ),
        )
    )


@component
def App():
    return html.div(

        # Bootstrap CSS
       html.link(
           {
               "rel": "stylesheet",
               "href": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
           }
       ),

        # FontAwesome CSS
        html.link(
            {
                "rel": "stylesheet",
                "href": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"
            }
        ),

        Navbar()
    )


app = FastAPI()
configure(app, App)



# Cada vez que hagas un cambio, guarda, detén el servidor y ejecuta, luego refresca la pestaña y listo. Para ejecutar la aplicación, usa el siguiente comando:
# uvicorn main:app 
#para activar el entorno virtual usa: source venv/bin/activate (Mac)