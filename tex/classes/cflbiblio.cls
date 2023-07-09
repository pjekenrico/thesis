\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{cflbiblio}[2019/01/22 Bibliography Report class]
\LoadClass[a4paper,12pt]{article}

%
\RequirePackage{a4}
\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage[english]{babel}
\RequirePackage{tgtermes}

% Math Symbols
\RequirePackage{amsmath}
\RequirePackage{amssymb}
\RequirePackage{amsthm}
\RequirePackage{relsize}
% Broken on Windows
%\RequirePackage{xfrac}

% Graphics
\RequirePackage{graphicx}

% Colors
\RequirePackage{pgfplots}
\usepgfplotslibrary{dateplot}
\pgfplotsset{compat=1.8}
\definecolor{darkblue}{HTML}{00688B}
\definecolor{darkgreen}{HTML}{6E8B3D}
\definecolor{cadet}{HTML}{DAE1FF}
\definecolor{salmon}{HTML}{FFB08A}

% Hyperref
\RequirePackage{hyperref}

% Nomenclature
\RequirePackage[refpage]{nomencl}
\RequirePackage{makeidx}

\input{cflenv}
\input{cflalg}

\input{cflbiblio}
