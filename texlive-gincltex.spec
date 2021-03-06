# revision 23835
# category Package
# catalog-ctan /macros/latex/contrib/gincltex
# catalog-date 2011-09-05 20:39:25 +0200
# catalog-license lppl1.3
# catalog-version 0.3
Name:		texlive-gincltex
Version:	0.3
Release:	11
Summary:	Include TeX files as graphics (.tex support for \includegraphics)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gincltex
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gincltex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gincltex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gincltex.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.3-2
+ Revision: 752315
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.3-1
+ Revision: 718556
- texlive-gincltex
- texlive-gincltex
- texlive-gincltex
- texlive-gincltex

