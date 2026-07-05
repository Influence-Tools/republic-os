---
type: Jurisdiction
title: "Lancaster County, VA"
classification: county
fips: "51103"
state: "VA"
demographics:
  population: 10936
  population_under_18: 1588
  population_18_64: 4984
  population_65_plus: 4364
  median_household_income: 69713
  poverty_rate: 10.27
  homeownership_rate: 81.48
  unemployment_rate: 9.55
  median_home_value: 327000
  gini_index: 0.4937
  vacancy_rate: 23.95
  race_white: 7494
  race_black: 2803
  race_asian: 69
  race_native: 6
  hispanic: 192
  bachelors_plus: 5198
districts:
  - to: "us/states/va/districts/01"
    rel: in-district
    area_weight: 0.6404
  - to: "us/states/va/districts/senate/25"
    rel: in-district
    area_weight: 0.6195
  - to: "us/states/va/districts/house/67"
    rel: in-district
    area_weight: 0.6195
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Lancaster County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10936 |
| Under 18 | 1588 |
| 18–64 | 4984 |
| 65+ | 4364 |
| Median household income | 69713 |
| Poverty rate | 10.27 |
| Homeownership rate | 81.48 |
| Unemployment rate | 9.55 |
| Median home value | 327000 |
| Gini index | 0.4937 |
| Vacancy rate | 23.95 |
| White | 7494 |
| Black | 2803 |
| Asian | 69 |
| Native | 6 |
| Hispanic/Latino | 192 |
| Bachelor's or higher | 5198 |

## Districts

- [VA-01](/us/states/va/districts/01.md) — 64% (congressional)
- [VA Senate District 25](/us/states/va/districts/senate/25.md) — 62% (state senate)
- [VA House District 67](/us/states/va/districts/house/67.md) — 62% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
