%include	/usr/lib/rpm/macros.perl
Summary:	CGI-Out perl module
Summary(pl):	Modu³ perla CGI-Out
Name:		perl-CGI-Out
Version:	100.010301
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/CGI-Out-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-libnet
Provides:	perl(CGI::BigDeath)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI-Out is a helper routine for building CGI programs. It buffers
stdout until you're completed building your output. If you should get
an error before you are finished, then it will display a nice error
message (in HTML), log the error, and send email about the problem.

%description -l pl
CGI-Out zawiera procedurê pomocn± przy tworzeniu programów CGI.

%prep
%setup -q -n CGI-Out-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/CGI/*.pm
%{_mandir}/man3/*
