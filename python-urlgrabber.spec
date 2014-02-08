%define oname urlgrabber
%define name python-%oname
%define version 3.9.1

Summary: A high-level cross-protocol url-grabber
Name: %{name}
Version: %{version}
Release: 6
Source0: http://urlgrabber.baseurl.org/download/%{oname}-%{version}.tar.gz
Patch1: urlgrabber-HEAD.patch
License: LGPLv2+
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArchitectures: noarch
Url: http://urlgrabber.baseurl.org/
BuildRequires: python-devel
BuildRequires: python-curl
Requires: python-curl

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
%patch1 -p1

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




%changelog
* Tue Feb 21 2012 abf
- The release updated by ABF

* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 3.9.1-4mdv2011.0
+ Revision: 668048
- mass rebuild

* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 3.9.1-3mdv2011.0
+ Revision: 590018
- rebuild for python 2.7
- rebuild for python 2.7

* Sun Sep 27 2009 Götz Waschk <waschk@mandriva.org> 3.9.1-1mdv2011.0
+ Revision: 449750
- new version
- drop patch 0
- add Fedora patch for int/float multiplication bug

* Wed Aug 05 2009 Götz Waschk <waschk@mandriva.org> 3.9.0-1mdv2010.0
+ Revision: 410206
- update build deps
- new version
- new url
- depend on pycurl
- add timeout patch from Fedora

* Mon Jun 08 2009 Götz Waschk <waschk@mandriva.org> 3.1.0-1mdv2010.0
+ Revision: 383899
- update to new version 3.1.0

* Mon Dec 29 2008 Crispin Boylan <crisb@mandriva.org> 3.0.0-2mdv2009.1
+ Revision: 321179
- Rebuild for 2.6

* Thu Aug 14 2008 Götz Waschk <waschk@mandriva.org> 3.0.0-1mdv2009.0
+ Revision: 271733
- new version
- update license

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 2.9.9-7mdv2009.0
+ Revision: 259857
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 2.9.9-6mdv2009.0
+ Revision: 247705
- rebuild

* Tue Feb 12 2008 Thierry Vignaud <tv@mandriva.org> 2.9.9-4mdv2008.1
+ Revision: 166738
- fix description-line-too-long
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 2.9.9-4mdv2008.0
+ Revision: 67518
- rebuild


* Wed Dec 13 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.9.9-3mdv2007.0
+ Revision: 96456
- include egg-info files
- Import python-urlgrabber

* Fri Jul 21 2006 Götz Waschk <waschk@mandriva.org> 2.9.9-1mdv2007.0
- Rebuild

* Fri May 19 2006 Götz Waschk <waschk@mandriva.org> 2.9.9-1mdk
- New release 2.9.9

* Sat Feb 25 2006 Götz Waschk <waschk@mandriva.org> 2.9.8-1mdk
- New release 2.9.8

* Wed Jan 11 2006 Michael Scherer <misc@mandriva.org> 2.9.6-2mdk
- Use new python macro
- use mkrel

* Tue Apr 26 2005 G�tz Waschk <waschk@mandriva.org> 2.9.6-1mdk
- New release 2.9.6

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 2.9.0-2mdk
- Rebuild for new python

* Thu Nov 25 2004 G�tz Waschk <waschk@linux-mandrake.com> 2.9.0-1mdk
- initial package

