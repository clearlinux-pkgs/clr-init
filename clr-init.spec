#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clr-init
Version  : 0.1.2
Release  : 3
URL      : https://github.com/clearlinux/clr-init/archive/V0.1.2.tar.gz
Source0  : https://github.com/clearlinux/clr-init/archive/V0.1.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: clr-init-doc
BuildRequires : meson
BuildRequires : ninja
BuildRequires : pkgconfig(libcryptsetup)
BuildRequires : python3

%description
## clr-init
small init wrote with C programming language that takes information from the cmdline in proc to mount root and execute
/sbin/init from the root partition.

%package doc
Summary: doc components for the clr-init package.
Group: Documentation

%description doc
doc components for the clr-init package.


%prep
%setup -q -n clr-init-0.1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1517418645
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain  builddir
ninja -v -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)
/usr/lib/initrd.d/clr-init.img.gz

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
