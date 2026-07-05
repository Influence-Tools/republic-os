---
type: Jurisdiction
title: "Southampton County, VA"
classification: county
fips: "51175"
state: "VA"
demographics:
  population: 17964
  population_under_18: 3679
  population_18_64: 4703
  population_65_plus: 9582
  median_household_income: 70795
  poverty_rate: 8.72
  homeownership_rate: 76.11
  unemployment_rate: 5.48
  median_home_value: 216200
  gini_index: 0.4029
  vacancy_rate: 12.06
  race_white: 11038
  race_black: 5240
  race_asian: 140
  race_native: 57
  hispanic: 453
  bachelors_plus: 3555
districts:
  - to: "us/states/va/districts/04"
    rel: in-district
    area_weight: 0.6197
  - to: "us/states/va/districts/02"
    rel: in-district
    area_weight: 0.3803
  - to: "us/states/va/districts/senate/17"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/va/districts/house/83"
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

# Southampton County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17964 |
| Under 18 | 3679 |
| 18–64 | 4703 |
| 65+ | 9582 |
| Median household income | 70795 |
| Poverty rate | 8.72 |
| Homeownership rate | 76.11 |
| Unemployment rate | 5.48 |
| Median home value | 216200 |
| Gini index | 0.4029 |
| Vacancy rate | 12.06 |
| White | 11038 |
| Black | 5240 |
| Asian | 140 |
| Native | 57 |
| Hispanic/Latino | 453 |
| Bachelor's or higher | 3555 |

## Districts

- [VA-04](/us/states/va/districts/04.md) — 62% (congressional)
- [VA-02](/us/states/va/districts/02.md) — 38% (congressional)
- [VA Senate District 17](/us/states/va/districts/senate/17.md) — 100% (state senate)
- [VA House District 83](/us/states/va/districts/house/83.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
