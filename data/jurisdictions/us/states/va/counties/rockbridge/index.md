---
type: Jurisdiction
title: "Rockbridge County, VA"
classification: county
fips: "51163"
state: "VA"
demographics:
  population: 22531
  population_under_18: 3839
  population_18_64: 12509
  population_65_plus: 6183
  median_household_income: 65469
  poverty_rate: 7.51
  homeownership_rate: 79.27
  unemployment_rate: 3.86
  median_home_value: 248800
  gini_index: 0.448
  vacancy_rate: 15.92
  race_white: 20297
  race_black: 697
  race_asian: 196
  race_native: 41
  hispanic: 522
  bachelors_plus: 8383
districts:
  - to: "us/states/va/districts/06"
    rel: in-district
    area_weight: 0.9966
  - to: "us/states/va/districts/senate/3"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/va/districts/house/37"
    rel: in-district
    area_weight: 0.685
  - to: "us/states/va/districts/house/36"
    rel: in-district
    area_weight: 0.3148
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Rockbridge County, VA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 22531 |
| Under 18 | 3839 |
| 18–64 | 12509 |
| 65+ | 6183 |
| Median household income | 65469 |
| Poverty rate | 7.51 |
| Homeownership rate | 79.27 |
| Unemployment rate | 3.86 |
| Median home value | 248800 |
| Gini index | 0.448 |
| Vacancy rate | 15.92 |
| White | 20297 |
| Black | 697 |
| Asian | 196 |
| Native | 41 |
| Hispanic/Latino | 522 |
| Bachelor's or higher | 8383 |

## Districts

- [VA-06](/us/states/va/districts/06.md) — 100% (congressional)
- [VA Senate District 3](/us/states/va/districts/senate/3.md) — 100% (state senate)
- [VA House District 37](/us/states/va/districts/house/37.md) — 68% (state house)
- [VA House District 36](/us/states/va/districts/house/36.md) — 31% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
