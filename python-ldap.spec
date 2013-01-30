#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define 	module	ldap
Summary:	LDAP Module for Python
Summary(pl.UTF-8):	Moduł LDAP dla Pythona
Name:		python-%{module}
Version:	2.4.10
Release:	1
Epoch:		1
License:	Public Domain
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/p/python-ldap/%{name}-%{version}.tar.gz
# Source0-md5:	d76131af192771567d3f2d2aff9469a9
Patch0:		%{name}-sasl2.patch
Patch1:		build.patch
URL:		http://python-ldap.sourceforge.net/
BuildRequires:	cyrus-sasl >= 2.1.0
BuildRequires:	openldap-devel >= 2.4.6
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
Requires:	python-modules
Provides:	ldapmodule
Obsoletes:	ldapmodule
Obsoletes:	python-ldapmodule
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides access to the LDAP (C language) library.

%description -l pl.UTF-8
Moduł ten umożliwia dostęp do bibliotek LDAP.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
%{__python} setup.py build

%if %{with tests}
%{__python} setup.py test

PYTHONPATH=$(echo build/lib.linux-*/) \
%{__python} -c "import ldap; print ldap.__version__; ldapo = ldap.initialize('localhost')"
%endif

%install
rm -rf $RPM_BUILD_ROOT
#PYTHONPATH=$RPM_BUILD_ROOT%{py_sitedir}
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/*.py[co]
%{py_sitedir}/ldap
%{py_sitedir}/*.egg-info
