import pytest
from get_papers.fetch import fetch_pubmed_ids, fetch_pubmed_details


def test_fetch_pubmed_ids():
    ids = fetch_pubmed_ids("cancer immunotherapy", retmax=5)
    assert isinstance(ids, list)
    assert len(ids) > 0
    assert all(isinstance(i, str) for i in ids)


def test_fetch_pubmed_details():
    ids = fetch_pubmed_ids("covid-19 vaccine", retmax=3)
    papers = fetch_pubmed_details(ids)
    assert isinstance(papers, list)
    assert len(papers) > 0
    for paper in papers:
        assert "PubmedID" in paper
        assert "Title" in paper
        assert "Authors" in paper