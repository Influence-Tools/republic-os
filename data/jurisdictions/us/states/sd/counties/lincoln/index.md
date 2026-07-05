---
type: Jurisdiction
title: "Lincoln County, SD"
classification: county
fips: "46083"
state: "SD"
demographics:
  population: 70638
  population_under_18: 20222
  population_18_64: 24562
  population_65_plus: 25854
  median_household_income: 99166
  poverty_rate: 5.58
  homeownership_rate: 71.24
  unemployment_rate: 1.68
  median_home_value: 348300
  gini_index: 0.4381
  vacancy_rate: 2.89
  race_white: 63223
  race_black: 1691
  race_asian: 1230
  race_native: 361
  hispanic: 2226
  bachelors_plus: 27417
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 0.9988
  - to: "us/states/sd/districts/senate/16"
    rel: in-district
    area_weight: 0.7995
  - to: "us/states/sd/districts/senate/6"
    rel: in-district
    area_weight: 0.1794
  - to: "us/states/sd/districts/senate/13"
    rel: in-district
    area_weight: 0.0119
  - to: "us/states/sd/districts/senate/12"
    rel: in-district
    area_weight: 0.0081
  - to: "us/states/sd/districts/house/16"
    rel: in-district
    area_weight: 0.7995
  - to: "us/states/sd/districts/house/6"
    rel: in-district
    area_weight: 0.1794
  - to: "us/states/sd/districts/house/13"
    rel: in-district
    area_weight: 0.0119
  - to: "us/states/sd/districts/house/12"
    rel: in-district
    area_weight: 0.0081
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Lincoln County, SD

County jurisdiction — 4 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 70638 |
| Under 18 | 20222 |
| 18–64 | 24562 |
| 65+ | 25854 |
| Median household income | 99166 |
| Poverty rate | 5.58 |
| Homeownership rate | 71.24 |
| Unemployment rate | 1.68 |
| Median home value | 348300 |
| Gini index | 0.4381 |
| Vacancy rate | 2.89 |
| White | 63223 |
| Black | 1691 |
| Asian | 1230 |
| Native | 361 |
| Hispanic/Latino | 2226 |
| Bachelor's or higher | 27417 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 16](/us/states/sd/districts/senate/16.md) — 80% (state senate)
- [SD Senate District 6](/us/states/sd/districts/senate/6.md) — 18% (state senate)
- [SD Senate District 13](/us/states/sd/districts/senate/13.md) — 1% (state senate)
- [SD Senate District 12](/us/states/sd/districts/senate/12.md) — 1% (state senate)
- [SD House District 16](/us/states/sd/districts/house/16.md) — 80% (state house)
- [SD House District 6](/us/states/sd/districts/house/6.md) — 18% (state house)
- [SD House District 13](/us/states/sd/districts/house/13.md) — 1% (state house)
- [SD House District 12](/us/states/sd/districts/house/12.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
