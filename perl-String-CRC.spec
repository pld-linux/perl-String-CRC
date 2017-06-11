#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	String
%define		pnam	CRC
Summary:	String::CRC - Perl interface to Cyclic Redundancy Check generation
Summary(pl.UTF-8):	String::CRC - perlowy interfejs do generowania CRC
Name:		perl-String-CRC
Version:	1.0
Release:	21
License:	Public Domain
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/String/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ba07f022b5abf869a7b73f98f8abcf9f
URL:		http://search.cpan.org/dist/String-CRC/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
String::CRC module calculates CRC of various lenghts.

%description -l pl.UTF-8
Moduł String::CRC oblicza CRC różnej długości.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
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
%attr(755,root,root) %{perl_vendorarch}/auto/String/CRC/CRC.so
%{_mandir}/man3/*
