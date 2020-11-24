# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/SoMuchForSubtlety/f1viewer
%global goipath         github.com/SoMuchForSubtlety/f1viewer
Version:                1.4.0

%gometa

%global common_description %{expand:
🏎️ TUI for F1TV.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           f1viewer
Release:        3%{?dist}
Summary:        🏎️ TUI for F1TV

License:        GPLv3
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/atotto/clipboard)
BuildRequires:  golang(github.com/gdamore/tcell)
BuildRequires:  golang(github.com/rivo/tview)
BuildRequires:  golang(github.com/SoMuchForSubtlety/golark)
BuildRequires:  golang(github.com/SoMuchForSubtlety/keyring)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/f1viewer %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Nov 24 22:30:28 CET 2020 SoMuchForSubtlety <jakob@ahrer.dev> - 1.4.0-3
- Fix name
* Tue Nov 24 22:12:40 CET 2020 SoMuchForSubtlety <jakob@ahrer.dev> - 1.4.0-2
- Fix tcell dependency
* Tue Nov 24 18:57:14 CET 2020 SoMuchForSubtlety <jakob@ahrer.dev> - 1.4.0-1
- Initial package

