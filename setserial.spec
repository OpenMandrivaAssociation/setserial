Summary:	A utility for configuring serial ports
Name:		setserial
Version:	2.17
Release:	%mkrel 14
License:	GPL
Group:		System/Configuration/Hardware
URL:		http://setserial.sourceforge.net/
Source0: 	ftp://tsx-11.mit.edu/pub/linux/sources/sbin/%{name}-%{version}.tar.bz2
Patch0:		setserial-2.17-LDFLAGS.diff
BuildRequires:  groff-for-man
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Setserial is a basic system utility for displaying or setting serial port
information. Setserial can reveal and allow you to alter the I/O port and IRQ
that a particular serial device is using, and more.

You should install setserial because you may find it useful for detecting
and/or altering device information.

%prep
%setup -q
%patch0 -p0

%build
rm -f config.cache

%configure

%ifarch %{ix86}
%make
%else
%make DEFS="-DHAVE_ASM_IOCTLS_H=1 -DHAVE_LINUX_HAYESESP_H=1"
%endif

%install
rm -rf %{buildroot}

install -m755 %{name} -D %{buildroot}/bin/%{name}
install -m644 %{name}.8 -D %{buildroot}%{_mandir}/man8/%{name}.8

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc README rc.serial *.lsm *.conf Documentation
%{_mandir}/man8/%{name}.8*
%defattr(755,root,root,755)
/bin/%{name}


