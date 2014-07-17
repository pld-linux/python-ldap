#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		module	ldap
Summary:	LDAP client API for Python
Summary(pl.UTF-8):	API klienckie LDAP dla Pythona
Name:		python-%{module}
Version:	2.4.15
Release:	1
Epoch:		1
License:	Python-like
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/p/python-ldap/%{name}-%{version}.tar.gz
# Source0-md5:	f12183c87579631584c4bbe2d85ad0d9
Patch0:		%{name}-sasl2.patch
Patch1:		build.patch
URL:		http://python-ldap.sourceforge.net/
BuildRequires:	cyrus-sasl >= 2.1.0
BuildRequires:	openldap-devel >= 2.4.6
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	rpm-pythonprov
Requires:	python-modules
Provides:	ldapmodule
Obsoletes:	ldapmodule
Obsoletes:	python-ldapmodule
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
python-ldap provides an object-oriented API to access LDAP directory
servers from Python programs. Mainly it wraps the OpenLDAP client libs
for that purpose.

Additionally the package contains modules for other LDAP-related stuff
(e.g. processing LDIF, LDAPURLs, LDAPv3 sub-schema, etc.).

%description -l pl.UTF-8
Moduł python-ldap dostarcza zorientowane obiektowo API pozwalające na
dostęp do usług katalogowych LDAP z poziomu programów w Pythonie.
Głównie obudowuje w tym celu biblioteki klienckie OpenLDAP.

Dodatkowo pakiet zawiera moduły do innych zadań związanych z LDAP (jak
przetwarzanie LDIF, LDAPURL, podschematy LDAPv3 itp.).

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

LDAPNOINIT=1 \
PYTHONPATH=$(echo build/lib.linux-*/) \
%{__python} -c "import ldap; print ldap.__version__; ldapo = ldap.initialize('ldap://localhost')"
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
%doc CHANGES LICENCE README TODO
%attr(755,root,root) %{py_sitedir}/_ldap.so
%{py_sitedir}/dsml.py[co]
%{py_sitedir}/ldapurl.py[co]
%{py_sitedir}/ldif.py[co]
%{py_sitedir}/ldap
%{py_sitedir}/python_ldap-%{version}-py*.egg-info
