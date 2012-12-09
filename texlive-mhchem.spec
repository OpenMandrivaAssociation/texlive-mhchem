# revision 23334
# category Package
# catalog-ctan /macros/latex/contrib/mhchem
# catalog-date 2011-06-05 22:15:19 +0200
# catalog-license lppl
# catalog-version 3.11
Name:		texlive-mhchem
Version:	3.11
Release:	2
Summary:	Typeset chemical formulae/equations and Risk and Safety phrases
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mhchem
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mhchem.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mhchem.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Currently, the mhchem bundle consists of two packages: mhchem
and rsphrase. The mhchem package provides two commands: one for
typesetting chemical molecular formulae and one for typesetting
chemical equations with these formulae. The rsphrase package
contains the text of all official Risk and Safety (R and S)
Phrases that are used to label chemicals. At the time being,
these phrases are available in Danish, English, French, German
(current spelling), and Spanish.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mhchem/mhchem.sty
%{_texmfdistdir}/tex/latex/mhchem/rsphrase.sty
%doc %{_texmfdistdir}/doc/latex/mhchem/legal.txt
%doc %{_texmfdistdir}/doc/latex/mhchem/mhchem.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.11-2
+ Revision: 753979
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.11-1
+ Revision: 719016
- texlive-mhchem
- texlive-mhchem
- texlive-mhchem
- texlive-mhchem

