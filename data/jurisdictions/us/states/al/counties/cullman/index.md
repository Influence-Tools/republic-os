---
type: Jurisdiction
title: "Cullman County, AL"
classification: county
fips: "01043"
state: "AL"
demographics:
  population: 90566
  population_under_18: 20313
  population_18_64: 53019
  population_65_plus: 17234
  median_household_income: 62656
  poverty_rate: 15.31
  homeownership_rate: 76.63
  unemployment_rate: 3.77
  median_home_value: 199100
  gini_index: 0.4536
  vacancy_rate: 11.35
  race_white: 82079
  race_black: 882
  race_asian: 498
  race_native: 341
  hispanic: 4563
  bachelors_plus: 16645
districts:
  - to: "us/states/al/districts/04"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/al/districts/senate/4"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/al/districts/house/12"
    rel: in-district
    area_weight: 0.5538
  - to: "us/states/al/districts/house/11"
    rel: in-district
    area_weight: 0.3547
  - to: "us/states/al/districts/house/14"
    rel: in-district
    area_weight: 0.0914
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Cullman County, AL

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 90566 |
| Under 18 | 20313 |
| 18–64 | 53019 |
| 65+ | 17234 |
| Median household income | 62656 |
| Poverty rate | 15.31 |
| Homeownership rate | 76.63 |
| Unemployment rate | 3.77 |
| Median home value | 199100 |
| Gini index | 0.4536 |
| Vacancy rate | 11.35 |
| White | 82079 |
| Black | 882 |
| Asian | 498 |
| Native | 341 |
| Hispanic/Latino | 4563 |
| Bachelor's or higher | 16645 |

## Districts

- [AL-04](/us/states/al/districts/04.md) — 100% (congressional)
- [AL Senate District 4](/us/states/al/districts/senate/4.md) — 100% (state senate)
- [AL House District 12](/us/states/al/districts/house/12.md) — 55% (state house)
- [AL House District 11](/us/states/al/districts/house/11.md) — 35% (state house)
- [AL House District 14](/us/states/al/districts/house/14.md) — 9% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
