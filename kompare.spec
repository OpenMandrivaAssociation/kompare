%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
#define git 20240524
%define gitbranch kf6
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Summary:	Graphical tool to display file differences
Name:		kompare
Version:	25.12.2
Release:	%{?git:0.%{git}.}1
Group:		Development/Tools
License:	GPLv2 LGPLv2 GFDL
Url:		https://invent.kde.org/sdk/kompare
%if 0%{?git:1}
Source0:	https://invent.kde.org/sdk/kompare/-/archive/%{gitbranch}/kompare-%{gitbranchd}.tar.bz2#/kompare-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kompare-%{version}.tar.xz
%endif
BuildRequires:	pkgconfig(icu-uc)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:	cmake(KF6Bookmarks)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6GuiAddons)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6NotifyConfig)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6Pty)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6GlobalAccel)
BuildRequires:	cmake(KF6TextEditor)
BuildRequires:	cmake(ECM)
BuildRequires:	%mklibname -d KF6IconWidgets
BuildRequires:	%mklibname -d komparediff2-kf6
# Just to make sure we don't pull in the conflicting Plasma5 package
BuildRequires:	plasma6-xdg-desktop-portal-kde
Requires:	diffutils

%rename plasma6-kompare

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

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
%{_libdir}/libkomparedialogpages.so*
%{_libdir}/libkompareinterface.so*
%{_qtdir}/plugins/kf6/parts/komparenavtreepart.so
%{_qtdir}/plugins/kf6/parts/komparepart.so
%{_datadir}/applications/org.kde.kompare.desktop
%{_datadir}/icons/hicolor/*/apps/kompare.*
%{_datadir}/kio/servicemenus/kompare.desktop
%{_datadir}/metainfo/org.kde.kompare.appdata.xml
%{_datadir}/qlogging-categories6/kompare.categories

%install -a
# No need to package -devel, nothing uses internal libraries
rm -rf %{buildroot}%{_includedir}/kompare %{buildroot}%{_libdir}/*.so
