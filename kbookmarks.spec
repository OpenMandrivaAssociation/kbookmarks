%define major 5
%define libname %mklibname KF5Bookmarks %{major}
%define devname %mklibname KF5Bookmarks -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kbookmarks
Version:	5.74.0
Release:	3
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 bookmark handling library
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: qmake5
BuildRequires: cmake(ECM)
BuildRequires: ninja
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant
Requires: %{libname} = %{EVRD}

%description
KBookmarks is an abstraction to bookmark handling.

%package -n %{libname}
Summary: The KDE Frameworks 5 bookmark handling library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KBookmarks is an abstraction to bookmark handling.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
KBookmarks is an abstraction to bookmark handling.

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

L="`pwd`/%{name}.lang"
cd %{buildroot}
for i in .%{_datadir}/locale/*/LC_MESSAGES/*.qm; do
	LNG=`echo $i |cut -d/ -f5`
	echo -n "%lang($LNG) " >>$L
	echo $i |cut -b2- >>$L
done

%files -f %{name}.lang
%{_datadir}/qlogging-categories5/kbookmarks.*categories

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5Bookmarks
%{_libdir}/qt5/mkspecs/modules/*

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}
