---
type: Jurisdiction
title: "Craig County, VA"
classification: county
fips: "51045"
state: "VA"
demographics:
  population: 4856
  population_under_18: 1122
  population_18_64: 2819
  population_65_plus: 915
  median_household_income: 69057
  poverty_rate: 13.75
  homeownership_rate: 83.75
  unemployment_rate: 2.17
  median_home_value: 189000
  gini_index: 0.4005
  vacancy_rate: 27.65
  race_white: 4652
  race_black: 3
  race_asian: 0
  race_native: 0
  hispanic: 72
  bachelors_plus: 934
districts:
  - to: "us/states/va/districts/09"
    rel: in-district
    area_weight: 0.9968
  - to: "us/states/va/districts/senate/3"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/va/districts/house/37"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Craig County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4856 |
| Under 18 | 1122 |
| 18–64 | 2819 |
| 65+ | 915 |
| Median household income | 69057 |
| Poverty rate | 13.75 |
| Homeownership rate | 83.75 |
| Unemployment rate | 2.17 |
| Median home value | 189000 |
| Gini index | 0.4005 |
| Vacancy rate | 27.65 |
| White | 4652 |
| Black | 3 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 72 |
| Bachelor's or higher | 934 |

## Districts

- [VA-09](/us/states/va/districts/09.md) — 100% (congressional)
- [VA Senate District 3](/us/states/va/districts/senate/3.md) — 100% (state senate)
- [VA House District 37](/us/states/va/districts/house/37.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
