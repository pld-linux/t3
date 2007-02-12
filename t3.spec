Summary:	3-D extrapolation of tetris
Summary(pl.UTF-8):   Trójwymiarowa ekstrapolacja tetrisa
Name:		t3
Version:	04.12.20
Release:	2
License:	GPL v2
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/t-3/%{name}-%{version}-beta.tgz
# Source0-md5:	689ac1f91b8fe66f9593ccf44f3ee33f
Patch0:		%{name}-makefile.patch
URL:		http://t-3.sourceforge.net/
BuildRequires:	glut-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
T^3 ("T-cubed") is the 3-D extrapolation of the widely popular
puzzle-arcade game, Tetris(tm). Whereas the objective of the classical
Tetris(tm) game was to arrange falling pieces into horizontal lines,
the objective of T^3 is to form square surfaces.

%description -l pl.UTF-8
T^3 ("T-sześcienny") jest trójwymiarową ekstrapolacją popularnej gry
Tetris(tm). Celem klasycznego Tetrisa(tm) jest ułożenie spadających
klocków w poziome linie, natomiast celem T^3 jest ułożenie
kwadratowych powierzchni.

%prep
%setup -q -n %{name}
%patch0 -p1

sed -i "s,data,%{_datadir}/%{name}/&," src/t3.cpp

%build
%{__make} \
	CPPFLAGS="%{rpmcflags} -I../include"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/data

install %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install data/* $RPM_BUILD_ROOT%{_datadir}/%{name}/data

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
