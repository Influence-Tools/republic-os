---
type: Jurisdiction
title: "Franklin County, KS"
classification: county
fips: "20059"
state: "KS"
demographics:
  population: 26106
  population_under_18: 6031
  population_18_64: 15397
  population_65_plus: 4678
  median_household_income: 77207
  poverty_rate: 8.67
  homeownership_rate: 72.23
  unemployment_rate: 2.98
  median_home_value: 198700
  gini_index: 0.3755
  vacancy_rate: 7.97
  race_white: 23647
  race_black: 279
  race_asian: 160
  race_native: 161
  hispanic: 1264
  bachelors_plus: 5947
districts:
  - to: "us/states/ks/districts/03"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ks/districts/senate/12"
    rel: in-district
    area_weight: 0.5407
  - to: "us/states/ks/districts/senate/3"
    rel: in-district
    area_weight: 0.4593
  - to: "us/states/ks/districts/house/59"
    rel: in-district
    area_weight: 0.9382
  - to: "us/states/ks/districts/house/5"
    rel: in-district
    area_weight: 0.0617
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Franklin County, KS

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 26106 |
| Under 18 | 6031 |
| 18–64 | 15397 |
| 65+ | 4678 |
| Median household income | 77207 |
| Poverty rate | 8.67 |
| Homeownership rate | 72.23 |
| Unemployment rate | 2.98 |
| Median home value | 198700 |
| Gini index | 0.3755 |
| Vacancy rate | 7.97 |
| White | 23647 |
| Black | 279 |
| Asian | 160 |
| Native | 161 |
| Hispanic/Latino | 1264 |
| Bachelor's or higher | 5947 |

## Districts

- [KS-03](/us/states/ks/districts/03.md) — 100% (congressional)
- [KS Senate District 12](/us/states/ks/districts/senate/12.md) — 54% (state senate)
- [KS Senate District 3](/us/states/ks/districts/senate/3.md) — 46% (state senate)
- [KS House District 59](/us/states/ks/districts/house/59.md) — 94% (state house)
- [KS House District 5](/us/states/ks/districts/house/5.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
