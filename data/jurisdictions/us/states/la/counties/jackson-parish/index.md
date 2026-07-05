---
type: Jurisdiction
title: "Jackson Parish, LA"
classification: county
fips: "22049"
state: "LA"
demographics:
  population: 14884
  population_under_18: 3102
  population_18_64: 8694
  population_65_plus: 3088
  median_household_income: 44925
  poverty_rate: 22.3
  homeownership_rate: 70.01
  unemployment_rate: 7.41
  median_home_value: 115600
  gini_index: 0.447
  vacancy_rate: 22.88
  race_white: 9868
  race_black: 3515
  race_asian: 58
  race_native: 58
  hispanic: 522
  bachelors_plus: 2099
districts:
  - to: "us/states/la/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/la/districts/senate/35"
    rel: in-district
    area_weight: 0.9093
  - to: "us/states/la/districts/senate/29"
    rel: in-district
    area_weight: 0.0907
  - to: "us/states/la/districts/house/13"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Jackson Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14884 |
| Under 18 | 3102 |
| 18–64 | 8694 |
| 65+ | 3088 |
| Median household income | 44925 |
| Poverty rate | 22.3 |
| Homeownership rate | 70.01 |
| Unemployment rate | 7.41 |
| Median home value | 115600 |
| Gini index | 0.447 |
| Vacancy rate | 22.88 |
| White | 9868 |
| Black | 3515 |
| Asian | 58 |
| Native | 58 |
| Hispanic/Latino | 522 |
| Bachelor's or higher | 2099 |

## Districts

- [LA-04](/us/states/la/districts/04.md) — 100% (congressional)
- [LA Senate District 35](/us/states/la/districts/senate/35.md) — 91% (state senate)
- [LA Senate District 29](/us/states/la/districts/senate/29.md) — 9% (state senate)
- [LA House District 13](/us/states/la/districts/house/13.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
