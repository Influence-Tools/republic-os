---
type: Jurisdiction
title: "Saluda County, SC"
classification: county
fips: "45081"
state: "SC"
demographics:
  population: 19131
  population_under_18: 4196
  population_18_64: 10995
  population_65_plus: 3940
  median_household_income: 51009
  poverty_rate: 18.7
  homeownership_rate: 78.68
  unemployment_rate: 3.22
  median_home_value: 146500
  gini_index: 0.4525
  vacancy_rate: 19.63
  race_white: 11275
  race_black: 4063
  race_asian: 71
  race_native: 76
  hispanic: 3275
  bachelors_plus: 3924
districts:
  - to: "us/states/sc/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/sc/districts/senate/25"
    rel: in-district
    area_weight: 0.6352
  - to: "us/states/sc/districts/senate/10"
    rel: in-district
    area_weight: 0.3646
  - to: "us/states/sc/districts/house/39"
    rel: in-district
    area_weight: 0.7713
  - to: "us/states/sc/districts/house/82"
    rel: in-district
    area_weight: 0.2284
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Saluda County, SC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19131 |
| Under 18 | 4196 |
| 18–64 | 10995 |
| 65+ | 3940 |
| Median household income | 51009 |
| Poverty rate | 18.7 |
| Homeownership rate | 78.68 |
| Unemployment rate | 3.22 |
| Median home value | 146500 |
| Gini index | 0.4525 |
| Vacancy rate | 19.63 |
| White | 11275 |
| Black | 4063 |
| Asian | 71 |
| Native | 76 |
| Hispanic/Latino | 3275 |
| Bachelor's or higher | 3924 |

## Districts

- [SC-03](/us/states/sc/districts/03.md) — 100% (congressional)
- [SC Senate District 25](/us/states/sc/districts/senate/25.md) — 64% (state senate)
- [SC Senate District 10](/us/states/sc/districts/senate/10.md) — 36% (state senate)
- [SC House District 39](/us/states/sc/districts/house/39.md) — 77% (state house)
- [SC House District 82](/us/states/sc/districts/house/82.md) — 23% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
