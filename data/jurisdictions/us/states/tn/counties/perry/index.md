---
type: Jurisdiction
title: "Perry County, TN"
classification: county
fips: "47135"
state: "TN"
demographics:
  population: 8697
  population_under_18: 1943
  population_18_64: 4847
  population_65_plus: 1907
  median_household_income: 55972
  poverty_rate: 18.06
  homeownership_rate: 73.82
  unemployment_rate: 5.82
  median_home_value: 126900
  gini_index: 0.4128
  vacancy_rate: 25.81
  race_white: 7841
  race_black: 24
  race_asian: 20
  race_native: 107
  hispanic: 120
  bachelors_plus: 1144
districts:
  - to: "us/states/tn/districts/07"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/tn/districts/senate/25"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tn/districts/house/72"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Perry County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8697 |
| Under 18 | 1943 |
| 18–64 | 4847 |
| 65+ | 1907 |
| Median household income | 55972 |
| Poverty rate | 18.06 |
| Homeownership rate | 73.82 |
| Unemployment rate | 5.82 |
| Median home value | 126900 |
| Gini index | 0.4128 |
| Vacancy rate | 25.81 |
| White | 7841 |
| Black | 24 |
| Asian | 20 |
| Native | 107 |
| Hispanic/Latino | 120 |
| Bachelor's or higher | 1144 |

## Districts

- [TN-07](/us/states/tn/districts/07.md) — 100% (congressional)
- [TN Senate District 25](/us/states/tn/districts/senate/25.md) — 100% (state senate)
- [TN House District 72](/us/states/tn/districts/house/72.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
