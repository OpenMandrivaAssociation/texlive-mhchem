# revision 33314
# category Package
# catalog-ctan /macros/latex/contrib/mhchem
# catalog-date 2014-03-28 07:32:42 +0100
# catalog-license lppl1.3
# catalog-version undef
Name:		texlive-mhchem
Version:	20140328
Release:	4
Summary:	Typeset chemical formulae/equations and Risk and Safety phrases
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mhchem
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mhchem.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mhchem.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides three packages: The mhchem package provides
commands for typesetting chemical molecular formulae and
equations. The hpstatement package provides commands for the
official hazard statements and precautionary statements (H and
P statements) that are used to label chemicals. The rsphrase
package provides commands for the official Risk and Safety (R
and S) Phrases that are used to label chemicals. The package
requires the expl3 bundle.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mhchem/hpstatement.sty
%{_texmfdistdir}/tex/latex/mhchem/mhchem.sty
%{_texmfdistdir}/tex/latex/mhchem/rsphrase.sty
%doc %{_texmfdistdir}/doc/latex/mhchem/README
%doc %{_texmfdistdir}/doc/latex/mhchem/lppl-1-3c.txt
%doc %{_texmfdistdir}/doc/latex/mhchem/manifest.txt
%doc %{_texmfdistdir}/doc/latex/mhchem/mhchem.pdf
%doc %{_texmfdistdir}/doc/latex/mhchem/mhchem.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
