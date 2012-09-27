%define		pkg	socket.io-client
Summary:	Socket.IO client for node.js
Name:		nodejs-%{pkg}
Version:	0.9.10
Release:	0.4
License:	MIT
Group:		Development/Libraries
URL:		http://socket.io/
Source0:	http://registry.npmjs.org/socket.io-client/-/%{pkg}-%{version}.tgz
# Source0-md5:	bb8dd0fce274d04f7c38351986cb9747
BuildRequires:	rpmbuild(macros) >= 1.634
BuildRequires:	sed >= 4.0
Requires:	nodejs
Requires:	nodejs-uglify-js >= 1.2.5
#    "ws": "0.4.x",
#    "xmlhttprequest": "1.4.2",
#    "active-x-obfuscator": "0.0.1"
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Socket.IO client for node.js.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -a package.json lib $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

cp -a bin $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md History.md
%dir %{nodejs_libdir}/%{pkg}
%{nodejs_libdir}/%{pkg}/package.json
%{nodejs_libdir}/%{pkg}/lib
%dir %{nodejs_libdir}/%{pkg}/bin
%attr(755,root,root) %{nodejs_libdir}/%{pkg}/bin/*
