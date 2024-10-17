Name:		texlive-gincltex
Version:	64967
Release:	2
Summary:	Include TeX files as graphics (.tex support for \includegraphics)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gincltex
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gincltex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gincltex.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gincltex.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package builds on the standard LaTeX packages graphics
and/or graphicx and allows external LaTeX source files to be
included, in the same way as graphic files, by
\includegraphics. In effect, then package adds support for the
.tex extension. Some of the lower level operations like
clipping and trimming are implemented using the adjustbox
package which includes native pdflatex support and uses the pdf
pacakge for other output formats.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/gincltex/gincltex.sty
%doc %{_texmfdistdir}/doc/latex/gincltex/README
%doc %{_texmfdistdir}/doc/latex/gincltex/gincltex.pdf
#- source
%doc %{_texmfdistdir}/source/latex/gincltex/gincltex.dtx
%doc %{_texmfdistdir}/source/latex/gincltex/gincltex.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
