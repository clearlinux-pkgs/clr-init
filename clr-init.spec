#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clr-init
Version  : 1.0.19
Release  : 37
URL      : https://github.com/clearlinux/clr-init/archive/V1.0.19.tar.gz
Source0  : https://github.com/clearlinux/clr-init/archive/V1.0.19.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: clr-init-license = %{version}-%{release}
BuildRequires : LVM2
BuildRequires : LVM2-extras
BuildRequires : ModemManager
BuildRequires : NetworkManager
BuildRequires : alsa-utils
BuildRequires : bluez
BuildRequires : btrfs-progs
BuildRequires : clr-systemd-config
BuildRequires : colord
BuildRequires : dosfstools
BuildRequires : e2fsprogs
BuildRequires : fuse
BuildRequires : fwupd
BuildRequires : glibc-bin
BuildRequires : glibc-lib-avx2
BuildRequires : gnome-settings-daemon
BuildRequires : kbd
BuildRequires : keyutils
BuildRequires : kmod
BuildRequires : less
BuildRequires : libinput
BuildRequires : libmtp
BuildRequires : mdadm
BuildRequires : multipath-tools
BuildRequires : pulseaudio
BuildRequires : rdma-core
BuildRequires : systemd
BuildRequires : systemd-extras
BuildRequires : thin-provisioning-tools
BuildRequires : thunderbolt-software-user-space
BuildRequires : udisks2
BuildRequires : upower
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
%setup -q -n clr-init-1.0.19
cd %{_builddir}/clr-init-1.0.19

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639161536
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1639161536
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/clr-init
cp %{_builddir}/clr-init-1.0.19/COPYING %{buildroot}/usr/share/package-licenses/clr-init/8624bcdae55baeef00cd11d5dfcfa60f68710a02
%make_install

%files
%defattr(-,root,root,-)
/usr/lib/initrd.d/clr-init.cpio.gz

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/clr-init/8624bcdae55baeef00cd11d5dfcfa60f68710a02
