Summary:	xwud application - dump image displayer for X
Summary(pl.UTF-8):	Aplikacja xwud do wyświetlania obrazów zrzutów pod X
Name:		xorg-app-xwud
Version:	1.0.6
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/xwud-%{version}.tar.xz
# Source0-md5:	5ff5dc120e8e927dc3c331c7fee33fc3
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.25
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xwud application allows X users to display in a window an image saved
in a specially formatted dump file, such as produced by xwd.

%description -l pl.UTF-8
Aplikacja xwud pozwala użytkownikom X wyświetlać w okienku obraz
zapisany w specjalnie sformatowanym pliku zrzutu, takim jak tworzony
przez xwd.

%prep
%setup -q -n xwud-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/xwud
%{_mandir}/man1/xwud.1*
