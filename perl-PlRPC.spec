%define module 	PlRPC
%define version 0.2020
%define release 8

Summary:	%{module} perl module
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License: 	GPL or Artistic
Group:		Development/Perl
URL:		ftp://ftp.funet.fi/pub/languages/perl/CPAN/authors/id/JWIED
Source0:	%{module}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	perl-Net-Daemon perl-Storable perl-devel perl-doc
Buildarch:	noarch

%description
%{module} - module for perl

%prep
%setup -q -n %{module}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor --defaultdeps
%{__make}

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README ChangeLog 
%{perl_vendorlib}/Bundle/*
%{perl_vendorlib}/RPC/*
%_mandir/man3*/*



%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.2020-6mdv2012.0
+ Revision: 765595
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.2020-5
+ Revision: 764123
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2020-4
+ Revision: 667293
- mass rebuild

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.2020-3mdv2011.0
+ Revision: 426575
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.2020-2mdv2009.0
+ Revision: 223992
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 0.2020-1mdv2008.1
+ Revision: 136335
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Jul 07 2007 Funda Wang <fwang@mandriva.org> 0.2020-1mdv2008.0
+ Revision: 49341
- BR perl-doc
- fix tarball dirname
- New version

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 0.2018-2mdv2008.0
+ Revision: 23321
- rebuild


* Mon Nov 29 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.2018-1mdk
- 0.2018.

* Thu Aug 14 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.2017-2mdk
- rebuild for new perl
- drop PREFIX
- use %%makeinstall_std macro

* Mon Jun 30 2003 François Pons <fpons@mandrakesoft.com> 0.2017-1mdk
- 0.2017.

* Fri May 16 2003 Guillaume Rousse <g.rousse@linux-mandrake.com> 0.2016-4mdk
- rebuild for dependencies

* Mon May 05 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.2016-3mdk
- buildrequires

* Wed Mar 12 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.2016-2mdk
- fix build & fix requires

* Mon Mar 04 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.2016-1mdk
- 0.2016

* Tue Sep 25 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.2015-1mdk
- added by Christian Zoffoli <czoffoli@linux-mandrake.com> :
	- first mandrake release

