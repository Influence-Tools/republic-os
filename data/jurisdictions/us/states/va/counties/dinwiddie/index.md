---
type: Jurisdiction
title: "Dinwiddie County, VA"
classification: county
fips: "51053"
state: "VA"
demographics:
  population: 28191
  population_under_18: 5632
  population_18_64: 17144
  population_65_plus: 5415
  median_household_income: 83704
  poverty_rate: 11.66
  homeownership_rate: 79.61
  unemployment_rate: 4.6
  median_home_value: 257800
  gini_index: 0.4321
  vacancy_rate: 11.02
  race_white: 18028
  race_black: 8415
  race_asian: 168
  race_native: 7
  hispanic: 1236
  bachelors_plus: 5286
districts:
  - to: "us/states/va/districts/04"
    rel: in-district
    area_weight: 0.9975
  - to: "us/states/va/districts/senate/13"
    rel: in-district
    area_weight: 0.5103
  - to: "us/states/va/districts/senate/17"
    rel: in-district
    area_weight: 0.4894
  - to: "us/states/va/districts/house/82"
    rel: in-district
    area_weight: 0.7892
  - to: "us/states/va/districts/house/83"
    rel: in-district
    area_weight: 0.2105
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Dinwiddie County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 28191 |
| Under 18 | 5632 |
| 18–64 | 17144 |
| 65+ | 5415 |
| Median household income | 83704 |
| Poverty rate | 11.66 |
| Homeownership rate | 79.61 |
| Unemployment rate | 4.6 |
| Median home value | 257800 |
| Gini index | 0.4321 |
| Vacancy rate | 11.02 |
| White | 18028 |
| Black | 8415 |
| Asian | 168 |
| Native | 7 |
| Hispanic/Latino | 1236 |
| Bachelor's or higher | 5286 |

## Districts

- [VA-04](/us/states/va/districts/04.md) — 100% (congressional)
- [VA Senate District 13](/us/states/va/districts/senate/13.md) — 51% (state senate)
- [VA Senate District 17](/us/states/va/districts/senate/17.md) — 49% (state senate)
- [VA House District 82](/us/states/va/districts/house/82.md) — 79% (state house)
- [VA House District 83](/us/states/va/districts/house/83.md) — 21% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
