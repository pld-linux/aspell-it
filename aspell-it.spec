Summary:	Italian dictionary for aspell
Summary(pl.UTF-8):	Włoski słownik dla aspella
Name:		aspell-it
Version:	2.2_20050523
%define	subv	0
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/it/aspell6-it-%{version}-%{subv}.tar.bz2
# Source0-md5:	b1217299a0b67d1e121494d7ec18a88d
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60.0
Requires:	aspell >= 3:0.60.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Italian dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Włoski słownik (lista słów) dla aspella.

%prep
%setup -q -n aspell6-it-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Copyright
%{_libdir}/aspell/*
%{_datadir}/aspell/*
