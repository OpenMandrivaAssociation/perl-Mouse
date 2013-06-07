%define upstream_name    Mouse
%define upstream_version 1.11

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
%setup -q -n %{upstream_name}-%{upstream_version}

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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.930.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue May 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.930.0-1
+ Revision: 675370
- update to new version 0.93

* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.920.0-1
+ Revision: 654128
- update to new version 0.92

* Mon Mar 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.910.0-1
+ Revision: 644769
- update to new version 0.91

* Thu Feb 24 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.900.0-1
+ Revision: 639672
- update to new version 0.90

* Wed Feb 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.890.0-1
+ Revision: 635191
- update to new version 0.89

* Mon Dec 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.880.0-1mdv2011.0
+ Revision: 612249
- update to new version 0.88
- update to new version 0.87

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.860.0-1mdv2011.0
+ Revision: 596626
- update to 0.86

* Sat Nov 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.820.0-1mdv2011.0
+ Revision: 594263
- update to new version 0.82

* Sat Oct 16 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.800.0-1mdv2011.0
+ Revision: 586086
- new version

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 0.640.0-1mdv2011.0
+ Revision: 561571
- update to 0.64

* Sun Jul 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.630.0-1mdv2011.0
+ Revision: 558794
- new version

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.620.0-2mdv2011.0
+ Revision: 556010
- rebuild for perl 5.12

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.620.0-1mdv2011.0
+ Revision: 551994
- update to 0.62

* Thu Apr 22 2010 Jérôme Quelin <jquelin@mandriva.org> 0.550.0-1mdv2010.1
+ Revision: 537884
- update to 0.55

* Sun Apr 18 2010 Jérôme Quelin <jquelin@mandriva.org> 0.540.0-1mdv2010.1
+ Revision: 536206
- update to 0.54

* Sat Mar 27 2010 Jérôme Quelin <jquelin@mandriva.org> 0.520.0-2mdv2010.1
+ Revision: 528113
- rebuild
- update to 0.52

* Mon Mar 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.510.0-1mdv2010.1
+ Revision: 519955
- update to 0.51

* Fri Mar 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.500.0-2mdv2010.1
+ Revision: 518456
- ship debug files in -debug

* Mon Feb 08 2010 Jérôme Quelin <jquelin@mandriva.org> 0.500.0-1mdv2010.1
+ Revision: 502106
- update to 0.50

* Tue Feb 02 2010 Jérôme Quelin <jquelin@mandriva.org> 0.490.0-1mdv2010.1
+ Revision: 499486
- update to 0.49

* Mon Feb 01 2010 Jérôme Quelin <jquelin@mandriva.org> 0.480.0-1mdv2010.1
+ Revision: 498980
- update to 0.48

* Fri Jan 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.470.0-1mdv2010.1
+ Revision: 491630
- update to 0.47

* Sun Jan 10 2010 Jérôme Quelin <jquelin@mandriva.org> 0.460.0-1mdv2010.1
+ Revision: 488605
- update to 0.46

* Wed Dec 23 2009 Jérôme Quelin <jquelin@mandriva.org> 0.450.100-1mdv2010.1
+ Revision: 481710
- update to 0.4501

* Mon Dec 21 2009 Jérôme Quelin <jquelin@mandriva.org> 0.450.0-1mdv2010.1
+ Revision: 480731
- update to 0.45

* Sat Dec 12 2009 Jérôme Quelin <jquelin@mandriva.org> 0.440.0-1mdv2010.1
+ Revision: 477615
- update to 0.44

* Tue Dec 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.430.0-1mdv2010.1
+ Revision: 474729
- update to 0.43

* Sun Dec 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.420.0-1mdv2010.1
+ Revision: 474102
- update to 0.42

* Sat Dec 05 2009 Jérôme Quelin <jquelin@mandriva.org> 0.410.0-1mdv2010.1
+ Revision: 473770
- mouse is now arch-dependant
- adding missing buildrequires:
- update to 0.41

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.400.0-1mdv2010.1
+ Revision: 460765
- update to 0.40

* Sun Sep 27 2009 Jérôme Quelin <jquelin@mandriva.org> 0.360.0-1mdv2010.0
+ Revision: 449992
- update to 0.36

* Thu Sep 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.330.0-1mdv2010.0
+ Revision: 448259
- update to 0.33

* Tue Sep 22 2009 Jérôme Quelin <jquelin@mandriva.org> 0.300.0-1mdv2010.0
+ Revision: 447135
- update to 0.30

* Fri Sep 18 2009 Jérôme Quelin <jquelin@mandriva.org> 0.290.0-1mdv2010.0
+ Revision: 444316
- update to 0.29

* Thu Sep 10 2009 Jérôme Quelin <jquelin@mandriva.org> 0.280.0-1mdv2010.0
+ Revision: 437171
- update to 0.28

* Mon Jul 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.27-1mdv2010.0
+ Revision: 392999
- update to new version 0.27

* Wed Jun 24 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.25-1mdv2010.0
+ Revision: 388888
- update to new version 0.25

* Mon Jun 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.23-1mdv2010.0
+ Revision: 384029
- update to new version 0.23

* Thu May 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.22-2mdv2010.0
+ Revision: 378181
- provides perl-Moose-implementation virtual package

* Mon May 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.22-1mdv2010.0
+ Revision: 371867
- update to new version 0.22

* Sun May 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.19-1mdv2010.0
+ Revision: 371228
- update to new version 0.19

* Thu Feb 26 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.17-1mdv2009.1
+ Revision: 345117
- update to new version 0.17

* Thu Feb 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.16-1mdv2009.1
+ Revision: 339773
- update to new version 0.16

* Sun Jan 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-1mdv2009.1
+ Revision: 324510
- update to new version 0.14

* Sun Dec 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-1mdv2009.1
+ Revision: 320438
- update to new version 0.13

* Mon Dec 08 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-1mdv2009.1
+ Revision: 311974
- update to new version 0.12

* Tue Nov 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-1mdv2009.1
+ Revision: 302140
- update to new version 0.11

* Wed Oct 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2009.1
+ Revision: 298186
- new version

* Wed Jul 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2009.0
+ Revision: 242119
- import perl-Mouse


* Wed Jul 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2009.0
- initial mdv release, generated with cpan2dist


