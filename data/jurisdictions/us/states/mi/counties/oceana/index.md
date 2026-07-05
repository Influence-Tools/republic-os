---
type: Jurisdiction
title: "Oceana County, MI"
classification: county
fips: "26127"
state: "MI"
demographics:
  population: 26915
  population_under_18: 5722
  population_18_64: 15146
  population_65_plus: 6047
  median_household_income: 62417
  poverty_rate: 13.63
  homeownership_rate: 84.45
  unemployment_rate: 6.48
  median_home_value: 190100
  gini_index: 0.4365
  vacancy_rate: 33.73
  race_white: 23001
  race_black: 273
  race_asian: 38
  race_native: 178
  hispanic: 4181
  bachelors_plus: 5631
districts:
  - to: "us/states/mi/districts/02"
    rel: in-district
    area_weight: 0.4182
  - to: "us/states/mi/districts/senate/32"
    rel: in-district
    area_weight: 0.418
  - to: "us/states/mi/districts/house/102"
    rel: in-district
    area_weight: 0.363
  - to: "us/states/mi/districts/house/101"
    rel: in-district
    area_weight: 0.0551
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Oceana County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 26915 |
| Under 18 | 5722 |
| 18–64 | 15146 |
| 65+ | 6047 |
| Median household income | 62417 |
| Poverty rate | 13.63 |
| Homeownership rate | 84.45 |
| Unemployment rate | 6.48 |
| Median home value | 190100 |
| Gini index | 0.4365 |
| Vacancy rate | 33.73 |
| White | 23001 |
| Black | 273 |
| Asian | 38 |
| Native | 178 |
| Hispanic/Latino | 4181 |
| Bachelor's or higher | 5631 |

## Districts

- [MI-02](/us/states/mi/districts/02.md) — 42% (congressional)
- [MI Senate District 32](/us/states/mi/districts/senate/32.md) — 42% (state senate)
- [MI House District 102](/us/states/mi/districts/house/102.md) — 36% (state house)
- [MI House District 101](/us/states/mi/districts/house/101.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
