#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Quantum
%define	pnam	Superpositions
Summary:	Quantum::Superpositions - QM-like superpositions in Perl
Summary(pl):	Quantum::Superpositions - superpozycje z mechaniki kwantowej w Perlu
Name:		perl-Quantum-Superpositions
Version:	1.05
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Class-Multimethods
%endif
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quantum::Superpositions provides a new scalar data structure: the
superposition. In a metaphor drawn from quantum mechanics,
superpositions store a collection of values by overlaying them in
parallel superimposed states within a single scalar variable.

The Quantum::Superpositions module adds two new operators to Perl:
any and all.

%description -l pl
Modu³ Quantum::Superpositions udostêpnia now± strukturê danych
skalarnych: superpozycjê. Jest to metafora pochodz±ca z mechaniki
kwantowej - superpozycje przechowuj± zestaw zmiennych poprzez
nak³adanie ich w równolegle z³o¿onych stanach w pojedynczej zmiennej
skalarnej.

Modu³ Quantum::Superpositions dodaje dwa nowe operatory do Perla: any
i all.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change*
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
