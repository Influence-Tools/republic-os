---
type: Jurisdiction
title: "Trinity County, CA"
classification: county
fips: "06105"
state: "CA"
demographics:
  population: 15860
  population_under_18: 2727
  population_18_64: 8338
  population_65_plus: 4795
  median_household_income: 53002
  poverty_rate: 20.7
  homeownership_rate: 71.73
  unemployment_rate: 8.39
  median_home_value: 325800
  gini_index: 0.4949
  vacancy_rate: 31.15
  race_white: 12412
  race_black: 174
  race_asian: 101
  race_native: 594
  hispanic: 973
  bachelors_plus: 3822
districts:
  - to: "us/states/ca/districts/02"
    rel: in-district
    area_weight: 0.998
  - to: "us/states/ca/districts/senate/2"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ca/districts/house/2"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Trinity County, CA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15860 |
| Under 18 | 2727 |
| 18–64 | 8338 |
| 65+ | 4795 |
| Median household income | 53002 |
| Poverty rate | 20.7 |
| Homeownership rate | 71.73 |
| Unemployment rate | 8.39 |
| Median home value | 325800 |
| Gini index | 0.4949 |
| Vacancy rate | 31.15 |
| White | 12412 |
| Black | 174 |
| Asian | 101 |
| Native | 594 |
| Hispanic/Latino | 973 |
| Bachelor's or higher | 3822 |

## Districts

- [CA-02](/us/states/ca/districts/02.md) — 100% (congressional)
- [CA Senate District 2](/us/states/ca/districts/senate/2.md) — 100% (state senate)
- [CA House District 2](/us/states/ca/districts/house/2.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
