---
type: Jurisdiction
title: "Charles City County, VA"
classification: county
fips: "51036"
state: "VA"
demographics:
  population: 6627
  population_under_18: 941
  population_18_64: 3904
  population_65_plus: 1782
  median_household_income: 75417
  poverty_rate: 9.45
  homeownership_rate: 86.26
  unemployment_rate: 3.9
  median_home_value: 241400
  gini_index: 0.4647
  vacancy_rate: 10.98
  race_white: 2977
  race_black: 2701
  race_asian: 71
  race_native: 367
  hispanic: 138
  bachelors_plus: 1198
districts:
  - to: "us/states/va/districts/04"
    rel: in-district
    area_weight: 0.9687
  - to: "us/states/va/districts/01"
    rel: in-district
    area_weight: 0.0107
  - to: "us/states/va/districts/senate/13"
    rel: in-district
    area_weight: 0.9799
  - to: "us/states/va/districts/house/81"
    rel: in-district
    area_weight: 0.9798
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Charles City County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6627 |
| Under 18 | 941 |
| 18–64 | 3904 |
| 65+ | 1782 |
| Median household income | 75417 |
| Poverty rate | 9.45 |
| Homeownership rate | 86.26 |
| Unemployment rate | 3.9 |
| Median home value | 241400 |
| Gini index | 0.4647 |
| Vacancy rate | 10.98 |
| White | 2977 |
| Black | 2701 |
| Asian | 71 |
| Native | 367 |
| Hispanic/Latino | 138 |
| Bachelor's or higher | 1198 |

## Districts

- [VA-04](/us/states/va/districts/04.md) — 97% (congressional)
- [VA-01](/us/states/va/districts/01.md) — 1% (congressional)
- [VA Senate District 13](/us/states/va/districts/senate/13.md) — 98% (state senate)
- [VA House District 81](/us/states/va/districts/house/81.md) — 98% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
