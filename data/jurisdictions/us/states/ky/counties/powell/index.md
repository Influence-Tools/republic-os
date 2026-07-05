---
type: Jurisdiction
title: "Powell County, KY"
classification: county
fips: "21197"
state: "KY"
demographics:
  population: 13038
  population_under_18: 3230
  population_18_64: 7695
  population_65_plus: 2113
  median_household_income: 40309
  poverty_rate: 22.48
  homeownership_rate: 68.25
  unemployment_rate: 5.77
  median_home_value: 141100
  gini_index: 0.4672
  vacancy_rate: 15.18
  race_white: 12345
  race_black: 264
  race_asian: 0
  race_native: 19
  hispanic: 214
  bachelors_plus: 1706
districts:
  - to: "us/states/ky/districts/06"
    rel: in-district
    area_weight: 0.9978
  - to: "us/states/ky/districts/senate/30"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/ky/districts/house/91"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Powell County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13038 |
| Under 18 | 3230 |
| 18–64 | 7695 |
| 65+ | 2113 |
| Median household income | 40309 |
| Poverty rate | 22.48 |
| Homeownership rate | 68.25 |
| Unemployment rate | 5.77 |
| Median home value | 141100 |
| Gini index | 0.4672 |
| Vacancy rate | 15.18 |
| White | 12345 |
| Black | 264 |
| Asian | 0 |
| Native | 19 |
| Hispanic/Latino | 214 |
| Bachelor's or higher | 1706 |

## Districts

- [KY-06](/us/states/ky/districts/06.md) — 100% (congressional)
- [KY Senate District 30](/us/states/ky/districts/senate/30.md) — 100% (state senate)
- [KY House District 91](/us/states/ky/districts/house/91.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
