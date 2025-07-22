# fetch.py
from typing import List, Dict
import requests
from xml.etree import ElementTree
import time

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"


def fetch_pubmed_ids(query: str, retmax: int = 20) -> List[str]:
    url = f"{BASE_URL}esearch.fcgi"
    
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": retmax
    }
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    # print(resp.json()["esearchresult"]["idlist"])
    return resp.json()["esearchresult"]["idlist"]


def fetch_pubmed_details(pubmed_ids: List[str]) -> List[Dict]:
    if not pubmed_ids:
        return []
    
    url = f"{BASE_URL}efetch.fcgi"
    
    params = {
        "db": "pubmed",
        "id": ",".join(pubmed_ids),
        "retmode": "xml"
    }

    resp = requests.get(url, params=params)
   
    resp.raise_for_status()
   
    tree = ElementTree.fromstring(resp.content)
    
    papers = []
    
    for article in tree.findall(".//PubmedArticle"):
        paper = {}
        
        paper["PubmedID"] = article.findtext(".//PMID")
        paper["Title"] = article.findtext(".//ArticleTitle")
        paper["PublicationDate"] = article.findtext(".//PubDate/Year") or "Unknown"
        # print(article.findtext(".//PubDate"))

        paper["Authors"] = []
        
        
        for author in article.findall(".//Author"):
            
            last = author.findtext("LastName")
            fore = author.findtext("ForeName")
            name = f"{fore} {last}" if fore and last else None
            aff = author.findtext("AffiliationInfo/Affiliation")
            # print(author.findtext("AffiliationInfo/Affiliation"))
            email = None
            
            if aff and "@" in aff:
                email = aff.split()[-1]  # crude extraction

            if name:
                paper["Authors"].append({"name": name,"affiliation": aff,"email": email})

        papers.append(paper)
        
        time.sleep(0.34)  # NCBI rate limits

    return papers
