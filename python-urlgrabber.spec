Summary:        A high-level cross-protocol url-grabber
Name:           python-urlgrabber
Version:        4.1.0
Release:        1
License:        LGPLv2+
Group:          Development/Python
Url:            https://urlgrabber.baseurl.org/
#Source0:		https://pypi.io/packages/source/u/urlgrabber/urlgrabber-%{version}.tar.gz
Source0:        https://github.com/rpm-software-management/urlgrabber/releases/download/urlgrabber-%(echo %version |sed -e 's,\.,-,g')/urlgrabber-%{version}.tar.gz
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pycurl)
BuildRequires:  python3dist(six)

BuildArch:      noarch

%description
A high-level cross-protocol url-grabber.

Using urlgrabber, data can be fetched in three basic ways:

  urlgrab(url) copy the file to the local filesystem
  urlopen(url) open the remote file and return a file object (like
  urllib2.urlopen)
  urlread(url) return the contents of the file as a string

When using these functions (or methods), urlgrabber supports the following
features:

  * identical behavior for http://, ftp://, and file:// urls
  * http keepalive - faster downloads of many files by using only a single
    connection
  * byte ranges - fetch only a portion of the file
  * reget - for a urlgrab, resume a partial download
  * progress meters - the ability to report download progress automatically,
    even when using urlopen!
  * throttling - restrict bandwidth usage
  * retries - automatically retry a download if it fails. The number of retries
    and failure types are configurable.
  * authenticated server access for http and ftp
  * proxy support - support for authenticated http and ftp proxies
  * mirror groups - treat a list of mirrors as a single source, automatically
    switching mirrors if there is a failure.

%files
%license LICENSE
%doc installed-docs/*
%{_bindir}/urlgrabber
%{_libexecdir}/urlgrabber-ext-down
%{py_sitedir}/urlgrabber
%{py_sitedir}/urlgrabber-*.*info/

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n urlgrabber-%version

%build
%py_build

%install
%py_install

# docs
mv %buildroot%_datadir/doc/urlgrabber-%version/ installed-docs

#sed -e "s|/usr/bin/python|%{__python}|" -i %{buildroot}%{_libexecdir}/urlgrabber-ext-down

