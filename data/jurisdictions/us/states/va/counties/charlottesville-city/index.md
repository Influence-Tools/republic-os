---
type: Jurisdiction
title: "Charlottesville city, VA"
classification: county
fips: "51540"
state: "VA"
demographics:
  population: 45437
  population_under_18: 9262
  population_18_64: 20866
  population_65_plus: 15309
  median_household_income: 74824
  poverty_rate: 19.65
  homeownership_rate: 44.24
  unemployment_rate: 3.7
  median_home_value: 486700
  gini_index: 0.5315
  vacancy_rate: 8.31
  race_white: 30209
  race_black: 7103
  race_asian: 3207
  race_native: 30
  hispanic: 3132
  bachelors_plus: 28510
districts:
  - to: "us/states/va/districts/05"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/senate/11"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/house/54"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Charlottesville city, VA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 45437 |
| Under 18 | 9262 |
| 18–64 | 20866 |
| 65+ | 15309 |
| Median household income | 74824 |
| Poverty rate | 19.65 |
| Homeownership rate | 44.24 |
| Unemployment rate | 3.7 |
| Median home value | 486700 |
| Gini index | 0.5315 |
| Vacancy rate | 8.31 |
| White | 30209 |
| Black | 7103 |
| Asian | 3207 |
| Native | 30 |
| Hispanic/Latino | 3132 |
| Bachelor's or higher | 28510 |

## Districts

- [VA-05](/us/states/va/districts/05.md) — 100% (congressional)
- [VA Senate District 11](/us/states/va/districts/senate/11.md) — 100% (state senate)
- [VA House District 54](/us/states/va/districts/house/54.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
