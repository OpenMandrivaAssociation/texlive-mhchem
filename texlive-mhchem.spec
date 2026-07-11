%global tl_name mhchem
%global tl_revision 69639

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Typeset chemical formulae/equations and H and P statements
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mhchem
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mhchem.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mhchem.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(amsmath)
Requires:	texlive(chemgreek)
Requires:	texlive(graphics)
Requires:	texlive(l3kernel)
Requires:	texlive(l3packages)
Requires:	texlive(tools)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides three packages: The mhchem package provides commands
for typesetting chemical molecular formulae and equations. The
hpstatement package provides commands for the official hazard statements
and precautionary statements (H and P statements) that are used to label
chemicals. The rsphrase package provides commands for the official Risk
and Safety (R and S) Phrases that are used to label chemicals. The
package requires the expl3 bundle.

