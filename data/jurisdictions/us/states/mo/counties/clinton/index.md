---
type: Jurisdiction
title: "Clinton County, MO"
classification: county
fips: "29049"
state: "MO"
demographics:
  population: 21414
  population_under_18: 4963
  population_18_64: 12402
  population_65_plus: 4049
  median_household_income: 70627
  poverty_rate: 12.3
  homeownership_rate: 75.75
  unemployment_rate: 2.97
  median_home_value: 226800
  gini_index: 0.4366
  vacancy_rate: 8.24
  race_white: 19862
  race_black: 178
  race_asian: 35
  race_native: 25
  hispanic: 567
  bachelors_plus: 4467
districts:
  - to: "us/states/mo/districts/06"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/12"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/9"
    rel: in-district
    area_weight: 0.5527
  - to: "us/states/mo/districts/house/8"
    rel: in-district
    area_weight: 0.4472
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Clinton County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21414 |
| Under 18 | 4963 |
| 18–64 | 12402 |
| 65+ | 4049 |
| Median household income | 70627 |
| Poverty rate | 12.3 |
| Homeownership rate | 75.75 |
| Unemployment rate | 2.97 |
| Median home value | 226800 |
| Gini index | 0.4366 |
| Vacancy rate | 8.24 |
| White | 19862 |
| Black | 178 |
| Asian | 35 |
| Native | 25 |
| Hispanic/Latino | 567 |
| Bachelor's or higher | 4467 |

## Districts

- [MO-06](/us/states/mo/districts/06.md) — 100% (congressional)
- [MO Senate District 12](/us/states/mo/districts/senate/12.md) — 100% (state senate)
- [MO House District 9](/us/states/mo/districts/house/9.md) — 55% (state house)
- [MO House District 8](/us/states/mo/districts/house/8.md) — 45% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
