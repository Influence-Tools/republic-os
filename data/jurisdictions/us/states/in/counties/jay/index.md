---
type: Jurisdiction
title: "Jay County, IN"
classification: county
fips: "18075"
state: "IN"
demographics:
  population: 20229
  population_under_18: 5185
  population_18_64: 11344
  population_65_plus: 3700
  median_household_income: 54969
  poverty_rate: 14.38
  homeownership_rate: 79.92
  unemployment_rate: 4.41
  median_home_value: 117500
  gini_index: 0.4108
  vacancy_rate: 12.32
  race_white: 18919
  race_black: 67
  race_asian: 11
  race_native: 12
  hispanic: 922
  bachelors_plus: 2463
districts:
  - to: "us/states/in/districts/03"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/in/districts/senate/19"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/in/districts/house/33"
    rel: in-district
    area_weight: 0.6707
  - to: "us/states/in/districts/house/79"
    rel: in-district
    area_weight: 0.3292
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Jay County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20229 |
| Under 18 | 5185 |
| 18–64 | 11344 |
| 65+ | 3700 |
| Median household income | 54969 |
| Poverty rate | 14.38 |
| Homeownership rate | 79.92 |
| Unemployment rate | 4.41 |
| Median home value | 117500 |
| Gini index | 0.4108 |
| Vacancy rate | 12.32 |
| White | 18919 |
| Black | 67 |
| Asian | 11 |
| Native | 12 |
| Hispanic/Latino | 922 |
| Bachelor's or higher | 2463 |

## Districts

- [IN-03](/us/states/in/districts/03.md) — 100% (congressional)
- [IN Senate District 19](/us/states/in/districts/senate/19.md) — 100% (state senate)
- [IN House District 33](/us/states/in/districts/house/33.md) — 67% (state house)
- [IN House District 79](/us/states/in/districts/house/79.md) — 33% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
