%include	/usr/lib/rpm/macros.python
Summary:	LDAP Module for Python
Summary(pl):	Modu³ LDAP dla Pythona
Name:		python-ldap
Version:	2.0.0pre04
Release:	3
License:	Public Domain
Group:		Libraries/Python
Source0:	http://prdownloads.sourceforge.net/python-ldap/%{name}-%{version}.tar.gz
URL:		http://python-ldap.sourceforge.net/
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	rpm-pythonprov
BuildRequires:	openldap-devel >= 1.2.6
%pyrequires_eq	python-modules
Requires:	openldap >= 1.2.6
Provides:	ldapmodule
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	ldapmodule
Obsoletes:	python-ldapmodule

%description
This module provides access to the LDAP (C language) library.

%description -l pl
Modu³ ten umo¿liwia dostêp do bibliotek LDAP.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

PYTHONPATH=$RPM_BUILD_ROOT%{py_sitedir}
export PYTHONPATH

python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

gzip -9fn README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/*.py[co]

%dir %{py_sitedir}/ldap
%{py_sitedir}/ldap/*.py[co]
