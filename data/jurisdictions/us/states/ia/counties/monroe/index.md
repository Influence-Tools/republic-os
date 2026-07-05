---
type: Jurisdiction
title: "Monroe County, IA"
classification: county
fips: "19135"
state: "IA"
demographics:
  population: 7513
  population_under_18: 1731
  population_18_64: 4234
  population_65_plus: 1548
  median_household_income: 70996
  poverty_rate: 9.18
  homeownership_rate: 81.29
  unemployment_rate: 3.13
  median_home_value: 156300
  gini_index: 0.3825
  vacancy_rate: 15.51
  race_white: 7146
  race_black: 90
  race_asian: 35
  race_native: 11
  hispanic: 156
  bachelors_plus: 1502
districts:
  - to: "us/states/ia/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/senate/13"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/house/26"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Monroe County, IA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7513 |
| Under 18 | 1731 |
| 18–64 | 4234 |
| 65+ | 1548 |
| Median household income | 70996 |
| Poverty rate | 9.18 |
| Homeownership rate | 81.29 |
| Unemployment rate | 3.13 |
| Median home value | 156300 |
| Gini index | 0.3825 |
| Vacancy rate | 15.51 |
| White | 7146 |
| Black | 90 |
| Asian | 35 |
| Native | 11 |
| Hispanic/Latino | 156 |
| Bachelor's or higher | 1502 |

## Districts

- [IA-03](/us/states/ia/districts/03.md) — 100% (congressional)
- [IA Senate District 13](/us/states/ia/districts/senate/13.md) — 100% (state senate)
- [IA House District 26](/us/states/ia/districts/house/26.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
