---
type: Jurisdiction
title: "Fluvanna County, VA"
classification: county
fips: "51065"
state: "VA"
demographics:
  population: 28092
  population_under_18: 5458
  population_18_64: 16537
  population_65_plus: 6097
  median_household_income: 96768
  poverty_rate: 7.68
  homeownership_rate: 88.69
  unemployment_rate: 4.2
  median_home_value: 314100
  gini_index: 0.4082
  vacancy_rate: 10.14
  race_white: 21323
  race_black: 3311
  race_asian: 251
  race_native: 56
  hispanic: 1288
  bachelors_plus: 10505
districts:
  - to: "us/states/va/districts/05"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/senate/10"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/house/56"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Fluvanna County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 28092 |
| Under 18 | 5458 |
| 18–64 | 16537 |
| 65+ | 6097 |
| Median household income | 96768 |
| Poverty rate | 7.68 |
| Homeownership rate | 88.69 |
| Unemployment rate | 4.2 |
| Median home value | 314100 |
| Gini index | 0.4082 |
| Vacancy rate | 10.14 |
| White | 21323 |
| Black | 3311 |
| Asian | 251 |
| Native | 56 |
| Hispanic/Latino | 1288 |
| Bachelor's or higher | 10505 |

## Districts

- [VA-05](/us/states/va/districts/05.md) — 100% (congressional)
- [VA Senate District 10](/us/states/va/districts/senate/10.md) — 100% (state senate)
- [VA House District 56](/us/states/va/districts/house/56.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
