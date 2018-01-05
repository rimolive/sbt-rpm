# doing a bootstrap build from public sbt binaries
# bootstrap exception is here:  https://fedorahosted.org/fpc/ticket/389
# meeting minutes with vote are here:  http://meetbot.fedoraproject.org/fedora-meeting-1/2014-02-13/fpc.2014-02-13-17.00.html

%global do_bootstrap 0

# build non-bootstrap packages with tests, cross-referenced sources, etc
%global do_proper 0
%global pkg_rel 8
%global scala_version 2.10.6
%global scala_short_version 2.10
%global sbt_bootstrap_version 0.13.12
%global sbt_major 0
%global sbt_minor 13
%global sbt_patch 13
%global sbt_build %{nil}
%global sbt_short_version %{sbt_major}.%{sbt_minor}
%global sbt_version %{sbt_major}.%{sbt_minor}.%{sbt_patch}
%global sbt_full_version %{sbt_version}%{sbt_build}
%global typesafe_repo http://repo.typesafe.com/typesafe/ivy-releases

%global ivy_local_dir ivy-local
%global installed_ivy_local %{_datadir}/%{name}/%{ivy_local_dir}

%global generic_ivy_artifact() %{1}/%{2}/%{3}/%{4}/jars/%{5}.jar
%global generic_ivy_descriptor() %{1}/%{2}/%{3}/%{4}/ivys/ivy.xml#/%{5}-%{4}-ivy.xml
%global sbt_ivy_artifact() %{typesafe_repo}/org.scala-sbt/%{1}/%{sbt_bootstrap_version}/jars/%{1}.jar
%global sbt_ivy_descriptor() %{typesafe_repo}/org.scala-sbt/%{1}/%{sbt_bootstrap_version}/ivys/ivy.xml#/%{1}-%{sbt_bootstrap_version}-ivy.xml

%global sbt_launcher_version 1.0.0-M1
%global sbt_ivy_version 2.3.0-sbt-2cf13e211b2cb31f0d3b317289dca70eca3362f6
%global sbt_bootstrap_ivy_version 2.3.0-sbt-2cc8d2761242b072cedb0a04cb39435c4fa24f9a
%global sbt_serialization_version 0.1.2
%global scala_pickling_version 0.10.1
%global template_resolver_version 0.1
%global quasiquotes_version 2.0.1
%global jline_version 2.13
%global jansi_version 1.11
%global sbt_ghpages_version 0.5.4
%global sbt_git_version 0.8.5
%global sbt_site_version 0.8.2
%global sbt_site_jar_version 0.8.2
%global sbt_jvcheck_version 0.1.0
%global sbt_doge_version 0.1.5
%global sbt_assembly_version 0.14.2
%global bintray_sbt_version 0.3.0
%global scalariform_version 0.1.4
%global sbt_scalariform_version 1.3.0
%global sbt_pgp_version 1.0.0
%global sxr_version 0.3.0
%global sbinary_version 0.4.2
%global scalacheck_version 1.11.4
%global specs2_version 2.3.11
%global testinterface_version 1.0
%global dispatch_http_version 0.8.9

%global want_sxr 1
%global want_specs2 1
%global want_scalacheck 1
%global want_dispatch_http 0

Name:		sbt
Version:	%{sbt_version}
Release:	%{pkg_rel}%{?dist}.2
Summary:	The simple build tool for Scala and Java projects

BuildArch:	noarch

License:	BSD
URL:	    http://www.scala-sbt.org
Source0:	https://github.com/sbt/sbt/archive/v%{version}%{sbt_build}.tar.gz

Patch0:	sbt-0.13.13-build-sbt.patch
Patch1:	sbt-0.13.13-launcher-cross-version.patch 

%if %{do_proper}
# sbt-ghpages plugin
Source1:	https://github.com/sbt/sbt-ghpages/archive/v%{sbt_ghpages_version}.tar.gz

# sbt-git plugin
Source2:	https://github.com/sbt/sbt-git/archive/v%{sbt_git_version}.tar.gz

# sbt-site plugin
Source3:	https://github.com/sbt/sbt-site/archive/%{sbt_site_version}.tar.gz

# sxr
Source4:	https://github.com/harrah/browse/archive/v%{sxr_version}.tar.gz
%endif # do_proper

# scalacheck
%if %{?want_scalacheck}
Source6:	http://oss.sonatype.org/content/repositories/releases/org/scalacheck/scalacheck_%{scala_short_version}/%{scalacheck_version}/scalacheck_%{scala_short_version}-%{scalacheck_version}.jar
%endif # want_scalacheck

Source16:	https://raw.github.com/willb/climbing-nemesis/master/climbing-nemesis.py
Source17:	https://raw.github.com/willb/rpm-packaging/master/sbt-packaging/sbt.boot.properties
Source15:	https://raw.github.com/willb/rpm-packaging/master/sbt-packaging/rpmbuild-sbt.boot.properties

# sbt script (to be obsoleted in future releases)
Source21:	https://raw.github.com/willb/rpm-packaging/master/sbt-packaging/sbt

Source34:	compiler-interface-%{sbt_bootstrap_version}-sources.jar
Source134:	%sbt_ivy_descriptor compiler-interface

Source57:	%sbt_ivy_artifact main 
Source157:	%sbt_ivy_descriptor main

Source62:	%sbt_ivy_artifact actions
Source162:	%sbt_ivy_descriptor actions

Source51:	%sbt_ivy_artifact interface 
Source151:	%sbt_ivy_descriptor interface
Source1510:	%generic_ivy_descriptor %typesafe_repo org.scala-sbt interface %sbt_version interface %sbt_version

Source52:	%sbt_ivy_artifact main-settings 
Source152:	%sbt_ivy_descriptor main-settings

Source56:	%sbt_ivy_artifact api 
Source156:	%sbt_ivy_descriptor api

Source58:	%sbt_ivy_artifact classpath 
Source158:	%sbt_ivy_descriptor classpath

Source67:	%sbt_ivy_artifact completion 
Source167:	%sbt_ivy_descriptor completion

Source41:	%sbt_ivy_artifact compiler-ivy-integration 
Source141:	%sbt_ivy_descriptor compiler-ivy-integration

Source55:	%sbt_ivy_artifact compiler-integration 
Source155:	%sbt_ivy_descriptor compiler-integration

Source70:	%sbt_ivy_artifact io 
Source170:	%sbt_ivy_descriptor io
Source1700:	%generic_ivy_descriptor %typesafe_repo org.scala-sbt io %sbt_version io %sbt_version

