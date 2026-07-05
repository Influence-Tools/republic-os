---
type: Jurisdiction
title: "LaGrange County, IN"
classification: county
fips: "18087"
state: "IN"
demographics:
  population: 40805
  population_under_18: 12952
  population_18_64: 21908
  population_65_plus: 5945
  median_household_income: 84487
  poverty_rate: 5.94
  homeownership_rate: 83.02
  unemployment_rate: 4.24
  median_home_value: 255900
  gini_index: 0.4143
  vacancy_rate: 14.88
  race_white: 38423
  race_black: 145
  race_asian: 28
  race_native: 54
  hispanic: 1845
  bachelors_plus: 3694
districts:
  - to: "us/states/in/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/in/districts/senate/13"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/in/districts/house/51"
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

# LaGrange County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 40805 |
| Under 18 | 12952 |
| 18–64 | 21908 |
| 65+ | 5945 |
| Median household income | 84487 |
| Poverty rate | 5.94 |
| Homeownership rate | 83.02 |
| Unemployment rate | 4.24 |
| Median home value | 255900 |
| Gini index | 0.4143 |
| Vacancy rate | 14.88 |
| White | 38423 |
| Black | 145 |
| Asian | 28 |
| Native | 54 |
| Hispanic/Latino | 1845 |
| Bachelor's or higher | 3694 |

## Districts

- [IN-03](/us/states/in/districts/03.md) — 100% (congressional)
- [IN Senate District 13](/us/states/in/districts/senate/13.md) — 100% (state senate)
- [IN House District 51](/us/states/in/districts/house/51.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
