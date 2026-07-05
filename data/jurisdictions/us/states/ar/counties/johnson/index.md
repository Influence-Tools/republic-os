---
type: Jurisdiction
title: "Johnson County, AR"
classification: county
fips: "05071"
state: "AR"
demographics:
  population: 26003
  population_under_18: 6299
  population_18_64: 15282
  population_65_plus: 4422
  median_household_income: 45995
  poverty_rate: 19.79
  homeownership_rate: 74.07
  unemployment_rate: 4.61
  median_home_value: 135300
  gini_index: 0.4527
  vacancy_rate: 10.72
  race_white: 21308
  race_black: 414
  race_asian: 852
  race_native: 156
  hispanic: 3606
  bachelors_plus: 3997
districts:
  - to: "us/states/ar/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ar/districts/senate/26"
    rel: in-district
    area_weight: 0.5944
  - to: "us/states/ar/districts/senate/28"
    rel: in-district
    area_weight: 0.4054
  - to: "us/states/ar/districts/house/45"
    rel: in-district
    area_weight: 0.973
  - to: "us/states/ar/districts/house/46"
    rel: in-district
    area_weight: 0.0267
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Johnson County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 26003 |
| Under 18 | 6299 |
| 18–64 | 15282 |
| 65+ | 4422 |
| Median household income | 45995 |
| Poverty rate | 19.79 |
| Homeownership rate | 74.07 |
| Unemployment rate | 4.61 |
| Median home value | 135300 |
| Gini index | 0.4527 |
| Vacancy rate | 10.72 |
| White | 21308 |
| Black | 414 |
| Asian | 852 |
| Native | 156 |
| Hispanic/Latino | 3606 |
| Bachelor's or higher | 3997 |

## Districts

- [AR-04](/us/states/ar/districts/04.md) — 100% (congressional)
- [AR Senate District 26](/us/states/ar/districts/senate/26.md) — 59% (state senate)
- [AR Senate District 28](/us/states/ar/districts/senate/28.md) — 41% (state senate)
- [AR House District 45](/us/states/ar/districts/house/45.md) — 97% (state house)
- [AR House District 46](/us/states/ar/districts/house/46.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
