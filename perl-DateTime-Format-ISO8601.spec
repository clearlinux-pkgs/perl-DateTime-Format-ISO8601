#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-DateTime-Format-ISO8601
Version  : 0.16
Release  : 16
URL      : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/DateTime-Format-ISO8601-0.16.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/DateTime-Format-ISO8601-0.16.tar.gz
Summary  : 'Parses ISO8601 formats'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-DateTime-Format-ISO8601-license = %{version}-%{release}
Requires: perl-DateTime-Format-ISO8601-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(DateTime)
BuildRequires : perl(DateTime::Format::Builder)
BuildRequires : perl(DateTime::Format::Strptime)
BuildRequires : perl(Importer)
BuildRequires : perl(Params::Validate)
BuildRequires : perl(Params::ValidationCompiler)
BuildRequires : perl(Specio)
BuildRequires : perl(Specio::Declare)
BuildRequires : perl(Specio::Exporter)
BuildRequires : perl(Specio::Library::Builtins)
BuildRequires : perl(Sub::Info)
BuildRequires : perl(Test2::V0)
BuildRequires : perl(namespace::autoclean)

%description
# NAME
DateTime::Format::ISO8601 - Parses ISO8601 formats
# VERSION
version 0.16

%package dev
Summary: dev components for the perl-DateTime-Format-ISO8601 package.
Group: Development
Provides: perl-DateTime-Format-ISO8601-devel = %{version}-%{release}
Requires: perl-DateTime-Format-ISO8601 = %{version}-%{release}

%description dev
dev components for the perl-DateTime-Format-ISO8601 package.


%package license
Summary: license components for the perl-DateTime-Format-ISO8601 package.
Group: Default

%description license
license components for the perl-DateTime-Format-ISO8601 package.


%package perl
Summary: perl components for the perl-DateTime-Format-ISO8601 package.
Group: Default
Requires: perl-DateTime-Format-ISO8601 = %{version}-%{release}

%description perl
perl components for the perl-DateTime-Format-ISO8601 package.


%prep
%setup -q -n DateTime-Format-ISO8601-0.16
cd %{_builddir}/DateTime-Format-ISO8601-0.16

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-DateTime-Format-ISO8601
cp %{_builddir}/DateTime-Format-ISO8601-0.16/LICENSE %{buildroot}/usr/share/package-licenses/perl-DateTime-Format-ISO8601/93c8de1b907e38cb6d6df92419c40c81c8afe7ad
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/DateTime::Format::ISO8601.3
/usr/share/man/man3/DateTime::Format::ISO8601::Types.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-DateTime-Format-ISO8601/93c8de1b907e38cb6d6df92419c40c81c8afe7ad

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
