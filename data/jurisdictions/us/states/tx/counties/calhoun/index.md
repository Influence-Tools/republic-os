---
type: Jurisdiction
title: "Calhoun County, TX"
classification: county
fips: "48057"
state: "TX"
demographics:
  population: 19868
  population_under_18: 4507
  population_18_64: 11546
  population_65_plus: 3815
  median_household_income: 79959
  poverty_rate: 7.66
  homeownership_rate: 77.27
  unemployment_rate: 7.37
  median_home_value: 171200
  gini_index: 0.432
  vacancy_rate: 19.97
  race_white: 11034
  race_black: 517
  race_asian: 824
  race_native: 60
  hispanic: 9821
  bachelors_plus: 3827
districts:
  - to: "us/states/tx/districts/27"
    rel: in-district
    area_weight: 0.7342
  - to: "us/states/tx/districts/senate/18"
    rel: in-district
    area_weight: 0.7217
  - to: "us/states/tx/districts/house/43"
    rel: in-district
    area_weight: 0.7216
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Calhoun County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19868 |
| Under 18 | 4507 |
| 18–64 | 11546 |
| 65+ | 3815 |
| Median household income | 79959 |
| Poverty rate | 7.66 |
| Homeownership rate | 77.27 |
| Unemployment rate | 7.37 |
| Median home value | 171200 |
| Gini index | 0.432 |
| Vacancy rate | 19.97 |
| White | 11034 |
| Black | 517 |
| Asian | 824 |
| Native | 60 |
| Hispanic/Latino | 9821 |
| Bachelor's or higher | 3827 |

## Districts

- [TX-27](/us/states/tx/districts/27.md) — 73% (congressional)
- [TX Senate District 18](/us/states/tx/districts/senate/18.md) — 72% (state senate)
- [TX House District 43](/us/states/tx/districts/house/43.md) — 72% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
