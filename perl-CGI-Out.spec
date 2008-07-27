%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
%define		pnam	Out
Summary:	CGI::Out perl module
Summary(pl.UTF-8):	Moduł perla CGI::Out
Name:		perl-CGI-Out
Version:	2006.0215
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b9aab3af9d578dd6df9db93e2337be94
URL:		http://search.cpan.org/dist/CGI-Out/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-libnet
BuildRequires:	rpm-perlprov >= 4.1-13
Provides:	perl(CGI::BigDeath)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::Out is a helper routine for building CGI programs. It buffers
stdout until you're completed building your output. If you should get
an error before you are finished, then it will display a nice error
message (in HTML), log the error, and send email about the problem.

%description -l pl.UTF-8
CGI::Out jest procedurą pomocną przy tworzeniu programów CGI. Buforuje
standardowe wyjście do czasu ukończenia tworzenia danych wyjściowych.
Jeśli wykonywanie skryptu zakończy się błędem, procedura wyświetli
ładny komunikat błędu (w HTML-u), zapisze komunikat do loga i
powiadomi o tym e-mailem.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/CGI/*.pm
%{_mandir}/man3/*
