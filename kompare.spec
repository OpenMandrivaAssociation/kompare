%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Summary:	A diff graphic tool for KDE
Name:		kompare
Version:	19.12.2
Release:	2
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Codecs)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5TextEditor)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(LibKompareDiff2)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	cmake(Qt5PrintSupport)

# (crazy) without won't work :)
Requires: diffutils

%description
Kompare is a GUI front-end program that enables differences between source
files to be viewed and merged. It can be used to compare differences on files
or the contents of folders, and it supports a variety of diff formats and
provide many options to customize the information level displayed.

Features:
 - Comparing directories
 - Reading diff files
 - Creating and applying patches

%files -f %{name}.lang
%{_bindir}/kompare
%{_libdir}/qt5/plugins/kf5/parts/komparenavtreepart.so
%{_libdir}/qt5/plugins/kf5/parts/komparepart.so
%{_datadir}/applications/org.kde.kompare.desktop
%{_datadir}/kservices5/komparenavtreepart.desktop
%{_datadir}/kservices5/komparepart.desktop
%{_datadir}/kservices5/ServiceMenus/kompare.desktop
%{_datadir}/kservicetypes5/kompareviewpart.desktop
%{_datadir}/kservicetypes5/komparenavigationpart.desktop
%{_iconsdir}/hicolor/*/apps/kompare.*
%{_datadir}/metainfo/*.appdata.xml

#----------------------------------------------------------------------------

%define komparedialogpages_major 5
%define libkomparedialogpages %mklibname komparedialogpages %{komparedialogpages_major}

%package -n %{libkomparedialogpages}
Summary:	Kompare shared library
Group:		System/Libraries

%description -n %{libkomparedialogpages}
Kompare shared library.

%files -n %{libkomparedialogpages}
%{_libdir}/libkomparedialogpages.so.%{komparedialogpages_major}*

#----------------------------------------------------------------------------

%define kompareinterface_major 5
%define libkompareinterface %mklibname kompareinterface %{kompareinterface_major}

%package -n %{libkompareinterface}
Summary:	Kompare shared library
Group:		System/Libraries

%description -n %{libkompareinterface}
Kompare shared library.

%files -n %{libkompareinterface}
%{_libdir}/libkompareinterface.so.%{kompareinterface_major}*

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for Kompare
Group:		Development/KDE and Qt
Requires:	%{libkomparedialogpages} = %{EVRD}
Requires:	%{libkompareinterface} = %{EVRD}
Conflicts:	kdesdk4-devel < 1:1.4.11.0

%description devel
This package includes the header files you will need to compile applications
based on Kompare libraries.

%files devel
%{_includedir}/kompare
%{_libdir}/libkompareinterface.so

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-html
