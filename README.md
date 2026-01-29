# truffle.econ

A Streamlit app for browsing papers from top economics journals with JEL code visualization.

## Features

- **JEL Code Visualization**: Interactive graph mapping papers by their JEL classification codes
  - X-axis: JEL letter categories (A-Z)
  - Y-axis: JEL subcodes (0-99)
  - Each paper appears as a line connecting its JEL codes
  - Color-coded by journal

- **Paper Browser**: Browse and filter papers from top economics journals
  - Filter by journal, topic (JEL category), and publication date
  - Expandable paper cards with abstracts
  - Direct links to full text

## Journals Covered

- American Economic Review (AER)
- Quarterly Journal of Economics (QJE)
- Econometrica (ECMA)
- Journal of Political Economy (JPE)
- Review of Economic Studies (REStud)

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/truffle-econ.git
cd truffle-econ

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

## Data

The app currently includes papers from the January/February 2026 issues of the covered journals. Paper data includes:

- Title and authors
- Journal and publication details
- JEL classification codes
- Abstract
- Link to full text

## JEL Classification

The Journal of Economic Literature (JEL) classification system is used to categorize economics papers. Categories include:

- A: General Economics and Teaching
- B: History of Economic Thought
- C: Mathematical and Quantitative Methods
- D: Microeconomics
- E: Macroeconomics and Monetary Economics
- F: International Economics
- G: Financial Economics
- H: Public Economics
- I: Health, Education, and Welfare
- J: Labor and Demographic Economics
- K: Law and Economics
- L: Industrial Organization
- M: Business Administration
- N: Economic History
- O: Economic Development
- P: Economic Systems
- Q: Agricultural and Natural Resource Economics
- R: Urban, Rural, Regional Economics
- Y: Miscellaneous
- Z: Other Special Topics

## License

MIT