Source61:	%sbt_ivy_artifact process 
Source161:	%sbt_ivy_descriptor process
Source1610: %generic_ivy_descriptor %typesafe_repo org.scala-sbt process %sbt_version process %sbt_version

Source40:	%sbt_ivy_artifact run 
Source140:	%sbt_ivy_descriptor run

Source69:	%sbt_ivy_artifact relation 
Source169:	%sbt_ivy_descriptor relation

Source33:	%sbt_ivy_artifact task-system 
Source133:	%sbt_ivy_descriptor task-system

Source66:	%sbt_ivy_artifact tasks 
Source166:	%sbt_ivy_descriptor tasks

Source65:	%sbt_ivy_artifact tracking 
Source165:	%sbt_ivy_descriptor tracking

Source73:	%sbt_ivy_artifact logic
Source173:	%sbt_ivy_descriptor logic

Source36:	%sbt_ivy_artifact testing 
Source136:	%sbt_ivy_descriptor testing

Source49:	%sbt_ivy_artifact apply-macro 
Source149:	%sbt_ivy_descriptor apply-macro

Source37:	%sbt_ivy_artifact command 
Source137:	%sbt_ivy_descriptor command

Source39:	launcher-interface-%{sbt_launcher_version}.jar
Source139:	launcher-interface-%{sbt_launcher_version}-ivy.xml

Source32:	%sbt_ivy_artifact ivy 
Source132:	%sbt_ivy_descriptor ivy
Source1320:	%generic_ivy_descriptor %typesafe_repo org.scala-sbt ivy %sbt_version ivy %sbt_version

Source47:	%sbt_ivy_artifact control 
Source147:	%sbt_ivy_descriptor control
Source1470:	%generic_ivy_descriptor %typesafe_repo org.scala-sbt control %sbt_version control %sbt_version

Source68:	%sbt_ivy_artifact cross 
Source168:	%sbt_ivy_descriptor cross
Source1680:	%generic_ivy_descriptor %typesafe_repo org.scala-sbt cross %sbt_version cross %sbt_version


Source46:	%sbt_ivy_artifact classfile 
Source146:	%sbt_ivy_descriptor classfile

Source38:	%sbt_ivy_artifact test-agent 
Source138:	%sbt_ivy_descriptor test-agent

Source45:	%sbt_ivy_artifact persist 
Source145:	%sbt_ivy_descriptor persist

Source53:	%sbt_ivy_artifact incremental-compiler 
Source153:	%sbt_ivy_descriptor incremental-compiler

Source54:	%sbt_ivy_artifact cache 
Source154:	%sbt_ivy_descriptor cache

Source59:	%sbt_ivy_artifact logging 
Source159:	%sbt_ivy_descriptor logging
Source1590:	%generic_ivy_descriptor %typesafe_repo org.scala-sbt logging %sbt_version logging %sbt_version

Source60:	%sbt_ivy_artifact compile 
Source160:	%sbt_ivy_descriptor compile

Source44:	%sbt_ivy_artifact collections 
Source144:	%sbt_ivy_descriptor collections
Source1440:	%generic_ivy_descriptor %typesafe_repo org.scala-sbt collections %sbt_version collections %sbt_version

#BUNDLED
Source89:   https://repo1.maven.org/maven2/org/scala-lang/modules/scala-pickling_2.10/0.10.1/scala-pickling_2.10-0.10.1.jar
Source189:  scala-pickling_%{scala_short_version}-%{scala_pickling_version}-ivy.xml

%if %{?want_specs2}
# specs
Source79:	https://oss.sonatype.org/content/repositories/releases/org/specs2/specs2_%{scala_short_version}/%{specs2_version}/specs2_%{scala_short_version}-%{specs2_version}.jar
%endif

Source97:	template-resolver-%{template_resolver_version}.jar
Source197:	template-resolver-%{template_resolver_version}-ivy.xml

%if %{do_bootstrap}
# include bootstrap libraries
Source35:	%sbt_ivy_artifact compiler-interface

Source48:	launcher-%{sbt_launcher_version}.jar
Source148:	launcher-%{sbt_launcher_version}-ivy.xml

Source63:	sbt-launch.jar

%if %{do_proper}
# sbt plugins
Source74:	http://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/com.typesafe.sbt/sbt-ghpages/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{sbt_ghpages_version}/jars/sbt-ghpages.jar
Source174:	http://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/com.typesafe.sbt/sbt-ghpages/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{sbt_ghpages_version}/ivys/ivy.xml#/%sbt-ghpages-%{sbt_bootstrap_version}-ivy.xml

Source75:	http://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/com.typesafe.sbt/sbt-site/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{sbt_site_jar_version}/jars/sbt-site.jar
Source175:	http://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/com.typesafe.sbt/sbt-site/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{sbt_site_jar_version}/ivys/ivy.xml#/sbt-site-%{sbt_bootstrap_version}-ivy.xml

Source76:	http://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/com.typesafe.sbt/sbt-git/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{sbt_git_version}/jars/sbt-git.jar
Source176:	http://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/com.typesafe.sbt/sbt-git/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{sbt_git_version}/ivys/ivy.xml#/sbt-git-%{sbt_bootstrap_version}-ivy.xml
%endif # do_proper

%if %{?want_sxr}
# sxr
Source77:	http://repo.typesafe.com/typesafe/ivy-releases/org.scala-sbt.sxr/sxr_%{scala_short_version}/%{sxr_version}/jars/sxr_%{scala_short_version}.jar
%endif # want_sxr

%if %{?want_dispatch_http}
# dispatch-http
Source81:	http://oss.sonatype.org/content/repositories/releases/net/databinder/dispatch-http_%{scala_short_version}/%{dispatch_http_version}/dispatch-http_%{scala_short_version}-%{dispatch_http_version}.jar
%endif # want_dispatch_http

Source99:	https://oss.sonatype.org/content/repositories/releases/org/scala-sbt/ivy/ivy/%{sbt_bootstrap_ivy_version}/ivy-%{sbt_bootstrap_ivy_version}.jar

%if %{do_proper}
# more plugins
Source90:	http://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/com.eed3si9n/sbt-doge/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{sbt_doge_version}/jars/sbt-doge.jar
Source190:	http://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/com.eed3si9n/sbt-doge/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{sbt_doge_version}/ivys/ivy.xml#sbt-doge-%{sbt_doge_version}-ivy.xml

