"""
truffle.econ - Top Economics Journals Paper Browser

A Streamlit app for browsing papers from top economics journals,
with JEL code visualization.
"""

import streamlit as st
import plotly.graph_objects as go
import pandas as pd
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

# Page configuration
st.set_page_config(
    page_title="truffle.econ",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for dark theme matching the reference design
st.markdown("""
<style>
    /* Main background and text colors */
    .stApp {
        background-color: #0a0a0a;
        color: #00ff88;
    }

    /* Header styling */
    .main-header {
        font-family: 'Courier New', monospace;
        font-size: 2.5rem;
        font-weight: bold;
        color: #00ff88;
        margin-bottom: 0;
        letter-spacing: 2px;
    }

    .sub-header {
        font-family: 'Courier New', monospace;
        font-size: 0.9rem;
        color: #666;
        margin-top: 0;
    }

    /* Card styling for papers */
    .paper-card {
        background-color: #111;
        border: 1px solid #00ff88;
        border-radius: 8px;
        padding: 1rem;
        margin-bottom: 1rem;
    }

    .paper-title {
        color: #00ff88;
        font-size: 1.1rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }

    .paper-authors {
        color: #888;
        font-size: 0.9rem;
        margin-bottom: 0.5rem;
    }

    .paper-journal {
        font-size: 0.8rem;
        padding: 2px 8px;
        border-radius: 4px;
        display: inline-block;
        margin-right: 8px;
    }

    .jel-code {
        background-color: #222;
        color: #00ff88;
        font-size: 0.75rem;
        padding: 2px 6px;
        border-radius: 3px;
        margin-right: 4px;
        font-family: 'Courier New', monospace;
    }

    /* Legend styling */
    .legend-container {
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
        margin: 1rem 0;
        padding: 0.5rem;
        background-color: #111;
        border-radius: 4px;
    }

    .legend-item {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        font-size: 0.8rem;
    }

    .legend-color {
        width: 20px;
        height: 3px;
        border-radius: 1px;
    }

    /* Filter section */
    .filter-section {
        background-color: #111;
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
    }

    /* Stats display */
    .stats-display {
        font-family: 'Courier New', monospace;
        font-size: 0.8rem;
        color: #666;
        text-align: right;
    }

    /* Streamlit overrides */
    .stSelectbox label, .stMultiSelect label {
        color: #00ff88 !important;
    }

    .stExpander {
        background-color: #111;
        border: 1px solid #333;
    }

    div[data-testid="stExpander"] details summary p {
        color: #00ff88;
    }

    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }

    ::-webkit-scrollbar-track {
        background: #111;
    }

    ::-webkit-scrollbar-thumb {
        background: #00ff88;
        border-radius: 4px;
    }

    /* Link styling */
    a {
        color: #00ff88 !important;
    }

    a:hover {
        color: #00ffaa !important;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Footer text */
    .footer-text {
        text-align: center;
        color: #444;
        font-size: 0.8rem;
        margin-top: 2rem;
        padding: 1rem;
        border-top: 1px solid #222;
    }
</style>
""", unsafe_allow_html=True)


def create_jel_visualization(papers, selected_paper_idx=None):
    """Create the JEL code visualization using Plotly."""

    fig = go.Figure()

    # Create a mapping from JEL letter to x position
    letter_to_x = {letter: i for i, letter in enumerate(JEL_LETTERS)}

    # Track which points have papers for hover info
    point_papers = defaultdict(list)

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
                point_papers[(x, y)].append((paper.title, code, paper_idx))

        if len(coords) < 1:
            continue

        # Get journal color
        color = JOURNAL_COLORS.get(paper.journal, "#888888")

        # Determine line width and opacity
        is_selected = selected_paper_idx is not None and paper_idx == selected_paper_idx
        line_width = 3 if is_selected else 1.5
        opacity = 1.0 if is_selected or selected_paper_idx is None else 0.3

        # Sort coords by x then y for consistent drawing
        coords.sort(key=lambda c: (c[0], c[1]))

        # Draw lines connecting JEL codes
        if len(coords) >= 2:
            xs = [c[0] for c in coords]
            ys = [c[1] for c in coords]

            fig.add_trace(go.Scatter(
                x=xs,
                y=ys,
                mode='lines+markers',
                line=dict(color=color, width=line_width),
                marker=dict(size=6 if is_selected else 4, color=color),
                opacity=opacity,
                name=paper.title[:40] + "..." if len(paper.title) > 40 else paper.title,
                hovertemplate=f"<b>{paper.title[:50]}...</b><br>" +
                             f"Journal: {JOURNAL_ABBREVIATIONS.get(paper.journal, paper.journal)}<br>" +
                             "JEL: %{text}<extra></extra>",
                text=[c[2] for c in coords],
                customdata=[paper_idx] * len(coords),
                showlegend=False
            ))
        else:
            # Single JEL code - just a point
            fig.add_trace(go.Scatter(
                x=[coords[0][0]],
                y=[coords[0][1]],
                mode='markers',
                marker=dict(size=8 if is_selected else 5, color=color),
                opacity=opacity,
                name=paper.title[:40] + "..." if len(paper.title) > 40 else paper.title,
                hovertemplate=f"<b>{paper.title[:50]}...</b><br>" +
                             f"Journal: {JOURNAL_ABBREVIATIONS.get(paper.journal, paper.journal)}<br>" +
                             f"JEL: {coords[0][2]}<extra></extra>",
                customdata=[paper_idx],
                showlegend=False
            ))

    # Add invisible scatter for all JEL points to show hover info
    all_x, all_y, all_text = [], [], []
    for i, letter in enumerate(JEL_LETTERS):
        for num in range(0, 100, 10):  # Sample every 10 for cleaner display
            code = f"{letter}{num:02d}"
            desc = get_jel_description(code)
            if desc != "Unknown":
                all_x.append(i)
                all_y.append(num)
                all_text.append(f"{code}: {desc}")

    # Configure layout for dark theme
    fig.update_layout(
        plot_bgcolor='#0a0a0a',
        paper_bgcolor='#0a0a0a',
        font=dict(color='#00ff88', family='Courier New'),
        xaxis=dict(
            tickmode='array',
            tickvals=list(range(len(JEL_LETTERS))),
            ticktext=JEL_LETTERS,
            title=None,
            gridcolor='#222',
            showgrid=True,
            zeroline=False,
            tickfont=dict(size=10),
        ),
        yaxis=dict(
            title=None,
            range=[100, -5],  # Inverted so 0 is at top
            gridcolor='#222',
            showgrid=True,
            zeroline=False,
            tickfont=dict(size=10),
            dtick=10,
        ),
        margin=dict(l=40, r=20, t=30, b=40),
        height=400,
        hovermode='closest',
        showlegend=False,
    )

    return fig


def create_legend():
    """Create the journal color legend."""
    legend_html = '<div class="legend-container">'
    for journal, color in JOURNAL_COLORS.items():
        abbrev = JOURNAL_ABBREVIATIONS.get(journal, journal[:3])
        legend_html += f'''
            <div class="legend-item">
                <div class="legend-color" style="background-color: {color};"></div>
                <span style="color: {color};">{abbrev}</span>
            </div>
        '''
    legend_html += '</div>'
    return legend_html


def display_paper_card(paper, idx):
    """Display a paper as an expandable card."""
    color = JOURNAL_COLORS.get(paper.journal, "#888888")
    abbrev = JOURNAL_ABBREVIATIONS.get(paper.journal, paper.journal[:3])

    # Create expander for each paper
    with st.expander(f"**{paper.title}**", expanded=False):
        # Authors
        st.markdown(f"*{', '.join(paper.authors)}*")

        # Journal and date
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(
                f'<span class="paper-journal" style="background-color: {color}22; '
                f'border: 1px solid {color}; color: {color};">{abbrev}</span>'
                f'<span style="color: #666; font-size: 0.8rem;">'
                f'{paper.month:02d}/{paper.year}'
                f'{" • Vol. " + str(paper.volume) if paper.volume else ""}'
                f'{", No. " + str(paper.issue) if paper.issue else ""}'
                f'{" • pp. " + paper.pages if paper.pages else ""}</span>',
                unsafe_allow_html=True
            )
        with col2:
            if paper.url:
                st.markdown(f'[📄 Full Text]({paper.url})')

        # JEL codes
        jel_html = " ".join([f'<span class="jel-code">{code}</span>' for code in paper.jel_codes])
        st.markdown(f'<div style="margin: 0.5rem 0;">{jel_html}</div>', unsafe_allow_html=True)

        # Abstract
        if paper.abstract:
            st.markdown("**Abstract:**")
            st.markdown(f'<p style="color: #aaa; font-size: 0.9rem;">{paper.abstract}</p>',
                       unsafe_allow_html=True)


def main():
    # Header
    st.markdown('<h1 class="main-header">TRUFFLE.ECON</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">JEL CODE MAP</p>', unsafe_allow_html=True)

    # Get all papers
    all_papers = get_all_papers()
    journals = get_journals()

    # Create legend
    st.markdown(create_legend(), unsafe_allow_html=True)

    # Sidebar filters (but we'll put them in main area for this design)
    col_filter1, col_filter2, col_filter3 = st.columns(3)

    with col_filter1:
        selected_journals = st.multiselect(
            "Filter by Journal",
            options=journals,
            default=journals,
            key="journal_filter"
        )

    with col_filter2:
        # Get unique broad topics (first letter of JEL codes)
        all_topics = set()
        for paper in all_papers:
            for code in paper.jel_codes:
                if code:
                    all_topics.add(code[0])
        topic_options = sorted(all_topics)
        topic_labels = {t: f"{t} - {get_category_name(t)}" for t in topic_options}

        selected_topics = st.multiselect(
            "Filter by Topic (JEL Category)",
            options=topic_options,
            format_func=lambda x: topic_labels.get(x, x),
            default=[],
            key="topic_filter"
        )

    with col_filter3:
        month_options = sorted(set((p.year, p.month) for p in all_papers), reverse=True)
        month_labels = {(y, m): f"{m:02d}/{y}" for y, m in month_options}
        selected_months = st.multiselect(
            "Filter by Month",
            options=month_options,
            format_func=lambda x: month_labels.get(x, str(x)),
            default=[],
            key="month_filter"
        )

    # Filter papers
    filtered_papers = all_papers.copy()

    if selected_journals:
        filtered_papers = [p for p in filtered_papers if p.journal in selected_journals]

    if selected_topics:
        filtered_papers = [p for p in filtered_papers
                         if any(code[0] in selected_topics for code in p.jel_codes if code)]

    if selected_months:
        filtered_papers = [p for p in filtered_papers
                         if (p.year, p.month) in selected_months]

    # Stats display
    st.markdown(
        f'<p class="stats-display">{len(filtered_papers)} papers • '
        f'{len(set(p.journal for p in filtered_papers))} journals • '
        f'{len(set(c for p in filtered_papers for c in p.jel_codes))} unique JEL codes</p>',
        unsafe_allow_html=True
    )

    # JEL Visualization
    fig = create_jel_visualization(filtered_papers)
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

    # X-axis label explaining the letters
    st.markdown(
        '<p style="text-align: center; color: #444; font-size: 0.75rem; margin-top: -20px;">'
        'JEL Categories: A-General • B-History of Thought • C-Quantitative Methods • D-Micro • '
        'E-Macro • F-International • G-Finance • H-Public • I-Health/Education • J-Labor • '
        'K-Law • L-Industrial Org • M-Business • N-Economic History • O-Development • P-Systems • '
        'Q-Agricultural/Environmental • R-Urban/Regional • Y-Misc • Z-Other</p>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    # Papers section header
    st.markdown('<h2 style="color: #00ff88; font-family: Courier New;">PAPERS</h2>',
               unsafe_allow_html=True)

    # Sort options
    sort_col1, sort_col2 = st.columns([3, 1])
    with sort_col2:
        sort_option = st.selectbox(
            "Sort by",
            options=["Journal", "Date (Newest)", "Date (Oldest)", "Title"],
            key="sort_option"
        )

    # Sort papers
    if sort_option == "Journal":
        filtered_papers.sort(key=lambda p: (p.journal, -p.year, -p.month, p.title))
    elif sort_option == "Date (Newest)":
        filtered_papers.sort(key=lambda p: (-p.year, -p.month, p.title))
    elif sort_option == "Date (Oldest)":
        filtered_papers.sort(key=lambda p: (p.year, p.month, p.title))
    else:
        filtered_papers.sort(key=lambda p: p.title)

    # Group and display papers
    if sort_option == "Journal":
        current_journal = None
        for idx, paper in enumerate(filtered_papers):
            if paper.journal != current_journal:
                current_journal = paper.journal
                color = JOURNAL_COLORS.get(current_journal, "#888")
                st.markdown(
                    f'<h3 style="color: {color}; font-family: Courier New; '
                    f'margin-top: 1.5rem; margin-bottom: 0.5rem;">{current_journal}</h3>',
                    unsafe_allow_html=True
                )
            display_paper_card(paper, idx)
    else:
        for idx, paper in enumerate(filtered_papers):
            display_paper_card(paper, idx)

    # Footer
    st.markdown(
        '<div class="footer-text">'
        'truffle.econ • Data from AER, QJE, Econometrica, JPE, REStud<br>'
        'Built with Streamlit • Explore economics research'
        '</div>',
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
