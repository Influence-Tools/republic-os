---
type: Jurisdiction
title: "Scott County, IL"
classification: county
fips: "17171"
state: "IL"
demographics:
  population: 4937
  population_under_18: 1030
  population_18_64: 2765
  population_65_plus: 1142
  median_household_income: 66705
  poverty_rate: 11.46
  homeownership_rate: 78.98
  unemployment_rate: 2.72
  median_home_value: 96400
  gini_index: 0.458
  vacancy_rate: 14.18
  race_white: 4719
  race_black: 58
  race_asian: 22
  race_native: 3
  hispanic: 80
  bachelors_plus: 910
districts:
  - to: "us/states/il/districts/15"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/senate/50"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/house/100"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Scott County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4937 |
| Under 18 | 1030 |
| 18–64 | 2765 |
| 65+ | 1142 |
| Median household income | 66705 |
| Poverty rate | 11.46 |
| Homeownership rate | 78.98 |
| Unemployment rate | 2.72 |
| Median home value | 96400 |
| Gini index | 0.458 |
| Vacancy rate | 14.18 |
| White | 4719 |
| Black | 58 |
| Asian | 22 |
| Native | 3 |
| Hispanic/Latino | 80 |
| Bachelor's or higher | 910 |

## Districts

- [IL-15](/us/states/il/districts/15.md) — 100% (congressional)
- [IL Senate District 50](/us/states/il/districts/senate/50.md) — 100% (state senate)
- [IL House District 100](/us/states/il/districts/house/100.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
