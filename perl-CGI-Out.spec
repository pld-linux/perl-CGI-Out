%define	pdir	CGI
%define	pnam	Out
%include	/usr/lib/rpm/macros.perl
Summary:	CGI-Out perl module
Summary(pl):	Modu� perla CGI-Out
Name:		perl-CGI-Out
Version:	100.010301
Release:	5

License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
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
CGI-Out zawiera procedur� pomocn� przy tworzeniu program�w CGI.

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
