"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Test Project."""


if __name__ == "__main__":
    main(prog_name="test-project")  # pragma: no cover
