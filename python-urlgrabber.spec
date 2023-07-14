%define oname   urlgrabber

%global majorver 4
%global minorver 0
%global patchver 0
%global dashversion %{majorver}-%{minorver}-%{patchver}

Summary:        A high-level cross-protocol url-grabber
Name:           python-%oname
Version:        %{majorver}.%{minorver}.%{patchver}
Release:        3
License:        LGPLv2+
Group:          Development/Python
Url:            http://urlgrabber.baseurl.org/
Source0:        https://github.com/rpm-software-management/urlgrabber/releases/download/urlgrabber-%{dashversion}/urlgrabber-%{version}.tar.gz
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pycurl)
BuildRequires:  python3dist(six)
%{?python_provide:%python_provide python3-%{oname}}

BuildArch:      noarch

%global _description \
A high-level cross-protocol url-grabber. \
\
Using urlgrabber, data can be fetched in three basic ways: \
\
  urlgrab(url) copy the file to the local filesystem \
  urlopen(url) open the remote file and return a file object (like \
  urllib2.urlopen) \
  urlread(url) return the contents of the file as a string \
\
When using these functions (or methods), urlgrabber supports the following \
features: \
\
  * identical behavior for http://, ftp://, and file:// urls \
  * http keepalive - faster downloads of many files by using only a single \
    connection \
  * byte ranges - fetch only a portion of the file \
  * reget - for a urlgrab, resume a partial download \
  * progress meters - the ability to report download progress automatically, \
    even when using urlopen! \
  * throttling - restrict bandwidth usage \
  * retries - automatically retry a download if it fails. The number of retries \
    and failure types are configurable. \
  * authenticated server access for http and ftp \
  * proxy support - support for authenticated http and ftp proxies \
  * mirror groups - treat a list of mirrors as a single source, automatically \
    switching mirrors if there is a failure.

%description %_description

%prep
%autosetup -n %oname-%version -p1

%build
%py3_build

%install
%py3_install

mv %buildroot%_datadir/doc/%oname-%version/ installed-docs

sed -e "s|/usr/bin/python|%{__python3}|" -i %{buildroot}%{_libexecdir}/%oname-ext-down

%files
%license LICENSE
%doc installed-docs/*
%{_bindir}/%oname
%{_libexecdir}/%oname-ext-down
%{python3_sitelib}/%oname/
%{python3_sitelib}/*.egg-info
