%define python_sitepkgsdir %(echo `python -c "import sys; print (sys.prefix + '/lib/python' + sys.version[:3] + '/site-packages/')"`)

Summary:	LDAP Module for Python
Summary(pl):	Modu³ LDAP dla Pythona
Name:		python-ldap
Version:	1.10alpha3
Release:	1
License:	Public Domain 
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Source0:	http://prdownloads.sourceforge.net/python-ldap/%{name}-%{version}-src.tar.gz
Patch0:		%{name}-openldap2.x.patch
Patch1:		%{name}-Makefile.patch
Patch2:		%{name}-no_ufn.patch
URL:		http://python-ldap.sourceforge.net/
BuildRequires:	python-devel >= 2.1
Requires:	python >= 1.5
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
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
# %%configure will not work!
CFLAGS="%{rpmcflags}" sh configure --prefix=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{python_sitepkgsdir},%{_examplesdir}/%{name}}

%{__make} install DESTDIR="$RPM_BUILD_ROOT"
install Demo/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}

gzip -9fn README TODO ChangeLog Doc/_ldap/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Doc/_ldap/*.gz *.gz
%dir %{python_sitepkgsdir}/%{name}/*.py*
%attr(755,root,root) %{python_sitepkgsdir}/*.so
%{python_sitepkgsdir}/*.pth
%{_examplesdir}/%{name}
