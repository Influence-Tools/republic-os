---
type: Jurisdiction
title: "Washington County, MO"
classification: county
fips: "29221"
state: "MO"
demographics:
  population: 23470
  population_under_18: 5526
  population_18_64: 13736
  population_65_plus: 4208
  median_household_income: 56043
  poverty_rate: 17.38
  homeownership_rate: 78.41
  unemployment_rate: 3.64
  median_home_value: 129400
  gini_index: 0.4767
  vacancy_rate: 16.9
  race_white: 21617
  race_black: 416
  race_asian: 31
  race_native: 6
  hispanic: 266
  bachelors_plus: 2558
districts:
  - to: "us/states/mo/districts/03"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/senate/3"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/house/144"
    rel: in-district
    area_weight: 0.7532
  - to: "us/states/mo/districts/house/118"
    rel: in-district
    area_weight: 0.2466
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Washington County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 23470 |
| Under 18 | 5526 |
| 18–64 | 13736 |
| 65+ | 4208 |
| Median household income | 56043 |
| Poverty rate | 17.38 |
| Homeownership rate | 78.41 |
| Unemployment rate | 3.64 |
| Median home value | 129400 |
| Gini index | 0.4767 |
| Vacancy rate | 16.9 |
| White | 21617 |
| Black | 416 |
| Asian | 31 |
| Native | 6 |
| Hispanic/Latino | 266 |
| Bachelor's or higher | 2558 |

## Districts

- [MO-03](/us/states/mo/districts/03.md) — 100% (congressional)
- [MO Senate District 3](/us/states/mo/districts/senate/3.md) — 100% (state senate)
- [MO House District 144](/us/states/mo/districts/house/144.md) — 75% (state house)
- [MO House District 118](/us/states/mo/districts/house/118.md) — 25% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
