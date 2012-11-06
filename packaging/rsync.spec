#
# Please submit bugfixes or comments via http://bugs.tizen.org/
#

Name:           rsync
Version:        3.0.8
Release:        1
License:        GPL-3.0+
Summary:        A program for synchronizing files over a network
Url:            http://rsync.samba.org/
Group:          Applications/Internet
Source0:        http://rsync.samba.org/ftp/rsync/src/rsync-%{version}.tar.gz
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel
BuildRequires:  pkgconfig(popt)

%description
Rsync uses a reliable algorithm to bring remote and host files into
sync very quickly. Rsync is fast because it just sends the differences
in the files over the network instead of sending the complete
files. Rsync is often used as a very powerful mirroring process or
just as a more capable replacement for the rcp command. A technical
report which describes the rsync algorithm is included in this
package.

%package support
Summary:        Support files for rsync
Group:          Applications/System
Requires:       %{name} = %{version}

%description support
Support filrs for rsync

%prep
%setup -q

%build

%configure --disable-static
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root,-)
%doc COPYING README
%{_bindir}/rsync
%doc %{_mandir}/man1/rsync.1*
%doc %{_mandir}/man5/rsyncd.conf.5*


