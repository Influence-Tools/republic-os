---
type: Jurisdiction
title: "Major County, OK"
classification: county
fips: "40093"
state: "OK"
demographics:
  population: 7628
  population_under_18: 1933
  population_18_64: 4072
  population_65_plus: 1623
  median_household_income: 71266
  poverty_rate: 11.04
  homeownership_rate: 82.46
  unemployment_rate: 2.64
  median_home_value: 149600
  gini_index: 0.4144
  vacancy_rate: 14.37
  race_white: 6399
  race_black: 1
  race_asian: 40
  race_native: 67
  hispanic: 837
  bachelors_plus: 1416
districts:
  - to: "us/states/ok/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ok/districts/senate/27"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/house/58"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Major County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7628 |
| Under 18 | 1933 |
| 18–64 | 4072 |
| 65+ | 1623 |
| Median household income | 71266 |
| Poverty rate | 11.04 |
| Homeownership rate | 82.46 |
| Unemployment rate | 2.64 |
| Median home value | 149600 |
| Gini index | 0.4144 |
| Vacancy rate | 14.37 |
| White | 6399 |
| Black | 1 |
| Asian | 40 |
| Native | 67 |
| Hispanic/Latino | 837 |
| Bachelor's or higher | 1416 |

## Districts

- [OK-03](/us/states/ok/districts/03.md) — 100% (congressional)
- [OK Senate District 27](/us/states/ok/districts/senate/27.md) — 100% (state senate)
- [OK House District 58](/us/states/ok/districts/house/58.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
