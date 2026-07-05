---
type: Jurisdiction
title: "Ripley County, IN"
classification: county
fips: "18137"
state: "IN"
demographics:
  population: 29095
  population_under_18: 6862
  population_18_64: 16774
  population_65_plus: 5459
  median_household_income: 70573
  poverty_rate: 10.11
  homeownership_rate: 76.85
  unemployment_rate: 3.03
  median_home_value: 222500
  gini_index: 0.4367
  vacancy_rate: 7.46
  race_white: 27539
  race_black: 218
  race_asian: 152
  race_native: 7
  hispanic: 577
  bachelors_plus: 5913
districts:
  - to: "us/states/in/districts/09"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/in/districts/senate/42"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/in/districts/house/67"
    rel: in-district
    area_weight: 0.8439
  - to: "us/states/in/districts/house/55"
    rel: in-district
    area_weight: 0.156
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Ripley County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 29095 |
| Under 18 | 6862 |
| 18–64 | 16774 |
| 65+ | 5459 |
| Median household income | 70573 |
| Poverty rate | 10.11 |
| Homeownership rate | 76.85 |
| Unemployment rate | 3.03 |
| Median home value | 222500 |
| Gini index | 0.4367 |
| Vacancy rate | 7.46 |
| White | 27539 |
| Black | 218 |
| Asian | 152 |
| Native | 7 |
| Hispanic/Latino | 577 |
| Bachelor's or higher | 5913 |

## Districts

- [IN-09](/us/states/in/districts/09.md) — 100% (congressional)
- [IN Senate District 42](/us/states/in/districts/senate/42.md) — 100% (state senate)
- [IN House District 67](/us/states/in/districts/house/67.md) — 84% (state house)
- [IN House District 55](/us/states/in/districts/house/55.md) — 16% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
