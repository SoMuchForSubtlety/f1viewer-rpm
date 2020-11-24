# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/SoMuchForSubtlety/golark
%global goipath         github.com/SoMuchForSubtlety/golark
Version:                1.1.1

%gometa

%global common_description %{expand:
A Skylark API client for go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        A Skylark API client for go

License:        GPLv3
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%endif

%gopkgfiles

%changelog
* Tue Nov 24 21:43:12 CET 2020 SoMuchForSubtlety <jakob@ahrer.dev> - 1.1.1-2
- Disable tests
* Tue Nov 24 20:59:34 CET 2020 SoMuchForSubtlety <jakob@ahrer.dev> - 1.1.1-1
- Fix test
* Tue Nov 24 20:34:26 CET 2020 SoMuchForSubtlety <jakob@ahrer.dev> - 1.1.0-1
- Initial package

