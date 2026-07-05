---
type: Jurisdiction
title: "Bolivar County, MS"
classification: county
fips: "28011"
state: "MS"
demographics:
  population: 29534
  population_under_18: 7273
  population_18_64: 17205
  population_65_plus: 5056
  median_household_income: 39585
  poverty_rate: 32.63
  homeownership_rate: 62.64
  unemployment_rate: 7.11
  median_home_value: 130000
  gini_index: 0.5399
  vacancy_rate: 12.86
  race_white: 9162
  race_black: 18674
  race_asian: 282
  race_native: 12
  hispanic: 787
  bachelors_plus: 7780
districts:
  - to: "us/states/ms/districts/02"
    rel: in-district
    area_weight: 0.9983
  - to: "us/states/ms/districts/senate/12"
    rel: in-district
    area_weight: 0.7413
  - to: "us/states/ms/districts/senate/13"
    rel: in-district
    area_weight: 0.2582
  - to: "us/states/ms/districts/house/29"
    rel: in-district
    area_weight: 0.6493
  - to: "us/states/ms/districts/house/50"
    rel: in-district
    area_weight: 0.2052
  - to: "us/states/ms/districts/house/26"
    rel: in-district
    area_weight: 0.0872
  - to: "us/states/ms/districts/house/31"
    rel: in-district
    area_weight: 0.0578
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Bolivar County, MS

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 29534 |
| Under 18 | 7273 |
| 18–64 | 17205 |
| 65+ | 5056 |
| Median household income | 39585 |
| Poverty rate | 32.63 |
| Homeownership rate | 62.64 |
| Unemployment rate | 7.11 |
| Median home value | 130000 |
| Gini index | 0.5399 |
| Vacancy rate | 12.86 |
| White | 9162 |
| Black | 18674 |
| Asian | 282 |
| Native | 12 |
| Hispanic/Latino | 787 |
| Bachelor's or higher | 7780 |

## Districts

- [MS-02](/us/states/ms/districts/02.md) — 100% (congressional)
- [MS Senate District 12](/us/states/ms/districts/senate/12.md) — 74% (state senate)
- [MS Senate District 13](/us/states/ms/districts/senate/13.md) — 26% (state senate)
- [MS House District 29](/us/states/ms/districts/house/29.md) — 65% (state house)
- [MS House District 50](/us/states/ms/districts/house/50.md) — 21% (state house)
- [MS House District 26](/us/states/ms/districts/house/26.md) — 9% (state house)
- [MS House District 31](/us/states/ms/districts/house/31.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
