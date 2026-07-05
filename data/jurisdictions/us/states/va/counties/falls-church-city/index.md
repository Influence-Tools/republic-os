---
type: Jurisdiction
title: "Falls Church city, VA"
classification: county
fips: "51610"
state: "VA"
demographics:
  population: 14710
  population_under_18: 4013
  population_18_64: 4335
  population_65_plus: 6362
  median_household_income: 143262
  poverty_rate: 4.02
  homeownership_rate: 52.53
  unemployment_rate: 4.98
  median_home_value: 1055600
  gini_index: 0.4564
  vacancy_rate: 4.74
  race_white: 10333
  race_black: 559
  race_asian: 1344
  race_native: 17
  hispanic: 1587
  bachelors_plus: 13423
districts:
  - to: "us/states/va/districts/08"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/senate/37"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/va/districts/house/13"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Falls Church city, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14710 |
| Under 18 | 4013 |
| 18–64 | 4335 |
| 65+ | 6362 |
| Median household income | 143262 |
| Poverty rate | 4.02 |
| Homeownership rate | 52.53 |
| Unemployment rate | 4.98 |
| Median home value | 1055600 |
| Gini index | 0.4564 |
| Vacancy rate | 4.74 |
| White | 10333 |
| Black | 559 |
| Asian | 1344 |
| Native | 17 |
| Hispanic/Latino | 1587 |
| Bachelor's or higher | 13423 |

## Districts

- [VA-08](/us/states/va/districts/08.md) — 100% (congressional)
- [VA Senate District 37](/us/states/va/districts/senate/37.md) — 100% (state senate)
- [VA House District 13](/us/states/va/districts/house/13.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
