%define major 5
%define libname %mklibname KF5Bookmarks %{major}
%define devname %mklibname KF5Bookmarks -d
%define debug_package %{nil}

Name: kbookmarks
Version: 4.99.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/unstable/frameworks/%{version}/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 bookmark handling library
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
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

%prep
%setup -q
%cmake

%build
%make -C build

%install
%makeinstall_std -C build
mkdir -p %{buildroot}%{_libdir}/qt5
mv %{buildroot}%{_prefix}/mkspecs %{buildroot}%{_libdir}/qt5

L="`pwd`/%{name}.lang"
cd %{buildroot}
for i in .%{_datadir}/locale/*/LC_MESSAGES/*.qm; do
	LNG=`echo $i |cut -d/ -f5`
	echo -n "%lang($LNG) " >>$L
	echo $i |cut -b2- >>$L
done

%files -f %{name}.lang

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5Bookmarks
%{_libdir}/qt5/mkspecs/modules/*
