Name:		aider
Version:	0.86.2
Release:	1
Summary:	AI pair programming in your terminal
License:	Apache-2.0
Group:		Development/Other
URL:		https://github.com/Aider-AI/aider
Source0:	https://files.pythonhosted.org/packages/source/a/aider-chat/aider_chat-%{version}.tar.gz
Patch0:		0001-allow-python-3.14.patch
BuildArch:	noarch
# Exact pins in METADATA would require PyPI versions cooker does not ship.
# Rich deps look like "(python3.14dist(foo) < 9 with ...)" so do not
# anchor at start-of-string.
%global __requires_exclude python[0-9.]*dist
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)
Requires:	python
Requires:	python%{pyver}dist(configargparse)
Requires:	python%{pyver}dist(gitpython)
Requires:	python%{pyver}dist(jsonschema)
Requires:	python%{pyver}dist(rich)
Requires:	python%{pyver}dist(prompt-toolkit)
Requires:	python%{pyver}dist(backoff)
Requires:	python%{pyver}dist(pathspec)
Requires:	python%{pyver}dist(diskcache)
Requires:	python%{pyver}dist(packaging)
Requires:	python%{pyver}dist(beautifulsoup4)
Requires:	python%{pyver}dist(pyyaml)
Requires:	python%{pyver}dist(diff-match-patch)
Requires:	python%{pyver}dist(pypandoc)
Requires:	python%{pyver}dist(flake8)
Requires:	python%{pyver}dist(pexpect)
Requires:	python%{pyver}dist(json5)
Requires:	python%{pyver}dist(psutil)
Requires:	python%{pyver}dist(watchfiles)
Requires:	python%{pyver}dist(pillow)
Requires:	python%{pyver}dist(shtab)
Requires:	python%{pyver}dist(oslex)
Requires:	python%{pyver}dist(networkx)
Requires:	python%{pyver}dist(scipy)
Requires:	python%{pyver}dist(importlib-metadata)
Requires:	python%{pyver}dist(fastapi)
Requires:	python%{pyver}dist(orjson)
Requires:	python%{pyver}dist(pydub)
Requires:	python%{pyver}dist(socksio)
Requires:	python%{pyver}dist(pyperclip)
Requires:	python%{pyver}dist(httpx)
Requires:	python%{pyver}dist(openai)
Requires:	python%{pyver}dist(litellm)
Requires:	python%{pyver}dist(tiktoken)
Requires:	python%{pyver}dist(grep-ast)
Requires:	python%{pyver}dist(sounddevice)
Requires:	python%{pyver}dist(importlib-resources)
Requires:	python%{pyver}dist(posthog)
Requires:	python%{pyver}dist(mixpanel)
Recommends:	llama-cpp-server
Recommends:	ollama
Recommends:	git-core
Recommends:	pkgconfig(portaudio-2.0)

%description
Aider is a terminal pair-programmer that edits a git repo with an
LLM. It works with any OpenAI-compatible server, including cooker
llama-server and Ollama:

  export OPENAI_API_BASE=http://127.0.0.1:8080/v1
  export OPENAI_API_KEY=local
  aider --model openai/local

LiteLLM, grep-ast (repo-map), voice (sounddevice), and the
telemetry modules are packaged as system Python modules. The
Streamlit/Playwright browser extras are not: they pull a separate
web stack and download browser binaries.

%prep
%autosetup -p1 -n aider_chat-%{version}

%build
# nothing

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
python -m pip install \
	--no-deps --no-build-isolation --no-compile \
	--root %{buildroot} --prefix %{_prefix} \
	.
if [ -f %{buildroot}%{_bindir}/aider ]; then
	sed -i '1s|^#!/usr/bin/env python3|#!/usr/bin/python|' \
		%{buildroot}%{_bindir}/aider
	sed -i '1s|^#!/usr/bin/python3|#!/usr/bin/python|' \
		%{buildroot}%{_bindir}/aider
fi

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/aider
%{py_sitedir}/aider
%{py_sitedir}/aider_chat-*.*-info
