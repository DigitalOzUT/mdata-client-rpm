%define name mdata-client
%define version 0.0.1 
%define release 1
%define dist .el6

Name: mdata-client
Version: 0.0.1
Release: 1%{?dist}
Summary: Metadata retrieval and manipulation tools for use within guests of the SmartOS hypervisor. 

Group:Administration
License: MIT
URL: https://github.com/joyent/mdata-client
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Source: %{name}-%{version}.tar.gz 

%description
Metadata retrieval and manipulation tools for use within guests of the SmartOS hypervisor.

%prep
%setup -q -n %{name}

%build
make

%install
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}/lib

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/sbin/mdata-get
/usr/sbin/mdata-list
/usr/sbin/mdata-put
/usr/sbin/mdata-delete
/usr/share/man/man1/mdata-get.1.gz
/usr/share/man/man1/mdata-list.1.gz
/usr/share/man/man1/mdata-put.1.gz
/usr/share/man/man1/mdata-delete.1.gz

%changelog
* Wed Oct 12 2016 Miroslav Bagljas <miroslav.bagljas@erigones.com>
- Initial package 
