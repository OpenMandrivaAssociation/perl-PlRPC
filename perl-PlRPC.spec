%define module 	PlRPC

Summary:	%{module} perl module
Name:		perl-%{module}
Version:	0.2020
Release:	12
License:	GPLv2 or Artistic
Group:		Development/Perl
Url:		ftp://ftp.funet.fi/pub/languages/perl/CPAN/authors/id/JWIED
Source0:	%{module}-%{version}.tar.bz2
Buildarch:	noarch
BuildRequires:	perl-Net-Daemon
BuildRequires:	perl-Storable
BuildRequires:	perl-devel
BuildRequires:	perl-doc

%description
%{module} - module for perl

%prep
%setup -qn %{module}

%build

%__perl Makefile.PL INSTALLDIRS=vendor --defaultdeps
%make

%install
%makeinstall_std

%files 
%doc README ChangeLog 
%{perl_vendorlib}/Bundle/*
%{perl_vendorlib}/RPC/*
%{_mandir}/man3/*

