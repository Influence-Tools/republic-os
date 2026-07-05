---
type: Jurisdiction
title: "Warren County, IN"
classification: county
fips: "18171"
state: "IN"
demographics:
  population: 8464
  population_under_18: 1833
  population_18_64: 4819
  population_65_plus: 1812
  median_household_income: 82425
  poverty_rate: 10.98
  homeownership_rate: 82.38
  unemployment_rate: 4.39
  median_home_value: 182500
  gini_index: 0.3765
  vacancy_rate: 9.36
  race_white: 8021
  race_black: 12
  race_asian: 40
  race_native: 7
  hispanic: 123
  bachelors_plus: 1433
districts:
  - to: "us/states/in/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/in/districts/senate/23"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/in/districts/house/13"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Warren County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8464 |
| Under 18 | 1833 |
| 18–64 | 4819 |
| 65+ | 1812 |
| Median household income | 82425 |
| Poverty rate | 10.98 |
| Homeownership rate | 82.38 |
| Unemployment rate | 4.39 |
| Median home value | 182500 |
| Gini index | 0.3765 |
| Vacancy rate | 9.36 |
| White | 8021 |
| Black | 12 |
| Asian | 40 |
| Native | 7 |
| Hispanic/Latino | 123 |
| Bachelor's or higher | 1433 |

## Districts

- [IN-04](/us/states/in/districts/04.md) — 100% (congressional)
- [IN Senate District 23](/us/states/in/districts/senate/23.md) — 100% (state senate)
- [IN House District 13](/us/states/in/districts/house/13.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
