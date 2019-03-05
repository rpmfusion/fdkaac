Name:           fdkaac
Version:        1.0.0
Release:        2%{?dist}
Summary:        Command line frontend for libfdk-aac encoder

License:        zlib
URL:            https://github.com/nu774/%{name}
Source:         %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  fdk-aac-devel


%description
fdkaac reads linear PCM audio in either WAV, raw PCM, or CAF format,
and encodes it into either M4A / AAC file.

If the input file is "-", data is read from stdin. Likewise, if the
output file is "-", data is written to stdout if one of streamable AAC
transport formats are selected by -f.

When CAF input and M4A output is used, tags in CAF file are copied into
the resulting M4A.


%prep
%autosetup


%build
autoreconf -fiv
export LDFLAGS="%{?__global_ldflags} -L%{_libdir}/fdk-aac"
%configure
%make_build

%install
%make_install


%files
%license COPYING
%doc README ChangeLog
%{_bindir}/fdkaac
%{_mandir}/man1/*


%changelog
* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 24 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-1
- Update to 1.0.0

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.6.3-8
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 0.6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 25 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 16 2016 Christopher Atherton <the8lack8ox@gmail.com> - 0.6.3-3
- Add BuildRequires autoconf automake

* Fri Sep 16 2016 Christopher Atherton <the8lack8ox@gmail.com> - 0.6.3-2
- Spec file cleanup

* Sun Sep 11 2016 Christopher Atherton <the8lack8ox@gmail.com> - 0.6.3-1
- Update to latest release
- Spec file cleanup

* Wed Jan 13 2016 Christopher Atherton <the8lack8ox@gmail.com> - 0.6.2-2
- Change package name to fdkaac-cli

* Mon Jan 11 2016 Christopher Atherton <the8lack8ox@gmail.com> - 0.6.2-1
- Initial spec
