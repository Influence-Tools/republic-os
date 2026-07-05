---
type: Jurisdiction
title: "Gogebic County, MI"
classification: county
fips: "26053"
state: "MI"
demographics:
  population: 14319
  population_under_18: 2346
  population_18_64: 7770
  population_65_plus: 4203
  median_household_income: 52732
  poverty_rate: 14.4
  homeownership_rate: 80.98
  unemployment_rate: 6.49
  median_home_value: 107200
  gini_index: 0.4788
  vacancy_rate: 32.76
  race_white: 13031
  race_black: 68
  race_asian: 86
  race_native: 346
  hispanic: 291
  bachelors_plus: 3441
districts:
  - to: "us/states/mi/districts/01"
    rel: in-district
    area_weight: 0.773
  - to: "us/states/mi/districts/senate/38"
    rel: in-district
    area_weight: 0.7731
  - to: "us/states/mi/districts/house/110"
    rel: in-district
    area_weight: 0.7731
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Gogebic County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14319 |
| Under 18 | 2346 |
| 18–64 | 7770 |
| 65+ | 4203 |
| Median household income | 52732 |
| Poverty rate | 14.4 |
| Homeownership rate | 80.98 |
| Unemployment rate | 6.49 |
| Median home value | 107200 |
| Gini index | 0.4788 |
| Vacancy rate | 32.76 |
| White | 13031 |
| Black | 68 |
| Asian | 86 |
| Native | 346 |
| Hispanic/Latino | 291 |
| Bachelor's or higher | 3441 |

## Districts

- [MI-01](/us/states/mi/districts/01.md) — 77% (congressional)
- [MI Senate District 38](/us/states/mi/districts/senate/38.md) — 77% (state senate)
- [MI House District 110](/us/states/mi/districts/house/110.md) — 77% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
