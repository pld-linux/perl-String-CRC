%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	CRC
Summary:	String::CRC perl module
Summary(pl):	Modu³ perla String::CRC
Name:		perl-String-CRC
Version:	1.0
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
String::CRC - calculates CRC of various lenghts.

%description -l pl
String::CRC - oblicza CRC ró¿nej d³ugo¶ci.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitearch}/String/CRC.pm
%dir %{perl_sitearch}/auto/String/CRC
%{perl_sitearch}/auto/String/CRC/CRC.bs
%attr(755,root,root) %{perl_sitearch}/auto/String/CRC/CRC.so
%{_mandir}/man3/*
