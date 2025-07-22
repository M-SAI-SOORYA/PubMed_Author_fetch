from typing import List, Dict


def extract_non_academic(authors: List[Dict]) -> List[Dict]:
    non_academic = []
    for a in authors:
        aff = a.get("affiliation", "").lower()
        if any(word in aff for word in ["pharma", "biotech", "inc", "ltd", "gmbh", "corp"]):
            non_academic.append(a)
   
    return non_academic


def extract_emails(authors: List[Dict]) -> str:
    for a in authors:
        if a.get("email"):
            return a["email"]
    
    return "No Email :("