Source91:	http://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/com.typesafe.sbt/sbt-javaversioncheck/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{sbt_jvcheck_version}/jars/sbt-javaversioncheck.jar
Source191:	http://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/com.typesafe.sbt/sbt-javaversioncheck/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{sbt_jvcheck_version}/ivys/ivy.xml#sbt-javaversioncheck-%{sbt_jvcheck_version}-ivy.xml

Source92:	http://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/com.typesafe.sbt/sbt-scalariform/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{sbt_scalariform_version}/jars/sbt-scalariform.jar
Source192:	http://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/com.typesafe.sbt/sbt-scalariform/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{sbt_scalariform_version}/ivys/ivy.xml#sbt-scalariform-%{sbt_scalariform_version}-ivy.xml

Source93:	http://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/com.jsuereth/sbt-pgp/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{sbt_pgp_version}/jars/sbt-pgp.jar
Source193:	http://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/com.jsuereth/sbt-pgp/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{sbt_pgp_version}/ivys/ivy.xml#sbt-pgp-%{sbt_pgp_version}-ivy.xml

Source94:	http://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/com.eed3si9n/sbt-assembly/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{sbt_assembly_version}/jars/sbt-assembly.jar
Source194:	http://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/com.eed3si9n/sbt-assembly/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{sbt_assembly_version}/ivys/ivy.xml#sbt-assembly-%{sbt_assembly_version}-ivy.xml

Source95:	http://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/me.lessis/bintray-sbt/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{bintray_sbt_version}/jars/bintray-sbt.jar
Source195:	http://repo.scala-sbt.org/scalasbt/sbt-plugin-releases/me.lessis/bintray-sbt/scala_%{scala_short_version}/sbt_%{sbt_short_version}/%{bintray_sbt_version}/ivys/ivy.xml#bintray-sbt-%{bintray_sbt_version}-ivy.xml

Source96:	https://repo1.maven.org/maven2/org/scalariform/scalariform_%{scala_short_version}/%{scalariform_version}/scalariform_%{scala_short_version}-%{scalariform_version}.jar
Source196:	https://repo1.maven.org/maven2/org/scalariform/scalariform_%{scala_short_version}/%{scalariform_version}/scalariform_%{scala_short_version}-%{scalariform_version}.pom
%endif # do_proper

%endif # do_bootstrap

Source88:	https://oss.sonatype.org/content/repositories/releases/org/scala-sbt/ivy/ivy/%{sbt_ivy_version}/ivy-%{sbt_ivy_version}.jar
Source440:	ivy-%{sbt_ivy_version}-ivy.xml

Source71:	%sbt_ivy_artifact sbt 
Source171:	%sbt_ivy_descriptor sbt

#BUNDLED
Source86:   serialization_%{scala_short_version}-%{sbt_serialization_version}.jar
Source186:  serialization_%{scala_short_version}-%{sbt_serialization_version}-ivy.xml

#BUNDLED
Source98:	quasiquotes_%{scala_short_version}-%{quasiquotes_version}.jar
Source198:	quasiquotes_%{scala_short_version}-%{quasiquotes_version}-ivy.xml

Source200: 	https://github.com/sbt/launcher/archive/v%{sbt_launcher_version}.tar.gz

Source370:  jawn-parser_2.10-0.6.0-ivy.xml
Source371:  jawn-parser_2.10-0.6.0.jar
Source400:	json4s-support_2.10-0.6.0-ivy.xml
Source401:	json4s-support_2.10-0.6.0.jar

%if %{do_bootstrap}
Source460:	ivy-%{sbt_bootstrap_ivy_version}-ivy.xml
Source450:	sxr_2.10-0.3.0-ivy.xml
Source461:	aether-api-1.0.1.v20141111-ivy.xml
Source470:	aether-connector-basic-1.0.1.v20141111-ivy.xml
Source480:	aether-impl-1.0.1.v20141111-ivy.xml
Source490:	aether-spi-1.0.1.v20141111-ivy.xml
Source500:	aether-util-1.0.1.v20141111-ivy.xml
Source510:	guava-18.0-ivy.xml
Source520:	maven-aether-provider-3.2.3-ivy.xml
Source521:	maven-aether-provider-3.2.3.jar
Source530:	org.eclipse.sisu.inject-0.3.0.M1-ivy.xml
Source540:	org.eclipse.sisu.plexus-0.3.0.M1-ivy.xml
Source550:	maven-model-3.2.3-ivy.xml
Source560:	maven-model-builder-3.2.3-ivy.xml
Source561:	maven-model-builder-3.2.3.jar
Source570:	maven-repository-metadata-3.2.3-ivy.xml
Source571:	maven-repository-metadata-3.2.3.jar
Source580:	plexus-classworlds-2.5.1-ivy.xml
Source590:	plexus-component-annotations-1.5.5-ivy.xml
Source600:	plexus-interpolation-1.19-ivy.xml
Source610:	plexus-utils-2.1-ivy.xml
Source620:	plexus-utils-3.0.17-ivy.xml
Source630:	javax.inject-1-ivy.xml
%endif # do_bootstrap

Source640:	%generic_ivy_artifact %typesafe_repo org.scala-sbt main %sbt_version main %sbt_version
Source641:	%generic_ivy_descriptor %typesafe_repo org.scala-sbt main %sbt_version main %sbt_version


Source650:  https://oss.sonatype.org/service/local/repositories/releases/content/org/scala-sbt/sbt-giter8-resolver/sbt-giter8-resolver_2.10/0.1.0/sbt-giter8-resolver_2.10-0.1.0.jar
Source660:  https://oss.sonatype.org/service/local/repositories/releases/content/org/foundweekends/giter8/giter8_2.10/0.7.1/giter8_2.10-0.7.1.jar

BuildRequires:	java-devel
BuildRequires:	python
# maven is required because climbing-nemesis.py uses xmvn-resolve
BuildRequires:	maven-local
BuildRequires:	ivy-local
# packaging/publishing needs these
BuildRequires:	mvn(com.google.guava:guava)
BuildRequires:	mvn(javax.inject:javax.inject)
BuildRequires:	mvn(org.eclipse.aether:aether-impl)
BuildRequires:	mvn(org.eclipse.aether:aether-api)
BuildRequires:	mvn(org.eclipse.aether:aether-spi)
BuildRequires:	mvn(org.eclipse.aether:aether-util)
BuildRequires:	mvn(org.eclipse.aether:aether-connector-basic)
BuildRequires:	mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:	mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires:	mvn(org.codehaus.plexus:plexus-classworlds)
BuildRequires:	mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:	mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:	mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:	mvn(org.bouncycastle:bcprov-jdk16)
BuildRequires:	mvn(org.bouncycastle:bcpg-jdk16)
BuildRequires:	mvn(org.fusesource.jansi:jansi)
BuildRequires:	jline
BuildRequires:	proguard

