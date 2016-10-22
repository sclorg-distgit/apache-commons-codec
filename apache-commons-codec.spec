%{?scl:%scl_package apache-commons-codec}
%{!?scl:%global pkg_name %{name}}

%{?thermostat_find_provides_and_requires}


%global base_name codec
%global short_name commons-%{base_name}

Name:          %{?scl_prefix}apache-%{short_name}
Version:       1.8
Release:       6.3%{?dist}
Summary:       Implementations of common encoders and decoders
License:       ASL 2.0
URL:           http://commons.apache.org/%{base_name}/

Source0:       http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
# Data in DoubleMetaphoneTest.java originally has an inadmissible license.
# The author gives MIT in e-mail communication.
Source1:       aspell-mail.txt


BuildArch:     noarch

BuildRequires: maven30-maven-local
BuildRequires: maven30-apache-commons-parent >= 26-7
BuildRequires: maven30-maven-antrun-plugin
BuildRequires: maven30-maven-assembly-plugin
BuildRequires: maven30-maven-resources-plugin
BuildRequires: maven30-maven-doxia-sitetools
BuildRequires: maven30-maven-plugin-bundle


%description
Commons Codec is an attempt to provide definitive implementations of
commonly used encoders and decoders. Examples include Base64, Hex,
Phonetic and URLs.

%package javadoc
Summary:       API documentation for %{name}

%description javadoc
%{summary}.

%prep
%{?scl:scl enable maven30 %{scl} - << "EOF"}
%setup -q -n %{short_name}-%{version}-src
cp %{SOURCE1} aspell-mail.txt
sed -i 's/\r//' RELEASE-NOTES*.txt LICENSE.txt NOTICE.txt

# compatibility symlinks and aliases
%mvn_file : %{pkg_name} %{short_name}
%mvn_alias : %{short_name}:%{short_name}
%{?scl:EOF}

%build
%{?scl:scl enable maven30 %{scl} - << "EOF"}
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable maven30 %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}
%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES* aspell-mail.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt aspell-mail.txt

%changelog
* Tue Jun 17 2014 Severin Gehwolf <sgehwolf@redhat.com> - 1.8-6.3
- Build against maven30 collection.

* Mon Jan 20 2014 Omair Maijd <omajid@redhat.com> - 1.8-6.2
- Rebuild in order to fix osgi()-style provides.
- Resolves: RHBZ#1054813

* Tue Nov 12 2013 Michal Srb <msrb@redhat.com> - 1.8-6.1
- Enable SCL for thermostat

* Fri Sep 20 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8-6
- Add BuildRequires on apache-commons-parent >= 26-7

