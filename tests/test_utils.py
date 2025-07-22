from get_papers.utils import extract_non_academic, extract_emails

def test_extract_non_academic():
    authors = [
        {"name": "Dr. X", "affiliation": "Pfizer Inc."},
        {"name": "Dr. Y", "affiliation": "University of California"},
    ]
    result = extract_non_academic(authors)
    assert len(result) == 1
    assert result[0]["name"] == "Dr. X"


def test_extract_emails():
    authors = [
        {"name": "Dr. A", "email": "a@example.com"},
        {"name": "Dr. B"}
    ]
    email = extract_emails(authors)
    assert email == "a@example.com"


