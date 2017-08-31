Name:           fdkaac
Version:        0.6.3
Release:        5%{?dist}
Summary:        Command line frontend for libfdk-aac encoder

License:        zlib
URL:            https://github.com/nu774/%{name}
Source:         https://github.com/nu774/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  autoconf automake
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
