---
type: Jurisdiction
title: "Alpine County, CA"
classification: county
fips: "06003"
state: "CA"
demographics:
  population: 1616
  population_under_18: 321
  population_18_64: 954
  population_65_plus: 341
  median_household_income: 105521
  poverty_rate: 9.96
  homeownership_rate: 78.16
  unemployment_rate: 4.42
  median_home_value: 590200
  gini_index: 0.4997
  vacancy_rate: 72.08
  race_white: 986
  race_black: 0
  race_asian: 36
  race_native: 426
  hispanic: 216
  bachelors_plus: 590
districts:
  - to: "us/states/ca/districts/03"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/ca/districts/senate/4"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ca/districts/house/1"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Alpine County, CA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1616 |
| Under 18 | 321 |
| 18–64 | 954 |
| 65+ | 341 |
| Median household income | 105521 |
| Poverty rate | 9.96 |
| Homeownership rate | 78.16 |
| Unemployment rate | 4.42 |
| Median home value | 590200 |
| Gini index | 0.4997 |
| Vacancy rate | 72.08 |
| White | 986 |
| Black | 0 |
| Asian | 36 |
| Native | 426 |
| Hispanic/Latino | 216 |
| Bachelor's or higher | 590 |

## Districts

- [CA-03](/us/states/ca/districts/03.md) — 100% (congressional)
- [CA Senate District 4](/us/states/ca/districts/senate/4.md) — 100% (state senate)
- [CA House District 1](/us/states/ca/districts/house/1.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
