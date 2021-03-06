HEADER = (
"""
%-------------------------------------------------------------------------------
%	SECTION TITLE
%-------------------------------------------------------------------------------
\cvsection{Honors \& Awards}
""")

SUB_HEADER = (
"""
%-------------------------------------------------------------------------------
%	SUBSECTION TITLE
%-------------------------------------------------------------------------------
\cvsubsection{{{category}}}

%-------------------------------------------------------------------------------
%	CONTENT
%-------------------------------------------------------------------------------
\\begin{{cvhonors}}
"""
)

TEMPLATE = (
"""
    %---------------------------------------------------------
    \cvhonor
        {{{title}}} % Title
        {{{amount}}} % Amount
        {{{location}}} % Location
        {{{date}}} % Date(s)"""
)

SUB_FOOTER = (
"""
\end{cvhonors}
"""
)

FOOTER = ""

