# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/gsterjov/go-libsecret
%global goipath         github.com/gsterjov/go-libsecret
%global commit          a6f4afe4910cad8688db3e0e9b9ac92ad22d54e1

%gometa

%global common_description %{expand:
A native go library that manages secrets via the freedesktop.org Secret Service
DBus API.}

%global golicenses      LICENSE
Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        A native go library that manages secrets via the freedesktop.org Secret Service DBus API

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/godbus/dbus)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Nov 24 21:09:48 CET 2020 SoMuchForSubtlety <jakob@ahrer.dev> - 0-0.1.20201124gita6f4afe
- Initial package

