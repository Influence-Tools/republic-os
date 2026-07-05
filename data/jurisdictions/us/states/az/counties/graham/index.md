---
type: Jurisdiction
title: "Graham County, AZ"
classification: county
fips: "04009"
state: "AZ"
demographics:
  population: 39232
  population_under_18: 10124
  population_18_64: 23421
  population_65_plus: 5687
  median_household_income: 67325
  poverty_rate: 17.26
  homeownership_rate: 73.14
  unemployment_rate: 7.7
  median_home_value: 212000
  gini_index: 0.4221
  vacancy_rate: 9.74
  race_white: 24317
  race_black: 641
  race_asian: 225
  race_native: 3505
  hispanic: 12075
  bachelors_plus: 4853
districts:
  - to: "us/states/az/districts/06"
    rel: in-district
    area_weight: 0.6326
  - to: "us/states/az/districts/02"
    rel: in-district
    area_weight: 0.3674
  - to: "us/states/az/districts/senate/19"
    rel: in-district
    area_weight: 0.633
  - to: "us/states/az/districts/senate/6"
    rel: in-district
    area_weight: 0.367
  - to: "us/states/az/districts/house/19"
    rel: in-district
    area_weight: 0.633
  - to: "us/states/az/districts/house/6"
    rel: in-district
    area_weight: 0.367
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, az]
timestamp: "2026-07-03"
---

# Graham County, AZ

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 39232 |
| Under 18 | 10124 |
| 18–64 | 23421 |
| 65+ | 5687 |
| Median household income | 67325 |
| Poverty rate | 17.26 |
| Homeownership rate | 73.14 |
| Unemployment rate | 7.7 |
| Median home value | 212000 |
| Gini index | 0.4221 |
| Vacancy rate | 9.74 |
| White | 24317 |
| Black | 641 |
| Asian | 225 |
| Native | 3505 |
| Hispanic/Latino | 12075 |
| Bachelor's or higher | 4853 |

## Districts

- [AZ-06](/us/states/az/districts/06.md) — 63% (congressional)
- [AZ-02](/us/states/az/districts/02.md) — 37% (congressional)
- [AZ Senate District 19](/us/states/az/districts/senate/19.md) — 63% (state senate)
- [AZ Senate District 6](/us/states/az/districts/senate/6.md) — 37% (state senate)
- [AZ House District 19](/us/states/az/districts/house/19.md) — 63% (state house)
- [AZ House District 6](/us/states/az/districts/house/6.md) — 37% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
