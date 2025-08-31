"""Build static HTML site from directory of HTML templates and plain files."""

import pathlib
import click


@click.command(help="Templated static website generator.")
@click.argument("input_dir", nargs=1 , type=click.Path(exists=True))

@click.option(
    "-o", "--output", "output_dir",
    type=click.Path(file_okay=False, dir_okay=True, writable=True, path_type=pathlib.Path),
    help="Output directory.",
)
@click.option(
    "-v", "--verbose",
    is_flag=True,
    help="Print more output.",
)


def main(input_dir):
    input_dir = pathlib.Path(input_dir)
    print(f"DEBUG input_dir={input_dir}")






if __name__ == "__main__":
    main()





