---
type: Jurisdiction
title: "Marion County, MO"
classification: county
fips: "29127"
state: "MO"
demographics:
  population: 28457
  population_under_18: 6834
  population_18_64: 16217
  population_65_plus: 5406
  median_household_income: 62903
  poverty_rate: 14.21
  homeownership_rate: 69.3
  unemployment_rate: 3.79
  median_home_value: 162000
  gini_index: 0.4157
  vacancy_rate: 12.34
  race_white: 25370
  race_black: 1192
  race_asian: 228
  race_native: 68
  hispanic: 582
  bachelors_plus: 6618
districts:
  - to: "us/states/mo/districts/06"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/mo/districts/senate/18"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/mo/districts/house/5"
    rel: in-district
    area_weight: 0.9992
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Marion County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 28457 |
| Under 18 | 6834 |
| 18–64 | 16217 |
| 65+ | 5406 |
| Median household income | 62903 |
| Poverty rate | 14.21 |
| Homeownership rate | 69.3 |
| Unemployment rate | 3.79 |
| Median home value | 162000 |
| Gini index | 0.4157 |
| Vacancy rate | 12.34 |
| White | 25370 |
| Black | 1192 |
| Asian | 228 |
| Native | 68 |
| Hispanic/Latino | 582 |
| Bachelor's or higher | 6618 |

## Districts

- [MO-06](/us/states/mo/districts/06.md) — 100% (congressional)
- [MO Senate District 18](/us/states/mo/districts/senate/18.md) — 100% (state senate)
- [MO House District 5](/us/states/mo/districts/house/5.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
