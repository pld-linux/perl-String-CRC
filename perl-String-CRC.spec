%include	/usr/lib/rpm/macros.perl
Summary:	String-CRC perl module
Summary(pl):	Modu³ perla String-CRC
Name:		perl-String-CRC
Version:	1.0
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/String/String-CRC-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
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
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/String/CRC/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/String/CRC
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitearch}/String/CRC.pm

%dir %{perl_sitearch}/auto/String/CRC
%{perl_sitearch}/auto/String/CRC/.packlist
%{perl_sitearch}/auto/String/CRC/CRC.bs
%attr(755,root,root) %{perl_sitearch}/auto/String/CRC/CRC.so

%{_mandir}/man3/*
