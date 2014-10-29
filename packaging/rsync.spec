Name:           rsync
Version:        3.1.1
Release:        0
License:        GPL-3.0+
Summary:        A program for synchronizing files over a network
Url:            http://rsync.samba.org/
#X-Vcs-Url:     git://git.samba.org/rsync
Group:          Applications/Internet
Source0:        http://rsync.samba.org/ftp/rsync/src/rsync-%{version}.tar.gz
Source1001:     rsync.manifest
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
Requires:       %{name} = %{version}-%{release}

%description support
Support filrs for rsync

%prep
%setup -q
cp %{SOURCE1001} .

%build

%configure --disable-static
%__make %{?_smp_mflags}

%install
%make_install


%docs_package

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%license COPYING
%{_bindir}/rsync

