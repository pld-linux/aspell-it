Summary:	Italian dictionary for aspell
Summary(pl):	W這ski s這wnik dla aspella
Name:		aspell-it
Version:	0.53
%define	subv	0
Release:	1
Epoch:		1
License:	GPL (?)
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/it/%{name}-%{version}-%{subv}.tar.bz2
# Source0-md5:	ab3cce02bf8bfdf4116f9f7e602cf4b7
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 0.50.0
Requires:	aspell >= 0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Italian dictionary (i.e. word list) for aspell.

%description -l pl
W這ski s這wnik (lista s堯w) dla aspella.

%prep
%setup -q -n %{name}-%{version}-%{subv}

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