BuildRequires:	javapackages-tools
Requires:	    javapackages-tools

BuildRequires:	mvn(oro:oro)
BuildRequires:	mvn(commons-httpclient:commons-httpclient)
BuildRequires:	apache-ivy
BuildRequires:	mvn(org.jsoup:jsoup)

BuildRequires:	scala
Requires:	    scala

Requires:	mvn(oro:oro)
Requires:	mvn(commons-httpclient:commons-httpclient)
Requires:	apache-ivy
Requires:	mvn(org.jsoup:jsoup)
Requires:	proguard

Requires:	mvn(org.bouncycastle:bcprov-jdk16)
Requires:	mvn(org.bouncycastle:bcpg-jdk16)
Requires:	mvn(org.fusesource.jansi:jansi)
Requires:	jline

#CONFLICT sbinary built with old scala
Requires:	sbinary = %{sbinary_version}
BuildRequires:	test-interface = %{testinterface_version}
Requires:	    test-interface = %{testinterface_version}

%if !%{do_bootstrap}

%if %{do_proper}
BuildRequires:	sbt-ghpages = %{sbt_ghpages_version}
BuildRequires:	sbt-site = %{sbt_site_version}
BuildRequires:	sbt-git = %{sbt_git_version}

BuildRequires:	sxr = %{sxr_version}
BuildRequires:	scalacheck = %{scalacheck_version}
BuildRequires:	specs2 = %{specs2_version}
%endif

%endif

%description
sbt is the simple build tool for Scala and Java projects.

%prep
%setup -q -n %{name}-%{sbt_version}%{sbt_build}

%if !%{do_proper}
%patch0 -p1
%endif

#BUNDLED put the launcher src code in place
tar xvzf %{SOURCE200} --strip-components=1 launcher-%{sbt_launcher_version}/launcher-implementation
tar xvzf %{SOURCE200} --strip-components=1 launcher-%{sbt_launcher_version}/launcher-interface

%patch1 -p1

sed -i -e '/% "test"/d' project/Util.scala

cp %{SOURCE15} .
cp %{SOURCE17} .

cp %{SOURCE16} .
chmod 755 climbing-nemesis.py

mkdir %{ivy_local_dir}

%if %{do_bootstrap}
cp %{SOURCE63} .
%endif

./climbing-nemesis.py org.scala-lang scala-library %{ivy_local_dir} --version %{scala_version}
./climbing-nemesis.py org.scala-lang scala-compiler %{ivy_local_dir} --version %{scala_version}
./climbing-nemesis.py org.scala-lang scala-reflect %{ivy_local_dir} --version %{scala_version}

cp %{SOURCE171} org.scala-sbt.sbt-%{sbt_bootstrap_version}.ivy.xml
sed -i -e '/precompiled/d' org.scala-sbt.sbt-%{sbt_bootstrap_version}.ivy.xml
./climbing-nemesis.py --jarfile %{SOURCE71} --ivyfile org.scala-sbt.sbt-%{sbt_bootstrap_version}.ivy.xml org.scala-sbt sbt %{ivy_local_dir} --version %{sbt_bootstrap_version}

./climbing-nemesis.py --jarfile %{SOURCE34} --ivyfile %{SOURCE134} org.scala-sbt compiler-interface %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE57} --ivyfile %{SOURCE157} org.scala-sbt main %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE640} --ivyfile %{SOURCE641} org.scala-sbt main %{ivy_local_dir} --version %{sbt_version}
./climbing-nemesis.py --jarfile %{SOURCE62} --ivyfile %{SOURCE162} org.scala-sbt actions %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE52} --ivyfile %{SOURCE152} org.scala-sbt main-settings %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE32} --ivyfile %{SOURCE132} org.scala-sbt ivy %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE32} --ivyfile %{SOURCE1320} org.scala-sbt ivy %{ivy_local_dir} --version %{sbt_version}
./climbing-nemesis.py --jarfile %{SOURCE33} --ivyfile %{SOURCE133} org.scala-sbt task-system %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE36} --ivyfile %{SOURCE136} org.scala-sbt testing %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE37} --ivyfile %{SOURCE137} org.scala-sbt command %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE40} --ivyfile %{SOURCE140} org.scala-sbt run %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE41} --ivyfile %{SOURCE141} org.scala-sbt compiler-ivy-integration %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE55} --ivyfile %{SOURCE155} org.scala-sbt compiler-integration %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE56} --ivyfile %{SOURCE156} org.scala-sbt api %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE58} --ivyfile %{SOURCE158} org.scala-sbt classpath %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE61} --ivyfile %{SOURCE161} org.scala-sbt process %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE61} --ivyfile %{SOURCE1610} org.scala-sbt process %{ivy_local_dir} --version %{sbt_version}
./climbing-nemesis.py --jarfile %{SOURCE65} --ivyfile %{SOURCE165} org.scala-sbt tracking %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE66} --ivyfile %{SOURCE166} org.scala-sbt tasks %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE67} --ivyfile %{SOURCE167} org.scala-sbt completion %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE69} --ivyfile %{SOURCE169} org.scala-sbt relation %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE70} --ivyfile %{SOURCE1700} org.scala-sbt io %{ivy_local_dir} --version %{sbt_version}
./climbing-nemesis.py --jarfile %{SOURCE73} --ivyfile %{SOURCE173} org.scala-sbt logic %{ivy_local_dir} --version %{sbt_bootstrap_version}

./climbing-nemesis.py org.scala-tools.sbinary sbinary_%{scala_short_version} %{ivy_local_dir} --version 0.4.2 --jarfile %{_javadir}/sbinary.jar

./climbing-nemesis.py --jarfile %{SOURCE47} --ivyfile %{SOURCE1470} org.scala-sbt control %{ivy_local_dir} --version %{sbt_version}
./climbing-nemesis.py --jarfile %{SOURCE51} --ivyfile %{SOURCE1510} org.scala-sbt interface %{ivy_local_dir} --version %{sbt_version}
./climbing-nemesis.py --jarfile %{SOURCE51} --ivyfile %{SOURCE151} org.scala-sbt interface %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE70} --ivyfile %{SOURCE170} org.scala-sbt io %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE68} --ivyfile %{SOURCE168} org.scala-sbt cross %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE47} --ivyfile %{SOURCE147} org.scala-sbt control %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py jline jline %{ivy_local_dir} --version %{jline_version} --jarfile %{_javadir}/jline/jline.jar

