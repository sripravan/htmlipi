from htmlipi import template

@template
def render(r, ctx):
  with r.html():
    with r.head():
      with r.style():
        r(
        """
          body {
            background-color: #000;
            font: 1.1em Arial, Helvetica, sans-serif;
          }

          img {
            max-width: 100%;
            display: block;
          }

          figure {
            margin: 0;
            display: grid;
            grid-template-rows: 1fr auto;
          }

          figure > img {
            grid-row: 1 / -1;
            grid-column: 1;
          }

          figure a {
            color: black;
            text-decoration: none;
          }

          figcaption {
            grid-row: 2;
            grid-column: 1;
            background-color: rgba(255,255,255,.5);
            padding: .2em .5em;
            justify-self: start;
          }

          .container {
            display: grid;
            gap: 10px;
            grid-template-columns: repeat(4, 1fr);
            grid-template-rows: masonry;
          }
        """
        )
    with r.body():
      with r.div(**{"class": "container"}):
        for image in ctx.images:
          with r.figure():
            r.img(src=image["download_url"])
            with r.figcaption():
              with r.a(href="#"):
                r(image["author"])