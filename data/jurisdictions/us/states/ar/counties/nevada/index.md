---
type: Jurisdiction
title: "Nevada County, AR"
classification: county
fips: "05099"
state: "AR"
demographics:
  population: 8159
  population_under_18: 1807
  population_18_64: 4582
  population_65_plus: 1770
  median_household_income: 53886
  poverty_rate: 20.25
  homeownership_rate: 76.01
  unemployment_rate: 4.62
  median_home_value: 83300
  gini_index: 0.3972
  vacancy_rate: 24.54
  race_white: 5328
  race_black: 2580
  race_asian: 0
  race_native: 0
  hispanic: 392
  bachelors_plus: 938
districts:
  - to: "us/states/ar/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ar/districts/senate/3"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ar/districts/house/89"
    rel: in-district
    area_weight: 0.7911
  - to: "us/states/ar/districts/house/98"
    rel: in-district
    area_weight: 0.2088
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Nevada County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8159 |
| Under 18 | 1807 |
| 18–64 | 4582 |
| 65+ | 1770 |
| Median household income | 53886 |
| Poverty rate | 20.25 |
| Homeownership rate | 76.01 |
| Unemployment rate | 4.62 |
| Median home value | 83300 |
| Gini index | 0.3972 |
| Vacancy rate | 24.54 |
| White | 5328 |
| Black | 2580 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 392 |
| Bachelor's or higher | 938 |

## Districts

- [AR-04](/us/states/ar/districts/04.md) — 100% (congressional)
- [AR Senate District 3](/us/states/ar/districts/senate/3.md) — 100% (state senate)
- [AR House District 89](/us/states/ar/districts/house/89.md) — 79% (state house)
- [AR House District 98](/us/states/ar/districts/house/98.md) — 21% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