./climbing-nemesis.py --jarfile %{SOURCE46} --ivyfile %{SOURCE146} org.scala-sbt classfile %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE53} --ivyfile %{SOURCE153} org.scala-sbt incremental-compiler %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE60} --ivyfile %{SOURCE160} org.scala-sbt compile %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE45} --ivyfile %{SOURCE145} org.scala-sbt persist %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE59} --ivyfile %{SOURCE159} org.scala-sbt logging %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE54} --ivyfile %{SOURCE154} org.scala-sbt cache %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE38} --ivyfile %{SOURCE138} org.scala-sbt test-agent %{ivy_local_dir} --version %{sbt_bootstrap_version}

./climbing-nemesis.py --jarfile %{SOURCE68} --ivyfile %{SOURCE1680} org.scala-sbt cross %{ivy_local_dir} --version %{sbt_version}
./climbing-nemesis.py --jarfile %{SOURCE59} --ivyfile %{SOURCE1590} org.scala-sbt logging %{ivy_local_dir} --version %{sbt_version}
./climbing-nemesis.py --jarfile %{SOURCE44} --ivyfile %{SOURCE1440} org.scala-sbt collections %{ivy_local_dir} --version %{sbt_version}
./climbing-nemesis.py --jarfile %{SOURCE44} --ivyfile %{SOURCE144} org.scala-sbt collections %{ivy_local_dir} --version %{sbt_bootstrap_version}

./climbing-nemesis.py org.fusesource.jansi jansi %{ivy_local_dir} --version %{jansi_version} --jarfile %{_javadir}/jansi/jansi.jar
./climbing-nemesis.py org.scala-sbt serialization_%{scala_short_version} %{ivy_local_dir} --version %{sbt_serialization_version} --jarfile %{SOURCE86} --ivyfile %{SOURCE186}
./climbing-nemesis.py org.json4s json4s-core_2.10 %{ivy_local_dir} --version 3.2.10 --jarfile %{_javadir}/json4s/json4s-core.jar
./climbing-nemesis.py org.json4s json4s-ast_2.10 %{ivy_local_dir} --version 3.2.7 --jarfile %{_javadir}/json4s/json4s-ast.jar
./climbing-nemesis.py org.json4s json4s-ast_2.10 %{ivy_local_dir} --version 3.2.10 --jarfile %{_javadir}/json4s/json4s-ast.jar
./climbing-nemesis.py org.spire-math jawn-parser_2.10 %{ivy_local_dir} --version 0.6.0 --jarfile %{SOURCE371} --ivyfile %{SOURCE370}
./climbing-nemesis.py org.spire-math json4s-support_2.10 %{ivy_local_dir} --version 0.6.0 --jarfile %{SOURCE401} --ivyfile %{SOURCE400}
./climbing-nemesis.py org.fusesource.jansi jansi-native %{ivy_local_dir} --version 1.7 --jarfile /usr/lib/java/jansi-native/jansi-native.jar
./climbing-nemesis.py org.fusesource.hawtjni hawtjni-runtime %{ivy_local_dir} --version 1.15 --jarfile %{_sourcedir}/hawtjni-runtime-1.8.jar
./climbing-nemesis.py org.scala-sbt.ivy ivy %{ivy_local_dir} --version %{sbt_ivy_version} --jarfile %{SOURCE88} --ivyfile %{SOURCE440}
./climbing-nemesis.py com.jcraft jsch %{ivy_local_dir} --version 0.1.50 --jarfile %{_sourcedir}/jsch-0.1.46.jar
./climbing-nemesis.py com.jcraft jsch %{ivy_local_dir} --version 0.1.46 --jarfile %{_sourcedir}/jsch-0.1.46.jar
./climbing-nemesis.py junit junit %{ivy_local_dir} --version 4.11 --jarfile %{_javadir}/junit.jar
./climbing-nemesis.py org.hamcrest hamcrest-core %{ivy_local_dir} --version 1.3 --jarfile %{_javadir}/hamcrest/core.jar

%if %{?want_specs2}
./climbing-nemesis.py org.specs2 specs2_2.10 %{ivy_local_dir} --version %{specs2_version} --jarfile %{SOURCE79}
%endif # want_specs2

./climbing-nemesis.py org.scala-sbt launcher-interface %{ivy_local_dir} --version %{sbt_launcher_version} --jarfile %{_sourcedir}/launcher-interface-%{sbt_launcher_version}.jar

./climbing-nemesis.py --jarfile %{SOURCE89} --ivyfile %{SOURCE189} org.scala-lang.modules scala-pickling_%{scala_short_version} %{ivy_local_dir} --version %{scala_pickling_version}
./climbing-nemesis.py com.thoughtworks.paranamer paranamer %{ivy_local_dir} --version 2.6 --jarfile %{_javadir}/paranamer/paranamer.jar
./climbing-nemesis.py org.scalamacros quasiquotes_2.10 %{ivy_local_dir} --version 2.0.1 --jarfile %{SOURCE98} --ivyfile %{SOURCE198}

# scalacheck
%if %{?want_scalacheck}
./climbing-nemesis.py --jarfile %{SOURCE6} org.scalacheck scalacheck %{ivy_local_dir} --version %{scalacheck_version} --scala %{scala_short_version}
%endif

./climbing-nemesis.py --jarfile %{SOURCE97} --ivyfile %{SOURCE197} org.scala-sbt template-resolver %{ivy_local_dir} --version %{template_resolver_version}
./climbing-nemesis.py --jarfile %{SOURCE49} --ivyfile %{SOURCE149} org.scala-sbt apply-macro %{ivy_local_dir} --version %{sbt_bootstrap_version}

# Giter8 dependencies
./climbing-nemesis.py org.scala-sbt.sbt-giter8-resolver sbt-giter8-resolver_2.10 %{ivy_local_dir} --version 0.1.0 --jarfile %{SOURCE650}
./climbing-nemesis.py org.foundweekends.giter8 giter8_2.10 %{ivy_local_dir} --version 0.7.1 --jarfile %{SOURCE660}

