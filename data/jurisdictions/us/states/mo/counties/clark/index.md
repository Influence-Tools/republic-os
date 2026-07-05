---
type: Jurisdiction
title: "Clark County, MO"
classification: county
fips: "29045"
state: "MO"
demographics:
  population: 6675
  population_under_18: 1595
  population_18_64: 3629
  population_65_plus: 1451
  median_household_income: 51781
  poverty_rate: 11.2
  homeownership_rate: 78.25
  unemployment_rate: 5.03
  median_home_value: 130700
  gini_index: 0.4504
  vacancy_rate: 25.05
  race_white: 6334
  race_black: 127
  race_asian: 6
  race_native: 0
  hispanic: 65
  bachelors_plus: 921
districts:
  - to: "us/states/mo/districts/06"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/senate/18"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/4"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Clark County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6675 |
| Under 18 | 1595 |
| 18–64 | 3629 |
| 65+ | 1451 |
| Median household income | 51781 |
| Poverty rate | 11.2 |
| Homeownership rate | 78.25 |
| Unemployment rate | 5.03 |
| Median home value | 130700 |
| Gini index | 0.4504 |
| Vacancy rate | 25.05 |
| White | 6334 |
| Black | 127 |
| Asian | 6 |
| Native | 0 |
| Hispanic/Latino | 65 |
| Bachelor's or higher | 921 |

## Districts

- [MO-06](/us/states/mo/districts/06.md) — 100% (congressional)
- [MO Senate District 18](/us/states/mo/districts/senate/18.md) — 100% (state senate)
- [MO House District 4](/us/states/mo/districts/house/4.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
