Name:    libwbxml2
Version: 0.11.6
Release: 1
Summary: Library to parse, encode and handle WBXML documents
Group:   System/Libraries
License: LGPLv2+
URL:     https://git.sailfishos.org/mer-core/libwbxml2
Source0: %{name}-%{version}.tar.gz
BuildRequires: expat-devel zlib-devel popt-devel
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: cmake

%description
The WBXML Library (aka libwbxml) contains a library and its associated
tools to Parse, Encode and Handle WBXML documents.  The WBXML format
is a binary representation of XML, defined by the Wap Forum, and used
to reduce bandwidth in mobile communications.

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
%{summary}.

%package doc
Summary:   Documentation for %{name}
Group:     Documentation
Requires:  %{name} = %{version}-%{release}

%description doc
%{summary}.

%prep
%setup -q -n %{name}-%{version}/upstream

%build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr -DWBXML_INSTALL_FULL_HEADERS=ON ..
make

%install
rm -rf %{buildroot}
make -C build DESTDIR=%{buildroot} install
rm -rf build

mv %{buildroot}%{_docdir}/* %{buildroot}%{_docdir}/%{name}-%{version}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING GNU-LGPL
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/cmake/Modules/FindLibWbxml2.cmake

%files doc
%defattr(-,root,root,-)
%{_docdir}/%{name}-%{version}
