---
type: Jurisdiction
title: "Clay County, SD"
classification: county
fips: "46027"
state: "SD"
demographics:
  population: 15219
  population_under_18: 2645
  population_18_64: 10718
  population_65_plus: 1856
  median_household_income: 56850
  poverty_rate: 19.73
  homeownership_rate: 50.82
  unemployment_rate: 6.99
  median_home_value: 232300
  gini_index: 0.4801
  vacancy_rate: 11.42
  race_white: 12933
  race_black: 278
  race_asian: 452
  race_native: 574
  hispanic: 504
  bachelors_plus: 4977
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/sd/districts/senate/17"
    rel: in-district
    area_weight: 0.8275
  - to: "us/states/sd/districts/senate/18"
    rel: in-district
    area_weight: 0.1722
  - to: "us/states/sd/districts/house/17"
    rel: in-district
    area_weight: 0.8275
  - to: "us/states/sd/districts/house/18"
    rel: in-district
    area_weight: 0.1722
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Clay County, SD

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15219 |
| Under 18 | 2645 |
| 18–64 | 10718 |
| 65+ | 1856 |
| Median household income | 56850 |
| Poverty rate | 19.73 |
| Homeownership rate | 50.82 |
| Unemployment rate | 6.99 |
| Median home value | 232300 |
| Gini index | 0.4801 |
| Vacancy rate | 11.42 |
| White | 12933 |
| Black | 278 |
| Asian | 452 |
| Native | 574 |
| Hispanic/Latino | 504 |
| Bachelor's or higher | 4977 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 17](/us/states/sd/districts/senate/17.md) — 83% (state senate)
- [SD Senate District 18](/us/states/sd/districts/senate/18.md) — 17% (state senate)
- [SD House District 17](/us/states/sd/districts/house/17.md) — 83% (state house)
- [SD House District 18](/us/states/sd/districts/house/18.md) — 17% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
