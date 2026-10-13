Name:		python-zeep
Version:	4.3.3
Release:	1
Summary:	A Python SOAP client
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/zeep/
Source0:	zeep-%{version}.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(lxml)
BuildRequires:	python%{pyver}dist(requests)
BuildRequires:	python%{pyver}dist(requests-toolbelt)
BuildRequires:	python%{pyver}dist(requests-file)
BuildRequires:	python%{pyver}dist(isodate)
BuildRequires:	python%{pyver}dist(platformdirs)
BuildArch:	noarch

%prep -a
cat >> pyproject.toml << 'EOF'

[tool.setuptools.packages.find]
where = ["src"]
EOF

%description
A Python SOAP client.

%files
%{py_sitedir}/*
