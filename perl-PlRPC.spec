%define module 	PlRPC
%define version 0.2020
%define release %mkrel 4

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

