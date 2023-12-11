# Alternating_Case

[![License: AGPL](https://img.shields.io/badge/License-AGPL-blue.svg)](https://github.com/gotreasa/alternating_case/blob/main/LICENSE)
[![Sonarcloud Status](https://sonarcloud.io/api/project_badges/measure?project=gotreasa_alternating_case&metric=alert_status)](https://sonarcloud.io/dashboard?id=gotreasa_alternating_case)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=gotreasa_alternating_case&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=gotreasa_alternating_case)
[![Build Status](https://github.com/gotreasa/alternating_case/actions/workflows/cicd.yml/badge.svg)](https://github.com/gotreasa/alternating_case/actions/workflows/cicd.yml)
[![Can I Deploy main to test](https://gotreasa.pactflow.io/pacticipants/alternating_case_app/branches/main/latest-version/can-i-deploy/to-environment/test/badge)](https://gotreasa.pactflow.io/hal-browser/browser.html#https://gotreasa.pactflow.io/pacticipants/alternating_case_app/branches/main/latest-version/can-i-deploy/to-environment/test/badge)

Welcome to the Python Template created via a cookiecutter recipe. The project template is designed for a development via a `Double Loop approach` (BDD-TDD) using pytest and several other pytest libs.

## Description

altERnaTIng cAsE <=> ALTerNAtiNG CaSe
Define `String.prototype.toAlternatingCase` (or a similar function/method such as `to_alternating_case`/`toAlternatingCase`/`ToAlternatingCase` in your selected language; see the initial solution for details) such that each lowercase letter becomes uppercase and each uppercase letter becomes lowercase. For example:

```
"hello world".toAlternatingCase() === "HELLO WORLD"
"HELLO WORLD".toAlternatingCase() === "hello world"
"hello WORLD".toAlternatingCase() === "HELLO world"
"HeLLo WoRLD".toAlternatingCase() === "hEllO wOrld"
"12345".toAlternatingCase()       === "12345"                   // Non-alphabetical characters are unaffected
"1a2b3c4d5e".toAlternatingCase()  === "1A2B3C4D5E" # pragma: allowlist secret
"String.prototype.toAlternatingCase".toAlternatingCase() === "sTRING.PROTOTYPE.TOaLTERNATINGcASE"
```

As usual, your function/method should be pure, i.e. it should not mutate the original string.
