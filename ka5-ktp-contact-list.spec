%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		ktp-contact-list
Summary:	ktp-contact-list
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	64f0e18938403d967caca7e62a6553d3
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-ktp-common-internals-devel
BuildRequires:	kf5-extra-cmake-modules >= 1.7.0
BuildRequires:	kf5-kcmutils-devel >= 5.11
BuildRequires:	kf5-kdbusaddons-devel >= 5.11
BuildRequires:	kf5-ki18n-devel >= 5.11
BuildRequires:	kf5-kiconthemes-devel >= 5.11
BuildRequires:	kf5-kio-devel >= 5.11
BuildRequires:	kf5-knotifications-devel >= 5.11
BuildRequires:	kf5-knotifyconfig-devel >= 5.11
BuildRequires:	kf5-kpeople-devel >= 5.11
BuildRequires:	kf5-kwindowsystem-devel >= 5.11
BuildRequires:	kf5-kxmlgui-devel >= 5.11
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	telepathy-qt5-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE Telepathy contact list.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktp-contactlist
%{_desktopdir}/org.kde.ktpcontactlist.desktop
%{_datadir}/dbus-1/services/org.kde.ktpcontactlist.service
