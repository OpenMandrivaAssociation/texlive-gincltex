%global tl_name gincltex
%global tl_revision 78251

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3
Release:	%{tl_revision}.1
Summary:	Include TeX files as graphics (.tex support for \includegraphics)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gincltex
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gincltex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gincltex.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gincltex.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(svn-prov)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package builds on the standard LaTeX packages graphics and/or
graphicx and allows external LaTeX source files to be included, in the
same way as graphic files, by \includegraphics. In effect, then package
adds support for the .tex extension. Some of the lower level operations
like clipping and trimming are implemented using the adjustbox package
which includes native pdfLaTeX support and uses the pgf package for
other output formats.

