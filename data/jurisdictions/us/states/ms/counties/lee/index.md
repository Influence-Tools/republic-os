---
type: Jurisdiction
title: "Lee County, MS"
classification: county
fips: "28081"
state: "MS"
demographics:
  population: 83034
  population_under_18: 20728
  population_18_64: 49176
  population_65_plus: 13130
  median_household_income: 67863
  poverty_rate: 14.55
  homeownership_rate: 70.78
  unemployment_rate: 5.06
  median_home_value: 199500
  gini_index: 0.4624
  vacancy_rate: 13.45
  race_white: 52273
  race_black: 24874
  race_asian: 823
  race_native: 148
  hispanic: 2933
  bachelors_plus: 21774
districts:
  - to: "us/states/ms/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ms/districts/senate/6"
    rel: in-district
    area_weight: 0.6847
  - to: "us/states/ms/districts/senate/7"
    rel: in-district
    area_weight: 0.3152
  - to: "us/states/ms/districts/house/19"
    rel: in-district
    area_weight: 0.4103
  - to: "us/states/ms/districts/house/18"
    rel: in-district
    area_weight: 0.297
  - to: "us/states/ms/districts/house/16"
    rel: in-district
    area_weight: 0.1512
  - to: "us/states/ms/districts/house/17"
    rel: in-district
    area_weight: 0.1415
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Lee County, MS

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 83034 |
| Under 18 | 20728 |
| 18–64 | 49176 |
| 65+ | 13130 |
| Median household income | 67863 |
| Poverty rate | 14.55 |
| Homeownership rate | 70.78 |
| Unemployment rate | 5.06 |
| Median home value | 199500 |
| Gini index | 0.4624 |
| Vacancy rate | 13.45 |
| White | 52273 |
| Black | 24874 |
| Asian | 823 |
| Native | 148 |
| Hispanic/Latino | 2933 |
| Bachelor's or higher | 21774 |

## Districts

- [MS-01](/us/states/ms/districts/01.md) — 100% (congressional)
- [MS Senate District 6](/us/states/ms/districts/senate/6.md) — 68% (state senate)
- [MS Senate District 7](/us/states/ms/districts/senate/7.md) — 32% (state senate)
- [MS House District 19](/us/states/ms/districts/house/19.md) — 41% (state house)
- [MS House District 18](/us/states/ms/districts/house/18.md) — 30% (state house)
- [MS House District 16](/us/states/ms/districts/house/16.md) — 15% (state house)
- [MS House District 17](/us/states/ms/districts/house/17.md) — 14% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
