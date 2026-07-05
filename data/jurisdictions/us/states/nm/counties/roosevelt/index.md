---
type: Jurisdiction
title: "Roosevelt County, NM"
classification: county
fips: "35041"
state: "NM"
demographics:
  population: 18928
  population_under_18: 4745
  population_18_64: 11343
  population_65_plus: 2840
  median_household_income: 52685
  poverty_rate: 21.85
  homeownership_rate: 60.65
  unemployment_rate: 5.43
  median_home_value: 135800
  gini_index: 0.4537
  vacancy_rate: 13.24
  race_white: 11756
  race_black: 120
  race_asian: 121
  race_native: 175
  hispanic: 8486
  bachelors_plus: 3429
districts:
  - to: "us/states/nm/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nm/districts/senate/27"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nm/districts/house/64"
    rel: in-district
    area_weight: 0.7273
  - to: "us/states/nm/districts/house/63"
    rel: in-district
    area_weight: 0.2727
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nm]
timestamp: "2026-07-03"
---

# Roosevelt County, NM

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18928 |
| Under 18 | 4745 |
| 18–64 | 11343 |
| 65+ | 2840 |
| Median household income | 52685 |
| Poverty rate | 21.85 |
| Homeownership rate | 60.65 |
| Unemployment rate | 5.43 |
| Median home value | 135800 |
| Gini index | 0.4537 |
| Vacancy rate | 13.24 |
| White | 11756 |
| Black | 120 |
| Asian | 121 |
| Native | 175 |
| Hispanic/Latino | 8486 |
| Bachelor's or higher | 3429 |

## Districts

- [NM-03](/us/states/nm/districts/03.md) — 100% (congressional)
- [NM Senate District 27](/us/states/nm/districts/senate/27.md) — 100% (state senate)
- [NM House District 64](/us/states/nm/districts/house/64.md) — 73% (state house)
- [NM House District 63](/us/states/nm/districts/house/63.md) — 27% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
