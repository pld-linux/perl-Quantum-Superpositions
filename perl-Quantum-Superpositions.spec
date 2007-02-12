#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Quantum
%define		pnam	Superpositions
Summary:	Quantum::Superpositions - QM-like superpositions in Perl
Summary(pl.UTF-8):   Quantum::Superpositions - superpozycje z mechaniki kwantowej w Perlu
Name:		perl-Quantum-Superpositions
Version:	2.02
Release:	1
# same as perl (5.6.1 or later)
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	40a3a398ca24be6de510667d92c02f5e
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Class-Multimethods
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quantum::Superpositions provides a new scalar data structure: the
superposition. In a metaphor drawn from quantum mechanics,
superpositions store a collection of values by overlaying them in
parallel superimposed states within a single scalar variable.

The Quantum::Superpositions module adds two new operators to Perl:
any and all.

%description -l pl.UTF-8
Moduł Quantum::Superpositions udostępnia nową strukturę danych
skalarnych: superpozycję. Jest to metafora pochodząca z mechaniki
kwantowej - superpozycje przechowują zestaw zmiennych poprzez
nakładanie ich w równolegle złożonych stanach w pojedynczej zmiennej
skalarnej.

Moduł Quantum::Superpositions dodaje dwa nowe operatory do Perla: any
i all.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change*
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
