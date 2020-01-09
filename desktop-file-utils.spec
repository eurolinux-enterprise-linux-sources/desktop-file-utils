%global pkg desktop-file-utils
%global pkgname desktop-file-utils

Summary: Utilities for manipulating .desktop files
Name: desktop-file-utils
Version: 0.23
Release: 1%{?dist}
URL: https://www.freedesktop.org/software/desktop-file-utils
Source0: https://www.freedesktop.org/software/desktop-file-utils/releases/%{name}-%{version}.tar.xz
Source1: desktop-entry-mode-init.el
# Add Pantheon to the list of desktop environments (#1333550, fdo#97385)
# upstream patch by David Faure
# https://cgit.freedesktop.org/xdg/desktop-file-utils/commit/?id=5b88c95c45e91781aed441c446210c6979350c3f
Patch0: desktop-file-utils-0.23-add-pantheon.patch
License: GPLv2+
Group: Development/Tools

BuildRequires: glib2-devel
BuildRequires: emacs
Requires: emacs-filesystem
Provides: emacs-%{pkg} = %{version}-%{release}
Provides: emacs-%{pkg}-el = %{version}-%{release}
Obsoletes: emacs-%{pkg} < 0.20-3
Obsoletes: emacs-%{pkg}-el < 0.20-3

%description
.desktop files are used to describe an application for inclusion in
GNOME or KDE menus.  This package contains desktop-file-validate which
checks whether a .desktop file complies with the specification at
http://www.freedesktop.org/standards/, and desktop-file-install
which installs a desktop file to the standard directory, optionally
fixing it up in the process.


%prep
%setup -q
%patch0 -p1 -b .add-pantheon

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

