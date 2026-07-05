---
type: Jurisdiction
title: "Clark County, SD"
classification: county
fips: "46025"
state: "SD"
demographics:
  population: 3917
  population_under_18: 1151
  population_18_64: 1845
  population_65_plus: 921
  median_household_income: 70726
  poverty_rate: 10.85
  homeownership_rate: 77.54
  unemployment_rate: 3.96
  median_home_value: 158400
  gini_index: 0.4407
  vacancy_rate: 16.97
  race_white: 3558
  race_black: 21
  race_asian: 27
  race_native: 29
  hispanic: 209
  bachelors_plus: 564
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/sd/districts/senate/4"
    rel: in-district
    area_weight: 0.8158
  - to: "us/states/sd/districts/senate/22"
    rel: in-district
    area_weight: 0.1841
  - to: "us/states/sd/districts/house/4"
    rel: in-district
    area_weight: 0.8158
  - to: "us/states/sd/districts/house/22"
    rel: in-district
    area_weight: 0.1841
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Clark County, SD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3917 |
| Under 18 | 1151 |
| 18–64 | 1845 |
| 65+ | 921 |
| Median household income | 70726 |
| Poverty rate | 10.85 |
| Homeownership rate | 77.54 |
| Unemployment rate | 3.96 |
| Median home value | 158400 |
| Gini index | 0.4407 |
| Vacancy rate | 16.97 |
| White | 3558 |
| Black | 21 |
| Asian | 27 |
| Native | 29 |
| Hispanic/Latino | 209 |
| Bachelor's or higher | 564 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 4](/us/states/sd/districts/senate/4.md) — 82% (state senate)
- [SD Senate District 22](/us/states/sd/districts/senate/22.md) — 18% (state senate)
- [SD House District 4](/us/states/sd/districts/house/4.md) — 82% (state house)
- [SD House District 22](/us/states/sd/districts/house/22.md) — 18% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
