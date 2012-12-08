Summary:	Kannada TTF fonts (Unicode encoded)
Name:		fonts-ttf-kannada
Version:	1.0
Release:	%mkrel 11

Url:		http://kannada.sourceforge.net/
# dated 2002-10-27
Source0:	http://brahmi.sourceforge.net/dl/Sampige.ttf.bz2
License:	GPL
Group:		System/Fonts/True type
BuildArch:	noarch
BuildRequires: fontconfig
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildRequires:	freetype-tools

%description
Kannada TTF fonts usable to display Unicode encoded text; through text
engines like pango etc.


%prep

#%setup
 
%build

%install
rm -fr %buildroot

install -d %buildroot/%_datadir/fonts/TTF/kannada/
bzcat %{SOURCE0} > %buildroot/%_datadir/fonts/TTF/kannada/Sampige.ttf

%clean
rm -fr %buildroot

%files
%defattr(0644,root,root,0755)
#%doc README
%dir %_datadir/fonts/TTF/
%dir %_datadir/fonts/TTF/kannada/
%_datadir/fonts/TTF/kannada/*.ttf





%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.0-10mdv2011.0
+ Revision: 675418
- br fontconfig for fc-query used in new rpm-setup-build

* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.0-9
+ Revision: 675182
- rebuild for new rpm-setup

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0-8
+ Revision: 664331
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-7mdv2011.0
+ Revision: 605197
- rebuild

* Wed Jan 20 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0-6mdv2010.1
+ Revision: 494148
- fc-cache is now called by an rpm filetrigger

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0-5mdv2009.1
+ Revision: 351077
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0-4mdv2009.0
+ Revision: 220890
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.0-3mdv2008.1
+ Revision: 125140
- kill re-definition of %%buildroot on Pixel's request


* Fri Aug 04 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-04 23:11:41 (52891)
- Normalize fonts with new paths

* Fri Aug 04 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-04 21:03:55 (52805)
- import fonts-ttf-kannada-1.0-2mdk

* Wed Feb 08 2006 Frederic Crozat <fcrozat@mandriva.com> 1.0-2mdk
- Don't package fontconfig cache file
- Fix prereq
- touch parent directory to workaround rpm changing directory last modification
  time (breaking fontconfig cache consistency detection)

