---
type: Jurisdiction
title: "Wythe County, VA"
classification: county
fips: "51197"
state: "VA"
demographics:
  population: 28188
  population_under_18: 5981
  population_18_64: 7771
  population_65_plus: 14436
  median_household_income: 57745
  poverty_rate: 15.19
  homeownership_rate: 76.96
  unemployment_rate: 4.0
  median_home_value: 171200
  gini_index: 0.4798
  vacancy_rate: 10.67
  race_white: 26248
  race_black: 644
  race_asian: 225
  race_native: 4
  hispanic: 449
  bachelors_plus: 5603
districts:
  - to: "us/states/va/districts/09"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/senate/7"
    rel: in-district
    area_weight: 0.6217
  - to: "us/states/va/districts/senate/5"
    rel: in-district
    area_weight: 0.3783
  - to: "us/states/va/districts/house/46"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Wythe County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 28188 |
| Under 18 | 5981 |
| 18–64 | 7771 |
| 65+ | 14436 |
| Median household income | 57745 |
| Poverty rate | 15.19 |
| Homeownership rate | 76.96 |
| Unemployment rate | 4.0 |
| Median home value | 171200 |
| Gini index | 0.4798 |
| Vacancy rate | 10.67 |
| White | 26248 |
| Black | 644 |
| Asian | 225 |
| Native | 4 |
| Hispanic/Latino | 449 |
| Bachelor's or higher | 5603 |

## Districts

- [VA-09](/us/states/va/districts/09.md) — 100% (congressional)
- [VA Senate District 7](/us/states/va/districts/senate/7.md) — 62% (state senate)
- [VA Senate District 5](/us/states/va/districts/senate/5.md) — 38% (state senate)
- [VA House District 46](/us/states/va/districts/house/46.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
