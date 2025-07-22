import typer
import csv
from typing import Optional
from get_papers.fetch import fetch_pubmed_ids, fetch_pubmed_details
from get_papers.filter import filter_papers

app = typer.Typer()

@app.command()
def get(
    query: str,
    file: Optional[str] = typer.Option(None, "--file", "-f"),
    debug: bool = typer.Option(False, "--debug", "-d")
):
    """Fetch and filter PubMed papers based on query."""
    try:
        if debug:
            typer.echo(f"Fetching IDs for query: {query}")

        ids = fetch_pubmed_ids(query)
        if debug:
            typer.echo(f"Found {len(ids)} IDs")

        papers = fetch_pubmed_details(ids)
     
        filtered = filter_papers(papers)

        if file:
            with open(file, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=list(filtered[0].keys()))
                writer.writeheader()
                writer.writerows(filtered)
            typer.echo(f"Saved {len(filtered)} results to {file}")
        else:
            for row in filtered:
                typer.echo(row)

    except Exception as e:
        typer.echo(f"Error: {e}", err=True)

if __name__ == "__main__":
    app()