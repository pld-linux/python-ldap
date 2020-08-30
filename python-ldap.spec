#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_with	tests	# unit tests (require LDAP server)

Summary:	LDAP client API for Python 2
Summary(pl.UTF-8):	API klienckie LDAP dla Pythona 2
Name:		python-ldap
Version:	3.3.1
Release:	1
Epoch:		1
License:	Python-like
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/python-ldap/
Source0:	https://files.pythonhosted.org/packages/source/p/python-ldap/%{name}-%{version}.tar.gz
# Source0-md5:	7608579722c491e42f5f63b3f88a95fb
URL:		http://python-ldap.sourceforge.net/
BuildRequires:	cyrus-sasl-devel >= 2.1.0
BuildRequires:	openldap-devel >= 2.4.6
BuildRequires:	openssl-devel
%if %{with tests}
BuildRequires:	openldap >= 2.4.6
BuildRequires:	openldap-servers >= 2.4.6
%endif
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pyasn1 >= 0.3.7
BuildRequires:	python-pyasn1_modules >= 0.1.5
%endif
%endif
%if %{with python2}
BuildRequires:	python3-devel >= 1:3.4
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pyasn1 >= 0.3.7
BuildRequires:	python3-pyasn1_modules >= 0.1.5
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-modules >= 1:2.7
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

%package -n python3-ldap
Summary:	LDAP client API for Python 3
Summary(pl.UTF-8):	API klienckie LDAP dla Pythona 3
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-ldap
python-ldap provides an object-oriented API to access LDAP directory
servers from Python programs. Mainly it wraps the OpenLDAP client libs
for that purpose.

Additionally the package contains modules for other LDAP-related stuff
(e.g. processing LDIF, LDAPURLs, LDAPv3 sub-schema, etc.).

%description -n python3-ldap -l pl.UTF-8
Moduł python-ldap dostarcza zorientowane obiektowo API pozwalające na
dostęp do usług katalogowych LDAP z poziomu programów w Pythonie.
Głównie obudowuje w tym celu biblioteki klienckie OpenLDAP.

Dodatkowo pakiet zawiera moduły do innych zadań związanych z LDAP (jak
przetwarzanie LDIF, LDAPURL, podschematy LDAPv3 itp.).

%prep
%setup -q

%build
%if %{with python2}
%py_build %{?with_tests:test}

%if %{with tests}
LDAPNOINIT=1 \
PYTHONPATH=$(echo build-2/lib.linux-*/) \
%{__python} -c "import ldap; print ldap.__version__; ldapo = ldap.initialize('ldap://localhost')"
%endif
%endif

%if %{with python3}
%py3_build %{?with_tests:test}

%if %{with tests}
LDAPNOINIT=1 \
PYTHONPATH=$(echo build-3/lib.linux-*/) \
%{__python3} -c "import ldap; print ldap.__version__; ldapo = ldap.initialize('ldap://localhost')"
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/slapdtest
%py_postclean
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/slapdtest
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES LICENCE README TODO
%attr(755,root,root) %{py_sitedir}/_ldap.so
%{py_sitedir}/ldapurl.py[co]
%{py_sitedir}/ldif.py[co]
%{py_sitedir}/ldap
%{py_sitedir}/python_ldap-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-ldap
%defattr(644,root,root,755)
%doc CHANGES LICENCE README TODO
%attr(755,root,root) %{py3_sitedir}/_ldap.cpython-*.so
%{py3_sitedir}/ldap
%{py3_sitedir}/ldapurl.py
%{py3_sitedir}/ldif.py
%{py3_sitedir}/__pycache__/ldapurl.cpython-*.py[co]
%{py3_sitedir}/__pycache__/ldif.cpython-*.py[co]
%{py3_sitedir}/python_ldap-%{version}-py*.egg-info
%endif
