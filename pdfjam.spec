Name:           pdfjam
Version:        1.21
Release:        %mkrel 1
Summary:        Utilities for join, rotate and align PDFs

Group:          Publishing
# No version specified.
License:        GPL+
URL:            http://www.warwick.ac.uk/go/pdfjam
Source0:        http://www.warwick.ac.uk/go/pdfjam/pdfjam_%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}
BuildArch:      noarch
Requires:       tetex-latex

%description
PDFjam is a small collection of shell scripts which provide a simple
interface to some of the functionality of the excellent pdfpages
package (by Andreas Matthias) for pdfLaTeX.  At present the utilities
available are:

  * pdfnup, which allows PDF files to be "n-upped" in roughly the way
    that psnup does for PostScript files;
  * pdfjoin, which concatenates the pages of multiple PDF files
    together into a single file;
  * pdf90, which rotates the pages of one or more PDF files through 90
    degrees (anti-clockwise).

In every case, source files are left unchanged.

A potential drawback of these utilities is that any hyperlinks in the
source PDF are lost. On the positive side, there is no appreciable
degradation of image quality in processing PDF files with these
programs, unlike some other indirect methods such as "pdf2ps | psnup |
ps2pdf" (in the author's experience).


%prep
%setup -q -n pdfjam

%install
rm -rf $RPM_BUILD_ROOT

install -d -m 755 $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -p -m 755 scripts/* $RPM_BUILD_ROOT%{_bindir}/
install -p -m 644 man1/* $RPM_BUILD_ROOT%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING PDFjam-README.html pdfdroplets.png
%{_bindir}/*
%{_mandir}/man1/*
