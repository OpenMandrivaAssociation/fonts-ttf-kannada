Summary:	Kannada TTF fonts (Unicode encoded)
Name:		fonts-ttf-kannada
Version:	1.0
Release:	%mkrel 3

Url:		http://kannada.sourceforge.net/
# dated 2002-10-27
Source0:	http://brahmi.sourceforge.net/dl/Sampige.ttf.bz2
License:	GPL
Group:		System/Fonts/True type
BuildArch:	noarch
BuildRequires:	freetype-tools
Requires(post): fontconfig
Requires(postun): fontconfig

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

%post
touch %{_datadir}/fonts/TTF
[ -x %_bindir/fc-cache ] && %{_bindir}/fc-cache 

%postun
# 0 means a real uninstall
if [ "$1" = "0" ]; then
   [ -x %_bindir/fc-cache ] && %{_bindir}/fc-cache 
fi

%clean
rm -fr %buildroot

%files
%defattr(0644,root,root,0755)
#%doc README
%dir %_datadir/fonts/TTF/
%dir %_datadir/fonts/TTF/kannada/
%_datadir/fonts/TTF/kannada/*.ttf



