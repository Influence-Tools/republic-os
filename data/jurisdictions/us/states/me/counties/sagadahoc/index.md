---
type: Jurisdiction
title: "Sagadahoc County, ME"
classification: county
fips: "23023"
state: "ME"
demographics:
  population: 37285
  population_under_18: 6578
  population_18_64: 21527
  population_65_plus: 9180
  median_household_income: 87806
  poverty_rate: 10.03
  homeownership_rate: 77.84
  unemployment_rate: 4.6
  median_home_value: 333300
  gini_index: 0.4364
  vacancy_rate: 14.52
  race_white: 34730
  race_black: 187
  race_asian: 249
  race_native: 40
  hispanic: 754
  bachelors_plus: 17737
districts:
  - to: "us/states/me/districts/01"
    rel: in-district
    area_weight: 0.8098
  - to: "us/states/me/districts/senate/24"
    rel: in-district
    area_weight: 0.8058
  - to: "us/states/me/districts/house/49"
    rel: in-district
    area_weight: 0.3544
  - to: "us/states/me/districts/house/52"
    rel: in-district
    area_weight: 0.2832
  - to: "us/states/me/districts/house/51"
    rel: in-district
    area_weight: 0.0726
  - to: "us/states/me/districts/house/98"
    rel: in-district
    area_weight: 0.0599
  - to: "us/states/me/districts/house/50"
    rel: in-district
    area_weight: 0.0357
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, me]
timestamp: "2026-07-03"
---

# Sagadahoc County, ME

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 37285 |
| Under 18 | 6578 |
| 18–64 | 21527 |
| 65+ | 9180 |
| Median household income | 87806 |
| Poverty rate | 10.03 |
| Homeownership rate | 77.84 |
| Unemployment rate | 4.6 |
| Median home value | 333300 |
| Gini index | 0.4364 |
| Vacancy rate | 14.52 |
| White | 34730 |
| Black | 187 |
| Asian | 249 |
| Native | 40 |
| Hispanic/Latino | 754 |
| Bachelor's or higher | 17737 |

## Districts

- [ME-01](/us/states/me/districts/01.md) — 81% (congressional)
- [ME Senate District 24](/us/states/me/districts/senate/24.md) — 81% (state senate)
- [ME House District 49](/us/states/me/districts/house/49.md) — 35% (state house)
- [ME House District 52](/us/states/me/districts/house/52.md) — 28% (state house)
- [ME House District 51](/us/states/me/districts/house/51.md) — 7% (state house)
- [ME House District 98](/us/states/me/districts/house/98.md) — 6% (state house)
- [ME House District 50](/us/states/me/districts/house/50.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
