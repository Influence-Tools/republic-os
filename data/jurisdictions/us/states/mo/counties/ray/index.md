---
type: Jurisdiction
title: "Ray County, MO"
classification: county
fips: "29177"
state: "MO"
demographics:
  population: 23145
  population_under_18: 5271
  population_18_64: 13406
  population_65_plus: 4468
  median_household_income: 74573
  poverty_rate: 12.56
  homeownership_rate: 77.26
  unemployment_rate: 3.43
  median_home_value: 198800
  gini_index: 0.4368
  vacancy_rate: 8.21
  race_white: 21423
  race_black: 182
  race_asian: 76
  race_native: 317
  hispanic: 667
  bachelors_plus: 3415
districts:
  - to: "us/states/mo/districts/06"
    rel: in-district
    area_weight: 0.9982
  - to: "us/states/mo/districts/senate/21"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/house/53"
    rel: in-district
    area_weight: 0.5517
  - to: "us/states/mo/districts/house/7"
    rel: in-district
    area_weight: 0.4481
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Ray County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 23145 |
| Under 18 | 5271 |
| 18–64 | 13406 |
| 65+ | 4468 |
| Median household income | 74573 |
| Poverty rate | 12.56 |
| Homeownership rate | 77.26 |
| Unemployment rate | 3.43 |
| Median home value | 198800 |
| Gini index | 0.4368 |
| Vacancy rate | 8.21 |
| White | 21423 |
| Black | 182 |
| Asian | 76 |
| Native | 317 |
| Hispanic/Latino | 667 |
| Bachelor's or higher | 3415 |

## Districts

- [MO-06](/us/states/mo/districts/06.md) — 100% (congressional)
- [MO Senate District 21](/us/states/mo/districts/senate/21.md) — 100% (state senate)
- [MO House District 53](/us/states/mo/districts/house/53.md) — 55% (state house)
- [MO House District 7](/us/states/mo/districts/house/7.md) — 45% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
