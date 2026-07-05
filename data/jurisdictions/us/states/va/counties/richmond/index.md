---
type: Jurisdiction
title: "Richmond County, VA"
classification: county
fips: "51159"
state: "VA"
demographics:
  population: 9095
  population_under_18: 1613
  population_18_64: 5587
  population_65_plus: 1895
  median_household_income: 66304
  poverty_rate: 7.73
  homeownership_rate: 74.66
  unemployment_rate: 2.49
  median_home_value: 231500
  gini_index: 0.3812
  vacancy_rate: 19.97
  race_white: 5581
  race_black: 2439
  race_asian: 59
  race_native: 61
  hispanic: 686
  bachelors_plus: 1560
districts:
  - to: "us/states/va/districts/01"
    rel: in-district
    area_weight: 0.9082
  - to: "us/states/va/districts/senate/25"
    rel: in-district
    area_weight: 0.9022
  - to: "us/states/va/districts/house/67"
    rel: in-district
    area_weight: 0.9022
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Richmond County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9095 |
| Under 18 | 1613 |
| 18–64 | 5587 |
| 65+ | 1895 |
| Median household income | 66304 |
| Poverty rate | 7.73 |
| Homeownership rate | 74.66 |
| Unemployment rate | 2.49 |
| Median home value | 231500 |
| Gini index | 0.3812 |
| Vacancy rate | 19.97 |
| White | 5581 |
| Black | 2439 |
| Asian | 59 |
| Native | 61 |
| Hispanic/Latino | 686 |
| Bachelor's or higher | 1560 |

## Districts

- [VA-01](/us/states/va/districts/01.md) — 91% (congressional)
- [VA Senate District 25](/us/states/va/districts/senate/25.md) — 90% (state senate)
- [VA House District 67](/us/states/va/districts/house/67.md) — 90% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
