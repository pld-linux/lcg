Summary:	LDP Linux Consultants Guide
Summary(pl):	Przewodnik po Linuksowych Konsultantach
Name:		lcg
Version:	7.6.6
Release:	1
License:	distributable
Group:		Documentation
Source0:	http://www.tldp.org/LDP//%{name}/Consultants-Guide.html.tar.gz
URL:		http://www.tldp.org/LDP/%{name}/html/index.html
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Replacement for the Consultants-HOWTO. A listing of companies
providing commercial Linux related support. For further information,
see http://www.linuxports.com.

%description -l pl
Nastêpca Consultants-HOWTO. Lista firm zajmuj±cych siê komercyjnie
Linuksem. Wiêcej informacji na stronie http://www.linuxports.com.

%prep
%setup -q -n Consultants-Guide

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/LDP/%{name}

cp -ar * $RPM_BUILD_ROOT%{_docdir}/LDP/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_docdir}/LDP/%{name}