%if %{do_bootstrap}
./climbing-nemesis.py --jarfile %{SOURCE51} --ivyfile %{SOURCE151} org.scala-sbt interface %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py --jarfile %{SOURCE70} --ivyfile %{SOURCE170} org.scala-sbt io %{ivy_local_dir} --version %{sbt_bootstrap_version}
./climbing-nemesis.py com.jcraft jsch %{ivy_local_dir} --version 0.1.46 --jarfile %{_sourcedir}/jsch-0.1.46.jar
./climbing-nemesis.py org.codehaus.plexus plexus-component-annotations %{ivy_local_dir} --version 1.5.5 --jarfile %{_javadir}/plexus-containers/plexus-component-annotations.jar --ivyfile %{SOURCE590}
./climbing-nemesis.py org.codehaus.plexus plexus-classworlds %{ivy_local_dir} --version 2.5.1 --jarfile %{_javadir}/plexus-classworlds.jar --ivyfile %{SOURCE580}
./climbing-nemesis.py org.codehaus.plexus plexus-utils %{ivy_local_dir} --version 2.1 --jarfile %{_javadir}/plexus/utils.jar --ivyfile %{SOURCE610}
./climbing-nemesis.py org.codehaus.plexus plexus-utils %{ivy_local_dir} --version 3.0.17 --jarfile %{_javadir}/plexus/utils.jar --ivyfile %{SOURCE620}
./climbing-nemesis.py org.eclipse.aether aether-api %{ivy_local_dir} --version 1.0.1.v20141111 --jarfile %{_javadir}/aether/aether-api.jar --ivyfile %{SOURCE461}
./climbing-nemesis.py org.eclipse.aether aether-spi %{ivy_local_dir} --version 1.0.1.v20141111 --jarfile %{_javadir}/aether/aether-spi.jar --ivyfile %{SOURCE490}
./climbing-nemesis.py org.eclipse.aether aether-util %{ivy_local_dir} --version 1.0.1.v20141111 --jarfile %{_javadir}/aether/aether-util.jar --ivyfile %{SOURCE500}
./climbing-nemesis.py org.apache.maven maven-model %{ivy_local_dir}  --version 3.2.3 --jarfile %{_javadir}/maven/maven-model-2.0.2.jar --ivyfile %{SOURCE550}
./climbing-nemesis.py org.apache.maven maven-model-builder %{ivy_local_dir} --version 3.2.3 --jarfile %{SOURCE561} --ivyfile %{SOURCE560}
./climbing-nemesis.py org.apache.maven maven-repository-metadata %{ivy_local_dir} --version 3.2.3 --jarfile %{SOURCE571} --ivyfile %{SOURCE570}
./climbing-nemesis.py org.eclipse.sisu org.eclipse.sisu.inject %{ivy_local_dir} --version 0.3.0.M1 --jarfile %{_javadir}/org.eclipse.sisu.inject.jar --ivyfile %{SOURCE530}
./climbing-nemesis.py org.codehaus.plexus plexus-interpolation %{ivy_local_dir} --version 1.19 --jarfile %{_javadir}/plexus/interpolation.jar --ivyfile %{SOURCE600}
./climbing-nemesis.py org.scala-sbt.ivy ivy %{ivy_local_dir} --version %{sbt_bootstrap_ivy_version} --jarfile %{SOURCE99} --ivyfile %{SOURCE460}
./climbing-nemesis.py org.eclipse.aether aether-impl %{ivy_local_dir} --version 1.0.1.v20141111 --jarfile %{_javadir}/aether/aether-impl.jar --ivyfile %{SOURCE480}
./climbing-nemesis.py com.google.guava guava %{ivy_local_dir} --version 18.0 --jarfile %{_javadir}/guava.jar --ivyfile %{SOURCE510}
./climbing-nemesis.py javax.inject javax.inject %{ivy_local_dir} --version 1 --jarfile %{_javadir}/javax.inject/atinject.jar --ivyfile %{SOURCE630}
./climbing-nemesis.py org.eclipse.sisu org.eclipse.sisu.plexus %{ivy_local_dir} --version 0.3.0.M1 --jarfile %{_javadir}/org.eclipse.sisu.plexus.jar --ivyfile %{SOURCE540}
./climbing-nemesis.py org.eclipse.aether aether-connector-basic %{ivy_local_dir} --version 1.0.1.v20141111 --jarfile %{_javadir}/aether/aether-connector-basic.jar --ivyfile %{SOURCE470}
./climbing-nemesis.py org.apache.maven maven-aether-provider %{ivy_local_dir} --version 3.2.3 --jarfile %{SOURCE521} --ivyfile %{SOURCE520}

%if %{?want_sxr}
./climbing-nemesis.py --jarfile %{SOURCE77} --ivyfile %{SOURCE450} org.scala-sbt.sxr sxr_2.10 %{ivy_local_dir} --version %{sxr_version}
%endif # want_sxr

%endif # do_bootstrap

%if %{do_proper}
./climbing-nemesis.py --jarfile %{SOURCE74} --ivyfile %{SOURCE174} com.typesafe.sbt sbt-ghpages %{ivy_local_dir} --version %{sbt_ghpages_version}
./climbing-nemesis.py --jarfile %{SOURCE75} --ivyfile %{SOURCE175} com.typesafe.sbt sbt-site %{ivy_local_dir} --version %{sbt_site_jar_version}
./climbing-nemesis.py --jarfile %{SOURCE76} --ivyfile %{SOURCE176} com.typesafe.sbt sbt-git %{ivy_local_dir} --version %{sbt_git_version}

./climbing-nemesis.py --jarfile %{SOURCE90} --ivyfile %{SOURCE190} com.eed3si9n sbt-doge %{ivy_local_dir} --version %{sbt_doge_version}
./climbing-nemesis.py --jarfile %{SOURCE91} --ivyfile %{SOURCE191} com.typesafe.sbt sbt-javaversioncheck %{ivy_local_dir} --version %{sbt_jvcheck_version}
./climbing-nemesis.py --jarfile %{SOURCE92} --ivyfile %{SOURCE192} com.typesafe.sbt sbt-scalariform %{ivy_local_dir} --version %{sbt_scalariform_version}
./climbing-nemesis.py --jarfile %{SOURCE93} --ivyfile %{SOURCE193} com.jsuereth sbt-pgp %{ivy_local_dir} --version %{sbt_pgp_version}
./climbing-nemesis.py --jarfile %{SOURCE94} --ivyfile %{SOURCE194} com.eed3si9n sbt-assembly %{ivy_local_dir} --version %{sbt_assembly_version}
./climbing-nemesis.py --jarfile %{SOURCE95} --ivyfile %{SOURCE195} me.lessis bintray-sbt %{ivy_local_dir} --version %{bintray_sbt_version}
%endif

