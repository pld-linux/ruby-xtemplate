%define tarname xtemplate
Summary:	An XML/XHTML template library for Ruby
Summary(pl.UTF-8):	Biblioteka szablonów XML/XHTML dla języka Ruby
Name:		ruby-XTemplate
Version:	0.8.0
Release:	2
License:	GPL
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/%{tarname}/%{tarname}-%{version}.tar.gz
# Source0-md5:	84132c80f71d6f5fbb538f87d52e9388
URL:		http://xtemplate.sourceforge.net
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
#BuildArch:	noarch
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An XML/XHTML template library for Ruby.

%description -l pl.UTF-8
Biblioteka szablonów XML/XHTML dla języka Ruby.

%prep
%setup -q -n %{tarname}-%{version}

%build
ruby install.rb config \
	--site-ruby=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}

ruby install.rb setup

rdoc --op rdoc -S --main README README TUTORIAL lib

%install
rm -rf $RPM_BUILD_ROOT

ruby install.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc STATUS CHANGES samples rdoc/*
%attr(755,root,root) %{_bindir}/xtemplate
%dir %{ruby_rubylibdir}/xtemplate
%{ruby_rubylibdir}/xtemplate/*.rb
%{ruby_rubylibdir}/xtemplate.rb
