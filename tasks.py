from invoke import task


@task
def pdf(c, svg=False, file=""):
    if svg:
        c.run(f"latex -shell-escape {file}")
    else:
        c.run(f"latex {file}")
    c.run(f"bibtex {file}")
    c.run(f"latex {file}")
    c.run(f"latex {file}")
    c.run(f"dvips {file}")
    c.run(f"ps2pdf {file}.ps")


@task
def pdflatex(c, svg=False, file=""):
    if svg:
        c.run(f"pdflatex -shell-escape {file}")
    else:
        c.run(f"pdflatex {file}")
    c.run(f"pdflatex {file}")
    # c.run(f"bibtex {file}")
    # c.run(f"pdflatex {file}")
    # c.run(f"pdflatex {file}")
