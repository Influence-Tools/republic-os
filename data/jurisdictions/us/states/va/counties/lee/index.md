---
type: Jurisdiction
title: "Lee County, VA"
classification: county
fips: "51105"
state: "VA"
demographics:
  population: 21900
  population_under_18: 3996
  population_18_64: 12840
  population_65_plus: 5064
  median_household_income: 41827
  poverty_rate: 28.83
  homeownership_rate: 73.02
  unemployment_rate: 9.52
  median_home_value: 98900
  gini_index: 0.4745
  vacancy_rate: 21.42
  race_white: 20294
  race_black: 950
  race_asian: 40
  race_native: 48
  hispanic: 525
  bachelors_plus: 3067
districts:
  - to: "us/states/va/districts/09"
    rel: in-district
    area_weight: 0.9983
  - to: "us/states/va/districts/senate/6"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/va/districts/house/45"
    rel: in-district
    area_weight: 0.9987
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Lee County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21900 |
| Under 18 | 3996 |
| 18–64 | 12840 |
| 65+ | 5064 |
| Median household income | 41827 |
| Poverty rate | 28.83 |
| Homeownership rate | 73.02 |
| Unemployment rate | 9.52 |
| Median home value | 98900 |
| Gini index | 0.4745 |
| Vacancy rate | 21.42 |
| White | 20294 |
| Black | 950 |
| Asian | 40 |
| Native | 48 |
| Hispanic/Latino | 525 |
| Bachelor's or higher | 3067 |

## Districts

- [VA-09](/us/states/va/districts/09.md) — 100% (congressional)
- [VA Senate District 6](/us/states/va/districts/senate/6.md) — 100% (state senate)
- [VA House District 45](/us/states/va/districts/house/45.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
