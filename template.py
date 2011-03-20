placeholder_dict={"summary","name","version","release","license","group","description","prep", \
"build","configure","install","check","files","_bindir","_infodir","_mandir","post","prerun","clean"}
spec_template=
"""
Summary: $summary
Name: $name
Version: $version
Release: $release%{?dist}
License: $license
Group: $group
#Source0: http://ftp.gnu.org/gnu/m4/m4-%{version}.tar.xz
#Source1: http://ftp.gnu.org/gnu/m4/m4-%{version}.tar.xz.sig
#URL: http://www.gnu.org/software/m4/
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}
#old Buildroot %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
#Requires(post): /sbin/install-info
#Requires(preun): /sbin/install-info

%define debug_package %{nil}
#to clean up the tree nicely
%description
$description

%prep
#%setup -q
#chmod 644 COPYING
$prep

%build
$build

%configure
#make %{?_smp_mflags}
$configure

%install
rm -rf $RPM_BUILD_ROOT
#make install INSTALL="%{__install} -p" DESTDIR=$RPM_BUILD_ROOT
#make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
$install

%check
#make %{?_smp_mflags} check
$check

%files
#%defattr(-,root,root,-)
$default_attr
$files
%doc AUTHORS COPYING ChangeLog NEWS README THANKS TODO
#%{_bindir}/m4
%{_bindir}/$_bindir
#%{_infodir}/*
%{_infodir}/$_infodir
#%{_mandir}/man1/m4.1*
%{_mandir}/$_mandir

%post
#if [ -f %{_infodir}/m4.info ]; then # --excludedocs?
#    /sbin/install-info %{_infodir}/m4.info %{_infodir}/dir || :
#fi
$post

%preun
#if [ "$1" = 0 ]; then
#    if [ -f %{_infodir}/m4.info ]; then # --excludedocs?
#        /sbin/install-info --delete %{_infodir}/m4.info %{_infodir}/dir || :
#    fi
#fi
$prerun

%clean
rm -rf $RPM_BUILD_ROOT
$clean
"""
