---
type: Jurisdiction
title: "Grant County, OK"
classification: county
fips: "40053"
state: "OK"
demographics:
  population: 4131
  population_under_18: 979
  population_18_64: 2213
  population_65_plus: 939
  median_household_income: 60758
  poverty_rate: 17.5
  homeownership_rate: 76.3
  unemployment_rate: 4.3
  median_home_value: 105700
  gini_index: 0.4555
  vacancy_rate: 25.47
  race_white: 3569
  race_black: 84
  race_asian: 6
  race_native: 95
  hispanic: 194
  bachelors_plus: 870
districts:
  - to: "us/states/ok/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/senate/19"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/house/38"
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

# Grant County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4131 |
| Under 18 | 979 |
| 18–64 | 2213 |
| 65+ | 939 |
| Median household income | 60758 |
| Poverty rate | 17.5 |
| Homeownership rate | 76.3 |
| Unemployment rate | 4.3 |
| Median home value | 105700 |
| Gini index | 0.4555 |
| Vacancy rate | 25.47 |
| White | 3569 |
| Black | 84 |
| Asian | 6 |
| Native | 95 |
| Hispanic/Latino | 194 |
| Bachelor's or higher | 870 |

## Districts

- [OK-03](/us/states/ok/districts/03.md) — 100% (congressional)
- [OK Senate District 19](/us/states/ok/districts/senate/19.md) — 100% (state senate)
- [OK House District 38](/us/states/ok/districts/house/38.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
