---
type: Jurisdiction
title: "Cedar County, MO"
classification: county
fips: "29039"
state: "MO"
demographics:
  population: 14615
  population_under_18: 3510
  population_18_64: 7725
  population_65_plus: 3380
  median_household_income: 48181
  poverty_rate: 16.98
  homeownership_rate: 74.09
  unemployment_rate: 2.58
  median_home_value: 168100
  gini_index: 0.495
  vacancy_rate: 16.89
  race_white: 13588
  race_black: 72
  race_asian: 4
  race_native: 49
  hispanic: 320
  bachelors_plus: 2636
districts:
  - to: "us/states/mo/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/28"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/125"
    rel: in-district
    area_weight: 0.59
  - to: "us/states/mo/districts/house/127"
    rel: in-district
    area_weight: 0.4099
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Cedar County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14615 |
| Under 18 | 3510 |
| 18–64 | 7725 |
| 65+ | 3380 |
| Median household income | 48181 |
| Poverty rate | 16.98 |
| Homeownership rate | 74.09 |
| Unemployment rate | 2.58 |
| Median home value | 168100 |
| Gini index | 0.495 |
| Vacancy rate | 16.89 |
| White | 13588 |
| Black | 72 |
| Asian | 4 |
| Native | 49 |
| Hispanic/Latino | 320 |
| Bachelor's or higher | 2636 |

## Districts

- [MO-04](/us/states/mo/districts/04.md) — 100% (congressional)
- [MO Senate District 28](/us/states/mo/districts/senate/28.md) — 100% (state senate)
- [MO House District 125](/us/states/mo/districts/house/125.md) — 59% (state house)
- [MO House District 127](/us/states/mo/districts/house/127.md) — 41% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