# dispatch-http
%if %{?want_dispatch_http}
./climbing-nemesis.py --jarfile %{SOURCE81} net.databinder dispatch-http_%{scala_short_version} %{ivy_local_dir} --version %{dispatch_http_version}
%endif

# test-interface
./climbing-nemesis.py org.scala-sbt test-interface %{ivy_local_dir} --version 1.0

%if !%{do_proper}
sed -i -e '/sbt-doge/d' project/plugins.sbt
sed -i -e '/sbt-ghpages/d' project/plugins.sbt
sed -i -e '/sbt-git/d' project/plugins.sbt
sed -i -e '/sbt-javaversioncheck/d' project/plugins.sbt
sed -i -e '/sbt-pgp/d' project/plugins.sbt
sed -i -e '/sbt-scalariform/d' project/plugins.sbt
sed -i -e '/sbt-site/d' project/plugins.sbt
sed -i -e '/bintray-sbt/d' project/plugins.sbt
sed -i -e '/sbt-assembly/d' project/plugins.sbt
cat project/plugins.sbt
rm -f main/src/main/src/main/scala/sbt/plugin/Giter8ResolverPlugin.scala
sed -i '/Giter8/s/^/\/\//g' main/src/main/scala/sbt/PluginDiscovery.scala 
%endif

for props in rpmbuild-sbt.boot.properties sbt.boot.properties ; do
    sed -i -e 's/FEDORA_SCALA_VERSION/%{scala_version}/g' $props
    sed -i -e 's/FEDORA_SBT_VERSION/%{sbt_version}/g' $props
done

sed -i -e 's/0.13.12/%{sbt_bootstrap_version}/g' project/build.properties

# remove any references to Scala 2.10.2
sed -i -e 's/["]2[.]10[.][2345]["]/\"2.10.6\"/g' $(find . -name \*.xml)

%if !%{do_proper}
rm -f project/Docs.scala
rm -f project/Formatting.scala
rm -f project/NightlyPlugin.scala
rm -f project/Release.scala
rm -f project/SiteMap.scala
rm -f project/StatusPlugin.scala
%endif

mkdir sbt-boot-dir
%if %{do_bootstrap}
mkdir -p sbt-boot-dir/scala-%{scala_version}/org.scala-sbt/%{name}/%{sbt_bootstrap_version}/
mkdir -p sbt-boot-dir/scala-%{scala_version}/lib
for jar in $(find %{ivy_local_dir}/ -name \*.jar | grep fusesource) ; do 
   cp --symbolic-link $(readlink $jar) sbt-boot-dir/scala-%{scala_version}/lib
done

# this is a hack, obvs
for jar in $(find %{ivy_local_dir}/ -name \*.jar | grep bouncycastle) ; do 
   cp --symbolic-link $(readlink $jar) sbt-boot-dir/scala-%{scala_version}/lib
done

#BUNDLED
for jar in $(find %{ivy_local_dir}/ -name \*.jar | grep scala-pickling) ; do
   cp $jar sbt-boot-dir/scala-%{scala_version}/org.scala-sbt/%{name}/%{sbt_bootstrap_version}/
done

#BUNDLED
for jar in $(find %{ivy_local_dir}/ -name \*.jar | grep serialization) ; do
   cp $jar sbt-boot-dir/scala-%{scala_version}/org.scala-sbt/%{name}/%{sbt_bootstrap_version}/
done
%endif

sed -i -e 's/["]2[.]10[.][2345]["]/\"%{scala_version}\"/g' $(find . -name \*.sbt -type f) $(find . -name \*.xml) $(find . -name \*.scala)
sed -i -e 's/["]2[.]10[.]2-RC2["]/\"%{scala_version}\"/g' $(find . -name \*.sbt -type f)

%build

%if %{do_bootstrap}
java -Xms512M -Xmx1536M -Xss1M -XX:+CMSClassUnloadingEnabled -jar -Dfedora.sbt.ivy.dir=$PWD/%{ivy_local_dir} -Dfedora.sbt.boot.dir=$PWD/sbt-boot-dir/ -Divy.checksums='""' -Dsbt.boot.properties=$PWD/rpmbuild-sbt.boot.properties sbt-launch.jar package "set publishTo in Global := Some(Resolver.file(\"published\", file(\"published\"))(Resolver.ivyStylePatterns) ivys \"$(pwd)/published/[organization]/[module]/[revision]/ivy.xml\" artifacts \"$(pwd)/published/[organization]/[module]/[revision]/[artifact]-[revision].[ext]\")" publish makePom
%else
export SBT_IVY_DIR=$PWD/%{ivy_local_dir}
export SBT_BOOT_DIR=$PWD/sbt-boot-dir/
export SBT_BOOT_PROPERTIES=rpmbuild-sbt.boot.properties
sbt package "set publishTo in Global := Some(Resolver.file(\"published\", file(\"published\"))(Resolver.ivyStylePatterns) ivys \"$(pwd)/published/[organization]/[module]/[revision]/ivy.xml\" artifacts \"$(pwd)/published/[organization]/[module]/[revision]/[artifact]-[revision].[ext]\")" publish makePom
%endif

# XXX: this is a hack; we seem to get correct metadata but bogus JARs
# from "sbt publish" for some reason
for f in $(find published -name \*.jar ) ; do
    find . -ipath \*target\* -and -name $(basename $f) -exec cp '{}' $f \;
done

%install

mkdir -p %{buildroot}/%{_javadir}/%{name}

# collect and install SBT jars
find published -name \*.jar | grep -v sbt-launch.jar | grep %{sbt_full_version}.jar | xargs -I JAR cp JAR %{buildroot}/%{_javadir}/%{name}

mkdir -p %{buildroot}/%{_bindir}
cp -p %{SOURCE21} %{buildroot}/%{_bindir}/%{name}
chmod 755 %{buildroot}/%{_bindir}/%{name}

pushd %{buildroot}/%{_javadir}/%{name}
for jar in *.jar ; do
    mv $jar $(echo $jar | sed -e 's/-%{sbt_full_version}//g')
done
popd

%if %{do_bootstrap}
# manually install BUNDLED launcher
cp launcher-implementation/target/launcher-implementation-%{sbt_full_version}.jar %{buildroot}/%{_javadir}/%{name}/launcher-implementation.jar
cp launcher-interface/target/launcher-interface-%{sbt_full_version}.jar %{buildroot}/%{_javadir}/%{name}/launcher-interface.jar

