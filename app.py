"""
truffle.econ - Top Economics Journals Paper Browser

A Streamlit app for browsing papers from top economics journals,
with JEL code visualization.
"""

import streamlit as st
import plotly.graph_objects as go
from collections import defaultdict
import sys
import os

# Add the current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data.jel_codes import (
    JEL_CODES, JEL_CATEGORIES, JEL_LETTERS,
    get_jel_description, get_category_name, parse_jel_code
)
from data.papers import (
    PAPERS_2026, JOURNAL_COLORS, JOURNAL_ABBREVIATIONS,
    get_all_papers, get_journals
)

# Short names for journals (used in checkboxes and legend)
JOURNAL_SHORT_NAMES = {
    "American Economic Review": "AER",
    "Quarterly Journal of Economics": "QJE",
    "Journal of Political Economy": "JPE",
    "Review of Economic Studies": "REStud",
    "Econometrica": "Econometrica",
}

# Page configuration
st.set_page_config(
    page_title="truffle.econ",
    page_icon="🍄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for clean white theme with Tiempos-like font
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Source+Serif+Pro:wght@400;600;700&display=swap');

    /* Main background and text colors - clean white theme */
    .stApp {
        background-color: #ffffff;
        color: #1a1a1a;
    }

    /* Use Source Serif Pro as Tiempos alternative */
    body, .stMarkdown, p, span, div {
        font-family: 'Source Serif Pro', Georgia, 'Times New Roman', serif;
    }

    /* Header styling */
    .main-header {
        font-family: 'Source Serif Pro', Georgia, serif;
        font-size: 2.2rem;
        font-weight: 700;
        color: #1a1a1a;
        margin-bottom: 0.2rem;
        letter-spacing: 0.5px;
    }

    .sub-header {
        font-family: 'Source Serif Pro', Georgia, serif;
        font-size: 1rem;
        color: #666;
        margin-top: 0;
        font-weight: 400;
    }

    /* Legend styling - horizontal layout */
    .legend-box {
        display: flex;
        flex-wrap: wrap;
        gap: 1.5rem;
        padding: 0.75rem 0;
        margin-bottom: 1rem;
        border-bottom: 1px solid #e0e0e0;
    }

    .legend-entry {
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .legend-line {
        width: 24px;
        height: 3px;
        border-radius: 2px;
    }

    .legend-label {
        font-size: 0.85rem;
        color: #333;
        font-weight: 500;
    }

    /* Paper card styling */
    .paper-title-text {
        font-family: 'Source Serif Pro', Georgia, serif;
        font-size: 1.05rem;
        font-weight: 600;
        color: #1a1a1a;
        line-height: 1.4;
    }

    .paper-authors {
        font-size: 0.9rem;
        color: #555;
        margin: 0.3rem 0;
        font-style: italic;
    }

    .paper-meta {
        font-size: 0.85rem;
        color: #666;
        margin: 0.5rem 0;
    }

    .journal-badge {
        display: inline-block;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-right: 0.5rem;
    }

    .jel-tag {
        display: inline-block;
        background-color: #f5f5f5;
        color: #333;
        font-size: 0.75rem;
        padding: 2px 6px;
        border-radius: 3px;
        margin-right: 4px;
        margin-bottom: 4px;
        font-family: 'Consolas', 'Monaco', monospace;
        border: 1px solid #ddd;
    }

    .abstract-text {
        font-size: 0.9rem;
        color: #444;
        line-height: 1.6;
        margin-top: 0.5rem;
        text-align: justify;
    }

    /* Filter section styling */
    .filter-label {
        font-size: 0.85rem;
        font-weight: 600;
        color: #333;
        margin-bottom: 0.5rem;
    }

    /* Section headers */
    .section-header {
        font-family: 'Source Serif Pro', Georgia, serif;
        font-size: 1.3rem;
        font-weight: 700;
        color: #1a1a1a;
        margin: 1.5rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #1a1a1a;
    }

    /* Stats display */
    .stats-text {
        font-size: 0.85rem;
        color: #888;
        text-align: right;
        margin-bottom: 0.5rem;
    }

    /* Link styling */
    a {
        color: #0066cc !important;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Streamlit checkbox overrides - fix for mobile visibility */
    .stCheckbox label {
        font-family: 'Source Serif Pro', Georgia, serif !important;
        font-size: 0.9rem !important;
        color: #333 !important;
    }

    .stCheckbox label p {
        color: #333 !important;
    }

    .stCheckbox label span {
        color: #333 !important;
    }

    /* Ensure checkbox text is visible on all devices */
    [data-testid="stCheckbox"] label {
        color: #333 !important;
    }

    [data-testid="stCheckbox"] p {
        color: #333 !important;
    }

    .stSelectbox label {
        font-family: 'Source Serif Pro', Georgia, serif !important;
        color: #333 !important;
    }

    /* Expander styling */
    .streamlit-expanderHeader {
        font-family: 'Source Serif Pro', Georgia, serif !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
        color: #1a1a1a !important;
    }

    div[data-testid="stExpander"] {
        border: 1px solid #e0e0e0;
        border-radius: 4px;
        margin-bottom: 0.5rem;
    }

    /* Footer */
    .footer-text {
        text-align: center;
        color: #999;
        font-size: 0.8rem;
        margin-top: 3rem;
        padding: 1.5rem;
        border-top: 1px solid #e0e0e0;
    }

    /* Journal header in papers section */
    .journal-header {
        font-family: 'Source Serif Pro', Georgia, serif;
        font-weight: 600;
        margin-top: 1.5rem;
        margin-bottom: 0.75rem;
    }
</style>
""", unsafe_allow_html=True)


def create_jel_visualization(papers, highlighted_paper_idx=None):
    """Create the JEL code visualization using Plotly."""

    fig = go.Figure()

    # Create a mapping from JEL letter to x position
    letter_to_x = {letter: i for i, letter in enumerate(JEL_LETTERS)}

    # First, add a background grid of all possible JEL points (subtle)
    grid_x, grid_y, grid_text = [], [], []
    for i, letter in enumerate(JEL_LETTERS):
        for num in range(0, 100, 5):  # Every 5 for grid points
            code = f"{letter}{num:02d}"
            desc = get_jel_description(code)
            grid_x.append(i)
            grid_y.append(num)
            if desc != "Unknown":
                grid_text.append(f"<b>{code}</b><br>{desc}")
            else:
                # Try to get category description
                cat_desc = get_category_name(letter)
                grid_text.append(f"<b>{code}</b><br>{cat_desc}")

    # Add invisible grid points for hover
    fig.add_trace(go.Scatter(
        x=grid_x,
        y=grid_y,
        mode='markers',
        marker=dict(size=8, color='rgba(200,200,200,0.3)', symbol='square'),
        hovertemplate='%{text}<extra></extra>',
        text=grid_text,
        showlegend=False,
        name='JEL Grid'
    ))

    # Add lines for each paper connecting its JEL codes
    for paper_idx, paper in enumerate(papers):
        if not paper.jel_codes:
            continue

        # Parse JEL codes to coordinates
        coords = []
        for code in paper.jel_codes:
            letter, number = parse_jel_code(code)
            if letter in letter_to_x:
                x = letter_to_x[letter]
                y = number
                coords.append((x, y, code))

        if len(coords) < 1:
            continue

        # Get journal color
        color = JOURNAL_COLORS.get(paper.journal, "#888888")
        abbrev = JOURNAL_SHORT_NAMES.get(paper.journal, paper.journal[:3])

        # Determine if this paper is highlighted
        is_highlighted = highlighted_paper_idx is not None and paper_idx == highlighted_paper_idx

        # Set opacity based on highlight state
        if highlighted_paper_idx is not None:
            opacity = 1.0 if is_highlighted else 0.15
            line_width = 4 if is_highlighted else 1.5
            marker_size = 10 if is_highlighted else 5
        else:
            opacity = 0.8
            line_width = 2
            marker_size = 6

        # Sort coords by x then y for consistent drawing
        coords.sort(key=lambda c: (c[0], c[1]))

        # Build JEL codes string for hover
        jel_codes_str = ", ".join([c[2] for c in coords])

        # Create hover text with paper info
        hover_text = (
            f"<b>{paper.title}</b><br>"
            f"<i>{abbrev}</i><br>"
            f"JEL: {jel_codes_str}"
        )

        xs = [c[0] for c in coords]
        ys = [c[1] for c in coords]

        fig.add_trace(go.Scatter(
            x=xs,
            y=ys,
            mode='lines+markers',
            line=dict(color=color, width=line_width),
            marker=dict(size=marker_size, color=color),
            opacity=opacity,
            hovertemplate=hover_text + '<extra></extra>',
            customdata=[paper_idx] * len(coords),
            showlegend=False,
            name=paper.title[:30]
        ))

    # Configure layout for clean white theme
    fig.update_layout(
        plot_bgcolor='#fafafa',
        paper_bgcolor='#ffffff',
        font=dict(color='#333', family='Source Serif Pro, Georgia, serif'),
        xaxis=dict(
            tickmode='array',
            tickvals=list(range(len(JEL_LETTERS))),
            ticktext=JEL_LETTERS,
            title=None,
            gridcolor='#e8e8e8',
            showgrid=True,
            zeroline=False,
            tickfont=dict(size=11, color='#555'),
            side='top',
            fixedrange=True,  # Disable zoom
        ),
        yaxis=dict(
            title=None,
            range=[-2, 100],
            gridcolor='#e8e8e8',
            showgrid=True,
            zeroline=False,
            tickfont=dict(size=10, color='#555'),
            dtick=10,
            fixedrange=True,  # Disable zoom
        ),
        margin=dict(l=40, r=20, t=40, b=20),
        height=450,
        hovermode='closest',
        showlegend=False,
        dragmode=False,  # Disable drag/selection
    )

    return fig


def create_legend_html():
    """Create the journal color legend as HTML."""
    items = []
    for journal, color in JOURNAL_COLORS.items():
        short_name = JOURNAL_SHORT_NAMES.get(journal, journal[:3])
        items.append(
            f'<div class="legend-entry">'
            f'<div class="legend-line" style="background-color: {color};"></div>'
            f'<span class="legend-label">{short_name}</span>'
            f'</div>'
        )
    return '<div class="legend-box">' + ''.join(items) + '</div>'


def display_paper(paper, paper_id):
    """Display a paper as an expandable section."""
    color = JOURNAL_COLORS.get(paper.journal, "#888888")
    abbrev = JOURNAL_SHORT_NAMES.get(paper.journal, paper.journal[:3])

    with st.expander(paper.title, expanded=False):
        # Authors
        st.markdown(f'<p class="paper-authors">{", ".join(paper.authors)}</p>',
                   unsafe_allow_html=True)

        # Journal badge and metadata
        meta_html = (
            f'<span class="journal-badge" style="background-color: {color}22; '
            f'border: 1px solid {color}; color: {color};">{abbrev}</span>'
            f'<span class="paper-meta">'
        )

        if paper.volume:
            meta_html += f'Vol. {paper.volume}'
        if paper.issue:
            meta_html += f', No. {paper.issue}'
        if paper.pages:
            meta_html += f', pp. {paper.pages}'
        meta_html += f' ({paper.month}/{paper.year})</span>'

        st.markdown(meta_html, unsafe_allow_html=True)

        # JEL codes
        jel_html = ''.join([f'<span class="jel-tag">{code}</span>' for code in paper.jel_codes])
        st.markdown(f'<div style="margin: 0.75rem 0;">{jel_html}</div>', unsafe_allow_html=True)

        # Abstract
        if paper.abstract:
            st.markdown(f'<p class="abstract-text">{paper.abstract}</p>', unsafe_allow_html=True)

        # Link to full text
        if paper.url:
            st.markdown(f'[Read full text →]({paper.url})')


def main():
    # Header
    st.markdown('<h1 class="main-header">truffle.econ</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Browse the latest from top economics journals</p>', unsafe_allow_html=True)

    # Get all papers and journals
    all_papers = get_all_papers()
    journals = get_journals()

    # Legend
    st.markdown(create_legend_html(), unsafe_allow_html=True)

    # === FILTERS FOR GRAPH ===
    st.markdown('<p class="filter-label">Filter journals:</p>', unsafe_allow_html=True)

    # Initialize session state for graph journal checkbox keys
    for i, journal in enumerate(journals):
        key = f"graph_journal_{i}"
        if key not in st.session_state:
            st.session_state[key] = True

    # Deselect All button for graph
    deselect_col, spacer_col = st.columns([1, 4])
    with deselect_col:
        if st.button("Deselect All", key="deselect_all_graph"):
            for i in range(len(journals)):
                st.session_state[f"graph_journal_{i}"] = False
            st.rerun()

    # Journal checkboxes in a row
    journal_cols = st.columns(5)
    selected_journals = []

    for i, journal in enumerate(journals):
        short_name = JOURNAL_SHORT_NAMES.get(journal, journal[:3])
        with journal_cols[i]:
            checked = st.checkbox(
                short_name,
                key=f"graph_journal_{i}"
            )
            if checked:
                selected_journals.append(journal)

    # Month filter dropdown
    month_options = sorted(set((p.year, p.month) for p in all_papers), reverse=True)
    month_labels = ["All months"] + [f"{m:02d}/{y}" for y, m in month_options]
    month_values = [None] + list(month_options)

    col1, col2, col3 = st.columns([1, 1, 2])
    with col1:
        selected_month_idx = st.selectbox(
            "Month/Year",
            options=range(len(month_labels)),
            format_func=lambda x: month_labels[x],
            key="graph_month_filter"
        )
    selected_month = month_values[selected_month_idx]

    # Filter papers for graph
    graph_papers = all_papers.copy()

    if selected_journals:
        graph_papers = [p for p in graph_papers if p.journal in selected_journals]
    else:
        graph_papers = []

    if selected_month:
        graph_papers = [p for p in graph_papers if (p.year, p.month) == selected_month]

    # Stats
    with col3:
        st.markdown(
            f'<p class="stats-text">{len(graph_papers)} papers displayed</p>',
            unsafe_allow_html=True
        )

    # JEL Visualization
    fig = create_jel_visualization(graph_papers)

    # Display chart with disabled interactivity except hover
    st.plotly_chart(
        fig,
        width="stretch",
        config={
            'displayModeBar': False,
            'scrollZoom': False,
            'doubleClick': False,
        }
    )

    # === PAPERS SECTION ===
    st.markdown('<h2 class="section-header">Papers</h2>', unsafe_allow_html=True)

    # Filters for papers section
    st.markdown('<p class="filter-label">Filter papers:</p>', unsafe_allow_html=True)

    # Initialize session state for paper journal checkbox keys
    for i, journal in enumerate(journals):
        key = f"paper_journal_{i}"
        if key not in st.session_state:
            st.session_state[key] = True

    # Deselect All button for papers
    deselect_paper_col, spacer_paper_col = st.columns([1, 4])
    with deselect_paper_col:
        if st.button("Deselect All", key="deselect_all_papers"):
            for i in range(len(journals)):
                st.session_state[f"paper_journal_{i}"] = False
            st.rerun()

    # Journal checkboxes for papers
    paper_journal_cols = st.columns(5)
    paper_selected_journals = []

    for i, journal in enumerate(journals):
        short_name = JOURNAL_SHORT_NAMES.get(journal, journal[:3])
        with paper_journal_cols[i]:
            checked = st.checkbox(
                short_name,
                key=f"paper_journal_{i}"
            )
            if checked:
                paper_selected_journals.append(journal)

    # Month dropdown for papers
    pcol1, pcol2, pcol3 = st.columns([1, 1, 2])
    with pcol1:
        paper_month_idx = st.selectbox(
            "Issue",
            options=range(len(month_labels)),
            format_func=lambda x: month_labels[x],
            key="paper_month_filter"
        )
    paper_selected_month = month_values[paper_month_idx]

    # Filter papers
    filtered_papers = all_papers.copy()

    if paper_selected_journals:
        filtered_papers = [p for p in filtered_papers if p.journal in paper_selected_journals]
    else:
        filtered_papers = []

    if paper_selected_month:
        filtered_papers = [p for p in filtered_papers if (p.year, p.month) == paper_selected_month]

    # Sort by journal then by title
    filtered_papers.sort(key=lambda p: (p.journal, p.title))

    # Display count
    with pcol3:
        st.markdown(
            f'<p class="stats-text">{len(filtered_papers)} papers</p>',
            unsafe_allow_html=True
        )

    # Display papers grouped by journal (use FULL journal name in header)
    current_journal = None
    for idx, paper in enumerate(filtered_papers):
        if paper.journal != current_journal:
            current_journal = paper.journal
            color = JOURNAL_COLORS.get(current_journal, "#888")
            # Use FULL journal name for headers
            st.markdown(
                f'<h3 class="journal-header" style="color: {color};">'
                f'{current_journal}</h3>',
                unsafe_allow_html=True
            )
        display_paper(paper, f"paper_{idx}")

    # Footer
    st.markdown(
        '<div class="footer-text">'
        'truffle.econ · Created by Ayush Shahi'
        '</div>',
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
