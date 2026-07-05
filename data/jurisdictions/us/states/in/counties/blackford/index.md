---
type: Jurisdiction
title: "Blackford County, IN"
classification: county
fips: "18009"
state: "IN"
demographics:
  population: 11950
  population_under_18: 2722
  population_18_64: 6597
  population_65_plus: 2631
  median_household_income: 51326
  poverty_rate: 16.18
  homeownership_rate: 73.86
  unemployment_rate: 3.71
  median_home_value: 107500
  gini_index: 0.4596
  vacancy_rate: 11.62
  race_white: 11330
  race_black: 77
  race_asian: 13
  race_native: 21
  hispanic: 283
  bachelors_plus: 1602
districts:
  - to: "us/states/in/districts/03"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/in/districts/senate/19"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/in/districts/house/33"
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

# Blackford County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11950 |
| Under 18 | 2722 |
| 18–64 | 6597 |
| 65+ | 2631 |
| Median household income | 51326 |
| Poverty rate | 16.18 |
| Homeownership rate | 73.86 |
| Unemployment rate | 3.71 |
| Median home value | 107500 |
| Gini index | 0.4596 |
| Vacancy rate | 11.62 |
| White | 11330 |
| Black | 77 |
| Asian | 13 |
| Native | 21 |
| Hispanic/Latino | 283 |
| Bachelor's or higher | 1602 |

## Districts

- [IN-03](/us/states/in/districts/03.md) — 100% (congressional)
- [IN Senate District 19](/us/states/in/districts/senate/19.md) — 100% (state senate)
- [IN House District 33](/us/states/in/districts/house/33.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
