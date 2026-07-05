---
type: Jurisdiction
title: "Clarke County, IA"
classification: county
fips: "19039"
state: "IA"
demographics:
  population: 9662
  population_under_18: 2470
  population_18_64: 5268
  population_65_plus: 1924
  median_household_income: 71641
  poverty_rate: 9.72
  homeownership_rate: 72.32
  unemployment_rate: 4.24
  median_home_value: 161100
  gini_index: 0.4405
  vacancy_rate: 9.97
  race_white: 7781
  race_black: 5
  race_asian: 54
  race_native: 97
  hispanic: 1624
  bachelors_plus: 1378
districts:
  - to: "us/states/ia/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/senate/12"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/house/24"
    rel: in-district
    area_weight: 0.7496
  - to: "us/states/ia/districts/house/23"
    rel: in-district
    area_weight: 0.2504
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Clarke County, IA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9662 |
| Under 18 | 2470 |
| 18–64 | 5268 |
| 65+ | 1924 |
| Median household income | 71641 |
| Poverty rate | 9.72 |
| Homeownership rate | 72.32 |
| Unemployment rate | 4.24 |
| Median home value | 161100 |
| Gini index | 0.4405 |
| Vacancy rate | 9.97 |
| White | 7781 |
| Black | 5 |
| Asian | 54 |
| Native | 97 |
| Hispanic/Latino | 1624 |
| Bachelor's or higher | 1378 |

## Districts

- [IA-03](/us/states/ia/districts/03.md) — 100% (congressional)
- [IA Senate District 12](/us/states/ia/districts/senate/12.md) — 100% (state senate)
- [IA House District 24](/us/states/ia/districts/house/24.md) — 75% (state house)
- [IA House District 23](/us/states/ia/districts/house/23.md) — 25% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
