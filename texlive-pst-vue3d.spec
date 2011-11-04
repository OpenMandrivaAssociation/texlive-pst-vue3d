# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-vue3d
# catalog-date 2008-02-21 14:49:16 +0100
# catalog-license lppl
# catalog-version 1.24
Name:		texlive-pst-vue3d
Version:	1.24
Release:	1
Summary:	Draw perspective views of three dimensional objects
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-vue3d
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-vue3d.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-vue3d.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-vue3d.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
With pst-vue3d three dimensional objects like cubes, spheres
and others can be viewed from different points. The
distribution includes a comprehensive set of examples of usage.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-vue3d/pst-vue3d.pro
%{_texmfdistdir}/tex/generic/pst-vue3d/pst-vue3d.tex
%{_texmfdistdir}/tex/latex/pst-vue3d/pst-vue3d.sty
%doc %{_texmfdistdir}/doc/generic/pst-vue3d/Changes
%doc %{_texmfdistdir}/doc/generic/pst-vue3d/README
%doc %{_texmfdistdir}/doc/generic/pst-vue3d/pst-vue3d-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-vue3d/pst-vue3d-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-vue3d/pst-vue3d-doc.tex
#- source
%doc %{_texmfdistdir}/source/generic/pst-vue3d/Makefile
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
