Summary:	Sphinx Extension adding support for custom favicons
Summary(pl.UTF-8):	Rozszerzenie Sphinksa dodające obsługę własnych favikonek
Name:		python3-sphinx_favicon
Version:	0.2
Release:	5
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx-favicon/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-favicon/sphinx-favicon-%{version}.tar.gz
# Source0-md5:	758925ab5b4669f214d0be843f033caa
URL:		https://pypi.org/project/sphinx-favicon/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools >= 1:40.9.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With sphinx-favicon, you can add custom favicons to your Sphinx HTML
documentation quickly and easily.

%description -l pl.UTF-8
Przy użyciu modułu sphinx-favicon można szybko i łatwo dodawać własne
favikonki do dokumentacji HTML generowanej przez Sphinksa.

%prep
%setup -q -n sphinx-favicon-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/sphinx-favicon
%{py3_sitescriptdir}/sphinx_favicon-%{version}-py*.egg-info
