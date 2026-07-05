---
type: Jurisdiction
title: "Marengo County, AL"
classification: county
fips: "01091"
state: "AL"
demographics:
  population: 18851
  population_under_18: 4154
  population_18_64: 10812
  population_65_plus: 3885
  median_household_income: 43825
  poverty_rate: 21.85
  homeownership_rate: 70.25
  unemployment_rate: 4.09
  median_home_value: 107400
  gini_index: 0.5327
  vacancy_rate: 19.96
  race_white: 8386
  race_black: 9592
  race_asian: 49
  race_native: 54
  hispanic: 506
  bachelors_plus: 3598
districts:
  - to: "us/states/al/districts/07"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/al/districts/senate/24"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/al/districts/house/68"
    rel: in-district
    area_weight: 0.5465
  - to: "us/states/al/districts/house/71"
    rel: in-district
    area_weight: 0.4533
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Marengo County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18851 |
| Under 18 | 4154 |
| 18–64 | 10812 |
| 65+ | 3885 |
| Median household income | 43825 |
| Poverty rate | 21.85 |
| Homeownership rate | 70.25 |
| Unemployment rate | 4.09 |
| Median home value | 107400 |
| Gini index | 0.5327 |
| Vacancy rate | 19.96 |
| White | 8386 |
| Black | 9592 |
| Asian | 49 |
| Native | 54 |
| Hispanic/Latino | 506 |
| Bachelor's or higher | 3598 |

## Districts

- [AL-07](/us/states/al/districts/07.md) — 100% (congressional)
- [AL Senate District 24](/us/states/al/districts/senate/24.md) — 100% (state senate)
- [AL House District 68](/us/states/al/districts/house/68.md) — 55% (state house)
- [AL House District 71](/us/states/al/districts/house/71.md) — 45% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
