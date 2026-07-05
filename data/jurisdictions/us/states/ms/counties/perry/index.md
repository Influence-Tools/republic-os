---
type: Jurisdiction
title: "Perry County, MS"
classification: county
fips: "28111"
state: "MS"
demographics:
  population: 11449
  population_under_18: 2507
  population_18_64: 6708
  population_65_plus: 2234
  median_household_income: 49634
  poverty_rate: 18.38
  homeownership_rate: 81.54
  unemployment_rate: 1.99
  median_home_value: 124000
  gini_index: 0.4232
  vacancy_rate: 15.48
  race_white: 8873
  race_black: 1758
  race_asian: 239
  race_native: 5
  hispanic: 216
  bachelors_plus: 1451
districts:
  - to: "us/states/ms/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ms/districts/senate/45"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ms/districts/house/105"
    rel: in-district
    area_weight: 0.8808
  - to: "us/states/ms/districts/house/86"
    rel: in-district
    area_weight: 0.119
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Perry County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11449 |
| Under 18 | 2507 |
| 18–64 | 6708 |
| 65+ | 2234 |
| Median household income | 49634 |
| Poverty rate | 18.38 |
| Homeownership rate | 81.54 |
| Unemployment rate | 1.99 |
| Median home value | 124000 |
| Gini index | 0.4232 |
| Vacancy rate | 15.48 |
| White | 8873 |
| Black | 1758 |
| Asian | 239 |
| Native | 5 |
| Hispanic/Latino | 216 |
| Bachelor's or higher | 1451 |

## Districts

- [MS-04](/us/states/ms/districts/04.md) — 100% (congressional)
- [MS Senate District 45](/us/states/ms/districts/senate/45.md) — 100% (state senate)
- [MS House District 105](/us/states/ms/districts/house/105.md) — 88% (state house)
- [MS House District 86](/us/states/ms/districts/house/86.md) — 12% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
