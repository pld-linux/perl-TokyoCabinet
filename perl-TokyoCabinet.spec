#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	TokyoCabinet - Perl binding for Tokyo Cabinet
Summary(pl.UTF-8):	TokyoCabinet - wiązania Perla do biblioteki Tokyo Cabinet
Name:		perl-TokyoCabinet
Version:	1.34
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages/Perl
Source0:	http://fallabs.com/tokyocabinet/perlpkg/tokyocabinet-perl-%{version}.tar.gz
# Source0-md5:	e83e45e6a209dd81530b57d9414fd6ab
URL:		http://fallabs.com/tokyocabinet/
BuildRequires:	bzip2-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	tokyocabinet-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tokyo Cabinet is a library of routines for managing a database. The
database is a simple data file containing records, each is a pair of a
key and a value. Every key and value is serial bytes with variable
length. Both binary data and character string can be used as a key and
a value. There is neither concept of data tables nor data types.
Records are organized in hash table, B+ tree, or fixed-length array.

This package contains Perl binding for the library.

%description -l pl.UTF-8
Tokyo Cabinet to biblioteka procedur do zarządzania bazą danych. Baza
danych to prosty plik danych zawierający pary klucz-wartość. Każdy
klucz oraz wartość to szereg bajtów o zmiennej długości. Jako kluczy
oraz wartości można używać zarówno danych binarnych, jak i łańcuchów
znaków. Nie ma konceptu tabel danych ani typów danych. Rekordy są
zorganizowane w tablicy haszującej, B+ drzewie lub tablicy o stałej
długości.

Ten pakiet zawiera wiązania Perla do biblioteki.

%prep
%setup -q -n tokyocabinet-perl-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

# tests and pod
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/{memsize.pl,tc?test.pl,*.pod}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/index.html
%{perl_vendorarch}/TokyoCabinet.pm
%dir %{perl_vendorarch}/auto/TokyoCabinet
%attr(755,root,root) %{perl_vendorarch}/auto/TokyoCabinet/TokyoCabinet.so
%{_mandir}/man3/TokyoCabinet.3pm*
