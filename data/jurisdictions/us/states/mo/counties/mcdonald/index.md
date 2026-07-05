---
type: Jurisdiction
title: "McDonald County, MO"
classification: county
fips: "29119"
state: "MO"
demographics:
  population: 23701
  population_under_18: 6037
  population_18_64: 13977
  population_65_plus: 3687
  median_household_income: 52375
  poverty_rate: 16.78
  homeownership_rate: 67.34
  unemployment_rate: 6.82
  median_home_value: 154700
  gini_index: 0.4291
  vacancy_rate: 12.92
  race_white: 16618
  race_black: 466
  race_asian: 320
  race_native: 355
  hispanic: 2949
  bachelors_plus: 2494
districts:
  - to: "us/states/mo/districts/07"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/senate/29"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/mo/districts/house/159"
    rel: in-district
    area_weight: 0.7159
  - to: "us/states/mo/districts/house/158"
    rel: in-district
    area_weight: 0.2839
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# McDonald County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 23701 |
| Under 18 | 6037 |
| 18–64 | 13977 |
| 65+ | 3687 |
| Median household income | 52375 |
| Poverty rate | 16.78 |
| Homeownership rate | 67.34 |
| Unemployment rate | 6.82 |
| Median home value | 154700 |
| Gini index | 0.4291 |
| Vacancy rate | 12.92 |
| White | 16618 |
| Black | 466 |
| Asian | 320 |
| Native | 355 |
| Hispanic/Latino | 2949 |
| Bachelor's or higher | 2494 |

## Districts

- [MO-07](/us/states/mo/districts/07.md) — 100% (congressional)
- [MO Senate District 29](/us/states/mo/districts/senate/29.md) — 100% (state senate)
- [MO House District 159](/us/states/mo/districts/house/159.md) — 72% (state house)
- [MO House District 158](/us/states/mo/districts/house/158.md) — 28% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
