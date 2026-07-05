---
type: Jurisdiction
title: "Ascension Parish, LA"
classification: county
fips: "22005"
state: "LA"
demographics:
  population: 130314
  population_under_18: 34379
  population_18_64: 79102
  population_65_plus: 16833
  median_household_income: 91549
  poverty_rate: 10.34
  homeownership_rate: 80.99
  unemployment_rate: 4.42
  median_home_value: 279600
  gini_index: 0.4207
  vacancy_rate: 8.25
  race_white: 83657
  race_black: 30108
  race_asian: 1453
  race_native: 361
  hispanic: 10961
  bachelors_plus: 33395
districts:
  - to: "us/states/la/districts/02"
    rel: in-district
    area_weight: 0.5545
  - to: "us/states/la/districts/01"
    rel: in-district
    area_weight: 0.3538
  - to: "us/states/la/districts/05"
    rel: in-district
    area_weight: 0.0916
  - to: "us/states/la/districts/senate/18"
    rel: in-district
    area_weight: 0.6682
  - to: "us/states/la/districts/senate/2"
    rel: in-district
    area_weight: 0.3316
  - to: "us/states/la/districts/house/81"
    rel: in-district
    area_weight: 0.3685
  - to: "us/states/la/districts/house/58"
    rel: in-district
    area_weight: 0.3471
  - to: "us/states/la/districts/house/88"
    rel: in-district
    area_weight: 0.1474
  - to: "us/states/la/districts/house/59"
    rel: in-district
    area_weight: 0.1367
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Ascension Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 130314 |
| Under 18 | 34379 |
| 18–64 | 79102 |
| 65+ | 16833 |
| Median household income | 91549 |
| Poverty rate | 10.34 |
| Homeownership rate | 80.99 |
| Unemployment rate | 4.42 |
| Median home value | 279600 |
| Gini index | 0.4207 |
| Vacancy rate | 8.25 |
| White | 83657 |
| Black | 30108 |
| Asian | 1453 |
| Native | 361 |
| Hispanic/Latino | 10961 |
| Bachelor's or higher | 33395 |

## Districts

- [LA-02](/us/states/la/districts/02.md) — 55% (congressional)
- [LA-01](/us/states/la/districts/01.md) — 35% (congressional)
- [LA-05](/us/states/la/districts/05.md) — 9% (congressional)
- [LA Senate District 18](/us/states/la/districts/senate/18.md) — 67% (state senate)
- [LA Senate District 2](/us/states/la/districts/senate/2.md) — 33% (state senate)
- [LA House District 81](/us/states/la/districts/house/81.md) — 37% (state house)
- [LA House District 58](/us/states/la/districts/house/58.md) — 35% (state house)
- [LA House District 88](/us/states/la/districts/house/88.md) — 15% (state house)
- [LA House District 59](/us/states/la/districts/house/59.md) — 14% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
