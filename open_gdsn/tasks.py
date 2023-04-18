from invoke import task

@task
def start(c):
    c.run("python3 src/main.py", pty=True)

@task
def test(c):
    c.run("pytest src", pty=True)

@task
def coverage_report(c):
    c.run("coverage run --branch -m pytest src", pty=True)
    c.run("coverage html", pty=True)

@task
def lint(c):
    c.run("pylint src", pty=True)

@task
def format(c):
    c.run("autopep8 --in-place --recursive src", pty=True)
