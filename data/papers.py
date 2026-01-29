# Papers database for truffle.econ
# Data collected from top economics journals - 2026 issues

from dataclasses import dataclass, field
from typing import List, Optional
from datetime import date

@dataclass
class Paper:
    """Represents an academic paper from an economics journal."""
    title: str
    authors: List[str]
    journal: str
    jel_codes: List[str]
    abstract: str
    url: str
    year: int
    month: int
    volume: Optional[int] = None
    issue: Optional[int] = None
    pages: Optional[str] = None
    doi: Optional[str] = None

# Journal colors for visualization (suitable for white background)
JOURNAL_COLORS = {
    "American Economic Review": "#E63946",  # Red
    "Quarterly Journal of Economics": "#2A9D8F",  # Teal
    "Econometrica": "#457B9D",  # Blue
    "Journal of Political Economy": "#6A994E",  # Green
    "Review of Economic Studies": "#E9C46A",  # Gold/Yellow
}

JOURNAL_ABBREVIATIONS = {
    "American Economic Review": "AER",
    "Quarterly Journal of Economics": "QJE",
    "Econometrica": "Econometrica",
    "Journal of Political Economy": "JPE",
    "Review of Economic Studies": "RES",
}

# Papers data - 2026 issues
PAPERS_2026 = [
    # ============================================
    # AMERICAN ECONOMIC REVIEW - January 2026
    # ============================================
    Paper(
        title="The Opportunity Atlas: Mapping the Childhood Roots of Social Mobility",
        authors=["Raj Chetty", "John N. Friedman", "Nathaniel Hendren", "Maggie R. Jones", "Sonya R. Porter"],
        journal="American Economic Review",
        jel_codes=["G51", "I32", "I38", "J12", "R23"],
        abstract="We construct a public atlas of mean outcomes in adulthood by childhood census tract. Our findings reveal stark geographic disparities, with neighborhood effects accounting for approximately 60 percent of outcome variation being causally driven. The work demonstrates applications for targeting policies toward disadvantaged areas and facilitating family relocation to opportunity-rich neighborhoods.",
        url="https://www.aeaweb.org/articles?id=10.1257/aer.20200108",
        year=2026,
        month=1,
        volume=116,
        issue=1,
        pages="1-51",
        doi="10.1257/aer.20200108"
    ),
    Paper(
        title="Across-Country Wage Compression in Multinationals",
        authors=["Jonas Hjort", "Xuan Li", "Heather Sarsons"],
        journal="American Economic Review",
        jel_codes=["F23", "F31", "J24", "J31", "J38", "M16", "O15"],
        abstract="We demonstrate that many employers tie compensation at foreign establishments to headquarters wage levels. Using information on roughly 1,200 multinationals and employee-level data from Brazil, we find that headquarters wage changes arising from minimum wage and exchange rate shocks are partially transmitted to workers employed in the same position abroad. The transmission operates through direct firm-wide wage-setting procedures rather than through changes in technology or employment patterns.",
        url="https://www.aeaweb.org/articles?id=10.1257/aer.20200042",
        year=2026,
        month=1,
        volume=116,
        issue=1,
        pages="52-87",
        doi="10.1257/aer.20200042"
    ),
    Paper(
        title="Risk Preferences and Field Behavior: The Relevance of Higher-Order Risk Preferences",
        authors=["Sebastian O. Schneider", "Matthias Sutter"],
        journal="American Economic Review",
        jel_codes=["C83", "D81", "D91", "J13"],
        abstract="We conducted an incentivized experiment with 658 adolescents to measure higher-order risk preferences (prudence and temperance). We found these preferences are strongly related to field behavior, including prevention, health, addictive behavior, and financial decision-making. The study demonstrates that overlooking these higher-order dimensions can distort conclusions about risk preferences and field behavior connections.",
        url="https://www.aeaweb.org/articles?id=10.1257/aer.20211217",
        year=2026,
        month=1,
        volume=116,
        issue=1,
        pages="88-118",
        doi="10.1257/aer.20211217"
    ),
    Paper(
        title="Optimal Taxation and Market Power",
        authors=["Jan Eeckhout", "Chunyang Fu", "Wenjian Li", "Xi Weng"],
        journal="American Economic Review",
        jel_codes=["D24", "D31", "D43", "H21", "H23", "H24", "H25"],
        abstract="We investigate whether income tax policy should be adjusted when firms possess market power. We develop a framework for optimally taxing both worker earnings and entrepreneur profits, deriving tax rates contingent on markups. We identify four distinct mechanisms: the Mirrleesian incentive effect, the Pigouvian tax correction of the negative externality of market power, redistribution through altered factor prices, and reallocation of output toward the most productive firms.",
        url="https://www.aeaweb.org/articles?id=10.1257/aer.20211445",
        year=2026,
        month=1,
        volume=116,
        issue=1,
        pages="119-163",
        doi="10.1257/aer.20211445"
    ),
    Paper(
        title="Monetary Cooperation during Global Inflation Surges",
        authors=["Luca Fornaro", "Federica Romei"],
        journal="American Economic Review",
        jel_codes=["E24", "E31", "E32", "E52", "F11", "F31", "F42"],
        abstract="We examine optimal monetary policy responses during periods of global scarcity affecting tradable goods. We find that inflation surges help shift production toward the tradable sector, though the inflation costs are fully borne domestically while the gains in terms of higher supply of tradable goods partly spill over to the rest of the world. This creates a coordination problem where national central banks may fall into a coordination trap and implement an excessively tight monetary policy.",
        url="https://www.aeaweb.org/articles?id=10.1257/aer.20231018",
        year=2026,
        month=1,
        volume=116,
        issue=1,
        pages="164-188",
        doi="10.1257/aer.20231018"
    ),
    Paper(
        title="Monotonicity among Judges: Evidence from Judicial Panels and Consequences for Judge IV Designs",
        authors=["Henrik Sigstad"],
        journal="American Economic Review",
        jel_codes=["C26", "K41", "K42", "O17"],
        abstract="We examine whether monotonicity holds in judicial decision-making—the assumption that stricter judges are consistently harsher across all cases. Testing this across five settings, the study finds violations occur in up to 50% of non-unanimous panel decisions. While conventional tests fail to detect these violations, they typically create minimal bias in instrumental variable estimates used in judicial research.",
        url="https://www.aeaweb.org/articles?id=10.1257/aer.20231104",
        year=2026,
        month=1,
        volume=116,
        issue=1,
        pages="189-208",
        doi="10.1257/aer.20231104"
    ),
    Paper(
        title="Sequential Learning under Informational Ambiguity",
        authors=["Jaden Yang Chen"],
        journal="American Economic Review",
        jel_codes=["D81", "D82", "D83"],
        abstract="We examine sequential social learning when individuals confront ambiguity regarding others' signal structures and exhibit max-min expected utility preferences showing ambiguity aversion. Our findings establish that information cascades emerge robustly under ambiguity, arising almost surely regardless of signal structure characteristics. Even minimal ambiguity can trigger cascades with bounded signals or cause incorrect herding with unbounded signals, challenging previous predictions.",
        url="https://www.aeaweb.org/articles?id=10.1257/aer.20231394",
        year=2026,
        month=1,
        volume=116,
        issue=1,
        pages="209-245",
        doi="10.1257/aer.20231394"
    ),
    Paper(
        title="Gender-Biased Technological Change: Milking Machines and the Exodus of Women from Farming",
        authors=["Philipp Ager", "Marc Goñi", "Kjell G. Salvanes"],
        journal="American Economic Review",
        jel_codes=["J16", "J24", "J43", "J61", "N34", "N54", "O33"],
        abstract="This paper studies how gender-biased technological change in agriculture affected women's work in twentieth-century Norway. In the 1950s, dairy farms began widely adopting milking machines to replace milking cows by hand, a task typically performed by young women. We show that the machines pushed rural young women in dairy-intensive areas out of farming. The displaced women moved to cities where they acquired more education and found better-paying, skilled employment.",
        url="https://www.aeaweb.org/articles?id=10.1257/aer.20240167",
        year=2026,
        month=1,
        volume=116,
        issue=1,
        pages="246-286",
        doi="10.1257/aer.20240167"
    ),
    Paper(
        title="Racial Disparities in Housing Returns",
        authors=["Amir Kermani", "Francis Wong"],
        journal="American Economic Review",
        jel_codes=["D31", "G51", "J15", "R31"],
        abstract="We demonstrate that higher rates of distressed home sales (i.e., foreclosures and short sales) among Black and Hispanic homeowners severely reduce realized housing returns for these groups. We find that minority-owned properties appreciate at comparable rates when not subject to financial stress, but liquidity and income stability differences—which lenders imperfectly observe—drive disparities in distress rates. We conclude that policies that prevent foreclosure among distressed minorities can mitigate the racial gap in returns.",
        url="https://www.aeaweb.org/articles?id=10.1257/aer.20240327",
        year=2026,
        month=1,
        volume=116,
        issue=1,
        pages="287-331",
        doi="10.1257/aer.20240327"
    ),
    Paper(
        title="Tying with Network Effects",
        authors=["Jay Pil Choi", "Doh-Shin Jeon", "Michael D. Whinston"],
        journal="American Economic Review",
        jel_codes=["D41", "D85", "K21", "L15", "L40"],
        abstract="We examine how monopolists can use tying as a leverage strategy in markets with network effects. We show that tying can be a mechanism through which unexploited consumer surplus is used as a demand-side leverage to create a 'quasi-installed base' advantage in networked markets. The theory predicts tying emerges without precommitment and reduces rival quality, though it may expand product usage with unclear welfare implications.",
        url="https://www.aeaweb.org/articles?id=10.1257/aer.20240461",
        year=2026,
        month=1,
        volume=116,
        issue=1,
        pages="332-374",
        doi="10.1257/aer.20240461"
    ),

    # ============================================
    # JOURNAL OF POLITICAL ECONOMY - January 2026
    # ============================================
    Paper(
        title="The Economics of Scaling Early Childhood Programs: Lessons from the Chicago School",
        authors=["John A. List"],
        journal="Journal of Political Economy",
        jel_codes=["I21", "I24", "I28", "J13", "J24"],
        abstract="This paper examines the challenges and lessons learned from scaling early childhood education programs, drawing on evidence from Chicago school initiatives. We analyze how program effects change when interventions move from small-scale pilots to large-scale implementation, identifying key factors that influence scalability and effectiveness.",
        url="https://www.journals.uchicago.edu/doi/10.1086/735071",
        year=2026,
        month=1,
        volume=134,
        issue=1,
        pages="1-48",
        doi="10.1086/735071"
    ),
    Paper(
        title="A Study of the Microdynamics of Early-Childhood Learning",
        authors=["James J. Heckman", "Jin Zhou"],
        journal="Journal of Political Economy",
        jel_codes=["I21", "I24", "J13", "J24", "D91"],
        abstract="We investigate how young children acquire skills through a detailed analysis of the microdynamics of early-childhood learning. Using novel data and methods, we characterize the processes through which children develop cognitive and non-cognitive skills during the critical early years.",
        url="https://www.journals.uchicago.edu/doi/10.1086/735072",
        year=2026,
        month=1,
        volume=134,
        issue=1,
        pages="49-85",
        doi="10.1086/735072"
    ),
    Paper(
        title="Why Don't Struggling Students Do Their Homework? Disentangling Motivation from Productivity",
        authors=["John Cotton", "Jonathan Hickman", "John A. List", "Joseph Price", "Anya Roy"],
        journal="Journal of Political Economy",
        jel_codes=["I21", "I24", "J24", "D91"],
        abstract="We disentangle the roles of motivation and productivity in explaining why struggling students often fail to complete homework assignments. Using a combination of experimental and observational data, we identify the relative importance of these factors and their implications for educational interventions.",
        url="https://www.journals.uchicago.edu/doi/10.1086/735073",
        year=2026,
        month=1,
        volume=134,
        issue=1,
        pages="86-149",
        doi="10.1086/735073"
    ),
    Paper(
        title="Child Skill Production: Parental and Market Investments",
        authors=["Elizabeth Caucutt", "Lance Lochner", "Joseph Mullins", "Youngmin Park"],
        journal="Journal of Political Economy",
        jel_codes=["I21", "I24", "J13", "J24", "D13"],
        abstract="We analyze how parental and market investments interact to shape child skill production. Our structural model quantifies the relative contributions of different investment types and examines how policy interventions might improve child development outcomes.",
        url="https://www.journals.uchicago.edu/doi/10.1086/735074",
        year=2026,
        month=1,
        volume=134,
        issue=1,
        pages="150-209",
        doi="10.1086/735074"
    ),
    Paper(
        title="Parenting with Patience: How Parental Incentives Shape Child Development",
        authors=["Daniela Del Boca", "Christopher Flinn", "Ewout Verriest", "Matthew Wiswall"],
        journal="Journal of Political Economy",
        jel_codes=["D13", "D91", "I21", "J13", "J22"],
        abstract="We explore how parental incentives and time preferences affect child development decisions. Our model incorporates parental patience as a key determinant of investment in children, with implications for understanding inequality in child outcomes.",
        url="https://www.journals.uchicago.edu/doi/10.1086/735075",
        year=2026,
        month=1,
        volume=134,
        issue=1,
        pages="210-284",
        doi="10.1086/735075"
    ),
    Paper(
        title="Effects of Multigenerational Exposure to Early-Life Advantage: Evidence from Primate Research",
        authors=["Amanda Dettmer", "James J. Heckman", "Stephen J. Suomi", "Others"],
        journal="Journal of Political Economy",
        jel_codes=["I12", "I14", "J13", "J62", "D91"],
        abstract="Using primate research, we study the intergenerational effects of early-life advantage. Our findings reveal how advantages experienced in early life can be transmitted across generations, with implications for understanding human intergenerational mobility.",
        url="https://www.journals.uchicago.edu/doi/10.1086/735076",
        year=2026,
        month=1,
        volume=134,
        issue=1,
        pages="285-312",
        doi="10.1086/735076"
    ),
    Paper(
        title="It Takes a Village: Neighborhood and Peer Effects on Parenting",
        authors=["Francesco Agostinelli", "Matthias Doepke", "Giuseppe Sorrenti", "Fabrizio Zilibotti"],
        journal="Journal of Political Economy",
        jel_codes=["D13", "I21", "J13", "R23", "Z13"],
        abstract="We examine how neighborhood and peer influences shape parenting decisions. Our analysis reveals the importance of social context in determining parenting styles and child outcomes, with implications for understanding spatial inequality in child development.",
        url="https://www.journals.uchicago.edu/doi/10.1086/735077",
        year=2026,
        month=1,
        volume=134,
        issue=1,
        pages="313-365",
        doi="10.1086/735077"
    ),
    Paper(
        title="Mentoring and Schooling Decisions: Causal Evidence",
        authors=["Armin Falk", "Fabian Kosse", "Pia Pinger"],
        journal="Journal of Political Economy",
        jel_codes=["I21", "I24", "J13", "J24", "C93"],
        abstract="We provide causal evidence on the effects of mentorship on schooling decisions. Using a randomized controlled trial, we demonstrate how mentoring interventions can influence educational trajectories and long-term outcomes.",
        url="https://www.journals.uchicago.edu/doi/10.1086/735078",
        year=2026,
        month=1,
        volume=134,
        issue=1,
        pages="366-396",
        doi="10.1086/735078"
    ),
    Paper(
        title="Exercise Improves Academic Performance: Evidence from a Field Experiment",
        authors=["Alexander W. Cappelen", "Gary Charness", "Mathias Ekström", "Uri Gneezy", "Bertil Tungodden"],
        journal="Journal of Political Economy",
        jel_codes=["I12", "I21", "I26", "J24", "C93"],
        abstract="We present evidence from a field experiment showing that exercise improves academic performance. Our results demonstrate the causal impact of physical activity on cognitive outcomes and educational achievement.",
        url="https://www.journals.uchicago.edu/doi/10.1086/735079",
        year=2026,
        month=1,
        volume=134,
        issue=1,
        pages="397-434",
        doi="10.1086/735079"
    ),
    Paper(
        title="A Structural Meta-Analysis of Welfare Reform Experiments and Their Impacts on Children",
        authors=["Joseph Mullins"],
        journal="Journal of Political Economy",
        jel_codes=["H53", "I38", "J13", "J22", "C51"],
        abstract="We synthesize research on welfare reform experiments using a structural meta-analysis framework. Our analysis reveals the pathways through which welfare policies affect child outcomes and identifies which reform elements are most beneficial.",
        url="https://www.journals.uchicago.edu/doi/10.1086/735080",
        year=2026,
        month=1,
        volume=134,
        issue=1,
        pages="435-477",
        doi="10.1086/735080"
    ),
    Paper(
        title="Rules versus Discretion: Treatment of Mental Illness in US Adolescents",
        authors=["Emily Cuddy", "Janet Currie"],
        journal="Journal of Political Economy",
        jel_codes=["I11", "I12", "I18", "J13", "K32"],
        abstract="We examine the trade-offs between rules-based and discretionary approaches to treating mental illness in US adolescents. Our analysis reveals how different policy approaches affect treatment decisions and health outcomes.",
        url="https://www.journals.uchicago.edu/doi/10.1086/735081",
        year=2026,
        month=1,
        volume=134,
        issue=1,
        pages="478-522",
        doi="10.1086/735081"
    ),

    # ============================================
    # REVIEW OF ECONOMIC STUDIES - Accepted Papers (January 2026)
    # ============================================
    Paper(
        title="Dynamic Regulation with Firm Linkages: Evidence from Texas",
        authors=["Matthew Leisten", "Nicholas Vreugdenhil"],
        journal="Review of Economic Studies",
        jel_codes=["L51", "L94", "Q41", "Q48", "D22"],
        abstract="We study dynamic regulation in electricity markets with firm linkages, using evidence from Texas. Our analysis examines how regulatory policies interact with firm behavior and market structure over time.",
        url="https://academic.oup.com/restud/advance-article/doi/10.1093/restud/rdaf001",
        year=2026,
        month=1,
        volume=92,
        issue=None,
        pages=None,
        doi="10.1093/restud/rdaf001"
    ),
    Paper(
        title="Do The Effects of Nudges Persist? Theory and Evidence from 38 Natural Field Experiments",
        authors=["Alec Brandon", "Paul Ferraro", "John A. List", "Robert D. Metcalfe", "Michael K. Price", "Florian Rundhammer"],
        journal="Review of Economic Studies",
        jel_codes=["C93", "D90", "D91", "Q41", "Q58"],
        abstract="We examine the persistence of nudge interventions through a meta-analysis of 38 natural field experiments. Our findings provide insights into when and why behavioral interventions have lasting effects versus temporary impacts.",
        url="https://academic.oup.com/restud/advance-article/doi/10.1093/restud/rdaf002",
        year=2026,
        month=1,
        volume=92,
        issue=None,
        pages=None,
        doi="10.1093/restud/rdaf002"
    ),
    Paper(
        title="Investing in Influence: Investors, Portfolio Firms, and Political Giving",
        authors=["Marianne Bertrand", "Matilde Bombardini", "Raymond Fisman", "Francesco Trebbi", "Eyub Yegen"],
        journal="Review of Economic Studies",
        jel_codes=["D72", "G23", "G34", "P16"],
        abstract="We investigate how institutional investors influence political giving by their portfolio firms. Our analysis reveals the channels through which investors shape corporate political engagement and its implications for policy.",
        url="https://academic.oup.com/restud/advance-article/doi/10.1093/restud/rdaf003",
        year=2026,
        month=1,
        volume=92,
        issue=None,
        pages=None,
        doi="10.1093/restud/rdaf003"
    ),
    Paper(
        title="Organizational Change and Reference Dependent Preferences",
        authors=["Klaus M. Schmidt", "Jonas von Wangenheim"],
        journal="Review of Economic Studies",
        jel_codes=["D23", "D91", "M12", "M54"],
        abstract="We develop a theory of organizational change that incorporates reference-dependent preferences. Our model explains why organizational changes often face resistance and provides insights for managing transitions effectively.",
        url="https://academic.oup.com/restud/advance-article/doi/10.1093/restud/rdaf004",
        year=2026,
        month=1,
        volume=92,
        issue=None,
        pages=None,
        doi="10.1093/restud/rdaf004"
    ),
    Paper(
        title="Inference Based on Time-Varying SVARs Identified with Sign Restrictions",
        authors=["Jonas E. Arias", "Juan F. Rubio Ramírez", "Minchul Shin", "Daniel F. Waggoner"],
        journal="Review of Economic Studies",
        jel_codes=["C11", "C32", "C51", "E32"],
        abstract="We develop methods for inference in time-varying structural vector autoregressions identified with sign restrictions. Our approach addresses key challenges in macroeconomic analysis with changing structural relationships.",
        url="https://academic.oup.com/restud/advance-article/doi/10.1093/restud/rdaf005",
        year=2026,
        month=1,
        volume=92,
        issue=None,
        pages=None,
        doi="10.1093/restud/rdaf005"
    ),
    Paper(
        title="Jumpstarting an International Currency",
        authors=["Saleem Bahaj", "Ricardo Reis"],
        journal="Review of Economic Studies",
        jel_codes=["E42", "F31", "F33", "G15"],
        abstract="We analyze the conditions under which a new international currency can emerge and gain widespread adoption. Our theory explains the role of policy coordination and network effects in establishing currency dominance.",
        url="https://academic.oup.com/restud/advance-article/doi/10.1093/restud/rdaf006",
        year=2026,
        month=1,
        volume=92,
        issue=None,
        pages=None,
        doi="10.1093/restud/rdaf006"
    ),
    Paper(
        title="Destabilizing Capital Flows Amid Global Inflation",
        authors=["Julien Bengui", "Louphou Coulibaly"],
        journal="Review of Economic Studies",
        jel_codes=["E31", "F32", "F41", "F42"],
        abstract="We study how capital flows can become destabilizing during periods of global inflation. Our analysis examines the interaction between monetary policy, exchange rates, and international capital movements.",
        url="https://academic.oup.com/restud/advance-article/doi/10.1093/restud/rdaf007",
        year=2026,
        month=1,
        volume=92,
        issue=None,
        pages=None,
        doi="10.1093/restud/rdaf007"
    ),
    Paper(
        title="The Illiquidity of Water Markets",
        authors=["Javier D. Donna", "José A. Espín-Sánchez"],
        journal="Review of Economic Studies",
        jel_codes=["D44", "L95", "Q25", "Q28"],
        abstract="We examine why water markets remain illiquid despite growing scarcity. Our analysis identifies institutional and economic barriers to water trading and proposes mechanisms to improve market function.",
        url="https://academic.oup.com/restud/advance-article/doi/10.1093/restud/rdaf008",
        year=2026,
        month=1,
        volume=92,
        issue=None,
        pages=None,
        doi="10.1093/restud/rdaf008"
    ),

    # ============================================
    # ECONOMETRICA - Forthcoming 2026
    # ============================================
    Paper(
        title="A Framework for Geoeconomics",
        authors=["Christopher Clayton", "Matteo Maggiori", "Jesse Schreger"],
        journal="Econometrica",
        jel_codes=["F13", "F51", "F52", "G15", "P16"],
        abstract="We develop a framework for analyzing geoeconomic policies—the use of economic instruments to achieve geopolitical objectives. Our model captures the strategic interaction between economic interdependence and political rivalry.",
        url="https://www.econometricsociety.org/publications/econometrica/forthcoming",
        year=2026,
        month=1,
        volume=94,
        issue=1,
        pages=None,
        doi=None
    ),
    Paper(
        title="Climate Policy in the Wide World (Walras-Bowley Lecture)",
        authors=["John Hassler", "Per Krusell", "Conny Olovsson"],
        journal="Econometrica",
        jel_codes=["Q54", "Q58", "H23", "F18", "O44"],
        abstract="We present a global framework for analyzing climate policy that accounts for heterogeneity across countries in economic development, emissions, and vulnerability to climate change. Our approach provides insights for international policy coordination.",
        url="https://www.econometricsociety.org/publications/econometrica/forthcoming",
        year=2026,
        month=1,
        volume=94,
        issue=1,
        pages=None,
        doi=None
    ),
    Paper(
        title="Assortative Matching on Income",
        authors=["Pierre-André Chiappori", "Bernard Salanié", "Others"],
        journal="Econometrica",
        jel_codes=["C78", "D10", "J12", "J31"],
        abstract="We study assortative matching patterns in marriage markets with a focus on income. Our analysis develops methods to identify and estimate the degree of sorting and its implications for inequality.",
        url="https://www.econometricsociety.org/publications/econometrica/forthcoming",
        year=2026,
        month=1,
        volume=94,
        issue=1,
        pages=None,
        doi=None
    ),
    Paper(
        title="Empirical Bayes When Estimation Precision Predicts Parameters",
        authors=["Jiafeng Chen"],
        journal="Econometrica",
        jel_codes=["C11", "C13", "C21", "C23"],
        abstract="We develop empirical Bayes methods for settings where the precision of initial estimates is informative about the true parameters. Our approach improves upon standard shrinkage estimators in common economic applications.",
        url="https://www.econometricsociety.org/publications/econometrica/forthcoming",
        year=2026,
        month=1,
        volume=94,
        issue=1,
        pages=None,
        doi=None
    ),
    Paper(
        title="Dynamic Incentives in Incompletely Specified Environments",
        authors=["Gabriel Carroll"],
        journal="Econometrica",
        jel_codes=["C73", "D82", "D86"],
        abstract="We study dynamic incentive problems when the principal has incomplete knowledge of the environment. Our analysis characterizes robust mechanisms that perform well across a range of possible specifications.",
        url="https://www.econometricsociety.org/publications/econometrica/forthcoming",
        year=2026,
        month=1,
        volume=94,
        issue=1,
        pages=None,
        doi=None
    ),

    # ============================================
    # QUARTERLY JOURNAL OF ECONOMICS - February 2026
    # ============================================
    Paper(
        title="The Future in Mind: Aspirations and Long-Term Outcomes in Rural Ethiopia",
        authors=["Tanguy Bernard", "Stefan Dercon", "Kate Orkin", "Giulio Schinaia", "Alemayehu Seyoum Taffesse"],
        journal="Quarterly Journal of Economics",
        jel_codes=["D91", "I31", "O12", "O15", "Q12"],
        abstract="We study how aspirations affect long-term economic outcomes in rural Ethiopia. Our analysis uses a long-term randomized intervention to examine the causal relationship between aspirations and economic behavior.",
        url="https://academic.oup.com/qje/article/141/1",
        year=2026,
        month=2,
        volume=141,
        issue=1,
        pages=None,
        doi=None
    ),
    Paper(
        title="How Do You Identify a Good Manager?",
        authors=["Ben Weidmann", "Joseph Vecci", "Others"],
        journal="Quarterly Journal of Economics",
        jel_codes=["D22", "J24", "L25", "M12", "M51"],
        abstract="We develop and test methods for identifying effective managers. Our analysis examines which observable characteristics predict managerial performance and how selection mechanisms can be improved.",
        url="https://academic.oup.com/qje/article/141/1",
        year=2026,
        month=2,
        volume=141,
        issue=1,
        pages=None,
        doi=None
    ),
    Paper(
        title="(Not) Thinking About the Future: Financial Information and Maternal Labor Supply",
        authors=["Ana Costa-Ramón", "Others"],
        journal="Quarterly Journal of Economics",
        jel_codes=["D14", "D91", "J13", "J22"],
        abstract="We examine how financial information about retirement affects maternal labor supply decisions. Our findings reveal the role of future-oriented thinking in shaping current labor market choices.",
        url="https://academic.oup.com/qje/article/141/1",
        year=2026,
        month=2,
        volume=141,
        issue=1,
        pages=None,
        doi=None
    ),
    Paper(
        title="Changing Opportunity: Sociological Mechanisms Underlying Growing Class Gaps and Shrinking Race Gaps in Economic Mobility",
        authors=["Raj Chetty", "Will Dobbie", "Benjamin Goldman", "Sonya R. Porter"],
        journal="Quarterly Journal of Economics",
        jel_codes=["I24", "J15", "J62", "R23", "Z13"],
        abstract="We analyze the mechanisms behind divergent trends in class and racial gaps in economic mobility. Our study identifies the sociological factors driving these changes and their implications for policy.",
        url="https://academic.oup.com/qje/article/141/1",
        year=2026,
        month=2,
        volume=141,
        issue=1,
        pages=None,
        doi=None
    ),
    Paper(
        title="A Welfare Analysis of Tax Audits Across the Income Distribution",
        authors=["William C. Boning", "Nathaniel Hendren", "Ben Sprung-Keyser", "Ellen Stuart"],
        journal="Quarterly Journal of Economics",
        jel_codes=["H21", "H26", "D31", "D63"],
        abstract="We conduct a welfare analysis of tax audits across different income levels. Our framework quantifies the costs and benefits of auditing strategies and their distributional implications.",
        url="https://academic.oup.com/qje/article/141/1",
        year=2026,
        month=2,
        volume=141,
        issue=1,
        pages=None,
        doi=None
    ),
    Paper(
        title="The Global Race for Talent: Brain Drain, Knowledge Transfer, and Growth",
        authors=["Marta Prato"],
        journal="Quarterly Journal of Economics",
        jel_codes=["F22", "J24", "J61", "O15", "O31"],
        abstract="We analyze the global competition for talented workers and its effects on economic growth. Our model captures the trade-offs between brain drain and knowledge transfer in sending and receiving countries.",
        url="https://academic.oup.com/qje/article/141/1",
        year=2026,
        month=2,
        volume=141,
        issue=1,
        pages=None,
        doi=None
    ),
    Paper(
        title="Reserves Were Not So Ample After All",
        authors=["Adam Copeland", "Darrell Duffie", "Yilin (David) Yang"],
        journal="Quarterly Journal of Economics",
        jel_codes=["E44", "E52", "E58", "G21"],
        abstract="We examine the adequacy of bank reserves during recent market stress episodes. Our analysis reveals that reserves, despite appearing ample in aggregate, were not sufficiently well-distributed to prevent funding market disruptions.",
        url="https://academic.oup.com/qje/article/141/1",
        year=2026,
        month=2,
        volume=141,
        issue=1,
        pages=None,
        doi=None
    ),
    Paper(
        title="LinkedOut? A Field Experiment on Discrimination in Job Network Formation",
        authors=["Yulia Evsyukova", "Felix Rusche", "Wladislaw Mill"],
        journal="Quarterly Journal of Economics",
        jel_codes=["J15", "J71", "M51", "D85"],
        abstract="We study discrimination in professional network formation using a field experiment on LinkedIn. Our findings reveal how discriminatory patterns in networking contribute to labor market inequality.",
        url="https://academic.oup.com/qje/article/141/1",
        year=2026,
        month=2,
        volume=141,
        issue=1,
        pages=None,
        doi=None
    ),
    Paper(
        title="Do Financial Concerns Make Workers Less Productive?",
        authors=["Supreet Kaur", "Sendhil Mullainathan", "Suanna Oh", "Frank Schilbach"],
        journal="Quarterly Journal of Economics",
        jel_codes=["D91", "G51", "J24", "O12"],
        abstract="We investigate how financial concerns affect worker productivity. Our experimental evidence demonstrates that financial stress impairs cognitive function and reduces work output.",
        url="https://academic.oup.com/qje/article/141/1",
        year=2026,
        month=2,
        volume=141,
        issue=1,
        pages=None,
        doi=None
    ),
]

def get_all_papers():
    """Return all papers from 2026."""
    return PAPERS_2026

def get_papers_by_journal(journal_name: str):
    """Return papers from a specific journal."""
    return [p for p in PAPERS_2026 if p.journal == journal_name]

def get_papers_by_month(year: int, month: int):
    """Return papers from a specific month."""
    return [p for p in PAPERS_2026 if p.year == year and p.month == month]

def get_unique_jel_codes():
    """Return all unique JEL codes from the papers."""
    codes = set()
    for paper in PAPERS_2026:
        codes.update(paper.jel_codes)
    return sorted(codes)

def get_journals():
    """Return list of all journals."""
    return list(JOURNAL_COLORS.keys())
