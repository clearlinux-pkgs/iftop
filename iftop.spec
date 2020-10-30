#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : iftop
Version  : 1.0pre4
Release  : 4
URL      : http://www.ex-parrot.com/pdw/iftop/download/iftop-1.0pre4.tar.gz
Source0  : http://www.ex-parrot.com/pdw/iftop/download/iftop-1.0pre4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: iftop-bin = %{version}-%{release}
Requires: iftop-license = %{version}-%{release}
Requires: iftop-man = %{version}-%{release}
BuildRequires : libpcap-dev
BuildRequires : ncurses-dev
Patch1: 0001-Fix-build-with-GCC-10.patch

%description
iftop listens to network traffic on a named interface,  or
on  the  first  interface  it can find which looks like an
external interface if none is specified,  and  displays  a
table of current bandwidth usage by pairs of hosts.  iftop
must be run with sufficient  permissions  to  monitor  all
network  traffic  on  the  interface; see pcap(3) for more
information, but on most systems this means that  it  must
be run as root.

%package bin
Summary: bin components for the iftop package.
Group: Binaries
Requires: iftop-license = %{version}-%{release}

%description bin
bin components for the iftop package.


%package license
Summary: license components for the iftop package.
Group: Default

%description license
license components for the iftop package.


%package man
Summary: man components for the iftop package.
Group: Default

%description man
man components for the iftop package.


%prep
%setup -q -n iftop-1.0pre4
cd %{_builddir}/iftop-1.0pre4
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604097427
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1604097427
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/iftop
cp %{_builddir}/iftop-1.0pre4/COPYING %{buildroot}/usr/share/package-licenses/iftop/36e5838bb6423ae30077fba9556e883c6a534b1d
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/iftop

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/iftop/36e5838bb6423ae30077fba9556e883c6a534b1d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/iftop.8
