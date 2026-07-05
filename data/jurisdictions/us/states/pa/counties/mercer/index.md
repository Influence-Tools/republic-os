---
type: Jurisdiction
title: "Mercer County, PA"
classification: county
fips: "42085"
state: "PA"
demographics:
  population: 109257
  population_under_18: 20692
  population_18_64: 63294
  population_65_plus: 25271
  median_household_income: 59976
  poverty_rate: 13.16
  homeownership_rate: 72.39
  unemployment_rate: 5.34
  median_home_value: 164000
  gini_index: 0.4423
  vacancy_rate: 8.65
  race_white: 96236
  race_black: 6358
  race_asian: 709
  race_native: 102
  hispanic: 1837
  bachelors_plus: 26861
districts:
  - to: "us/states/pa/districts/16"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/pa/districts/senate/50"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/pa/districts/house/17"
    rel: in-district
    area_weight: 0.6948
  - to: "us/states/pa/districts/house/7"
    rel: in-district
    area_weight: 0.305
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Mercer County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 109257 |
| Under 18 | 20692 |
| 18–64 | 63294 |
| 65+ | 25271 |
| Median household income | 59976 |
| Poverty rate | 13.16 |
| Homeownership rate | 72.39 |
| Unemployment rate | 5.34 |
| Median home value | 164000 |
| Gini index | 0.4423 |
| Vacancy rate | 8.65 |
| White | 96236 |
| Black | 6358 |
| Asian | 709 |
| Native | 102 |
| Hispanic/Latino | 1837 |
| Bachelor's or higher | 26861 |

## Districts

- [PA-16](/us/states/pa/districts/16.md) — 100% (congressional)
- [PA Senate District 50](/us/states/pa/districts/senate/50.md) — 100% (state senate)
- [PA House District 17](/us/states/pa/districts/house/17.md) — 69% (state house)
- [PA House District 7](/us/states/pa/districts/house/7.md) — 30% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
