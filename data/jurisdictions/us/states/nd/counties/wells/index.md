---
type: Jurisdiction
title: "Wells County, ND"
classification: county
fips: "38103"
state: "ND"
demographics:
  population: 3890
  population_under_18: 910
  population_18_64: 1940
  population_65_plus: 1040
  median_household_income: 66114
  poverty_rate: 9.13
  homeownership_rate: 77.06
  unemployment_rate: 1.99
  median_home_value: 114500
  gini_index: 0.5072
  vacancy_rate: 19.1
  race_white: 3698
  race_black: 0
  race_asian: 9
  race_native: 14
  hispanic: 22
  bachelors_plus: 717
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/senate/14"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/house/14"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Wells County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3890 |
| Under 18 | 910 |
| 18–64 | 1940 |
| 65+ | 1040 |
| Median household income | 66114 |
| Poverty rate | 9.13 |
| Homeownership rate | 77.06 |
| Unemployment rate | 1.99 |
| Median home value | 114500 |
| Gini index | 0.5072 |
| Vacancy rate | 19.1 |
| White | 3698 |
| Black | 0 |
| Asian | 9 |
| Native | 14 |
| Hispanic/Latino | 22 |
| Bachelor's or higher | 717 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 14](/us/states/nd/districts/senate/14.md) — 100% (state senate)
- [ND House District 14](/us/states/nd/districts/house/14.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
