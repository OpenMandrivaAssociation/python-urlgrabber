%define oname urlgrabber
%define name python-%oname
%define version 2.9.9

Summary: A high-level cross-protocol url-grabber
Name: %{name}
Version: %{version}
Release: %mkrel 7
Source0: http://linux.duke.edu/projects/urlgrabber/download/%{oname}-%{version}.tar.bz2
License: LGPL
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArchitectures: noarch
Url: http://linux.duke.edu/projects/mini/urlgrabber/
BuildRequires: python-devel

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


%prep
%setup -q -n %oname-%version

%build
python setup.py build

%install
rm -rf %buildroot installed-docs
python setup.py install --root=%{buildroot}
mv %buildroot%_datadir/doc/%oname-%version/ installed-docs

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc installed-docs/*
%_bindir/%oname
%py_puresitedir/%oname/
%py_puresitedir/*.egg-info