* Mon Aug 19 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.8-5
- Migrate away from mvn-rpmbuild (#997446)

* Mon Jul 08 2013 Tomas Radej <tradej@redhat.com> - 1.8-4
- Fixed license tag (MIT is only in test that doesn't make it into binary RPM)

* Tue Jun 25 2013 Tomas Radej <tradej@redhat.com> - 1.8-2
- Clarified licensing of DoubleMetaphoneTest.java

* Fri May 03 2013 Mat Booth <fedora@matbooth.co.uk> - 1.8-1
- Update to 1.8, rhbz #957598

* Mon Apr 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7-5
- Remove unneeded BR: maven-idea-plugin

* Mon Feb 18 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.7-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 19 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7-2
- Add Provides/Obsoletes for jakarta-commons-codec

* Thu Oct 25 2012 Mat Booth <fedora@matbooth.co.uk> - 1.7-1
- Update to 1.7.
- Can finally remove the provides/obsoletes on the old jakarta name.

* Mon Sep 17 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-5
- Restore apache-commons-codec.jar symlink, resolves #857947

* Tue Aug  7 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-4
- Enable tests
- Install NOTICE with javadoc package
- Fix file permissions
- Remove versioned symlinks

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 7 2011 akurtakov <akurtakov@rh.akurtakov> 1.6-1
- Update to latest upstream (1.6).

* Wed Nov 30 2011 Alexander Kurtakov <akurtako@redhat.com> 1.4-13
- Build with maven 3.
- Adapt to current guidelines.

* Thu Feb 10 2011 mbooth <mbooth@sd.matbooth.co.uk> 1.4-12
- Drop versioned jars and javadocs.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri May 21 2010 Mat Booth <fedora@matbooth.co.uk> 1.4-10
- Correct dep-map names #594717.

* Fri May 21 2010 Alexander Kurtakov <akurtako@redhat.com> 1.4-9
- Obsolete/Provide commons-codec.

* Fri May 14 2010 Mat Booth <fedora@matbooth.co.uk> - 1.4-8
- Obsolete jakarta javadoc package.
- Keep legacy depmap around.

* Thu May 13 2010 Mat Booth <fedora@matbooth.co.uk> - 1.4-7
- Use global instead of define.
- Drop really old obsoletes/provides on short_name.
- Fix requires.

* Tue May 11 2010 Mat Booth <fedora@matbooth.co.uk> - 1.4-6
- Rename package (jakarta-commons-codec->apache-commons-codec).

* Tue Dec 8 2009 Mat Booth <fedora@matbooth.co.uk> - 1.4-5
- Enable OSGi automatic depsolving (from Alphonse Van Assche).

* Sun Nov 8 2009 Mat Booth <fedora@matbooth.co.uk> - 1.4-4
- Fix javadoc package requires

* Sat Nov 7 2009 Mat Booth <fedora@matbooth.co.uk> - 1.4-3
- Correct Obsoletes/Provides according to naming guidelines

* Sat Nov 7 2009 Mat Booth <fedora@matbooth.co.uk> - 1.4-2
- Add all maven related build reqs
- Require Java 1.6 because tests fail on GCJ

* Sat Nov 7 2009 Mat Booth <fedora@matbooth.co.uk> - 1.4-1
- Update to 1.4
- Rewrite spec file to build using upstream-preferred maven instead of ant
- Drop patch to add OSGi manifest (done automatically in the maven build)
- Install pom and add to maven dep-map
- Re-enable all tests

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.3-11.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.3-10.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jul 24 2008 Andrew Overholt <overholt@redhat.com> 1.3-9.4
- Update OSGi manifest.

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:1.3-9.3
- drop repotag
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0:1.3-9jpp.2
- Autorebuild for GCC 4.3

* Thu Sep 06 2007 Andrew Overholt <overholt@redhat.com> 1.3-8jpp.2
- Add OSGi manifest.

* Wed Mar 21 2007 Matt Wringe <mwringe@redhat.com> 0:1.3-8jpp.1
- Update to latest jpp version
- Fix rpmlint issues

* Wed Mar 21 2007 Matt Wringe <mwringe@redhat.com> 0:1.3-8jpp
- Fix some rpmlint warnings
- Update copyright year

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> 0:1.3-7jpp.2
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 26 2006 Matt Wringe <mwringe at redhat.com> 0:1.3-7jpp.1
- Merge with upstream version.

* Tue Sep 26 2006 Matt Wringe <mwringe at redhat.com> 0:1.3-7jpp
- Add missing java-javadoc requires and buildrequires.

* Mon Sep 25 2006 Matt Wringe <mwringe at redhat.com> 0:1.3-6jpp.1
- Merge with upstream version.

* Mon Sep 25 2006 Matt Wringe <mwringe at redhat.com> 0:1.3-6jpp
- Update jakarta-commons-codec-1.3-buildscript.patch to build
  offline.

* Thu Aug 10 2006 Matt Wringe <mwringe at redhat.com> 0:1.3-5jpp.1
- Merge with upstream version
 - Add missing javadoc requires

* Sat Jul 22 2006 Jakub Jelinek <jakub@redhat.com> - 0:1.3-4jpp_2fc
- Rebuilt

* Thu Jul 20 2006 Matt Wringe <mwringe at redhat.com> 0:1.3-4jpp_1fc
- Merged with upstream version
- Now is natively compiled

* Thu Jul 20 2006 Matt Wringe <mwringe at redhat.com> 0:1.3-4jpp
- Added conditional native compiling

* Tue Apr 04 2006 Ralph Apel <r.apel@r-apel.de> 0:1.3-3jpp
- First JPP-1.7 release

* Wed Sep 08 2004 Fernando Nasser <fnasser@redhat.com> 0:1.3-2jpp
- Do not stop on test failure

* Tue Sep 07 2004 Fernando Nasser <fnasser@redhat.com> 0:1.3-1jpp
- Upgrade to 1.3
- Rebuilt with Ant 1.6.2

* Thu Jan 22 2004 David Walluck <david@anti-microsoft.org> 0:1.2-1jpp
- 1.2
- use perl instead of patch

* Wed May 28 2003 Ville Skyttä <jpackage-discuss at zarb.org> - 0:1.1-1jpp
- First JPackage release.
