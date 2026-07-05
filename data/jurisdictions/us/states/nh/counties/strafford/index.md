---
type: Jurisdiction
title: "Strafford County, NH"
classification: county
fips: "33017"
state: "NH"
demographics:
  population: 132575
  population_under_18: 23399
  population_18_64: 86524
  population_65_plus: 22652
  median_household_income: 88570
  poverty_rate: 8.66
  homeownership_rate: 67.11
  unemployment_rate: 3.54
  median_home_value: 362800
  gini_index: 0.4273
  vacancy_rate: 8.0
  race_white: 116964
  race_black: 1534
  race_asian: 3618
  race_native: 34
  hispanic: 4248
  bachelors_plus: 48215
districts:
  - to: "us/states/nh/districts/01"
    rel: in-district
    area_weight: 0.9985
  - to: "us/states/nh/districts/senate/6"
    rel: in-district
    area_weight: 0.4636
  - to: "us/states/nh/districts/senate/4"
    rel: in-district
    area_weight: 0.2481
  - to: "us/states/nh/districts/senate/21"
    rel: in-district
    area_weight: 0.149
  - to: "us/states/nh/districts/senate/3"
    rel: in-district
    area_weight: 0.138
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nh]
timestamp: "2026-07-03"
---

# Strafford County, NH

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 132575 |
| Under 18 | 23399 |
| 18–64 | 86524 |
| 65+ | 22652 |
| Median household income | 88570 |
| Poverty rate | 8.66 |
| Homeownership rate | 67.11 |
| Unemployment rate | 3.54 |
| Median home value | 362800 |
| Gini index | 0.4273 |
| Vacancy rate | 8.0 |
| White | 116964 |
| Black | 1534 |
| Asian | 3618 |
| Native | 34 |
| Hispanic/Latino | 4248 |
| Bachelor's or higher | 48215 |

## Districts

- [NH-01](/us/states/nh/districts/01.md) — 100% (congressional)
- [NH Senate District 6](/us/states/nh/districts/senate/6.md) — 46% (state senate)
- [NH Senate District 4](/us/states/nh/districts/senate/4.md) — 25% (state senate)
- [NH Senate District 21](/us/states/nh/districts/senate/21.md) — 15% (state senate)
- [NH Senate District 3](/us/states/nh/districts/senate/3.md) — 14% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
