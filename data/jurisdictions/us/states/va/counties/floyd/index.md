---
type: Jurisdiction
title: "Floyd County, VA"
classification: county
fips: "51063"
state: "VA"
demographics:
  population: 15593
  population_under_18: 2909
  population_18_64: 8876
  population_65_plus: 3808
  median_household_income: 62191
  poverty_rate: 9.84
  homeownership_rate: 83.9
  unemployment_rate: 3.56
  median_home_value: 225400
  gini_index: 0.4693
  vacancy_rate: 16.92
  race_white: 14439
  race_black: 404
  race_asian: 62
  race_native: 19
  hispanic: 469
  bachelors_plus: 3927
districts:
  - to: "us/states/va/districts/09"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/senate/7"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/va/districts/house/47"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Floyd County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15593 |
| Under 18 | 2909 |
| 18–64 | 8876 |
| 65+ | 3808 |
| Median household income | 62191 |
| Poverty rate | 9.84 |
| Homeownership rate | 83.9 |
| Unemployment rate | 3.56 |
| Median home value | 225400 |
| Gini index | 0.4693 |
| Vacancy rate | 16.92 |
| White | 14439 |
| Black | 404 |
| Asian | 62 |
| Native | 19 |
| Hispanic/Latino | 469 |
| Bachelor's or higher | 3927 |

## Districts

- [VA-09](/us/states/va/districts/09.md) — 100% (congressional)
- [VA Senate District 7](/us/states/va/districts/senate/7.md) — 100% (state senate)
- [VA House District 47](/us/states/va/districts/house/47.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
