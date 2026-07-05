---
type: Jurisdiction
title: "Okfuskee County, OK"
classification: county
fips: "40107"
state: "OK"
demographics:
  population: 11278
  population_under_18: 2541
  population_18_64: 6683
  population_65_plus: 2054
  median_household_income: 48363
  poverty_rate: 25.83
  homeownership_rate: 68.82
  unemployment_rate: 3.54
  median_home_value: 115900
  gini_index: 0.4547
  vacancy_rate: 16.44
  race_white: 6943
  race_black: 737
  race_asian: 113
  race_native: 2063
  hispanic: 442
  bachelors_plus: 1459
districts:
  - to: "us/states/ok/districts/02"
    rel: in-district
    area_weight: 0.9984
  - to: "us/states/ok/districts/senate/8"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ok/districts/house/18"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Okfuskee County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11278 |
| Under 18 | 2541 |
| 18–64 | 6683 |
| 65+ | 2054 |
| Median household income | 48363 |
| Poverty rate | 25.83 |
| Homeownership rate | 68.82 |
| Unemployment rate | 3.54 |
| Median home value | 115900 |
| Gini index | 0.4547 |
| Vacancy rate | 16.44 |
| White | 6943 |
| Black | 737 |
| Asian | 113 |
| Native | 2063 |
| Hispanic/Latino | 442 |
| Bachelor's or higher | 1459 |

## Districts

- [OK-02](/us/states/ok/districts/02.md) — 100% (congressional)
- [OK Senate District 8](/us/states/ok/districts/senate/8.md) — 100% (state senate)
- [OK House District 18](/us/states/ok/districts/house/18.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
