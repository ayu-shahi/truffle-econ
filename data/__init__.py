# Data module for truffle.econ
from .jel_codes import JEL_CODES, JEL_CATEGORIES, JEL_LETTERS, get_jel_description, get_category_name, parse_jel_code
from .papers import (
    Paper, PAPERS_2026, JOURNAL_COLORS, JOURNAL_ABBREVIATIONS,
    get_all_papers, get_papers_by_journal, get_papers_by_month,
    get_unique_jel_codes, get_journals
)
