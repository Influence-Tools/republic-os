---
type: Jurisdiction
title: "Staunton city, VA"
classification: county
fips: "51790"
state: "VA"
demographics:
  population: 25948
  population_under_18: 5765
  population_18_64: 8545
  population_65_plus: 11638
  median_household_income: 65581
  poverty_rate: 12.41
  homeownership_rate: 60.88
  unemployment_rate: 5.28
  median_home_value: 259200
  gini_index: 0.4342
  vacancy_rate: 8.78
  race_white: 20567
  race_black: 2816
  race_asian: 361
  race_native: 61
  hispanic: 1233
  bachelors_plus: 9999
districts:
  - to: "us/states/va/districts/06"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/senate/3"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/va/districts/house/36"
    rel: in-district
    area_weight: 0.9987
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Staunton city, VA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25948 |
| Under 18 | 5765 |
| 18–64 | 8545 |
| 65+ | 11638 |
| Median household income | 65581 |
| Poverty rate | 12.41 |
| Homeownership rate | 60.88 |
| Unemployment rate | 5.28 |
| Median home value | 259200 |
| Gini index | 0.4342 |
| Vacancy rate | 8.78 |
| White | 20567 |
| Black | 2816 |
| Asian | 361 |
| Native | 61 |
| Hispanic/Latino | 1233 |
| Bachelor's or higher | 9999 |

## Districts

- [VA-06](/us/states/va/districts/06.md) — 100% (congressional)
- [VA Senate District 3](/us/states/va/districts/senate/3.md) — 100% (state senate)
- [VA House District 36](/us/states/va/districts/house/36.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
