---
type: Jurisdiction
title: "Union County, SD"
classification: county
fips: "46127"
state: "SD"
demographics:
  population: 17081
  population_under_18: 4432
  population_18_64: 5124
  population_65_plus: 7525
  median_household_income: 89636
  poverty_rate: 6.21
  homeownership_rate: 73.09
  unemployment_rate: 2.96
  median_home_value: 301100
  gini_index: 0.4704
  vacancy_rate: 3.66
  race_white: 15367
  race_black: 160
  race_asian: 190
  race_native: 167
  hispanic: 823
  bachelors_plus: 5959
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 0.9958
  - to: "us/states/sd/districts/senate/16"
    rel: in-district
    area_weight: 0.6389
  - to: "us/states/sd/districts/senate/17"
    rel: in-district
    area_weight: 0.3592
  - to: "us/states/sd/districts/house/16"
    rel: in-district
    area_weight: 0.6389
  - to: "us/states/sd/districts/house/17"
    rel: in-district
    area_weight: 0.3592
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Union County, SD

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17081 |
| Under 18 | 4432 |
| 18–64 | 5124 |
| 65+ | 7525 |
| Median household income | 89636 |
| Poverty rate | 6.21 |
| Homeownership rate | 73.09 |
| Unemployment rate | 2.96 |
| Median home value | 301100 |
| Gini index | 0.4704 |
| Vacancy rate | 3.66 |
| White | 15367 |
| Black | 160 |
| Asian | 190 |
| Native | 167 |
| Hispanic/Latino | 823 |
| Bachelor's or higher | 5959 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 16](/us/states/sd/districts/senate/16.md) — 64% (state senate)
- [SD Senate District 17](/us/states/sd/districts/senate/17.md) — 36% (state senate)
- [SD House District 16](/us/states/sd/districts/house/16.md) — 64% (state house)
- [SD House District 17](/us/states/sd/districts/house/17.md) — 36% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
