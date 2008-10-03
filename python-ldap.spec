Summary:	LDAP Module for Python
Summary(pl.UTF-8):	Moduł LDAP dla Pythona
Name:		python-ldap
Version:	2.3.5
Release:	2
Epoch:		1
License:	Public Domain
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/python-ldap/%{name}-%{version}.tar.gz
# Source0-md5:	c9732621075edc65b54233fff21fe07c
Patch0:		%{name}-sasl2.patch
URL:		http://python-ldap.sourceforge.net/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	openldap-devel >= 2.4.6
BuildRequires:	cyrus-sasl >= 2.1.0
%pyrequires_eq	python-modules
Provides:	ldapmodule
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	ldapmodule
Obsoletes:	python-ldapmodule

%description
This module provides access to the LDAP (C language) library.

%description -l pl.UTF-8
Moduł ten umożliwia dostęp do bibliotek LDAP.

%prep
%setup -q
%patch0 -p1

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

PYTHONPATH=$RPM_BUILD_ROOT%{py_sitedir}
export PYTHONPATH

python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT%{py_sitedir} -name "*.py" | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/*.py[co]
%{py_sitedir}/ldap
%{py_sitedir}/*.egg-info
