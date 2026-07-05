---
type: Jurisdiction
title: "Jefferson County, PA"
classification: county
fips: "42065"
state: "PA"
demographics:
  population: 43864
  population_under_18: 9365
  population_18_64: 24742
  population_65_plus: 9757
  median_household_income: 58686
  poverty_rate: 14.15
  homeownership_rate: 74.91
  unemployment_rate: 4.16
  median_home_value: 139700
  gini_index: 0.4472
  vacancy_rate: 16.94
  race_white: 42057
  race_black: 157
  race_asian: 121
  race_native: 26
  hispanic: 446
  bachelors_plus: 7591
districts:
  - to: "us/states/pa/districts/15"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/pa/districts/senate/25"
    rel: in-district
    area_weight: 0.6884
  - to: "us/states/pa/districts/senate/41"
    rel: in-district
    area_weight: 0.3114
  - to: "us/states/pa/districts/house/66"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Jefferson County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 43864 |
| Under 18 | 9365 |
| 18–64 | 24742 |
| 65+ | 9757 |
| Median household income | 58686 |
| Poverty rate | 14.15 |
| Homeownership rate | 74.91 |
| Unemployment rate | 4.16 |
| Median home value | 139700 |
| Gini index | 0.4472 |
| Vacancy rate | 16.94 |
| White | 42057 |
| Black | 157 |
| Asian | 121 |
| Native | 26 |
| Hispanic/Latino | 446 |
| Bachelor's or higher | 7591 |

## Districts

- [PA-15](/us/states/pa/districts/15.md) — 100% (congressional)
- [PA Senate District 25](/us/states/pa/districts/senate/25.md) — 69% (state senate)
- [PA Senate District 41](/us/states/pa/districts/senate/41.md) — 31% (state senate)
- [PA House District 66](/us/states/pa/districts/house/66.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
