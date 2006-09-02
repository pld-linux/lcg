Summary:	LDP Linux Consultants Guide
Summary(pl):	Przewodnik po Linuksowych Konsultantach
Name:		lcg
Version:	7.6.6
Release:	1
License:	distributable
Group:		Documentation
Source0:	http://www.tldp.org/LDP/lcg/Consultants-Guide.html.tar.gz
# Source0-md5:	d43716dbe6d771f57b1ee48f62e0b034
URL:		http://www.tldp.org/LDP/lcg/html/index.html
Requires:	LDP-base
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Replacement for the Consultants-HOWTO. A listing of companies
providing commercial Linux related support. For further information,
see http://www.linuxports.com/.

%description -l pl
Nastêpca Consultants-HOWTO. Lista firm zajmuj±cych siê komercyjnie
Linuksem. Wiêcej informacji na stronie http://www.linuxports.com/.

%prep
%setup -q -n Consultants-Guide

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/LDP/%{name}
cp -a * $RPM_BUILD_ROOT%{_docdir}/LDP/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_docdir}/LDP/%{name}
