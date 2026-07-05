---
type: Jurisdiction
title: "Fayette County, IN"
classification: county
fips: "18041"
state: "IN"
demographics:
  population: 23334
  population_under_18: 5136
  population_18_64: 13399
  population_65_plus: 4799
  median_household_income: 59321
  poverty_rate: 17.86
  homeownership_rate: 72.09
  unemployment_rate: 3.41
  median_home_value: 130700
  gini_index: 0.4249
  vacancy_rate: 13.6
  race_white: 21919
  race_black: 316
  race_asian: 17
  race_native: 33
  hispanic: 318
  bachelors_plus: 3315
districts:
  - to: "us/states/in/districts/06"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/in/districts/senate/42"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/in/districts/house/55"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Fayette County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 23334 |
| Under 18 | 5136 |
| 18–64 | 13399 |
| 65+ | 4799 |
| Median household income | 59321 |
| Poverty rate | 17.86 |
| Homeownership rate | 72.09 |
| Unemployment rate | 3.41 |
| Median home value | 130700 |
| Gini index | 0.4249 |
| Vacancy rate | 13.6 |
| White | 21919 |
| Black | 316 |
| Asian | 17 |
| Native | 33 |
| Hispanic/Latino | 318 |
| Bachelor's or higher | 3315 |

## Districts

- [IN-06](/us/states/in/districts/06.md) — 100% (congressional)
- [IN Senate District 42](/us/states/in/districts/senate/42.md) — 100% (state senate)
- [IN House District 55](/us/states/in/districts/house/55.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
