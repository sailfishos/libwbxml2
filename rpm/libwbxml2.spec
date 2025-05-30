%undefine __cmake_in_source_build

Name:    libwbxml2
Version: 0.11.10
Release: 1
Summary: Library to parse, encode and handle WBXML documents
License: LGPLv2+
URL:     https://github.com/sailfishos/libwbxml2
Source0: %{name}-%{version}.tar.gz
Patch0:  0001-Use-GNUInstallDirs.patch
BuildRequires: expat-devel
BuildRequires: cmake

%description
The WBXML Library (aka libwbxml) contains a library to Parse, Encode
and Handle WBXML documents. The WBXML format is a binary
representation of XML, defined by the Wap Forum, and used to reduce
bandwidth in mobile communications.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
%{summary}.

%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}

%description doc
%{summary}.

%package tools
Summary:   Tools for %{name}
Requires:  %{name} = %{version}-%{release}

%description tools
%{summary}. Provides tools to Parse and Encode WBXML documents.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%cmake -DWBXML_INSTALL_FULL_HEADERS=ON
%cmake_build

%install
%cmake_install

mv %{buildroot}%{_docdir}/* %{buildroot}%{_docdir}/%{name}-%{version}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING GNU-LGPL
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/*

%files doc
%{_docdir}/%{name}-%{version}

%files tools
%{_bindir}/*