# manually install BUNDLED pickling/serialization/quasiquotes
find sbt-boot-dir -name \*.jar | grep scala-pickling | xargs -I JAR cp JAR %{buildroot}/%{_javadir}/%{name}/scala-pickling.jar
find sbt-boot-dir -name \*.jar | grep serialization | xargs -I JAR cp JAR %{buildroot}/%{_javadir}/%{name}/serialization.jar
find sbt-boot-dir -name \*.jar | grep quasiquotes | xargs -I JAR cp JAR %{buildroot}/%{_javadir}/%{name}/quasiquotes.jar

# manually install sbt-giter8-resolver
cp %{ivy_local_dir}/org.scala-sbt.sbt-giter8-resolver/sbt-giter8-resolver/0.1.0/sbt-giter8-resolver-0.1.0.jar %{buildroot}%{_javadir}/%{name}/sbt-giter8-resolver.jar
%endif

rm -f %{buildroot}/%{_javadir}/%{name}/sbt-launch.jar

mkdir -p %{buildroot}/%{_sysconfdir}/%{name}

# XXXXXXX
for props in rpmbuild-sbt.boot.properties sbt.boot.properties ; do
    sed 's/debug/info/' < $props > %{buildroot}/%{_sysconfdir}/%{name}/$props
done

mkdir -p %{buildroot}/%{installed_ivy_local}

# remove things that we only needed for the bootstrap build
rm -rf %{ivy_local_dir}/net.databinder
rm -rf %{ivy_local_dir}/com.typesafe.sbt
rm -rf %{ivy_local_dir}/org.scalacheck
rm -rf %{ivy_local_dir}/org.scala-sbt.sxr
rm -rf %{ivy_local_dir}/cache
rm -rf %{ivy_local_dir}/org.scala-sbt/sbt-launch

(cd %{ivy_local_dir} ; tar --exclude=.md5 --exclude=.sha1 -cf - .) | (cd %{buildroot}/%{installed_ivy_local} ; tar -xf - )
(cd published ; tar --exclude=\*.md5 --exclude=\*.sha1 -cf - .) | (cd %{buildroot}/%{installed_ivy_local} ; tar -xf - )

for bootjar in $(find %{buildroot}/%{installed_ivy_local}/org.scala-sbt -type l) ; do
rm -f $bootjar
ln -s %{_javadir}/%{name}/$(basename $bootjar) $bootjar
done

%if %{do_bootstrap}

concretize() {
    src=$(readlink $1)
    rm $1 && cp $src $1
}

# copy other bootstrap dependency jars from their sources
for depjar in $(find %{buildroot}/%{installed_ivy_local} -lname %{_sourcedir}\* ) ; do
concretize $depjar
done

%endif # do_bootstrap

find %{buildroot}/%{installed_ivy_local} -name \*.lock -delete
find %{buildroot}/%{_datadir}/%{name} -name \*test-interface\* | xargs rm -rf

### install POM files
mkdir -p %{buildroot}/%{_mavenpomdir}
rm -f .rpm_pomfiles
touch .rpm_pomfiles
declare -a shortnames

for pom in $(find . -name \*.pom | grep -v compiler-interface | grep -v launch-test | grep -v sbt-launch | grep -v test-artifact | grep -v jmxri | grep -v bottom | grep -v top | grep -v middle | grep -v mvn | grep -v example-parent | grep -v example-child | grep -v app | grep -v sbtroot | grep -v gent) ; do 
    shortname=$(echo $pom | sed -e 's/^.*[/]\([a-z-]\+\)-0.13.13.pom$/\1/g')
    echo installing POM $pom to %{_mavenpomdir}/JPP.%{name}-${shortname}.pom
    cp $pom %{buildroot}/%{_mavenpomdir}/JPP.%{name}-${shortname}.pom
    echo %{_mavenpomdir}/JPP.%{name}-${shortname}.pom >> .rpm_pomfiles
    shortnames=( "${shortnames[@]}" $shortname )
done

echo shortnames are ${shortnames[@]}

for sub in ${shortnames[@]} ; do
    echo running add_maven_depmap JPP.%{name}-${sub}.pom %{name}/${sub}.jar
    %add_maven_depmap JPP.%{name}-${sub}.pom %{name}/${sub}.jar
done

%files -f .mfiles
%{_datadir}/%{name}
%{_bindir}/%{name}*
%{_javadir}/%{name}
%{_javadir}/%{name}/compiler-interface.jar
%{_javadir}/%{name}/quasiquotes.jar
%{_javadir}/%{name}/scala-pickling.jar
%{_javadir}/%{name}/serialization.jar
%{_javadir}/%{name}/sbt-giter8-resolver.jar

%{_sysconfdir}/%{name}
%doc README.md LICENSE NOTICE

%changelog
* Fri Nov 03 2017 Ricardo Martinelli <rmartine@redhat.com> - 0.13.13-2
- Bootstrap build improved
- Added giter8 support

* Fri Sep 01 2017 Pete MacKinnon <pmackinn@redhat.com> - 0.13.13-1
- Bootstrap build

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-8.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-8.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-8.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 21 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.13.1-8
- Non-bootstrap build

* Tue Jul 21 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.13.1-7
- Port to Ivy 2.4.0
- Fix compatibility with XMvn 2.4.0

* Fri Jul 10 2015 William Benton <willb@redhat.com> - 0.13.1-7
- bootstrap build
- fixes for Proguard
- don't ExcludeArch ARM

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.1-6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 22 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.13.1-6
- Rebuild to fix dangling jansi-native and hawtjni-runtime symlinks

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.1-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 4 2014 William Benton <willb@redhat.com> - 0.13.1-5
- fixes BZ 1072096

* Thu Jan 30 2014 William Benton <willb@redhat.com> - 0.13.1-4
- use native test-interface and sbinary packages in both bootstrap and non-bootstrap modes
- fix a bug that was crashing on rawhide

* Mon Jan 20 2014 William Benton <willb@redhat.com> - 0.13.1-3
- builds as non-bootstrap package
- numerous other minor fixes

* Wed Jan 15 2014 William Benton <willb@redhat.com> - 0.13.1-2
- use generated Ivy files
- use bootstrap test-interface in bootstrap package

* Sat Dec 14 2013 William Benton <willb@redhat.com> - 0.13.1-1
- updated to 0.13.1
- many other packaging fixes

* Thu Nov 7 2013 William Benton <willb@redhat.com> - 0.13.0-1
- initial package
