#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	String
%define		pnam	CRC
Summary:	String::CRC perl module
Summary(pl):	Modu³ perla String::CRC
Name:		perl-String-CRC
Version:	1.0
Release:	9
License:	Public Domain
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ba07f022b5abf869a7b73f98f8abcf9f
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
String::CRC - calculates CRC of various lenghts.

%description -l pl
String::CRC - oblicza CRC ró¿nej d³ugo¶ci.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorarch}/String/CRC.pm
%dir %{perl_vendorarch}/auto/String/CRC
%{perl_vendorarch}/auto/String/CRC/CRC.bs
%attr(755,root,root) %{perl_vendorarch}/auto/String/CRC/CRC.so
%{_mandir}/man3/*
