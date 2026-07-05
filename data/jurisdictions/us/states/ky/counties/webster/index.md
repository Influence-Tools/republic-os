---
type: Jurisdiction
title: "Webster County, KY"
classification: county
fips: "21233"
state: "KY"
demographics:
  population: 12842
  population_under_18: 3084
  population_18_64: 7435
  population_65_plus: 2323
  median_household_income: 59628
  poverty_rate: 13.52
  homeownership_rate: 73.78
  unemployment_rate: 4.11
  median_home_value: 112900
  gini_index: 0.4116
  vacancy_rate: 13.98
  race_white: 11337
  race_black: 522
  race_asian: 4
  race_native: 13
  hispanic: 912
  bachelors_plus: 1568
districts:
  - to: "us/states/ky/districts/01"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/ky/districts/senate/4"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ky/districts/house/12"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Webster County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12842 |
| Under 18 | 3084 |
| 18–64 | 7435 |
| 65+ | 2323 |
| Median household income | 59628 |
| Poverty rate | 13.52 |
| Homeownership rate | 73.78 |
| Unemployment rate | 4.11 |
| Median home value | 112900 |
| Gini index | 0.4116 |
| Vacancy rate | 13.98 |
| White | 11337 |
| Black | 522 |
| Asian | 4 |
| Native | 13 |
| Hispanic/Latino | 912 |
| Bachelor's or higher | 1568 |

## Districts

- [KY-01](/us/states/ky/districts/01.md) — 100% (congressional)
- [KY Senate District 4](/us/states/ky/districts/senate/4.md) — 100% (state senate)
- [KY House District 12](/us/states/ky/districts/house/12.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
