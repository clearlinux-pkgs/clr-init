#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clr-init
Version  : 1.0.2
Release  : 18
URL      : https://github.com/clearlinux/clr-init/archive/V1.0.2.tar.gz
Source0  : https://github.com/clearlinux/clr-init/archive/V1.0.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: clr-init-license = %{version}-%{release}
BuildRequires : LVM2
BuildRequires : bluez
BuildRequires : btrfs-progs
BuildRequires : dosfstools
BuildRequires : e2fsprogs
BuildRequires : glibc-bin
BuildRequires : glibc-lib-avx2
BuildRequires : kbd
BuildRequires : keyutils
BuildRequires : kmod
BuildRequires : less
BuildRequires : libgfortran-avx
BuildRequires : libinput
BuildRequires : libmtp
BuildRequires : mdadm
BuildRequires : multipath-tools
BuildRequires : systemd
BuildRequires : systemd-extras
BuildRequires : thin-provisioning-tools
BuildRequires : thunderbolt-software-user-space
BuildRequires : util-linux-bin
BuildRequires : xfsprogs

%description
## clr-init
Initrd created using systemd as init program
## Luks Encryption support

%package license
Summary: license components for the clr-init package.
Group: Default

%description license
license components for the clr-init package.


%prep
%setup -q -n clr-init-1.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1543888856
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1543888856
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/clr-init
cp COPYING %{buildroot}/usr/share/package-licenses/clr-init/COPYING
%make_install

%files
%defattr(-,root,root,-)
/usr/lib/initrd.d/clr-init.cpio.gz

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/clr-init/COPYING
