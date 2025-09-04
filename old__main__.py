"""Build static HTML site from directory of HTML templates and plain files."""
from __future__ import annotations
import sys
import json
import pathlib
import shutil
import click
import jinja2


@click.command(help="Templated static website generator.")
@click.argument("input_dir", nargs=1, type=click.Path(exists=True))
@click.option(
    "-o", "--output", "output_dir",
    type=click.Path(path_type=pathlib.Path),
    help="Output directory.",
)
@click.option(
    "-v", "--verbose",
    is_flag=True,
    help="Print more output.",
)
def main(input_dir, output_dir, verbose):
    """Build static HTML site from directory of HTML templates and files."""
    input_dir = pathlib.Path(input_dir)
    # print(f"DEBUG input_dir={input_dir}")

    template_dir = input_dir / "templates"
    config_path = input_dir / "config.json"
    output_dir = output_dir or pathlib.Path("generated_html")

    if output_dir.exists():
        click.echo(
            f"insta485generator error: '{output_dir}' already exists",
            err=True
        )
        sys.exit(1)

    # Read config.json
    try:
        with config_path.open(encoding="utf-8") as f:
            config_list = json.load(f)
    except FileNotFoundError:
        click.echo(
            f"insta485generator error: '{config_path}' not found",
            err=True
            )
        sys.exit(1)
    except json.JSONDecodeError as e:
        click.echo(
            f"insta485generator error: '{config_path}'\n{e}",
            err=True
            )
        click.echo(str(e), err=True)
        sys.exit(1)

    if not template_dir.exists():
        click.echo(
            f"insta485generator error: '{template_dir}' not found",
            err=True
            )
        sys.exit(1)

    # Jinja env
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(str(template_dir)),
        autoescape=jinja2.select_autoescape(["html", "xml"]),
    )

    try:    # Render each page
        for entry in config_list:
            url = (entry["url"] or "/").lstrip("/")
            tpl_name = entry["template"]
            ctx = entry.get("context", {})

            try:
                tpl = env.get_template(tpl_name)
                html = tpl.render(**ctx)
            except jinja2.exceptions.TemplateError as e:
                click.echo(
                    f"insta485generator error: '{tpl_name}'\n{e}",
                    err=True
                    )
                click.echo(str(e), err=True)
                sys.exit(1)

            out_path = (
                output_dir / "index.html") if url == "" else (
                    output_dir / url / "index.html"
                    )

            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(html, encoding="utf-8")
            if verbose:
                click.echo(f"Rendered {tpl_name} -> {out_path}")

    except FileNotFoundError as e:
        click.echo(
            f"insta485generator error: '{e.filename}' not found",
            err=True
            )
        sys.exit(1)

    # Copy static/* into output root
    static_src = input_dir / "static"
    if static_src.exists():
        for item in static_src.iterdir():
            dst = output_dir / item.name
            if item.is_dir():
                shutil.copytree(item, dst, dirs_exist_ok=True)
            else:
                shutil.copy2(item, dst)
        if verbose:
            click.echo(f"Copied {static_src} -> {output_dir}")


if __name__ == "__main__":
    main()
