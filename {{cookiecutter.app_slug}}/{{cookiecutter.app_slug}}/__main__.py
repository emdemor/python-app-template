import click
from {{cookiecutter.app_slug}}.utils import saudation
from {{cookiecutter.app_slug}}.mymodule.hello import say_hello

@click.command()
@click.option(
    "-a",
    "--arg",
    default="ARGUMENT",
    help="First argument",
    type=str,
)
@click.option(
    "--b",
    help="Second argument",
    type=str,
)
def main(arg, b):
    """ Main function"""

    say_hello()

    print(b)

    saudation(100, arg)


if __name__ == "__main__":
    main()