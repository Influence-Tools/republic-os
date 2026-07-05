---
type: Jurisdiction
title: "McCurtain County, OK"
classification: county
fips: "40089"
state: "OK"
demographics:
  population: 30863
  population_under_18: 8141
  population_18_64: 17213
  population_65_plus: 5509
  median_household_income: 51929
  poverty_rate: 21.2
  homeownership_rate: 73.06
  unemployment_rate: 4.75
  median_home_value: 144500
  gini_index: 0.4625
  vacancy_rate: 20.48
  race_white: 18542
  race_black: 2409
  race_asian: 321
  race_native: 4444
  hispanic: 2148
  bachelors_plus: 4165
districts:
  - to: "us/states/ok/districts/02"
    rel: in-district
    area_weight: 0.9928
  - to: "us/states/tx/districts/04"
    rel: in-district
    area_weight: 0.0071
  - to: "us/states/ok/districts/senate/5"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/ok/districts/house/1"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# McCurtain County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 30863 |
| Under 18 | 8141 |
| 18–64 | 17213 |
| 65+ | 5509 |
| Median household income | 51929 |
| Poverty rate | 21.2 |
| Homeownership rate | 73.06 |
| Unemployment rate | 4.75 |
| Median home value | 144500 |
| Gini index | 0.4625 |
| Vacancy rate | 20.48 |
| White | 18542 |
| Black | 2409 |
| Asian | 321 |
| Native | 4444 |
| Hispanic/Latino | 2148 |
| Bachelor's or higher | 4165 |

## Districts

- [OK-02](/us/states/ok/districts/02.md) — 99% (congressional)
- [TX-04](/us/states/tx/districts/04.md) — 1% (congressional)
- [OK Senate District 5](/us/states/ok/districts/senate/5.md) — 100% (state senate)
- [OK House District 1](/us/states/ok/districts/house/1.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
