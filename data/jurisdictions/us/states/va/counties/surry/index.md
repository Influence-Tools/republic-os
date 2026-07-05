---
type: Jurisdiction
title: "Surry County, VA"
classification: county
fips: "51181"
state: "VA"
demographics:
  population: 6549
  population_under_18: 1255
  population_18_64: 1684
  population_65_plus: 3610
  median_household_income: 78041
  poverty_rate: 10.53
  homeownership_rate: 79.54
  unemployment_rate: 4.99
  median_home_value: 238800
  gini_index: 0.4176
  vacancy_rate: 17.99
  race_white: 3630
  race_black: 2554
  race_asian: 23
  race_native: 0
  hispanic: 205
  bachelors_plus: 1795
districts:
  - to: "us/states/va/districts/04"
    rel: in-district
    area_weight: 0.9098
  - to: "us/states/va/districts/senate/13"
    rel: in-district
    area_weight: 0.9127
  - to: "us/states/va/districts/house/82"
    rel: in-district
    area_weight: 0.9125
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Surry County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6549 |
| Under 18 | 1255 |
| 18–64 | 1684 |
| 65+ | 3610 |
| Median household income | 78041 |
| Poverty rate | 10.53 |
| Homeownership rate | 79.54 |
| Unemployment rate | 4.99 |
| Median home value | 238800 |
| Gini index | 0.4176 |
| Vacancy rate | 17.99 |
| White | 3630 |
| Black | 2554 |
| Asian | 23 |
| Native | 0 |
| Hispanic/Latino | 205 |
| Bachelor's or higher | 1795 |

## Districts

- [VA-04](/us/states/va/districts/04.md) — 91% (congressional)
- [VA Senate District 13](/us/states/va/districts/senate/13.md) — 91% (state senate)
- [VA House District 82](/us/states/va/districts/house/82.md) — 91% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
