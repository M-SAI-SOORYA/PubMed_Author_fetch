from get_papers.filter import filter_papers


def test_filter_papers():
    papers = [
        {
            "PubmedID": "123456",
            "Title": "Sample Study",
            "PublicationDate": "2023",
            "Authors": [
                {"name": "Dr. Biotech", "affiliation": "Moderna Inc.", "email": "mod@rna.com"},
                {"name": "Dr. Academic", "affiliation": "MIT"}
            ]
        },
        {
            "PubmedID": "654321",
            "Title": "No Company",
            "PublicationDate": "2022",
            "Authors": [
                {"name": "Dr. Uni", "affiliation": "Harvard University"}
            ]
        }
    ]
    filtered = filter_papers(papers)
    assert len(filtered) == 1
    assert filtered[0]["PubmedID"] == "123456"
