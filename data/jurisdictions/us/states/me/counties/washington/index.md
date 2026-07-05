---
type: Jurisdiction
title: "Washington County, ME"
classification: county
fips: "23029"
state: "ME"
demographics:
  population: 31331
  population_under_18: 5809
  population_18_64: 17269
  population_65_plus: 8253
  median_household_income: 56024
  poverty_rate: 17.09
  homeownership_rate: 79.66
  unemployment_rate: 6.29
  median_home_value: 161800
  gini_index: 0.4594
  vacancy_rate: 34.7
  race_white: 27575
  race_black: 340
  race_asian: 107
  race_native: 1463
  hispanic: 796
  bachelors_plus: 7861
districts:
  - to: "us/states/me/districts/02"
    rel: in-district
    area_weight: 0.887
  - to: "us/states/me/districts/senate/6"
    rel: in-district
    area_weight: 0.8718
  - to: "us/states/me/districts/house/10"
    rel: in-district
    area_weight: 0.2779
  - to: "us/states/me/districts/house/8"
    rel: in-district
    area_weight: 0.1981
  - to: "us/states/me/districts/house/18"
    rel: in-district
    area_weight: 0.1912
  - to: "us/states/me/districts/house/11"
    rel: in-district
    area_weight: 0.1003
  - to: "us/states/me/districts/house/9"
    rel: in-district
    area_weight: 0.0901
  - to: "us/states/me/districts/house/12"
    rel: in-district
    area_weight: 0.0142
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, me]
timestamp: "2026-07-03"
---

# Washington County, ME

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 31331 |
| Under 18 | 5809 |
| 18–64 | 17269 |
| 65+ | 8253 |
| Median household income | 56024 |
| Poverty rate | 17.09 |
| Homeownership rate | 79.66 |
| Unemployment rate | 6.29 |
| Median home value | 161800 |
| Gini index | 0.4594 |
| Vacancy rate | 34.7 |
| White | 27575 |
| Black | 340 |
| Asian | 107 |
| Native | 1463 |
| Hispanic/Latino | 796 |
| Bachelor's or higher | 7861 |

## Districts

- [ME-02](/us/states/me/districts/02.md) — 89% (congressional)
- [ME Senate District 6](/us/states/me/districts/senate/6.md) — 87% (state senate)
- [ME House District 10](/us/states/me/districts/house/10.md) — 28% (state house)
- [ME House District 8](/us/states/me/districts/house/8.md) — 20% (state house)
- [ME House District 18](/us/states/me/districts/house/18.md) — 19% (state house)
- [ME House District 11](/us/states/me/districts/house/11.md) — 10% (state house)
- [ME House District 9](/us/states/me/districts/house/9.md) — 9% (state house)
- [ME House District 12](/us/states/me/districts/house/12.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
