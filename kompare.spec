Summary:	A diff graphic tool for KDE
Name:		kompare
Version:	4.14.3
Release:	2
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
BuildRequires:	libkomparediff2-devel

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
%{_kde_services}/komparenavtreepart.desktop
%{_kde_services}/komparepart.desktop
%{_kde_servicetypes}/kompareviewpart.desktop
%{_kde_servicetypes}/komparenavigationpart.desktop
%{_kde_iconsdir}/hicolor/*/apps/kompare.*
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
Requires:	%{libkompareinterface} = %{EVRD}
Conflicts:	kdesdk4-devel < 1:1.4.11.0

%description devel
This package includes the header files you will need to compile applications
based on Kompare libraries.

%files devel
%{_kde_includedir}/kompare
%{_kde_libdir}/libkomparedialogpages.so
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
* Tue Nov 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.3-1
- New version 4.14.3

* Wed Oct 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.2-1
- New version 4.14.2

* Mon Sep 29 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.1-1
- New version 4.14.1

* Tue Jul 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.3-1
- New version 4.13.3

* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.2-1
- New version 4.13.2

* Wed Apr 02 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.4-1
- New version 4.12.4

* Tue Mar 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.3-1
- New version 4.12.3

* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.1-1
- New version 4.12.1
- libkomparediff2 is moved into own package
- Add libkomparediff2-devel to BuildRequires

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.0-1
- Split from kdesdk4 package as upstream did
- New version 4.11.0
