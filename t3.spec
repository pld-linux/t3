Summary:	3-D extrapolation of tetris
Summary(pl):	Trójwymiarowa ekstrapolacja tetrisa
Name:		t3
Version:	04.11.29
Release:	0.1
License:	GPL v2
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/t-3/%{name}-%{version}-beta.tgz
# Source0-md5:	034625e44e4ac9e5a603d35895ee43fd
Patch0:		%{name}-makefile.patch
URL:		http://t-3.sourceforge.net/
BuildRequires:	gcc-c++
BuildRequires:	glut-devel
BuildRequires:	libtiff-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
T^3 ("T-cubed") is the 3-D extrapolation of the widely popular
puzzle-arcade game, Tetris(tm). Whereas the objective of the classical
Tetris(tm) game was to arrange falling pieces into horizontal lines,
the objective of T^3 is to form square surfaces.

%description -l pl
T^3 ("T-sze¶cienny") jest trójwymiarow± ekstrapolacj± popularnej gry
Tetris(tm). Celem klasycznego Tetrisa(tm) jest u³o¿enie spadaj±cych
klocków w poziome linie, natomiast celem T^3 jest u³o¿enie
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
%doc CHANGELOG.TXT README.TXT
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
