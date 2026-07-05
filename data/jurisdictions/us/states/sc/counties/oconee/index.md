---
type: Jurisdiction
title: "Oconee County, SC"
classification: county
fips: "45073"
state: "SC"
demographics:
  population: 80469
  population_under_18: 15374
  population_18_64: 45080
  population_65_plus: 20015
  median_household_income: 62388
  poverty_rate: 17.57
  homeownership_rate: 76.21
  unemployment_rate: 5.88
  median_home_value: 237100
  gini_index: 0.4947
  vacancy_rate: 18.02
  race_white: 67741
  race_black: 4291
  race_asian: 575
  race_native: 358
  hispanic: 5022
  bachelors_plus: 23640
districts:
  - to: "us/states/sc/districts/03"
    rel: in-district
    area_weight: 0.9969
  - to: "us/states/sc/districts/senate/1"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/sc/districts/house/1"
    rel: in-district
    area_weight: 0.7273
  - to: "us/states/sc/districts/house/2"
    rel: in-district
    area_weight: 0.272
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Oconee County, SC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 80469 |
| Under 18 | 15374 |
| 18–64 | 45080 |
| 65+ | 20015 |
| Median household income | 62388 |
| Poverty rate | 17.57 |
| Homeownership rate | 76.21 |
| Unemployment rate | 5.88 |
| Median home value | 237100 |
| Gini index | 0.4947 |
| Vacancy rate | 18.02 |
| White | 67741 |
| Black | 4291 |
| Asian | 575 |
| Native | 358 |
| Hispanic/Latino | 5022 |
| Bachelor's or higher | 23640 |

## Districts

- [SC-03](/us/states/sc/districts/03.md) — 100% (congressional)
- [SC Senate District 1](/us/states/sc/districts/senate/1.md) — 100% (state senate)
- [SC House District 1](/us/states/sc/districts/house/1.md) — 73% (state house)
- [SC House District 2](/us/states/sc/districts/house/2.md) — 27% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
