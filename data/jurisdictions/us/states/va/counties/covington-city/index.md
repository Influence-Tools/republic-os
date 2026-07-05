---
type: Jurisdiction
title: "Covington city, VA"
classification: county
fips: "51580"
state: "VA"
demographics:
  population: 5680
  population_under_18: 1549
  population_18_64: 1551
  population_65_plus: 2580
  median_household_income: 41944
  poverty_rate: 25.68
  homeownership_rate: 70.11
  unemployment_rate: 2.75
  median_home_value: 83500
  gini_index: 0.402
  vacancy_rate: 15.12
  race_white: 4525
  race_black: 720
  race_asian: 76
  race_native: 0
  hispanic: 202
  bachelors_plus: 526
districts:
  - to: "us/states/va/districts/06"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/senate/3"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/house/37"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Covington city, VA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5680 |
| Under 18 | 1549 |
| 18–64 | 1551 |
| 65+ | 2580 |
| Median household income | 41944 |
| Poverty rate | 25.68 |
| Homeownership rate | 70.11 |
| Unemployment rate | 2.75 |
| Median home value | 83500 |
| Gini index | 0.402 |
| Vacancy rate | 15.12 |
| White | 4525 |
| Black | 720 |
| Asian | 76 |
| Native | 0 |
| Hispanic/Latino | 202 |
| Bachelor's or higher | 526 |

## Districts

- [VA-06](/us/states/va/districts/06.md) — 100% (congressional)
- [VA Senate District 3](/us/states/va/districts/senate/3.md) — 100% (state senate)
- [VA House District 37](/us/states/va/districts/house/37.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
