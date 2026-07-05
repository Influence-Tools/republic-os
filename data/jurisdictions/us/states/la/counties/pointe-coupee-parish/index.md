---
type: Jurisdiction
title: "Pointe Coupee Parish, LA"
classification: county
fips: "22077"
state: "LA"
demographics:
  population: 20217
  population_under_18: 4322
  population_18_64: 11368
  population_65_plus: 4527
  median_household_income: 65961
  poverty_rate: 16.47
  homeownership_rate: 80.04
  unemployment_rate: 6.98
  median_home_value: 179300
  gini_index: 0.4597
  vacancy_rate: 24.88
  race_white: 12366
  race_black: 6584
  race_asian: 29
  race_native: 74
  hispanic: 715
  bachelors_plus: 3555
districts:
  - to: "us/states/la/districts/06"
    rel: in-district
    area_weight: 0.9956
  - to: "us/states/la/districts/senate/17"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/la/districts/house/18"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Pointe Coupee Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20217 |
| Under 18 | 4322 |
| 18–64 | 11368 |
| 65+ | 4527 |
| Median household income | 65961 |
| Poverty rate | 16.47 |
| Homeownership rate | 80.04 |
| Unemployment rate | 6.98 |
| Median home value | 179300 |
| Gini index | 0.4597 |
| Vacancy rate | 24.88 |
| White | 12366 |
| Black | 6584 |
| Asian | 29 |
| Native | 74 |
| Hispanic/Latino | 715 |
| Bachelor's or higher | 3555 |

## Districts

- [LA-06](/us/states/la/districts/06.md) — 100% (congressional)
- [LA Senate District 17](/us/states/la/districts/senate/17.md) — 100% (state senate)
- [LA House District 18](/us/states/la/districts/house/18.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
