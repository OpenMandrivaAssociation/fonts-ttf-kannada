Summary:	Kannada TTF fonts (Unicode encoded)
Name:		fonts-ttf-kannada
Version:	1.0
Release:	22
License:	GPLv2
Group:		System/Fonts/True type
Url:		http://kannada.sourceforge.net/
# dated 2002-10-27
Source0:	http://brahmi.sourceforge.net/dl/Sampige.ttf.bz2
BuildArch:	noarch
BuildRequires:	fontconfig
BuildRequires:	freetype-tools

%description
Kannada TTF fonts usable to display Unicode encoded text; through text
engines like pango etc.


%prep
#%setup
 
%build

%install
install -d %{buildroot}/%{_datadir}/fonts/TTF/kannada/
bzcat %{SOURCE0} > %{buildroot}/%{_datadir}/fonts/TTF/kannada/Sampige.ttf

%files
#%doc README
%dir %{_datadir}/fonts/TTF/
%dir %{_datadir}/fonts/TTF/kannada/
%{_datadir}/fonts/TTF/kannada/*.ttf

