%define oname urlgrabber

Summary: A high-level cross-protocol url-grabber

Name:		python-%{oname}
Version: 	3.10.1
Release: 	7
Source0: 	http://urlgrabber.baseurl.org/download/urlgrabber-%{version}.tar.gz
License: 	LGPLv2+
Group:		Development/Python
BuildArch: 	noarch
Url:		http://urlgrabber.baseurl.org/
BuildRequires: 	python-devel
BuildRequires: 	python2-curl
Requires: 	python2-curl

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
%setup -q -n %{oname}-%{version}

%build
python2 setup.py build

%install
rm -rf %{buildroot} installed-docs
python2 setup.py install --root=%{buildroot}
mv %{buildroot}%{_datadir}/doc/%{oname}-%{version}/ installed-docs

%clean

%files
%doc installed-docs/*
%{_bindir}/%{oname}
/usr/libexec/*
%{py2_puresitedir}/%{oname}/
%{py2_puresitedir}/*.egg-info

