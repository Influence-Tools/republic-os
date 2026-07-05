---
type: Jurisdiction
title: "Lafourche Parish, LA"
classification: county
fips: "22057"
state: "LA"
demographics:
  population: 96252
  population_under_18: 22001
  population_18_64: 58319
  population_65_plus: 15932
  median_household_income: 63135
  poverty_rate: 16.97
  homeownership_rate: 79.88
  unemployment_rate: 4.15
  median_home_value: 193900
  gini_index: 0.4619
  vacancy_rate: 8.89
  race_white: 72295
  race_black: 12330
  race_asian: 568
  race_native: 2675
  hispanic: 5678
  bachelors_plus: 18459
districts:
  - to: "us/states/la/districts/01"
    rel: in-district
    area_weight: 0.6613
  - to: "us/states/la/districts/03"
    rel: in-district
    area_weight: 0.1853
  - to: "us/states/la/districts/02"
    rel: in-district
    area_weight: 0.0219
  - to: "us/states/la/districts/senate/20"
    rel: in-district
    area_weight: 0.5552
  - to: "us/states/la/districts/senate/19"
    rel: in-district
    area_weight: 0.2328
  - to: "us/states/la/districts/senate/21"
    rel: in-district
    area_weight: 0.0371
  - to: "us/states/la/districts/senate/2"
    rel: in-district
    area_weight: 0.0203
  - to: "us/states/la/districts/house/54"
    rel: in-district
    area_weight: 0.6245
  - to: "us/states/la/districts/house/55"
    rel: in-district
    area_weight: 0.1793
  - to: "us/states/la/districts/house/51"
    rel: in-district
    area_weight: 0.0415
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Lafourche Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 96252 |
| Under 18 | 22001 |
| 18–64 | 58319 |
| 65+ | 15932 |
| Median household income | 63135 |
| Poverty rate | 16.97 |
| Homeownership rate | 79.88 |
| Unemployment rate | 4.15 |
| Median home value | 193900 |
| Gini index | 0.4619 |
| Vacancy rate | 8.89 |
| White | 72295 |
| Black | 12330 |
| Asian | 568 |
| Native | 2675 |
| Hispanic/Latino | 5678 |
| Bachelor's or higher | 18459 |

## Districts

- [LA-01](/us/states/la/districts/01.md) — 66% (congressional)
- [LA-03](/us/states/la/districts/03.md) — 19% (congressional)
- [LA-02](/us/states/la/districts/02.md) — 2% (congressional)
- [LA Senate District 20](/us/states/la/districts/senate/20.md) — 56% (state senate)
- [LA Senate District 19](/us/states/la/districts/senate/19.md) — 23% (state senate)
- [LA Senate District 21](/us/states/la/districts/senate/21.md) — 4% (state senate)
- [LA Senate District 2](/us/states/la/districts/senate/2.md) — 2% (state senate)
- [LA House District 54](/us/states/la/districts/house/54.md) — 62% (state house)
- [LA House District 55](/us/states/la/districts/house/55.md) — 18% (state house)
- [LA House District 51](/us/states/la/districts/house/51.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
