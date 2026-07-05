---
type: Jurisdiction
title: "Cabarrus County, NC"
classification: county
fips: "37025"
state: "NC"
demographics:
  population: 236133
  population_under_18: 59433
  population_18_64: 144662
  population_65_plus: 32038
  median_household_income: 89005
  poverty_rate: 9.27
  homeownership_rate: 71.17
  unemployment_rate: 4.64
  median_home_value: 354800
  gini_index: 0.4423
  vacancy_rate: 10.08
  race_white: 139597
  race_black: 45644
  race_asian: 14549
  race_native: 437
  hispanic: 30081
  bachelors_plus: 81556
districts:
  - to: "us/states/nc/districts/08"
    rel: in-district
    area_weight: 0.7733
  - to: "us/states/nc/districts/06"
    rel: in-district
    area_weight: 0.2262
  - to: "us/states/nc/districts/senate/34"
    rel: in-district
    area_weight: 0.9394
  - to: "us/states/nc/districts/senate/35"
    rel: in-district
    area_weight: 0.0605
  - to: "us/states/nc/districts/house/82"
    rel: in-district
    area_weight: 0.4738
  - to: "us/states/nc/districts/house/73"
    rel: in-district
    area_weight: 0.4027
  - to: "us/states/nc/districts/house/83"
    rel: in-district
    area_weight: 0.1234
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Cabarrus County, NC

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 236133 |
| Under 18 | 59433 |
| 18–64 | 144662 |
| 65+ | 32038 |
| Median household income | 89005 |
| Poverty rate | 9.27 |
| Homeownership rate | 71.17 |
| Unemployment rate | 4.64 |
| Median home value | 354800 |
| Gini index | 0.4423 |
| Vacancy rate | 10.08 |
| White | 139597 |
| Black | 45644 |
| Asian | 14549 |
| Native | 437 |
| Hispanic/Latino | 30081 |
| Bachelor's or higher | 81556 |

## Districts

- [NC-08](/us/states/nc/districts/08.md) — 77% (congressional)
- [NC-06](/us/states/nc/districts/06.md) — 23% (congressional)
- [NC Senate District 34](/us/states/nc/districts/senate/34.md) — 94% (state senate)
- [NC Senate District 35](/us/states/nc/districts/senate/35.md) — 6% (state senate)
- [NC House District 82](/us/states/nc/districts/house/82.md) — 47% (state house)
- [NC House District 73](/us/states/nc/districts/house/73.md) — 40% (state house)
- [NC House District 83](/us/states/nc/districts/house/83.md) — 12% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
