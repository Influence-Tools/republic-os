---
type: Jurisdiction
title: "Plymouth County, MA"
classification: county
fips: "25023"
state: "MA"
demographics:
  population: 535075
  population_under_18: 110836
  population_18_64: 318499
  population_65_plus: 105740
  median_household_income: 114201
  poverty_rate: 7.1
  homeownership_rate: 77.61
  unemployment_rate: 5.09
  median_home_value: 556000
  gini_index: 0.4625
  vacancy_rate: 6.86
  race_white: 411816
  race_black: 42910
  race_asian: 8987
  race_native: 801
  hispanic: 26184
  bachelors_plus: 220404
districts:
  - to: "us/states/ma/districts/09"
    rel: in-district
    area_weight: 0.5137
  - to: "us/states/ma/districts/08"
    rel: in-district
    area_weight: 0.0966
  - to: "us/states/ma/districts/04"
    rel: in-district
    area_weight: 0.0332
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ma]
timestamp: "2026-07-03"
---

# Plymouth County, MA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 535075 |
| Under 18 | 110836 |
| 18–64 | 318499 |
| 65+ | 105740 |
| Median household income | 114201 |
| Poverty rate | 7.1 |
| Homeownership rate | 77.61 |
| Unemployment rate | 5.09 |
| Median home value | 556000 |
| Gini index | 0.4625 |
| Vacancy rate | 6.86 |
| White | 411816 |
| Black | 42910 |
| Asian | 8987 |
| Native | 801 |
| Hispanic/Latino | 26184 |
| Bachelor's or higher | 220404 |

## Districts

- [MA-09](/us/states/ma/districts/09.md) — 51% (congressional)
- [MA-08](/us/states/ma/districts/08.md) — 10% (congressional)
- [MA-04](/us/states/ma/districts/04.md) — 3% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
