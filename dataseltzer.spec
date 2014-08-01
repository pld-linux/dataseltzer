Summary:	CGI component supporting dynamic Web publishing of data from SQLite/SpatiaLite DB file
Summary(pl.UTF-8):	Komponent CGI do dynamicznej publikacji na WWW danych z baz SQLite/SpatiaLite
Name:		dataseltzer
Version:	1.0.0
Release:	1
License:	AGPL v3+
Group:		Applications/WWW
Source0:	http://www.gaia-gis.it/gaia-sins/dataseltzer-sources/%{name}-%{version}.tar.gz
# Source0-md5:	5ffb0142d97f8a45875128f75ea4e40e
URL:		https://www.gaia-gis.it/fossil/dataseltzer
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	expat-devel
BuildRequires:	libcgi-devel
BuildRequires:	libspatialite-devel
BuildRequires:	libtool
BuildRequires:	minizip-devel
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dataSeltzer is a simple CGI component supporting dynamic Web
publishing of Data from a SQLite/SpatiaLite DB-file.

%description -l pl.UTF-8
dataSeltzer to prosty komponent CGI obsługujący dynamiczne
publikowanie na WWW danych z plików baz danych SQLite/SpatiaLite.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
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
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/dataSeltzer
