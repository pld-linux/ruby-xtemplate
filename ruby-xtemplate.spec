%define ruby_archdir    %(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	An XML/XHTML template library for Ruby
Summary(pl):	Biblioteka szablon�w XML/XHTML dla j�zyka Ruby
Name:		ruby-XTemplate
%define tarname xtemplate
Version:	0.7.0
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/%{tarname}/%{tarname}-%{version}.tar.gz
# Source0-md5:	069de93c3cb8a3f18dc47f16b98636a4
URL:		http://xtemplate.sourceforge.net
BuildRequires:	ruby
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An XML/XHTML template library for Ruby.

%description -l pl
Biblioteka szablon�w XML/XHTML dla j�zyka Ruby.

%prep
%setup -q -n %{tarname}-%{version}

%build
ruby install.rb config \
	--site-ruby=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}

ruby install.rb setup 

rdoc --op rdoc -S --main README README  TUTORIAL lib

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
