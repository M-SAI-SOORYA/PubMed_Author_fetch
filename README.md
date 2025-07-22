# README.md

# 📚 PubMed Paper Fetcher

A command-line and Streamlit-based tool to fetch research papers from PubMed using advanced queries. It filters papers with at least one author affiliated with a pharmaceutical or biotech company and exports the results as a CSV.

---

## 🚀 Features

- Fetch research papers using the full PubMed API query syntax.
- Identify and extract papers with authors from non-academic institutions (e.g., biotech/pharma).
- Save results as a CSV with:
  - PubMed ID
  - Title
  - Publication Date
  - Non-academic Author(s)
  - Company Affiliation(s)
  - Corresponding Author Email
- Streamlit GUI for easy interaction
- Fully typed and tested Python codebase

---

## 🛠 Installation

Make sure you have Python 3.8+ and Poetry installed.

```bash
# Clone the repository
git clone https://github.com/your-username/pubmed-paper-fetcher.git
cd pubmed-paper-fetcher

# Install dependencies
poetry install
```

---

## 💻 Usage (Command-Line)

### 🧾 Help
```bash
poetry run get-papers-list --help
```

### 🔍 Example
```bash
poetry run get-papers-list "cancer immunotherapy" --file output.csv --debug
```

---

## 🧪 Running Tests

```bash
poetry run pytest
```

---

## 🌐 GUI App (Streamlit)

Run the Streamlit interface:
```bash
poetry run streamlit run streamlit_app.py
```

### UI Features:
- Dropdown to pick example queries
- Custom query input
- Filename input
- Download CSV button

---

## 📁 Project Structure
```
get_papers/
├── __init__.py
├── fetch.py         # Handles PubMed API fetch
├── filter.py        # Filters papers with non-academic authors
├── utils.py         # Utility functions
├── cli.py           # Typer-based CLI entry point

streamlit_app.py     # Streamlit GUI

tests/
├── test_fetch.py    # Tests for fetching functions
├── test_utils.py    # Tests for utils
├── test_filter.py   # Tests for filtering logic

pyproject.toml       # Poetry project config
```

---

## 🧰 Built With
- [Poetry](https://python-poetry.org/) – Dependency management
- [Typer](https://typer.tiangolo.com/) – CLI creation
- [Streamlit](https://streamlit.io/) – Interactive UI
- [PubMed E-utilities](https://www.ncbi.nlm.nih.gov/books/NBK25501/) – Data source
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) – XML parsing

---

## 📬 Example Queries
Try these in CLI or Streamlit:

- `cancer immunotherapy`
- `covid-19 vaccine`
- `CRISPR gene editing`
- `Alzheimer's treatment`
- `AI drug discovery`

---

## 👤 Author
**Soorya Marri**

---

## 📄 License
MIT License
