#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-test_xml
Version  : 0.1.7
Release  : 7
URL      : https://rubygems.org/downloads/test_xml-0.1.7.gem
Source0  : https://rubygems.org/downloads/test_xml-0.1.7.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-bundler
BuildRequires : rubygem-mini_portile
BuildRequires : rubygem-nokogiri
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-support
BuildRequires : rubygem-test-unit

%description
= TestXml
== DESCRIPTION
TestXml is a small extension for testing XML/HTML. Extending RSpec and TestUnit it makes asserting and comparing XML snippets easy, and is especially helpful for testing RESTful web services and their XML representations.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n test_xml-0.1.7
gem spec %{SOURCE0} -l --ruby > rubygem-test_xml.gemspec

%build
export LANG=C
gem build rubygem-test_xml.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
test_xml-0.1.7.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/test_xml-0.1.6 && rspec spec/ && popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/test_xml-0.1.7.gem
/usr/lib64/ruby/gems/2.3.0/gems/test_xml-0.1.7/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/test_xml-0.1.7/CHANGES.md
/usr/lib64/ruby/gems/2.3.0/gems/test_xml-0.1.7/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/test_xml-0.1.7/README.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/test_xml-0.1.7/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/test_xml-0.1.7/lib/test_xml.rb
/usr/lib64/ruby/gems/2.3.0/gems/test_xml-0.1.7/lib/test_xml/assertions.rb
/usr/lib64/ruby/gems/2.3.0/gems/test_xml-0.1.7/lib/test_xml/matcher_methods.rb
/usr/lib64/ruby/gems/2.3.0/gems/test_xml-0.1.7/lib/test_xml/mini_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/test_xml-0.1.7/lib/test_xml/nokogiri.rb
/usr/lib64/ruby/gems/2.3.0/gems/test_xml-0.1.7/lib/test_xml/nokogiri/node.rb
/usr/lib64/ruby/gems/2.3.0/gems/test_xml-0.1.7/lib/test_xml/spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/test_xml-0.1.7/lib/test_xml/test_unit.rb
/usr/lib64/ruby/gems/2.3.0/gems/test_xml-0.1.7/lib/test_xml/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/test_xml-0.1.7/spec/matchers/contain_xml_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/test_xml-0.1.7/spec/matchers/contain_xml_structure_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/test_xml-0.1.7/spec/matchers/equal_xml_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/test_xml-0.1.7/spec/matchers/equal_xml_structure_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/test_xml-0.1.7/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/test_xml-0.1.7/test/nokogiri/test_node.rb
/usr/lib64/ruby/gems/2.3.0/gems/test_xml-0.1.7/test/test_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/test_xml-0.1.7/test/test_unit/test_assertions.rb
/usr/lib64/ruby/gems/2.3.0/gems/test_xml-0.1.7/test_xml.gemspec
/usr/lib64/ruby/gems/2.3.0/specifications/test_xml-0.1.7.gemspec
