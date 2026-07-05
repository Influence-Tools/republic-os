---
type: Jurisdiction
title: "Putnam County, IN"
classification: county
fips: "18133"
state: "IN"
demographics:
  population: 37280
  population_under_18: 7209
  population_18_64: 23603
  population_65_plus: 6468
  median_household_income: 78378
  poverty_rate: 8.69
  homeownership_rate: 75.4
  unemployment_rate: 3.09
  median_home_value: 218900
  gini_index: 0.407
  vacancy_rate: 7.37
  race_white: 34056
  race_black: 1244
  race_asian: 552
  race_native: 33
  hispanic: 839
  bachelors_plus: 6805
districts:
  - to: "us/states/in/districts/04"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/in/districts/senate/24"
    rel: in-district
    area_weight: 0.6493
  - to: "us/states/in/districts/senate/37"
    rel: in-district
    area_weight: 0.3507
  - to: "us/states/in/districts/house/44"
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

# Putnam County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 37280 |
| Under 18 | 7209 |
| 18–64 | 23603 |
| 65+ | 6468 |
| Median household income | 78378 |
| Poverty rate | 8.69 |
| Homeownership rate | 75.4 |
| Unemployment rate | 3.09 |
| Median home value | 218900 |
| Gini index | 0.407 |
| Vacancy rate | 7.37 |
| White | 34056 |
| Black | 1244 |
| Asian | 552 |
| Native | 33 |
| Hispanic/Latino | 839 |
| Bachelor's or higher | 6805 |

## Districts

- [IN-04](/us/states/in/districts/04.md) — 100% (congressional)
- [IN Senate District 24](/us/states/in/districts/senate/24.md) — 65% (state senate)
- [IN Senate District 37](/us/states/in/districts/senate/37.md) — 35% (state senate)
- [IN House District 44](/us/states/in/districts/house/44.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
