Name:		texlive-mhchem
Version:	69639
Release:	1
Summary:	Typeset chemical formulae/equations and Risk and Safety phrases
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mhchem
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mhchem.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mhchem.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/mhchem
%doc %{_texmfdistdir}/doc/latex/mhchem

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
