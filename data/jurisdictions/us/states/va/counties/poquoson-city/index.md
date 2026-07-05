---
type: Jurisdiction
title: "Poquoson city, VA"
classification: county
fips: "51735"
state: "VA"
demographics:
  population: 12639
  population_under_18: 3245
  population_18_64: 3583
  population_65_plus: 5811
  median_household_income: 120972
  poverty_rate: 4.49
  homeownership_rate: 84.6
  unemployment_rate: 3.17
  median_home_value: 400300
  gini_index: 0.3734
  vacancy_rate: 4.89
  race_white: 11384
  race_black: 238
  race_asian: 217
  race_native: 86
  hispanic: 525
  bachelors_plus: 4703
districts:
  - to: "us/states/va/districts/01"
    rel: in-district
    area_weight: 0.259
  - to: "us/states/va/districts/senate/24"
    rel: in-district
    area_weight: 0.2501
  - to: "us/states/va/districts/house/86"
    rel: in-district
    area_weight: 0.2501
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Poquoson city, VA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12639 |
| Under 18 | 3245 |
| 18–64 | 3583 |
| 65+ | 5811 |
| Median household income | 120972 |
| Poverty rate | 4.49 |
| Homeownership rate | 84.6 |
| Unemployment rate | 3.17 |
| Median home value | 400300 |
| Gini index | 0.3734 |
| Vacancy rate | 4.89 |
| White | 11384 |
| Black | 238 |
| Asian | 217 |
| Native | 86 |
| Hispanic/Latino | 525 |
| Bachelor's or higher | 4703 |

## Districts

- [VA-01](/us/states/va/districts/01.md) — 26% (congressional)
- [VA Senate District 24](/us/states/va/districts/senate/24.md) — 25% (state senate)
- [VA House District 86](/us/states/va/districts/house/86.md) — 25% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
