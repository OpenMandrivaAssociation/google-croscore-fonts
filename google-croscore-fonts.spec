%global fontname google-croscore
%global fontconf62 62-%{fontname}
%global fontconf30 30-0-%{fontname}

%global common_desc \
This package contains a collections of fonts that offers improved on-screen \
readability characteristics and the pan-European WGL character set and solves \
the needs of developers looking for width-compatible fonts to address document \
portability across platforms.


Name:           %{fontname}-fonts
Version:        1.23.0
Release:        1
Summary:        The width-compatible fonts for improved on-screen readability

Group:          System/Fonts/True type
License:        ASL 2.0
#URL:            
Source0:        http://gsdview.appspot.com/chromeos-localmirror/distfiles/croscorefonts-%{version}.tar.gz
Source1:        62-%{fontname}-arimo-fontconfig.conf
Source2:        62-%{fontname}-cousine-fontconfig.conf
Source3:        62-%{fontname}-tinos-fontconfig.conf
Source4:        30-0-%{fontname}-arimo-fontconfig.conf
Source5:        30-0-%{fontname}-cousine-fontconfig.conf
Source6:        30-0-%{fontname}-tinos-fontconfig.conf
Source7:        62-%{fontname}-symbolneu-fontconfig.conf

# Upstream has not provided license text in this 1.23.0 release
# Add ASL2.0 license text in LICENSE-2.0.txt file
Source8:        LICENSE-2.0.txt

BuildArch:      noarch
BuildRequires:  fontpackages-devel

%description
%common_desc


%package common
Summary:        Common files of %{name}
Requires:       fontpackages-filesystem

%description common
This package consists of files used by other %{name} packages.

# Repeat for every font family
%package -n %{fontname}-arimo-fonts
Summary:       The croscore Arimo family fonts 
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-arimo-fonts
%common_desc
Arimo was designed by Steve Matteson as an innovative, refreshing sans serif
design that is metrically compatible with Arial. Arimo offers improved 
on-screen readability characteristics and the pan-European WGL character set 
and solves the needs of developers looking for width-compatible fonts to 
address document portability across platforms.

%_font_pkg -n arimo -f *-%{fontname}-arimo.conf Arimo*.ttf

%package -n %{fontname}-cousine-fonts
Summary:       The croscore Cousine family fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-cousine-fonts
%common_desc
Cousine was designed by Steve Matteson as an innovative, refreshing sans serif
design that is metrically compatible with Courier New. Cousine offers improved
on-screen readability characteristics and the pan-European WGL character set
and solves the needs of developers looking for width-compatible fonts to 
address document portability across platforms.

%_font_pkg -n cousine -f *-%{fontname}-cousine.conf  Cousine*.ttf

%package -n %{fontname}-tinos-fonts
Summary:       The croscore Tinos family fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-tinos-fonts
%common_desc
Tinos was designed by Steve Matteson as an innovative, refreshing serif design
that is metrically compatible with Times New Roman. Tinos offers improved
on-screen readability characteristics and the pan-European WGL character set
and solves the needs of developers looking for width-compatible fonts to
address document portability across platforms.

%_font_pkg -n tinos -f *-%{fontname}-tinos.conf Tinos*.ttf

%package -n %{fontname}-symbolneu-fonts
Summary:       The croscore Symbol Neu family fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-symbolneu-fonts
%common_desc
Symbol Neu is a metrically compatible font to Symbol.

%_font_pkg -n symbolneu -f *-%{fontname}-symbolneu.conf SymbolNeu.ttf

%prep
%setup -q -n croscorefonts-%{version}
cp -p %{SOURCE8} .

%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

# Repeat for every font family
install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf62}-arimo.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf62}-cousine.conf
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf62}-tinos.conf
install -m 0644 -p %{SOURCE4} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf30}-arimo.conf
install -m 0644 -p %{SOURCE5} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf30}-cousine.conf
install -m 0644 -p %{SOURCE6} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf30}-tinos.conf
install -m 0644 -p %{SOURCE7} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf62}-symbolneu.conf

for fconf in %{fontconf62}-arimo.conf %{fontconf30}-arimo.conf \
             %{fontconf62}-cousine.conf %{fontconf30}-cousine.conf \
             %{fontconf62}-tinos.conf %{fontconf30}-tinos.conf \
       %{fontconf62}-symbolneu.conf; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done


%files common
%doc LICENSE-2.0.txt

