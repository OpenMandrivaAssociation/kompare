Summary:	A diff graphic tool for KDE
Name:		kompare
Version:	4.11.0
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	ftp://ftp.kde.org/pub/kde/%{ftpdir}/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel

%description
Kompare is a GUI front-end program that enables differences between source
files to be viewed and merged. It can be used to compare differences on files
or the contents of folders, and it supports a variety of diff formats and
provide many options to customize the information level displayed.

Features:
 - Comparing directories
 - Reading diff files
 - Creating and applying patches

%files
%{_kde_bindir}/kompare
%{_kde_libdir}/kde4/komparenavtreepart.so
%{_kde_libdir}/kde4/komparepart.so
%{_kde_applicationsdir}/kompare.desktop
%{_kde_appsdir}/kompare
%{_kde_iconsdir}/hicolor/128x128/apps/kompare.png
%{_kde_iconsdir}/hicolor/16x16/apps/kompare.png
%{_kde_iconsdir}/hicolor/22x22/apps/kompare.png
%{_kde_iconsdir}/hicolor/32x32/apps/kompare.png
%{_kde_iconsdir}/hicolor/48x48/apps/kompare.png
%{_kde_iconsdir}/hicolor/scalable/apps/kompare.svgz
%{_kde_services}/komparenavtreepart.desktop
%{_kde_services}/komparepart.desktop
%{_kde_servicetypes}/kompareviewpart.desktop
%{_kde_servicetypes}/komparenavigationpart.desktop
%{_kde_docdir}/*/*/kompare

#----------------------------------------------------------------------------

%define komparedialogpages_major 4
%define libkomparedialogpages %mklibname komparedialogpages %{komparedialogpages_major}

%package -n %{libkomparedialogpages}
Summary:	Kompare shared library
Group:		System/Libraries

%description -n %{libkomparedialogpages}
Kompare shared library.

%files -n %{libkomparedialogpages}
%{_kde_libdir}/libkomparedialogpages.so.%{komparedialogpages_major}*

#----------------------------------------------------------------------------

%define komparediff2_major 4
%define libkomparediff2 %mklibname komparediff2_ %{komparediff2_major}

%package -n %{libkomparediff2}
Summary:	Kompare shared library
Group:		System/Libraries

%description -n %{libkomparediff2}
Kompare shared library.

%files -n %{libkomparediff2}
%{_kde_libdir}/libkomparediff2.so.%{komparediff2_major}*

#----------------------------------------------------------------------------

%define kompareinterface_major 4
%define libkompareinterface %mklibname kompareinterface %{kompareinterface_major}

%package -n %{libkompareinterface}
Summary:	Kompare shared library
Group:		System/Libraries

%description -n %{libkompareinterface}
Kompare shared library.

%files -n %{libkompareinterface}
%{_kde_libdir}/libkompareinterface.so.%{kompareinterface_major}*

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for Kompare
Group:		Development/KDE and Qt
Requires:	%{libkomparedialogpages} = %{EVRD}
Requires:	%{libkomparediff2} = %{EVRD}
Requires:	%{libkompareinterface} = %{EVRD}
Conflicts:	kdesdk4-devel < 1:1.4.11.0

%description devel
This package includes the header files you will need to compile applications
based on Kompare libraries.

%files devel
%{_kde_includedir}/kompare
%{_kde_libdir}/libkomparedialogpages.so
%{_kde_libdir}/libkomparediff2.so
%{_kde_libdir}/libkompareinterface.so

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.0-1
- Split from kdesdk4 package as upstream did
- New version 4.11.0
