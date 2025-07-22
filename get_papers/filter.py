from typing import List, Dict
from get_papers.utils import extract_non_academic, extract_emails

def filter_papers(papers: List[Dict]) -> List[Dict]:
    results = []
    
    for paper in papers:
        
        non_acad_authors = extract_non_academic(paper.get("Authors", []))
        
        if not non_acad_authors:
            continue

        companies = list({a.get("affiliation") for a in non_acad_authors})
        
        names = [a["name"] for a in non_acad_authors]
        
        email = extract_emails(paper.get("Authors", []))

        results.append({
            "PubmedID": paper["PubmedID"],
            "Title": paper["Title"],
            "Publication Date": paper["PublicationDate"],
            "Non-academic Author(s)": "; ".join(names),
            "Company Affiliation(s)": "; ".join(companies),
            "Corresponding Author Email": email
        })
        
    return results
