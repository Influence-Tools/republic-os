---
type: Jurisdiction
title: "Lexington city, VA"
classification: county
fips: "51678"
state: "VA"
demographics:
  population: 7525
  population_under_18: 2143
  population_18_64: 2887
  population_65_plus: 2495
  median_household_income: 84517
  poverty_rate: 14.04
  homeownership_rate: 53.77
  unemployment_rate: 0.64
  median_home_value: 275200
  gini_index: 0.4491
  vacancy_rate: 22.12
  race_white: 6220
  race_black: 437
  race_asian: 262
  race_native: 56
  hispanic: 472
  bachelors_plus: 2721
districts:
  - to: "us/states/va/districts/06"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/senate/3"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/house/37"
    rel: in-district
    area_weight: 0.9958
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Lexington city, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7525 |
| Under 18 | 2143 |
| 18–64 | 2887 |
| 65+ | 2495 |
| Median household income | 84517 |
| Poverty rate | 14.04 |
| Homeownership rate | 53.77 |
| Unemployment rate | 0.64 |
| Median home value | 275200 |
| Gini index | 0.4491 |
| Vacancy rate | 22.12 |
| White | 6220 |
| Black | 437 |
| Asian | 262 |
| Native | 56 |
| Hispanic/Latino | 472 |
| Bachelor's or higher | 2721 |

## Districts

- [VA-06](/us/states/va/districts/06.md) — 100% (congressional)
- [VA Senate District 3](/us/states/va/districts/senate/3.md) — 100% (state senate)
- [VA House District 37](/us/states/va/districts/house/37.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
