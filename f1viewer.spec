Version:        2.3.0
Name:           f1viewer
Release:        4%{?dist}
Summary:        🏎️ TUI for F1TV

License:        GPLv3
URL:            https://github.com/SoMuchForSubtlety/%{name}
Source0:        https://github.com/SoMuchForSubtlety/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  golang
BuildRequires:  git
Requires:       xclip

# stop rpmbuild from trying to extract debug info
%define debug_package %{nil}

%description
extensible TUI application to access F1TV

%prep
%setup -q

%build
go env -w GO111MODULE="on"
go env -w GOPROXY="https://proxy.golang.org,direct"
go env -w GOSUMDB="sum.golang.org"
go env
go build \
    -trimpath \
    -ldflags="-s -w -X main.version=${pkgver}" \
    -o %{name} main.go

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md

%changelog
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

