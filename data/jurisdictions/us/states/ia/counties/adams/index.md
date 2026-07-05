---
type: Jurisdiction
title: "Adams County, IA"
classification: county
fips: "19003"
state: "IA"
demographics:
  population: 3622
  population_under_18: 806
  population_18_64: 1940
  population_65_plus: 876
  median_household_income: 71875
  poverty_rate: 9.09
  homeownership_rate: 77.14
  unemployment_rate: 3.93
  median_home_value: 131600
  gini_index: 0.5031
  vacancy_rate: 18.48
  race_white: 3434
  race_black: 11
  race_asian: 0
  race_native: 8
  hispanic: 63
  bachelors_plus: 854
districts:
  - to: "us/states/ia/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/senate/9"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/house/17"
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

# Adams County, IA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3622 |
| Under 18 | 806 |
| 18–64 | 1940 |
| 65+ | 876 |
| Median household income | 71875 |
| Poverty rate | 9.09 |
| Homeownership rate | 77.14 |
| Unemployment rate | 3.93 |
| Median home value | 131600 |
| Gini index | 0.5031 |
| Vacancy rate | 18.48 |
| White | 3434 |
| Black | 11 |
| Asian | 0 |
| Native | 8 |
| Hispanic/Latino | 63 |
| Bachelor's or higher | 854 |

## Districts

- [IA-03](/us/states/ia/districts/03.md) — 100% (congressional)
- [IA Senate District 9](/us/states/ia/districts/senate/9.md) — 100% (state senate)
- [IA House District 17](/us/states/ia/districts/house/17.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
