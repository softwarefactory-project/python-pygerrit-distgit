%global         sum Pygerrit provides a simple interface for clients to interact with Gerrit Code Review
%global         uname pygerrit

Name:           python-pygerrit
Version:        1.0.0
Release:        1%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://github.com/sonyxperiadev/%{uname}
Source0:        https://pypi.python.org/packages/04/9b/fd6b6169c59b2e5d19a5b50b0d9ab18ffd3126726e4a2dd9f0dcfd7ca2e6/%{uname}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python-ecdsa
Requires:       python-paramiko
Requires:       python-crypto
Requires:       python-requests

Buildrequires:  python2-devel
Buildrequires:  python-setuptools
Buildrequires:  python-pbr
Buildrequires:  python-nose

%description
Pygerrit provides a simple interface for clients to interact
with Gerrit Code Review via ssh or the REST API.

%package -n python2-pygerrit
Summary:        %{sum}
Requires:       python-ecdsa
Requires:       python-paramiko
Requires:       python-crypto
Requires:       python-requests

Buildrequires:  python2-devel
Buildrequires:  python-setuptools
Buildrequires:  python-pbr
Buildrequires:  python-nose

%description -n python2-pygerrit
Pygerrit provides a simiple interface for clients to interact
with Gerrit Code Review via ssh or the REST API.

%prep
%autosetup -n %{uname}-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%check
nosetests -v unittests.py

%files -n python2-pygerrit
%{python2_sitelib}/*

%changelog
* Tue Feb 21 2017 Fabien Boucher <fboucher@redhat.com> - 1.0.0-1
- Initial packaging