mkdir -p $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}
mv $RPM_BUILD_ROOT%{_emacs_sitelispdir}/*.el* $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}
install -Dpm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}/desktop-entry-mode-init.el
touch $RPM_BUILD_ROOT%{_emacs_sitestartdir}/desktop-entry-mode-init.elc

%files
%doc AUTHORS COPYING README NEWS
%{_bindir}/*
%{_mandir}/man1/desktop-file-install.1.gz
%{_mandir}/man1/desktop-file-validate.1.gz
%{_mandir}/man1/update-desktop-database.1.gz
%{_mandir}/man1/desktop-file-edit.1.gz
%{_emacs_sitestartdir}/desktop-entry-mode-init.el
%ghost %{_emacs_sitestartdir}/desktop-entry-mode-init.elc
%{_emacs_sitelispdir}/%{pkg}

%changelog
* Thu Nov 24 2016 Kalev Lember <klember@redhat.com> - 0.23-1
- Update to 0.23
- Resolves: #1386844

* Thu Apr 30 2015 Ray Strode <rstrode@redhat.com> 0.22-1
- Update to 0.22
  Resolves: #1217519

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.21-4
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.21-3
- Mass rebuild 2013-12-27

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 19 2012 Kalev Lember <kalevlember@gmail.com> - 0.21-1
- Update to 0.21

* Thu Sep 06 2012 Dan Mashal <dan.mashal@fedoraproject.org> 0.20-4
- Update F17 to 0.20 (#847097).

* Sat Aug 11 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.20-3
- Fold emacs-* subpackages into main (#690264).

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 18 2012 Matthias Clasen <mclasen@redhat.com> - 0.20-1
- Update to 0.20

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 23 2011 Matthias Clasen <mclasen@redhat.com> - 0.19-5
- Fix up locale lists just like other lists

* Tue Dec 20 2011 Matthias Clasen <mclasen@redhat.com> - 0.19-1
- Update to 0.19: support for Unity as desktop env, and support
  for Keywords

* Mon Jul 04 2011 Adam Williamson <awilliam@redhat.com> - 0.18-4
- add unity.patch from upstream: add Unity to list of registered
  environments

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 30 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.18-2
- Add desktop-entry-mode-init.el, fix emacs site-start dir ownership.

* Thu Jan 13 2011 Matthias Clasen <mclasen@redhat.com> - 0.18-1
- Update to 0.18

* Fri Nov  5 2010 Matthias Clasen <mclasen@redhat.com> - 0.16-3
- Don't warn about x-scheme-handler pseudo-mime-types

* Sat Sep 25 2010 Parag Nemade <paragn AT fedoraproject.org> - 0.16-2
- Merge-review cleanup (#225681)

* Thu Apr  1 2010 Matthias Clasen <mclasen@redhat.com> 0.16-1
- Update to 0.16

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 04 2009 Richard Hughes <rhughes@redhat.com> - 0.15-6
- Panu seems to be shipping the prov file in rpmbuild. Remove it here until we
  work out where it belongs.

* Wed Feb 04 2009 Richard Hughes <rhughes@redhat.com> - 0.15-5
- Panu merged the rpm bits for this feature, but we've got a new provides
  filename. Respin this package with the new name.

* Thu Jan 22 2009 Richard Hughes <rhughes@redhat.com> - 0.15-4
- Rename desktop-mime-type.prov to desktop_mime_type.prov and add the tiny
  macros.desktop_mime_type file so that we can trivially patch rpm to enable
  this new functionality.

* Fri May 02 2008 Richard Hughes <rhughes@redhat.com> - 0.15-3
- Add desktop-mime-type.prov so that we can automatically
  generate mimetype provides for packages at build time.
  This lets us do some cool things with PackageKit in the future.

* Wed Mar 19 2008 Ray Strode <rstrode@redhat.com> - 0.15-2
- Drop old unneeded obsoletes on desktop-file-validator
(bug 225681)

* Tue Mar  4 2008 Matthias Clasen <mclasen@redhat.com> - 0.15-1
- Update to 0.15
- Drop upstreamed patch

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.14-3
- Autorebuild for GCC 4.3

* Thu Dec  6 2007 Ray Strode <rstrode@redhat.com> 0.14-2
- make icon extension a warning not an error

* Fri Nov 30 2007 Christopher Stone <chris.stone@gmail.com> 0.14-1
- Upstream sync
- Remove no longer needed short option patch

* Wed Aug 15 2007 Matthias Clasen <mclasen@redhat.com> - 0.13-3
- Make the -m option work (#232761)

* Mon Aug  6 2007 Matthias Clasen <mclasen@redhat.com> - 0.13-2
- Update license field

* Tue Jun  5 2007 Matthias Clasen <mclasen@redhat.com> - 0.13-1
- Update to 0.13, which features a completely rewritten validator

* Thu Mar 08 2007 Florian La Roche <laroche@redhat.com> - 0.12-4
- remove empty post/preun scripts completely

* Tue Nov 28 2006 Ray Strode <rstrode@redhat.com> - 0.12-3
- drop some rm -f cruft
- don't call update-desktop-database from %%post or %%postun

* Tue Nov 28 2006 Ray Strode <rstrode@redhat.com> - 0.12-2
- make --vendor optional

* Tue Nov 28 2006 Ray Strode <rstrode@redhat.com> - 0.12-1
- Update to 0.12

* Fri Oct 27 2006 Ray Strode <rstrode@redhat.com> - 0.11-4
- commit the fix attempted in 0.11-2 and 0.11-3 to the right
  function...

* Fri Oct 27 2006 Ray Strode <rstrode@redhat.com> - 0.11-3
- actually apply the patch written in 0.11-2

* Thu Oct 26 2006 Ray Strode <rstrode@redhat.com> - 0.11-2
- make desktop file validation non-fatal until we
  add support for categories beginning with X- and clean up
  our menu system to not require invalid categories
  (bug 212048)

* Mon Oct 23 2006 Matthias Clasen <mclasen@redhat.com> - 0.11-1
- Update to 0.11

* Wed Jul 26 2006 Jesse Keating <jkeating@redhat.com> - 0.10-7
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.10-6.1
- bump again for double-long bug on ppc(64)

* Fri Feb 10 2006 Ray Strode <rstrode@redhat.com> - 0.10-6
- call update-desktop-database in %%preun (bug 180898)
- don't fail if update-desktop-database fails
- don't use %%makeinstall

* Fri Feb 10 2006 Ray Strode <rstrode@redhat.com> - 0.10-5
- call update-desktop-database in %%post (bug 180898)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.10-4.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Sun Jan 22 2006 Ray Strode <rstrode@redhat.com> - 0.10-4
- don't use uninitialized memory (bug 178591)

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Aug 31 2005 Ray Strode <rstrode@redhat.com> - 0.10-3
- bump build requires for glib to 2.2.0 (bug #146585).

* Thu May 12 2005 Ray Strode <rstrode@redhat.com> - 0.10-2
- Add build requires for emacs (bug #141297).

* Wed Jan 26 2005 Matthias Clasen <mclasen@redhat.com> - 0.10-1
- Update to 0.10

* Mon Oct 18 2004 Miloslav Trmac <mitr@redhat.com> - 0.9-2
- Output error message instead of assertion failure (#134934)

* Tue Sep 28 2004 Mark McLoughlin <markmc@redhat.com> 0.9-1
- Update to 0.9, remove upstreamed patches

* Mon Sep 27 2004 Ray Strode <rstrode@redhat.com> 0.8-6
- Swap if and else in egg_desktop_entries_get_locale_encoding
  to prevent allocating massive amounts of unneeded ram.

* Mon Sep 27 2004 Ray Strode <rstrode@redhat.com> 0.8-5
- Swap if and else in egg_desktop_entries_get_locale_country
  to prevent allocating massive amounts of unneeded ram.

* Thu Sep 23 2004 Ray Strode <rstrode@redhat.com> 0.8-4
- Fix the fix for --remove-show-in option

* Thu Sep 23 2004 Ray Strode <rstrode@redhat.com> 0.8-3
- Fix --remove-show-in option

* Mon Sep 13 2004 Dan Williams <dcbw@redhat.com> 0.8-2
- Fix RH #131983 (annoying log message about "entries != NULL")

* Fri Sep  3 2004 Mark McLoughlin <markmc@redhat.com> 0.8-1
- Update to 0.8

* Sat Jul 31 2004 Dan Williams <dcbw@redhat.com> 0.7-1
- Update to 0.7

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Mar  1 2004 Dan Williams <dcbw@redhat.com> 0.4-2
- Fix RH #117201, initial comment fails validation
- Add in, but do not use, Frederic Crozat's freedesktop.org
    menu-spec 0.8 patch

* Thu Feb 19 2004 Mark McLoughlin <markmc@redhat.com> 0.4-1
- Update to 0.4

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Sep  3 2003 Havoc Pennington <hp@redhat.com> 0.3-10
- fix for #103276 (int/size_t issue) from twoerner

* Mon Jul  7 2003 Alexander Larsson <alexl@redhat.com> 0.3-9
- Rebuild

* Mon Jun 23 2003 Havoc Pennington <hp@redhat.com> 0.3-8
- rebuild

* Thu Jun  5 2003 Jonathan Blandford <jrb@redhat.com> 0.3-6
- Backport patch to allow @MODIFIER in locale keys

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Dec  6 2002 Havoc Pennington <hp@redhat.com>
- rebuild

* Tue Aug  6 2002 Havoc Pennington <hp@redhat.com>
- fix more error messages

* Tue Aug  6 2002 Havoc Pennington <hp@redhat.com>
- remove old symlinks before creating new ones, chills out 
  a lot of error messages

* Tue Aug  6 2002 Havoc Pennington <hp@redhat.com>
- version 0.3

* Wed Jul 24 2002 Havoc Pennington <hp@redhat.com>
- 0.2.95 cvs snap, should fix OnlyShowIn

* Mon Jul 22 2002 Havoc Pennington <hp@redhat.com>
- 0.2.94 cvs snap, adds --print-available

* Tue Jul  9 2002 Havoc Pennington <hp@redhat.com>
- 0.2.93 cvs snap with a crash fixed, and corrects [KDE Desktop Entry]

* Fri Jun 21 2002 Havoc Pennington <hp@redhat.com>
- 0.2.92 cvs snap with --remove-key and checking for OnlyShowIn
  and missing trailing semicolons on string lists

* Fri Jun 21 2002 Havoc Pennington <hp@redhat.com>
- 0.2.91 cvs snap with --copy-name-to-generic-name and
  --copy-generic-name-to-name

* Sun Jun 16 2002 Havoc Pennington <hp@redhat.com>
- 0.2.90 cvs snap with --delete-original fixed

* Fri Jun 07 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Wed Jun  5 2002 Havoc Pennington <hp@redhat.com>
- 0.2

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 09 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Thu May  9 2002 Havoc Pennington <hp@redhat.com>
- initial build
