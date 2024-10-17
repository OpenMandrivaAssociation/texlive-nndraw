Name:		texlive-nndraw
Version:	59674
Release:	2
Summary:	Draw neural networks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nndraw
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nndraw.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nndraw.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nndraw.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
With this package you can create fully connected neural
networks in a simple and efficient way.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/nndraw
%{_texmfdistdir}/tex/latex/nndraw
%doc %{_texmfdistdir}/doc/latex/nndraw

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
