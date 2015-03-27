%define upstream_name    Mouse
%define upstream_version 2.4.1

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

License:    GPL+ or Artistic
Group:      Development/Perl
Summary:    Moose minus the antlers
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/G/GF/GFUJI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::Method::Modifiers)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(ExtUtils::ParseXS) >= 2.210.0
BuildRequires: perl(MRO::Compat)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl-devel

Provides:      perl-Moose-implementation

%description
the Moose manpage is wonderful.

Unfortunately, it's a little slow. Though significant progress has been
made over the years, the compile time penalty is a non-starter for some
applications.

Mouse aims to alleviate this by providing a subset of Moose's
functionality, faster. In particular, the Moose/has manpage is missing only
a few expert-level features.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/*


