#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : iftop
Version  : 1.0pre4
Release  : 2
URL      : http://www.ex-parrot.com/pdw/iftop/download/iftop-1.0pre4.tar.gz
Source0  : http://www.ex-parrot.com/pdw/iftop/download/iftop-1.0pre4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: iftop-bin
Requires: iftop-license
Requires: iftop-man
BuildRequires : libpcap-dev
BuildRequires : ncurses-dev

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
Requires: iftop-license
Requires: iftop-man

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

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536629932
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1536629932
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/iftop
cp COPYING %{buildroot}/usr/share/doc/iftop/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/iftop

%files license
%defattr(-,root,root,-)
/usr/share/doc/iftop/COPYING

%files man
%defattr(-,root,root,-)
/usr/share/man/man8/iftop.8
