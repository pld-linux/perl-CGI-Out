%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	CGI-Out perl module
Summary(pl):	Modu³ perla CGI-Out
Name:		perl-CGI-Out
Version:	96.081401
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/CGI-Out-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
CGI-Out is a helper routine for building CGI programs. It buffers stdout 
until you're completed building your output. If you should get an error 
before you are finished, then it will display a nice error message (in HTML),
log the error, and send email about the problem.

%description -l pl
CGI-Out zawiera procedurê pomocn± przy tworzeniu programów CGI. 

%prep
%setup -q -n CGI-Out-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/CGI/Out
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitelib}/CGI/*.pm
%{perl_sitearch}/auto/CGI/Out

%{_mandir}/man3/*
