---
type: Jurisdiction
title: "Westmoreland County, VA"
classification: county
fips: "51193"
state: "VA"
demographics:
  population: 18826
  population_under_18: 3615
  population_18_64: 5055
  population_65_plus: 10156
  median_household_income: 63398
  poverty_rate: 14.01
  homeownership_rate: 80.06
  unemployment_rate: 7.31
  median_home_value: 269600
  gini_index: 0.4633
  vacancy_rate: 28.82
  race_white: 11820
  race_black: 4424
  race_asian: 185
  race_native: 16
  hispanic: 1210
  bachelors_plus: 4505
districts:
  - to: "us/states/va/districts/01"
    rel: in-district
    area_weight: 0.9918
  - to: "us/states/va/districts/senate/25"
    rel: in-district
    area_weight: 0.9633
  - to: "us/states/va/districts/house/67"
    rel: in-district
    area_weight: 0.9633
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Westmoreland County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18826 |
| Under 18 | 3615 |
| 18–64 | 5055 |
| 65+ | 10156 |
| Median household income | 63398 |
| Poverty rate | 14.01 |
| Homeownership rate | 80.06 |
| Unemployment rate | 7.31 |
| Median home value | 269600 |
| Gini index | 0.4633 |
| Vacancy rate | 28.82 |
| White | 11820 |
| Black | 4424 |
| Asian | 185 |
| Native | 16 |
| Hispanic/Latino | 1210 |
| Bachelor's or higher | 4505 |

## Districts

- [VA-01](/us/states/va/districts/01.md) — 99% (congressional)
- [VA Senate District 25](/us/states/va/districts/senate/25.md) — 96% (state senate)
- [VA House District 67](/us/states/va/districts/house/67.md) — 96% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
