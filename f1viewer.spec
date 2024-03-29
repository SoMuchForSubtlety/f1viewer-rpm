Version:        2.7.0
Name:           f1viewer
Release:        1%{?dist}
Summary:        🏎️ TUI for F1TV

License:        GPLv3
URL:            https://github.com/SoMuchForSubtlety/%{name}
Source0:        https://github.com/SoMuchForSubtlety/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  git
BuildRequires:  wget
Suggests:       xclip

# stop rpmbuild from trying to extract debug info
%define debug_package %{nil}

%description
extensible TUI application to access F1TV

%prep
%setup -q
wget -q -O - https://raw.githubusercontent.com/canha/golang-tools-install-script/master/goinstall.sh | bash

%build
source /builddir/.bashrc
CGO_ENABLED=0 go build \
    -trimpath \
    -ldflags="-s -w -X main.version=%{version}" \
    -o %{name} main.go

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md

%changelog
* Thu Apr 07 2022 SoMuchForSubtlety <jakob@ahrer.dev> - 2.7.0-1
- bump release to 2.7.0
* Sun Mar 27 2022 SoMuchForSubtlety <jakob@ahrer.dev> - 2.6.2-1
- bump release to 2.6.2
* Sat Mar 26 22:20:00 CET 2022 SoMuchForSubtlety <jakob@ahrer.dev> - 2.6.1-1
- bump release to 2.6.1
* Wed Dec 1 19:15:00 CET 2021 SoMuchForSubtlety <jakob@ahrer.dev> - 2.6.0-1
- bump release to 2.6.0
* Wed Dec 1 19:15:00 CET 2021 SoMuchForSubtlety <jakob@ahrer.dev> - 2.5.0-2
- use go1.17 for build
* Wed Dec 1 19:02:00 CET 2021 SoMuchForSubtlety <jakob@ahrer.dev> - 2.5.0-1
- bump release to 2.5.0
* Sun Oct 31 15:33:00 CET 2021 SoMuchForSubtlety <jakob@ahrer.dev> - 2.4.0-1
- bump release to 2.4.0
* Tue Sep 7 22:30:00 CET 2021 SoMuchForSubtlety <jakob@ahrer.dev> - 2.3.0-6
- fix ldflags version param
* Tue Sep 7 22:30:00 CET 2021 SoMuchForSubtlety <jakob@ahrer.dev> - 2.3.0-5
- suse compatability
* Tue Sep 7 22:30:00 CET 2021 SoMuchForSubtlety <jakob@ahrer.dev> - 2.3.0-4
- set go proxy and sum db
* Tue Sep 7 22:30:00 CET 2021 SoMuchForSubtlety <jakob@ahrer.dev> - 2.3.0-3
- set go to module mode
* Tue Sep 7 22:30:00 CET 2021 SoMuchForSubtlety <jakob@ahrer.dev> - 2.3.0-2
- add git build dependency
* Tue Sep 7 22:30:00 CET 2021 SoMuchForSubtlety <jakob@ahrer.dev> - 2.3.0-1
- don't use rpm2go
* Wed Mar 24 20:30:16 CET 2021 SoMuchForSubtlety <jakob@ahrer.dev> - 1.5.0-1
- upgrade to 1.5.0
* Tue Nov 24 22:30:28 CET 2020 SoMuchForSubtlety <jakob@ahrer.dev> - 1.4.0-3
- Fix name
* Tue Nov 24 22:12:40 CET 2020 SoMuchForSubtlety <jakob@ahrer.dev> - 1.4.0-2
- Fix tcell dependency
* Tue Nov 24 18:57:14 CET 2020 SoMuchForSubtlety <jakob@ahrer.dev> - 1.4.0-1
- Initial package

