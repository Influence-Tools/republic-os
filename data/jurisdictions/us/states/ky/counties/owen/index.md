---
type: Jurisdiction
title: "Owen County, KY"
classification: county
fips: "21187"
state: "KY"
demographics:
  population: 11330
  population_under_18: 2499
  population_18_64: 6559
  population_65_plus: 2272
  median_household_income: 61134
  poverty_rate: 18.28
  homeownership_rate: 87.96
  unemployment_rate: 6.98
  median_home_value: 168700
  gini_index: 0.4136
  vacancy_rate: 21.08
  race_white: 10632
  race_black: 33
  race_asian: 5
  race_native: 11
  hispanic: 292
  bachelors_plus: 1859
districts:
  - to: "us/states/ky/districts/04"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/ky/districts/senate/20"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ky/districts/house/47"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Owen County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11330 |
| Under 18 | 2499 |
| 18–64 | 6559 |
| 65+ | 2272 |
| Median household income | 61134 |
| Poverty rate | 18.28 |
| Homeownership rate | 87.96 |
| Unemployment rate | 6.98 |
| Median home value | 168700 |
| Gini index | 0.4136 |
| Vacancy rate | 21.08 |
| White | 10632 |
| Black | 33 |
| Asian | 5 |
| Native | 11 |
| Hispanic/Latino | 292 |
| Bachelor's or higher | 1859 |

## Districts

- [KY-04](/us/states/ky/districts/04.md) — 100% (congressional)
- [KY Senate District 20](/us/states/ky/districts/senate/20.md) — 100% (state senate)
- [KY House District 47](/us/states/ky/districts/house/47.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
