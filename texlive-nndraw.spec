%global tl_name nndraw
%global tl_revision 59674

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Draw neural networks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/nndraw
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nndraw.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nndraw.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nndraw.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
With this package you can create fully connected neural networks in a
simple and efficient way.

