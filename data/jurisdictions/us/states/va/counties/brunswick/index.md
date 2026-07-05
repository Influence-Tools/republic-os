---
type: Jurisdiction
title: "Brunswick County, VA"
classification: county
fips: "51025"
state: "VA"
demographics:
  population: 15841
  population_under_18: 2423
  population_18_64: 9879
  population_65_plus: 3539
  median_household_income: 53084
  poverty_rate: 14.94
  homeownership_rate: 74.45
  unemployment_rate: 3.34
  median_home_value: 142700
  gini_index: 0.4554
  vacancy_rate: 18.6
  race_white: 6535
  race_black: 8198
  race_asian: 87
  race_native: 60
  hispanic: 456
  bachelors_plus: 2739
districts:
  - to: "us/states/va/districts/04"
    rel: in-district
    area_weight: 0.9986
  - to: "us/states/va/districts/senate/17"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/va/districts/house/83"
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

# Brunswick County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15841 |
| Under 18 | 2423 |
| 18–64 | 9879 |
| 65+ | 3539 |
| Median household income | 53084 |
| Poverty rate | 14.94 |
| Homeownership rate | 74.45 |
| Unemployment rate | 3.34 |
| Median home value | 142700 |
| Gini index | 0.4554 |
| Vacancy rate | 18.6 |
| White | 6535 |
| Black | 8198 |
| Asian | 87 |
| Native | 60 |
| Hispanic/Latino | 456 |
| Bachelor's or higher | 2739 |

## Districts

- [VA-04](/us/states/va/districts/04.md) — 100% (congressional)
- [VA Senate District 17](/us/states/va/districts/senate/17.md) — 100% (state senate)
- [VA House District 83](/us/states/va/districts/house/83.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
