%define pkgname xtemplate
Summary:	An XML/XHTML template library for Ruby
Summary(pl.UTF-8):	Biblioteka szablonów XML/XHTML dla języka Ruby
Name:		ruby-%{pkgname}
Version:	0.8.0
Release:	6
License:	GPL
Group:		Development/Libraries
Source0:	http://downloads.sourceforge.net/xtemplate/%{pkgname}-%{version}.tar.gz
# Source0-md5:	84132c80f71d6f5fbb538f87d52e9388
URL:		http://xtemplate.sourceforge.net
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildRequires:	sed >= 4.0
Provides:	ruby-XTemplate
Obsoletes:	ruby-XTemplate
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An XML/XHTML template library for Ruby.

%description -l pl.UTF-8
Biblioteka szablonów XML/XHTML dla języka Ruby.

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -n %{pkgname}-%{version}
%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/*

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib
rm -r ri/{Enumerable,Hash}
rm ri/created.rid
rm ri/cache.ri

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_ridir},%{ruby_rdocdir},%{_bindir}}

cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc STATUS CHANGES samples
%attr(755,root,root) %{_bindir}/xtemplate
%{ruby_vendorlibdir}/xtemplate.rb
%{ruby_vendorlibdir}/xtemplate

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/XTemplate
