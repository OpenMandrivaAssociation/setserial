Summary:	A utility for configuring serial ports
Name:		setserial
Version:	2.17
Release:	25
License:	GPL
Group:		System/Configuration/Hardware
URL:		http://setserial.sourceforge.net/
Source0: 	ftp://tsx-11.mit.edu/pub/linux/sources/sbin/%{name}-%{version}.tar.bz2
Patch0:		setserial-2.17-LDFLAGS.diff
Patch1:		setserial-hayesesp.patch
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
%patch1 -p1 -b .hayesesp

%build
rm -f config.cache

%configure

%ifarch %{ix86}
%make
%else
%make DEFS="-DHAVE_ASM_IOCTLS_H=1"
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


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 2.17-18mdv2011.0
+ Revision: 669969
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2.17-17mdv2011.0
+ Revision: 607532
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.17-16mdv2010.1
+ Revision: 521016
- P1: fix build (fedora)
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.17-15mdv2010.0
+ Revision: 427068
- rebuild

* Mon Dec 22 2008 Oden Eriksson <oeriksson@mandriva.com> 2.17-14mdv2009.1
+ Revision: 317229
- use %%ldflags (P0)

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2.17-13mdv2009.0
+ Revision: 225434
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 2.17-12mdv2008.1
+ Revision: 179501
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu May 17 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 2.17-11mdv2008.0
+ Revision: 27687
- Added URL tag.


* Sat Mar 17 2007 Oden Eriksson <oeriksson@mandriva.com> 2.17-10mdv2007.1
+ Revision: 145455
- Import setserial

* Sat Mar 17 2007 Oden Eriksson <oeriksson@mandriva.com> 2.17-10mdv2007.1
- use the %%mrel macro
- bunzip patches

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 2.17-9mdk
- Rebuild

* Tue Jan 25 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.17-8mdk
- rebuild

