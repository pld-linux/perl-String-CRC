%include	/usr/lib/rpm/macros.perl
Summary:	String-CRC perl module
Summary(pl):	Modu³ perla String-CRC
Name:		perl-String-CRC
Version:	1.0
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/String/String-CRC-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
String-CRC - calculates CRC of various lenghts.

%description -l pl
String-CRC - oblicza CRC ró¿nej d³ugo¶ci.

%prep
%setup -q -n String-CRC-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/String/CRC.pm
%dir %{perl_sitearch}/auto/String/CRC
%{perl_sitearch}/auto/String/CRC/CRC.bs
%attr(755,root,root) %{perl_sitearch}/auto/String/CRC/CRC.so
%{_mandir}/man3/*
