---
type: Jurisdiction
title: "Garvin County, OK"
classification: county
fips: "40049"
state: "OK"
demographics:
  population: 25860
  population_under_18: 6487
  population_18_64: 14703
  population_65_plus: 4670
  median_household_income: 58556
  poverty_rate: 16.97
  homeownership_rate: 67.71
  unemployment_rate: 3.37
  median_home_value: 147800
  gini_index: 0.4409
  vacancy_rate: 16.31
  race_white: 20020
  race_black: 352
  race_asian: 165
  race_native: 1153
  hispanic: 2695
  bachelors_plus: 4347
districts:
  - to: "us/states/ok/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ok/districts/senate/13"
    rel: in-district
    area_weight: 0.9846
  - to: "us/states/ok/districts/senate/43"
    rel: in-district
    area_weight: 0.0153
  - to: "us/states/ok/districts/house/42"
    rel: in-district
    area_weight: 0.6012
  - to: "us/states/ok/districts/house/48"
    rel: in-district
    area_weight: 0.3988
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Garvin County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25860 |
| Under 18 | 6487 |
| 18–64 | 14703 |
| 65+ | 4670 |
| Median household income | 58556 |
| Poverty rate | 16.97 |
| Homeownership rate | 67.71 |
| Unemployment rate | 3.37 |
| Median home value | 147800 |
| Gini index | 0.4409 |
| Vacancy rate | 16.31 |
| White | 20020 |
| Black | 352 |
| Asian | 165 |
| Native | 1153 |
| Hispanic/Latino | 2695 |
| Bachelor's or higher | 4347 |

## Districts

- [OK-04](/us/states/ok/districts/04.md) — 100% (congressional)
- [OK Senate District 13](/us/states/ok/districts/senate/13.md) — 98% (state senate)
- [OK Senate District 43](/us/states/ok/districts/senate/43.md) — 2% (state senate)
- [OK House District 42](/us/states/ok/districts/house/42.md) — 60% (state house)
- [OK House District 48](/us/states/ok/districts/house/48.md) — 40% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
