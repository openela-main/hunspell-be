Name: hunspell-be
Summary: Belarusian hunspell dictionaries
Version: 1.1
Release: 15%{?dist}
Source: https://downloads.sourceforge.net/project/aoo-extensions/2412/1/dict-be-official.oxt
URL: http://extensions.services.openoffice.org/project/dict-be-official
License: GPL+ and LGPLv2+
BuildArch: noarch

Requires: hunspell
Supplements: (hunspell and langpacks-be)

%description
Belarusian hunspell dictionaries.

%package -n hyphen-be
Requires: hyphen
Summary: Belarusian hyphenation rules
Supplements: (hyphen and langpacks-be)

%description -n hyphen-be
Belarusian hyphenation rules.

%prep
%autosetup -c -n hunspell-be

%build
sed -i -e "s/microsoft-cp1251/CP1251/g" be-official.aff hyph_be_BY.dic
tail -n +3 hyph_be_BY.dic| head -n 3 > README_hyph_be_BY

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p be-official.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/be_BY.aff
cp -p be-official.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/be_BY.dic
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_be_BY.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_be_BY.dic


%files
%{_datadir}/myspell/*

%files -n hyphen-be
%doc README_hyph_be_BY
%{_datadir}/hyphen/*

%changelog
* Sat Jul 07 2018 Parag Nemade <pnemade AT fedoraproject DOT org> - 1.1-15
- Update Source tag

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 19 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.1-11
- Add Supplements: tag for langpacks naming guidelines
- Clean the specfile to follow current packaging guidelines

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 23 2010 Caolán McNamara <caolanm@redhat.com> - 1.1-2
- add README_hyph_be_BY to subpackage

* Wed Sep 23 2009 Caolán McNamara <caolanm@redhat.com> - 1.1-1
- latest version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 01 2009 Caolán McNamara <caolanm@redhat.com> - 1.0.0-1
- latest version

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Sep 28 2008 Caolán McNamara <caolanm@redhat.com> - 0.1-1
- initial version
